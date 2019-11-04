from django.db import models
from datetime import datetime

class Contact(models.Model):
  listado = models.CharField(max_length=200)
  listado_id = models.IntegerField()
  nombre = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  telefono = models.CharField(max_length=100)
  mensaje = models.TextField(blank=True)
  fecha = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)
  def __str__(self):
    return self.name