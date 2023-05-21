from django.db import models

# Create your models here.


class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    imagen = models.ImageField(upload_to='articulo', null=True, blank=True)
    desechable= models.BooleanField(default=True)
    tipo_articulo= models.CharField(max_length=50)

def __str__(self):
    return self.nombre