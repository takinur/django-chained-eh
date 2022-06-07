from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):

    category_name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)
    details = models.CharField(max_length=50, null=True)
    
      
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__ (self):
          return self.category_name
      
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)
    details = models.CharField(max_length=50, null=True)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    purchase_date = models.DateTimeField(auto_now_add=True)
    # images = models.ImageField(upload_to='photos/products')
    images = models.FileField(upload_to='photos/products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        self.total_price = self.unit_price * self.quantity
        super(Product, self).save(*args, **kwargs)
        
    def delete(self, using=None, keep_parents=False):
        if(self.images.name != 'photos/products/blank.png'):
            self.images.storage.delete(self.images.name)
        super().delete()
    
    
    def __str__(self) -> str:
        return self.product_name
    
    