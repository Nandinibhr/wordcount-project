from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('count/', views.count, name ='count'),
    path('about/', views.about, name ='about'),
    path('', views.homepage, name='home'),
]
