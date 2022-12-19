from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.inicio, name="inicio"),


    path('vehiculos_index/', views.VehiculosListView.as_view(), name="vehiculos_index"),
    path('vehiculo_nuevo/', views.VehiculoView.as_view(), name="vehiculo_nuevo"),
    path('vehiculo_editar/<int:id>', views.vehiculo_editar, name="vehiculo_editar"),
    path('vehiculo_duplicar/<int:id>', views.vehiculo_duplicar, name="vehiculo_duplicar"),
    path('vehiculo_eliminar/<int:id>', views.vehiculo_eliminar, name="vehiculo_eliminar"),

    path('categorias_index/', views.CategoriasListView.as_view(), name="categorias_index"),
    path('categoria_nueva/', views.CategoriaView.as_view(), name="categoria_nueva"),
    path('categoria_editar/<int:id>', views.categoria_editar, name="categoria_editar"),
    path('categoria_eliminar/<int:id>', views.categoria_eliminar, name="categoria_eliminar"),

    path('resultado/', views.resultado, name="resultado"),
    path('nada/', views.nada, name="nada"),
    path('buscar/', views.buscar, name="buscar"),
    
    path('producto/<int:id>', views.producto, name="producto"),
    path('contacto/', views.contacto, name="contacto"),

    path('about/', views.about),

    path('accounts/', include('django.contrib.auth.urls')),

]

