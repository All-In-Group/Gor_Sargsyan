from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = "list"),
    path('update_task/<str:prk>',views.update_task, name = "update_task"),
    path('delete/<str:prk>',views.delete_task, name = "delete"),
]