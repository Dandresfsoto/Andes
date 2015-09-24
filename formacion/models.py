from django.db import models
from radicado.models import Radicado
from formador.models import Formador
from municipio.models import Municipio
from django.utils.encoding import smart_unicode

class Grupo(models.Model):
    formador = models.ForeignKey(Formador)
    municipio = models.ForeignKey(Municipio)

    def __unicode__(self):
        return smart_unicode(self.formador)