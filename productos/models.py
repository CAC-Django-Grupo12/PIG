from django.db import models

# Create your models here.


class Categoria(models.Model):

    categoria= models.CharField(max_length=20, verbose_name='Categoría')
    def __str__(self):
        return self.categoria


class Vehiculo(models.Model):

    marca= models.CharField(max_length=20)
    modelo= models.CharField(max_length=30)
    anio = models.IntegerField()
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion= models.CharField(max_length=300)
    puertas = models.CharField(max_length=1)
    precio= models.FloatField()
    fecha_publicacion= models.DateField()
    seleccionado=models.BooleanField(default=None,null=True)
    imagen=models.ImageField(upload_to='upload/',verbose_name="Imagen:",default=None,null=True)
