from multiprocessing import context
from django.shortcuts import get_object_or_404, render
# import product and category from models
from .models import Category, Product

# Create your views here.

def index(request):
    return render(request, 'index.html')


def listProduct(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories)
    else:
        products = Product.objects.all().order_by('id')
    
    # paginator = Paginator(products, 10)
    # page = request.GET.get('page')
    # paged_products = paginator.get_page(page)
    
    context = {'products': products,}
        
    return render(request, 'ShopApp/listProduct.html', context)