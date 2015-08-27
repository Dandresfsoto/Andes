from django.db import models
from django.utils.encoding import smart_unicode

class Grado(models.Model):
    grado = models.CharField(max_length=30)
    homologacion = models.IntegerField()

    def __unicode__(self):
        return smart_unicode(self.grado)