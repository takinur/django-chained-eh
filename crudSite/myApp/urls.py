from django.urls import path
from myApp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('list', views.listProduct, name='list'),
    path('list/<slug:category_slug>', views.listProduct, name='product_list_by_category'),
    path('createprod/', views.createProduct, name='createProduct'),
    path('editprod/<int:id>/', views.editProduct, name='editProduct'),
    path('deleteprod/<int:id>/', views.deleteProduct, name='deleteProduct')
]
