from django.db import models
from django.utils.encoding import smart_unicode

class Pqr(models.Model):
    fecha_recepcion = models.DateTimeField(auto_now_add=True)
    region = models.CharField(max_length=200)
    eje = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    telefono = models.CharField(max_length=200)
    municipio = models.CharField(max_length=200)
    mensaje = models.TextField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.nombre)