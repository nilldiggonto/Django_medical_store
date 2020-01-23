from django.shortcuts import render,get_object_or_404
from .models import Product,M_category,D_category
from django.views.generic import ListView,DeleteView,DetailView
from carts.models import Cart
# Create your views here.

def product_view(request):
    template_name = 'products/product_list.html'
    object_list = Product.objects.all()
    d_list  = D_category.objects.all()
    phase_category = M_category.objects.all()
    cart_obj,new_obj = Cart.objects.new_or_get(request)

    context = {
        'object_list':object_list,
        'd_list': d_list,
        'phase_category': phase_category,
        'cart':cart_obj,
            }
    return render(request,template_name,context)

def product_by_category(request,slug):
    template_name = 'products/product_list.html'
    category = get_object_or_404(M_category, slug=slug)
    object_list = Product.objects.filter(m_title =category.id)
    d_list  = D_category.objects.all()
    phase_category = M_category.objects.all()

    context = {
        'object_list':object_list,
        'd_list': d_list,
        'phase_category': phase_category,
        'r_category':category,
            }
    return render(request,template_name,context)

class ProductListView(ListView):
    queryset        = Product.objects.all()
    template_name   = 'products/product_list.html'
    
    
    # def get_context_data(self, **kwargs):
    #     context = super(ProductListView, self).get_context_data(**kwargs)
    #     return context


class ProductDetailView(DetailView):
    queryset        = Product.objects.all()
    template_name   = 'products/product_detail.html'
    def get_context_data(self, **kwargs):
         context = super(ProductDetailView, self).get_context_data(**kwargs)
         request = self.request
         cart_obj,new_obj = Cart.objects.new_or_get(request)
         context['cart'] = cart_obj
         return context
    




class ProductFeaturedListView(ListView):
    template_name   = 'products/product_list.html'

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    template_name   = 'products/product_detail.html'

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.featured()
    


