from django.db import models
from django.utils.encoding import smart_unicode
from departamento.models import Departamento
from municipio.models import Municipio
from region.models import Region

class Radicado(models.Model):
    region = models.ForeignKey(Region)
    numero = models.BigIntegerField()
    dane_sede = models.CharField(max_length=100,blank=True)
    sede_id = models.CharField(max_length=100,blank=True)
    municipio = models.ForeignKey(Municipio)
    categoria = models.CharField(max_length=100,blank=True)
    dane_institucion = models.CharField(max_length=100,blank=True)
    nombre_institucion = models.CharField(max_length=200,blank=True)
    nombre_sede = models.CharField(max_length=200,blank=True)
    zona = models.CharField(max_length=40,blank=True)
    matricula = models.BigIntegerField(blank=True)
    segmentacion = models.CharField(max_length=50,blank=True)
    regiones_dnp = models.CharField(max_length=50,blank=True)
    total_cpe = models.BigIntegerField(blank=True)
    cpe_computadores_oferta = models.BigIntegerField(blank=True)
    cpe_tabletas_oferta = models.BigIntegerField(blank=True)
    cpe_tabletas_demanda = models.BigIntegerField(blank=True)
    total_et = models.BigIntegerField(blank=True)
    aporte_et_computadores = models.BigIntegerField(blank=True)
    aporte_et_tabletas = models.BigIntegerField(blank=True)

    def __unicode__(self):
        return smart_unicode(self.numero)