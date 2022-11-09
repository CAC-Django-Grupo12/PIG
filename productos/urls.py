from django.urls import path 
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.inicio, name="inicio"),
    path('vehiculo/', views.vehiculo, name="vehiculo"),
    path('categoria/', views.categoria, name="categoria"),

    path('resultado/', views.resultado, name="resultado"),
    path('nada/', views.nada, name="nada"),
    path('buscar/', views.buscar, name="buscar"),
    
    path('producto/<int:id>', views.producto, name="producto"),
    path('contacto/', views.contacto, name="contacto"),

    path('about/', views.about),

]

