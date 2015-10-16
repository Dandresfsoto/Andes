from django.db import models
from gestor.models import Gestor
from formador.models import Formador
from django.utils.encoding import smart_unicode

class LiquidacionGestor(models.Model):
    gestor = models.ForeignKey(Gestor)
    fecha_terminacion = models.DateField()
    contrato = models.CharField(max_length=100)

    valor_inicial = models.FloatField()
    valor_ejecutado = models.FloatField()
    valor_pagado = models.FloatField()

    def __unicode__(self):
        return smart_unicode(self.gestor)

class LiquidacionFormador(models.Model):
    formador = models.ForeignKey(Formador)
    fecha_terminacion = models.DateField()
    contrato = models.CharField(max_length=100)

    valor_inicial = models.FloatField()
    valor_ejecutado = models.FloatField()
    valor_pagado = models.FloatField()

    def __unicode__(self):
        return smart_unicode(self.gestor)