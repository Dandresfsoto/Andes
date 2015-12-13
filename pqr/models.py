from django.db import models
from django.utils.encoding import smart_unicode
from region.models import Region
from funcionario.models import Funcionario

class Frecuentes(models.Model):
    pregunta = models.CharField(max_length=500)

    def __unicode__(self):
        return smart_unicode(self.pregunta)

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

class PqrRespuesta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    pqr = models.ForeignKey(Pqr)
    region = models.ForeignKey(Region)
    funcionario = models.ForeignKey(Funcionario)
    mensaje = models.TextField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.pqr)

class Llamadas(models.Model):
    fecha_recepcion = models.DateTimeField(auto_now_add=True)
    region = models.ForeignKey(Region)
    eje = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    telefono = models.CharField(max_length=200)
    municipio = models.CharField(max_length=200)
    frecuente = models.ForeignKey(Frecuentes)
    mensaje = models.TextField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.nombre)

class LlamadasRespuesta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    llamada = models.ForeignKey(Llamadas)
    region = models.ForeignKey(Region)
    funcionario = models.ForeignKey(Funcionario)
    mensaje = models.TextField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.llamada)