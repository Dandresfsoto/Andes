from django.db import models
from django.utils.encoding import smart_unicode

class Radicado(models.Model):
    numero = models.IntegerField()

    def __unicode__(self):
        return smart_unicode(self.numero)