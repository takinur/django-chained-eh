from django.contrib import admin
from django.urls import path, include
from myApp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='Home'),
    path('admin/', admin.site.urls),
    
    path('shopapp/', include('myApp.urls')),
   
   
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    