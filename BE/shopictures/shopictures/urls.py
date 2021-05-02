"""shopictures URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_image', csrf_exempt(views.add_image), name='add_image'),
    path('get_pictures', csrf_exempt(views.get_pictures), name='get_pictures'),
    path('get_pictures_with_keyword', csrf_exempt(views.get_pictures_with_keyword), name='get_pictures_with_keyword'),
]
