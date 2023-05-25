from django.db import models
import django

# Create your models here.


class Tipo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre



class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    imagen = models.ImageField(upload_to='articulo/img', null=True, blank=True)
    desechable= models.BooleanField(default=True)
    tipo_articulo= models.ForeignKey(Tipo,on_delete=models.SET_NULL,null=True)
    fecha_compra = models.DateField(default=django.utils.timezone.now,)
    precio = models.IntegerField()

def __str__(self):
    return self.nombre



