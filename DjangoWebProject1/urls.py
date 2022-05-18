"""
Definition of urls for DjangoWebProject1.
"""

from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('app/', include('app.urls')),
    path('admin/', admin.site.urls),
]
