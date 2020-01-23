from django.shortcuts import render,redirect
from .models import Cart
from django.http import JsonResponse
from products.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.




def cart_home(request):

    template_name = 'carts/cart.html'
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    context = {
       'cart':cart_obj,
    }
  
    return render(request,template_name,context)


def cart_update(request):
       product_id = request.POST.get('product_id')
       print(product_id)
       print(product_id)

       print(product_id)
       print(product_id)
       print(product_id)
       print(product_id)
       print(product_id)
       print(product_id)
       print(product_id)
       print(product_id)
       print(product_id)
       print(product_id)
       print(product_id)
       print(product_id)
       print(product_id)

       if product_id is not None:
         try:
            product_obj = Product.objects.get(id=product_id)
         except Product.DoesNotExist:
            print('something worng')
            return redirect('carts:cart')
         cart_obj,new_obj = Cart.objects.new_or_get(request)
         if product_obj in cart_obj.products.all():
                  cart_obj.products.remove(product_obj)
         
         else:
               cart_obj.products.add(product_obj)
      #  cart_obj.products.remove(product_obj)
         request.session['cart_total'] = cart_obj.products.count()
       return redirect('carts:cart')



@login_required(login_url='/login/')
def checkout(request):
       template_name = 'carts/checkout.html'
       return render(request,template_name)



