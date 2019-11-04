from django.db import models
from datetime import datetime

class Vendedor(models.Model):
    nombre = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/')
    descripcion = models.TextField(blank=True)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    fecha_cont = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.nombre
