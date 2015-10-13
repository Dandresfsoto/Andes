from django.db import models
from region.models import Region
from django.utils.encoding import smart_unicode

def content_file_name(instance, filename):
    return '/'.join(['Administrativo y Financiero', 'Informes',filename])

def soporte_obligacion_file_name(instance, filename):
    return '/'.join(['Administrativo y Financiero', 'Obligaciones',filename])


class Informes(models.Model):
    region = models.ForeignKey(Region)
    fecha = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=500)
    mes = models.CharField(max_length=50)
    excel_acceso = models.FileField(upload_to=content_file_name,blank=True)
    soporte_acceso = models.FileField(upload_to=content_file_name,blank=True)
    excel_formacion = models.FileField(upload_to=content_file_name,blank=True)
    soporte_formacion = models.FileField(upload_to=content_file_name,blank=True)

    def __unicode__(self):
        return smart_unicode(self.mes)

class Obligacion(models.Model):
    region = models.ForeignKey(Region)
    numero = models.IntegerField()
    descripcion = models.TextField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.numero)

class SoporteObligacion(models.Model):
    mes = models.TextField(max_length=100)
    obligacion = models.ForeignKey(Obligacion)
    descripcion = models.TextField(max_length=100)
    soporte = models.FileField(upload_to=soporte_obligacion_file_name)

    def __unicode__(self):
        return smart_unicode(self.mes)