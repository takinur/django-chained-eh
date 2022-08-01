from django import forms
from myApp.models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
    def _init_(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['']