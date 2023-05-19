from django.db import models

# Create your models here.
class Producto(models.Model):
    sku = models.CharField(max_length=10, primary_key=True, blank=False, null=False, unique=True, verbose_name="SKU")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    marca = models.CharField(max_length=20, verbose_name="Marca")

    def __str__(self):
        return self.sku

class Movimiento(models.Model):
    TIPO_MOVIMIENTO = (('SA','Salida'),('EN','Entrada'))
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, verbose_name="Producto")
    tipo = models.CharField(max_length=2, choices=TIPO_MOVIMIENTO, verbose_name="Tipo")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    precio = models.IntegerField(verbose_name="Precio")
    
    def __str__(self):
        return self.tipo + " | " +self.producto.nombre 