from django.urls import path 
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.inicio, name="inicio"),
    path('vehiculo/', views.vehiculo, name="vehiculo"),
    path('about/', views.about),
]