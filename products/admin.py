from django.contrib import admin
from .models import Product,D_category,M_category,Contact_admin
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model   = Product



admin.site.register(Product,ProductAdmin)
admin.site.register(D_category)
admin.site.register(M_category)
admin.site.register(Contact_admin)