from django.db import models
from region.models import Region
from django.utils.encoding import smart_unicode

class Gestor(models.Model):
    region = models.ForeignKey(Region)
    nombre = models.CharField(max_length=100)
    cedula = models.IntegerField()
    celular = models.BigIntegerField()
    correo = models.EmailField()
    hv = models.FileField(upload_to="Gestores/Hojas de Vida/",blank=True)
    certificacion = models.FileField(upload_to="Gestores/Certificacion Bancaria/",blank=True)
    rut = models.FileField(upload_to="Gestores/Rut/",blank=True)
    contrato = models.FileField(upload_to="Gestores/Contratos/",blank=True)
    seguro_agosto = models.FileField(upload_to="Gestores/Seguro/Agosto",blank=True)
    seguro_septiembre = models.FileField(upload_to="Gestores/Seguro/Septiembre",blank=True)
    seguro_octubre = models.FileField(upload_to="Gestores/Seguro/Octubre",blank=True)
    seguro_noviembre = models.FileField(upload_to="Gestores/Seguro/Noviembre",blank=True)
    seguro_diciembre = models.FileField(upload_to="Gestores/Seguro/Diciembre",blank=True)
    fecha_contratacion = models.DateField()
    fecha_terminacion = models.DateField(blank=True,null=True)

    def __unicode__(self):
        return smart_unicode(self.nombre)
