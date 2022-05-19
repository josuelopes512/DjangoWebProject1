"""
Definition of urls for DjangoWebProject1.
"""
from datetime import datetime
from django.urls import path
from app import forms, views as _views
from django.contrib.auth.views import LoginView, LogoutView


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('register/', views.register_request, name="register"),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]