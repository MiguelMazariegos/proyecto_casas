from django.db import models
from datetime import datetime
from vendedores.models import Vendedor

class Listado(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete = models.DO_NOTHING)
    titulo = models.CharField(max_length = 200)
    direccion = models.CharField(max_length=200)
    departamento = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.IntegerField()
    dormitorios = models.IntegerField()
    banios = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    mts = models.IntegerField()
    foto = models.ImageField(upload_to='photos/%Y/%m/%d/')
    foto1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    foto2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    foto3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    publicado = models.BooleanField(default = True)
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.titulo