from django.db import models
from django.utils.encoding import smart_unicode

class Genero(models.Model):
    genero = models.CharField(max_length=50)
    homologacion = models.CharField(max_length=1)

    def __unicode__(self):
        return smart_unicode(self.genero)