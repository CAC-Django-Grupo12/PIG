from django.urls import path 
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.inicio, name="inicio"),
    path('vehiculo/', views.vehiculo, name="vehiculo"),

    #path('categorias_index/', views.categorias_index, name="categorias_index"),
    path('categorias_index/', views.CategoriasListView.as_view(), name="categorias_index"),
    #path('categoria_nueva/', views.categoria_nueva, name="categoria_nueva"),
    path('categoria_nueva/', views.CategoriaView.as_view(), name="categoria_nueva"),
    path('categoria_editar/<int:id>', views.categoria_editar, name="categoria_editar"),
    path('categoria_eliminar/<int:id>', views.categoria_eliminar, name="categoria_eliminar"),

    path('resultado/', views.resultado, name="resultado"),
    path('nada/', views.nada, name="nada"),
    path('buscar/', views.buscar, name="buscar"),
    
    path('producto/<int:id>', views.producto, name="producto"),
    path('contacto/', views.contacto, name="contacto"),

    path('about/', views.about),

]

