from django.db import models
from region.models import Region
from django.utils.encoding import smart_unicode

class Funcionario(models.Model):
    region = models.ForeignKey(Region)

    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=15)
    celular = models.CharField(max_length=30,blank=True)
    correo = models.EmailField(blank=True)

    cargo = models.CharField(max_length=100,blank=True)
    profesion = models.CharField(max_length=30,blank=True)
    banco = models.CharField(max_length=100,blank=True)
    tipo_cuenta = models.CharField(max_length=50,blank=True)
    numero_cuenta = models.CharField(max_length=30,blank=True)
    eps = models.CharField(max_length=30,blank=True)
    pension = models.CharField(max_length=30,blank=True)
    arl = models.CharField(max_length=30,blank=True)
    foto = models.FileField(upload_to="Funcionarios/Foto/",blank=True)

    hv = models.FileField(upload_to="Funcionarios/Hojas de Vida/",blank=True)
    certificacion = models.FileField(upload_to="Funcionarios/Certificacion Bancaria/",blank=True)
    rut = models.FileField(upload_to="Funcionarios/Rut/",blank=True)
    contrato = models.FileField(upload_to="Funcionarios/Contratos/",blank=True)
    fotocopia_cedula = models.FileField(upload_to="Funcionarios/Fotocopia Cedula/",blank=True)
    antecedentes_judiciales = models.FileField(upload_to="Funcionarios/Antecedentes Judiciales/",blank=True)
    antecedentes_contraloria = models.FileField(upload_to="Funcionarios/Antecedentes Contraloria/",blank=True)

    seguro_enero = models.FileField(upload_to="Funcionarios/Seguro/Enero",blank=True)
    seguro_febrero = models.FileField(upload_to="Funcionarios/Seguro/Febrero",blank=True)
    seguro_marzo = models.FileField(upload_to="Funcionarios/Seguro/Marzo",blank=True)
    seguro_abril = models.FileField(upload_to="Funcionarios/Seguro/Abril",blank=True)
    seguro_mayo = models.FileField(upload_to="Funcionarios/Seguro/Mayo",blank=True)
    seguro_junio = models.FileField(upload_to="Funcionarios/Seguro/Junio",blank=True)
    seguro_julio = models.FileField(upload_to="Funcionarios/Seguro/Julio",blank=True)
    seguro_agosto = models.FileField(upload_to="Funcionarios/Seguro/Agosto",blank=True)
    seguro_septiembre = models.FileField(upload_to="Funcionarios/Seguro/Septiembre",blank=True)
    seguro_octubre = models.FileField(upload_to="Funcionarios/Seguro/Octubre",blank=True)
    seguro_noviembre = models.FileField(upload_to="Funcionarios/Seguro/Noviembre",blank=True)
    seguro_diciembre = models.FileField(upload_to="Funcionarios/Seguro/Diciembre",blank=True)

    fecha_contratacion = models.DateField()
    fecha_terminacion = models.DateField(blank=True,null=True)

    def __unicode__(self):
        return smart_unicode(self.nombre)