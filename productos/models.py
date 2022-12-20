from django.db import models
from datetime import date

# Create your models here.


class Categoria(models.Model):

    categoria= models.CharField(max_length=20, verbose_name='Categoría')
    def __str__(self):
        return self.categoria

class Usuario(models.Model):

    nombre_usuario= models.CharField(max_length=20, verbose_name='Nombre de Usuario')
    nombre= models.CharField(max_length=30, verbose_name='Nombre')
    apellido= models.CharField(max_length=30, verbose_name='Apellido')
    def __str__(self):
        return self.nombre_usuario


class Vehiculo(models.Model):

    marca= models.CharField(max_length=20, verbose_name='Marca')
    modelo= models.CharField(max_length=30, verbose_name='Modelo')
    anio = models.IntegerField(verbose_name='Año')
    categoria= models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name='Categoría')
    descripcion= models.CharField(max_length=300, verbose_name='Descripción')
    puertas = models.CharField(max_length=1)
    precio= models.FloatField()
    fecha_publicacion= models.DateField(verbose_name='Fecha publicación', default=None, null=True  )
    seleccionado=models.BooleanField(default=False,null=True)
    imagen=models.ImageField(upload_to='upload/',verbose_name="Imagen:",default=None,null=True)
    usuario= models.ForeignKey(Usuario, on_delete=models.PROTECT, verbose_name='Usuario')
    
    def __str__(self):
        return self.marca+' '+self.modelo+' '+str(self.anio)


class Contacto(models.Model):
    nombre= models.CharField(max_length=20, verbose_name='Nombre')
    apellido= models.CharField(max_length=20, verbose_name='Apellido')
    correo= models.CharField(max_length=150, verbose_name='Correo')
    mensaje= models.CharField(max_length=240, verbose_name='Mensaje')