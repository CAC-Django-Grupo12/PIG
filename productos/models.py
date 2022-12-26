from django.db import models
#from datetime import date
from PIL import Image as Im
import locale

locale.setlocale(locale.LC_ALL, '')

# Create your models here.


class Categoria(models.Model):

    categoria= models.CharField(max_length=20, verbose_name='Categoría')
    def __str__(self):
        return self.categoria


class Vehiculo(models.Model):

    marca= models.CharField(max_length=20, verbose_name='Marca')
    modelo= models.CharField(max_length=30, verbose_name='Modelo')
    anio = models.IntegerField(verbose_name='Año')
    categoria= models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name='Categoría')
    descripcion= models.CharField(max_length=300, verbose_name='Descripción')
    puertas = models.CharField(max_length=1)
    precio= models.FloatField()
    fecha_publicacion= models.DateField(verbose_name='Fecha publicación', default=None, null=True, blank=True  )
    seleccionado=models.BooleanField(default=False,null=True)
    imagen=models.ImageField(upload_to='upload/',verbose_name="Imagen:",default=None,null=True)

    def __str__(self):
        # return self.marca+' - '+self.modelo+' - '+str(self.anio)+' - '+'$ {:,.2f}'.format(self.precio).replace(",", "@").replace(".", ",").replace("@", ".")+' -[ID: '+str(self.id)+']'
        return self.marca+' - '+self.modelo+' - '+str(self.anio)+' - $ '+locale.format('%.0f', self.precio, grouping=True, monetary=True)+' -[ID: '+str(self.id)+']'


    def save(self):
        super().save()
        img = Im.open(self.imagen.path)
        # resize
        if img.height > 800 or img.width > 800:
            output_size = (800,800)
            img.thumbnail(output_size)
            img.save(self.imagen.path)



class Contacto(models.Model):
    nombre= models.CharField(max_length=20, verbose_name='Nombre')
    apellido= models.CharField(max_length=20, verbose_name='Apellido')
    correo= models.CharField(max_length=150, verbose_name='Correo')
    mensaje= models.CharField(max_length=240, verbose_name='Mensaje')