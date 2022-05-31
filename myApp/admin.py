from django.contrib import admin

from myApp.models import product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'detials', 'quantity', 'unit_price', 'total_price', 'purchase_date']
    prepopulated_fields = {'slug': ('product_name',),}
    exclude = ('total_price', )

admin.site.register(product, ProductAdmin)
# Register your models here.
