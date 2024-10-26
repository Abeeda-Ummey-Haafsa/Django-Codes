
from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.DjangoForm, name='django_form'),
]
