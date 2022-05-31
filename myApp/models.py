from django.db import models
from django.utils.text import slugify

# Create your models here.

class product(models.Model):
    product_name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)
    detials = models.CharField(max_length=50, null=True)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    purchase_date = models.DateTimeField(auto_now_add=True)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        self.total_price = self.unit_price * self.quantity
        super(product, self).save(*args, **kwargs)
    
    
    def __str__(self) -> str:
        return self.product_name
    
    