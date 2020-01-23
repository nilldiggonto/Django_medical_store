from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . views import home_page, login_page, register_page, contact_page,logout_user

urlpatterns = [
    
    path('',home_page,name='home'),
    path('product/',include('products.urls')),
    path('search/',include('search.urls')),
    path('cart/',include('carts.urls')),
    path('login/',login_page,name='login'),
    path('register/',register_page,name='register'),
    path('logout/',logout_user,name='logout'),
    path('contact/',contact_page,name='contact'),
    path('admin/', admin.site.urls),
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
