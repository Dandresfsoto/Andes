from django.db import models
from django.utils.encoding import smart_unicode

class Beneficiario(models.Model):
    beneficiario = models.CharField(max_length=100)
    homologacion = models.IntegerField()

    def __unicode__(self):
        return smart_unicode(self.beneficiario)