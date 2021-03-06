"""crepes_bretonnes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
[...]
"""
#from django.contrib import admin
from django.urls import path
from linker import views

urlpatterns = [
    #path('admin/', admin.site.urls), #to delete ?
    path('', views.home), # home page
    path('date',views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/',views.addition)
]