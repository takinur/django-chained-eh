from django.db import models

# Create your models here.

class product(models.Model):
    product_name = models.CharField(max_length=50)
    detials = models.CharField(max_length=50, null=True)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    purchase_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.product_name
        