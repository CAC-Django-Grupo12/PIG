from django.db import models

# Create your models here.

class Vehiculo(models.Model):

    marca= models.CharField(max_length=20)
    modelo= models.CharField(max_length=30)
    anio = models.IntegerField()
    categoria= models.CharField(max_length=20)
    descripcion= models.CharField(max_length=300)
    puertas = models.CharField(max_length=1)
    precio= models.FloatField()
    fecha_publicacion= models.DateField()
    # imagen= 
