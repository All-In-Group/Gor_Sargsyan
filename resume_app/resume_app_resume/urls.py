from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name = 'index'),
    path('create/',views.create,name = 'create'),
    path('show/<str:pk>',views.show_cv,name = 'show'),
    
]