from django.urls import path


from .views import product_by_category,product_view,ProductListView,ProductDetailView,ProductFeaturedListView,ProductFeaturedDetailView

app_name ='medical_product'

urlpatterns = [
    # path('',ProductListView.as_view(),name='product_list'),
    path('',product_view,name='product_list'),
    path('featured/',ProductFeaturedListView.as_view(),name='feature-list'),
    path('<str:slug>/',ProductDetailView.as_view(),name='product_detail'),
   
    path('featured/<str:slug>/',ProductFeaturedDetailView.as_view(),name='feature-detail'),
    path('category/<str:slug>/',product_by_category,name='category'),
]
