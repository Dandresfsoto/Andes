from django.db import models
from region.models import Region
from django.utils.encoding import smart_unicode

class Gestor(models.Model):
    region = models.ForeignKey(Region)
    nombre = models.CharField(max_length=100)
    cedula = models.IntegerField()
    celular = models.IntegerField()
    correo = models.EmailField()
    hv = models.FileField(upload_to="Gestores/Hojas de Vida/")
    certificacion = models.FileField(upload_to="Gestores/Certificacion Bancaria/")
    rut = models.FileField(upload_to="Gestores/Rut/")
    contrato = models.FileField(upload_to="Gestores/Contratos/")
    seguro_agosto = models.FileField(upload_to="Gestores/Seguro/Agosto")
    seguro_septiembre = models.FileField(upload_to="Gestores/Seguro/Septiembre")
    seguro_octubre = models.FileField(upload_to="Gestores/Seguro/Octubre")
    seguro_noviembre = models.FileField(upload_to="Gestores/Seguro/Noviembre")
    seguro_diciembre = models.FileField(upload_to="Gestores/Seguro/Diciembre")
    fecha_contratacion = models.DateField()
    fecha_terminacion = models.DateField(blank=True)

    def __unicode__(self):
        return smart_unicode(self.nombre)
