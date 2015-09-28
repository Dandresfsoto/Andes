from django.db import models
from formador.models import Formador
from municipio.models import Municipio
from django.utils.encoding import smart_unicode

class Grupo(models.Model):
    formador = models.ForeignKey(Formador)
    municipio = models.ForeignKey(Municipio)
    direccion = models.CharField(blank=True,max_length=200)
    horario = models.CharField(blank=True,max_length=200)

    def __unicode__(self):
        return smart_unicode(self.formador)