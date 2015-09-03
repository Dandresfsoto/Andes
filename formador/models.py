from django.db import models
from region.models import Region
from django.utils.encoding import smart_unicode

class Formador(models.Model):
    region = models.ForeignKey(Region)
    nombre = models.CharField(max_length=100)
    cedula = models.IntegerField()
    celular = models.BigIntegerField()
    correo = models.EmailField()
    hv = models.FileField(upload_to="Formadores/Hojas de Vida/",blank=True)
    certificacion = models.FileField(upload_to="Formadores/Certificacion Bancaria/",blank=True)
    rut = models.FileField(upload_to="Formadores/Rut/",blank=True)
    contrato = models.FileField(upload_to="Formadores/Contratos/",blank=True)
    seguro_enero = models.FileField(upload_to="Formadores/Seguro/Enero",blank=True)
    seguro_febrero = models.FileField(upload_to="Formadores/Seguro/Febrero",blank=True)
    seguro_marzo = models.FileField(upload_to="Formadores/Seguro/Marzo",blank=True)
    seguro_abril = models.FileField(upload_to="Formadores/Seguro/Abril",blank=True)
    seguro_mayo = models.FileField(upload_to="Formadores/Seguro/Mayo",blank=True)
    seguro_junio = models.FileField(upload_to="Formadores/Seguro/Junio",blank=True)
    seguro_julio = models.FileField(upload_to="Formadores/Seguro/Julio",blank=True)
    seguro_agosto = models.FileField(upload_to="Formadores/Seguro/Agosto",blank=True)
    seguro_septiembre = models.FileField(upload_to="Formadores/Seguro/Septiembre",blank=True)
    seguro_octubre = models.FileField(upload_to="Formadores/Seguro/Octubre",blank=True)
    seguro_noviembre = models.FileField(upload_to="Formadores/Seguro/Noviembre",blank=True)
    seguro_diciembre = models.FileField(upload_to="Formadores/Seguro/Diciembre",blank=True)
    fecha_contratacion = models.DateField()
    fecha_terminacion = models.DateField(blank=True,null=True)

    def __unicode__(self):
        return smart_unicode(self.nombre)