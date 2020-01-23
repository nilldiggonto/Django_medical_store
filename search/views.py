from django.shortcuts import render
from django.views.generic import ListView
from products.views import ProductListView
from products.models import Product
from django.db.models import Q
# Create your views here.

class SearchProductView(ListView):
    template_name = 'search/search.html'
    
    
    
    def get_context_data(self, **kwargs):
        context = super(SearchProductView, self).get_context_data(**kwargs)
        query  = self.request.GET.get('q')
        context['query'] = query

        return context
    
    def get_queryset(self,*args,**kwargs):
        # request  = self.request
        query = self.request.GET.get('q',None)
        if query is not None:
            lookups = Q(title__icontains=query) | Q(description__icontains=query)
            return Product.objects.filter(lookups).distinct()

        return Product.objects.all()

