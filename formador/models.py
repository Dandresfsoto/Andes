from django.db import models
from region.models import Region
from django.utils.encoding import smart_unicode

class Formador(models.Model):
    region = models.ForeignKey(Region)

    nombre = models.CharField(max_length=100)
    cedula = models.IntegerField()
    celular = models.CharField(max_length=100)
    correo = models.EmailField()

    cargo = models.CharField(max_length=100,blank=True)
    profesion = models.CharField(max_length=100,blank=True)
    banco = models.CharField(max_length=100,blank=True)
    tipo_cuenta = models.CharField(max_length=100,blank=True)
    numero_cuenta = models.CharField(max_length=100,blank=True)
    eps = models.CharField(max_length=100,blank=True)
    pension = models.CharField(max_length=100,blank=True)
    arl = models.CharField(max_length=100,blank=True)
    foto = models.FileField(upload_to="Formadores/Foto/",blank=True)

    hv = models.FileField(upload_to="Formadores/Hojas de Vida/",blank=True)
    certificacion = models.FileField(upload_to="Formadores/Certificacion Bancaria/",blank=True)
    rut = models.FileField(upload_to="Formadores/Rut/",blank=True)
    contrato = models.FileField(upload_to="Formadores/Contratos/",blank=True)
    fotocopia_cedula = models.FileField(upload_to="Formadores/Fotocopia Cedula/",blank=True)
    antecedentes_judiciales = models.FileField(upload_to="Formadores/Antecedentes Judiciales/",blank=True)
    antecedentes_contraloria = models.FileField(upload_to="Formadores/Antecedentes Contraloria/",blank=True)

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