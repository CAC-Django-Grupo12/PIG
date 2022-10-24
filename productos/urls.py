from django.urls import path 
from .import views

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('producto/<int:id>', views.producto, name="producto"),
    path('about/', views.about),
    path('contacto/', views.contacto, name="contacto"),
]