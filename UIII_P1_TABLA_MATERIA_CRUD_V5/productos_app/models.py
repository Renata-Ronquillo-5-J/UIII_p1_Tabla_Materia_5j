from django.db import models

# Create your models here.
class Productos(models.Model):
    IdProducto=models.IntegerField(primary_key=True,max_length=6)
    Nombre=models.CharField(max_length=100)
    Stock=models.IntegerField(max_length=100)
    Proveedor=models.CharField(max_length=100)
    PrecioVenta=models.IntegerField(max_length=100)
    PrecioMayoreo=models.IntegerField(max_length=100)
    Descripcion=models.CharField(max_length=100)


    def __str__(self):
        return self.IdProducto