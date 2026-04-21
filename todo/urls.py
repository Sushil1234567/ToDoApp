from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add_task),
    path('delete/<int:task_id>/', views.delete_task),
]

