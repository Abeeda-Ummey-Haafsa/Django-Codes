from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home_page"),
    path('about/', views.about, name="about_page"),
    path('form/', views.submit_form, name="submit_form"),
    # path('django_form/', views.DjangoForm, name="django_form"),
    # path('django_form/', views.StudentForm, name="django_form"),
    path('django_form/', views.PasswordValidation, name="django_form"),
]