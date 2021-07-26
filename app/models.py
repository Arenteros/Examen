from django.db import models

# Create your models here.

class TipoProducto(models.Model):
    tipo = models.CharField(max_length=40)

    def __str__(self):
        return self.tipo

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=40)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.nombre

opcion_pago = [
    [0,"DEBITO"],
    [1,"CREDITO"],
]

monto_donacion = [
    [0, 4990],
    [1, 5990],
    [2, 6990],
    
]

class suscriptor(models.Model):
    nombre = models.CharField(max_length=40)
    correo = models.EmailField()
    tipo_pago=models.IntegerField(choices=opcion_pago)
    monto_donacion=models.IntegerField(choices=monto_donacion)

    def __str__(self):
        return self.nombre