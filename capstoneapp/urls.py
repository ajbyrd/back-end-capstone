"""backendcapstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from capstoneapp import views
from capstoneapp.models import *
from capstoneapp.views import *

app_name = 'capstoneapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_user, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('home/', home, name='home'),
    path('inventory/', inventory_list, name='inventory'),
    path('inventoryform/', inventory_form, name='inventoryform')
]