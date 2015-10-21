from django.db import models
from region.models import Region
from django.utils.encoding import smart_unicode

class TipoGestor(models.Model):
    tipo = models.CharField(max_length=100)

    def __unicode__(self):
        return smart_unicode(self.tipo)

class Gestor(models.Model):
    region = models.ForeignKey(Region)
    tipo = models.ForeignKey(TipoGestor)

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
    foto = models.FileField(upload_to="Gestores/Foto/",blank=True)

    hv = models.FileField(upload_to="Gestores/Hojas de Vida/",blank=True)
    certificacion = models.FileField(upload_to="Gestores/Certificacion Bancaria/",blank=True)
    rut = models.FileField(upload_to="Gestores/Rut/",blank=True)
    contrato = models.FileField(upload_to="Gestores/Contratos/",blank=True)
    fotocopia_cedula = models.FileField(upload_to="Gestores/Fotocopia Cedula/",blank=True)
    antecedentes_judiciales = models.FileField(upload_to="Gestores/Antecedentes Judiciales/",blank=True)
    antecedentes_contraloria = models.FileField(upload_to="Gestores/Antecedentes Contraloria/",blank=True)

    seguro_enero = models.FileField(upload_to="Gestores/Seguro/Enero",blank=True)
    seguro_febrero = models.FileField(upload_to="Gestores/Seguro/Febrero",blank=True)
    seguro_marzo = models.FileField(upload_to="Gestores/Seguro/Marzo",blank=True)
    seguro_abril = models.FileField(upload_to="Gestores/Seguro/Abril",blank=True)
    seguro_mayo = models.FileField(upload_to="Gestores/Seguro/Mayo",blank=True)
    seguro_junio = models.FileField(upload_to="Gestores/Seguro/Junio",blank=True)
    seguro_julio = models.FileField(upload_to="Gestores/Seguro/Julio",blank=True)
    seguro_agosto = models.FileField(upload_to="Gestores/Seguro/Agosto",blank=True)
    seguro_septiembre = models.FileField(upload_to="Gestores/Seguro/Septiembre",blank=True)
    seguro_octubre = models.FileField(upload_to="Gestores/Seguro/Octubre",blank=True)
    seguro_noviembre = models.FileField(upload_to="Gestores/Seguro/Noviembre",blank=True)
    seguro_diciembre = models.FileField(upload_to="Gestores/Seguro/Diciembre",blank=True)
    fecha_contratacion = models.DateField()
    fecha_terminacion = models.DateField(blank=True,null=True)

    def __unicode__(self):
        return smart_unicode(self.nombre)
