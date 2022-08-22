from django.contrib import admin

from myApp.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('category_name',)}
    
    list_display = ('category_name', 'slug', 'details')
    
    class Meta:
        model = Product
        
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'details', 'quantity', 'unit_price', 'total_price', 'purchase_date']
    prepopulated_fields = {'slug': ('product_name',),}
    exclude = ('total_price', )

admin.site.register(Product, ProductAdmin)
# Register your models here.
