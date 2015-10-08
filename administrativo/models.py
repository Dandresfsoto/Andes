from django.db import models
from region.models import Region
from django.utils.encoding import smart_unicode

def content_file_name(instance, filename):
    return '/'.join(['Administrativo y Financiero', 'Informes',filename])


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