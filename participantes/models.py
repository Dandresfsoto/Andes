from django.db import models
from area.models import AreaCurricular
from grado.models import Grado
from beneficiario.models import Beneficiario
from genero.models import Genero
from diplomado.models import Diplomado
from radicado.models import Radicado
from django.utils.encoding import smart_unicode


class Participante(models.Model):
    diplomado = models.ForeignKey(Diplomado)
    radicado = models.ForeignKey(Radicado)
    cedula = models.BigIntegerField(unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,blank=True)
    telefono = models.CharField(max_length=15)
    area = models.ForeignKey(AreaCurricular)
    grado = models.ForeignKey(Grado)
    beneficiario = models.ForeignKey(Beneficiario)
    genero = models.ForeignKey(Genero)

    def __unicode__(self):
        return smart_unicode(self.nombres+" "+self.apellidos)