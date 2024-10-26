
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path("contact", views.contact, name="contact"),
    path('pracForms/', include('pracForms.urls')),
    path('pracModels/', include('pracModels.urls')),
    
]
