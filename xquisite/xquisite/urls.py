from django.contrib import admin
from django.urls import path, include
from .views import (
    home
)

urlpatterns = [
    path("admin/", admin.site.urls, name='home'),
    path('', home.as_view(), name='home'),
    path('', include('accounts.urls')),
    path('store/', include('store.urls')),
    path('medical/', include('medical.urls')),
]
