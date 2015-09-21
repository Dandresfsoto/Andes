from django.db import models
from radicado.models import Radicado
from gestor.models import Gestor
from region.models import Region
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User

def content_file_name(instance, filename):
    x = filename.split(".")
    filename = '.'.join([str(instance.radicado.numero),x[len(x)-1]])
    return '/'.join(['Acceso', 'R4', smart_unicode(instance.ciclo.nombre),smart_unicode(instance.actividad.nombre),str(instance.radicado.numero),filename])

class Ciclo(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return smart_unicode(self.nombre)

class Componente(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return smart_unicode(self.nombre)

class Modulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __unicode__(self):
        return smart_unicode('%s - %s' % (self.nombre, self.descripcion))

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=2000,blank=True)

    def __unicode__(self):
        return smart_unicode('%s - %s' % (self.nombre, self.titulo))

class Encargado(models.Model):
    encargado = models.CharField(max_length=100)

    def __unicode__(self):
        return smart_unicode(self.encargado)

class Entregables(models.Model):
    entregables = models.CharField(max_length=1000)

    def __unicode__(self):
        return smart_unicode(self.entregables)

class Valor(models.Model):
    valor = models.BigIntegerField()

    def __unicode__(self):
        return smart_unicode(self.valor)

class Corte(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.titulo)

class Evidencia(models.Model):
    radicado = models.ForeignKey(Radicado,related_name='numeroRadicado')
    gestor = models.ForeignKey(Gestor)
    ciclo = models.ForeignKey(Ciclo)
    componente = models.ForeignKey(Componente)
    modulo = models.ForeignKey(Modulo)
    actividad = models.ForeignKey(Actividad)
    encargado = models.ForeignKey(Encargado)
    valor = models.ForeignKey(Valor)
    soporte = models.FileField(upload_to=content_file_name,blank=True)
    corte = models.ForeignKey(Corte,blank=True,null=True)
    usuario = models.ForeignKey(User,blank=True,null=True)
    modificacion = models.DateTimeField(blank=True,null=True)

    def __unicode__(self):
        return smart_unicode(self.radicado)