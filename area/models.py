from django.db import models
from django.utils.encoding import smart_unicode

class AreaCurricular(models.Model):
    nombre = models.CharField(max_length=200)
    homologacion = models.IntegerField()

    def __unicode__(self):
        return smart_unicode(self.nombre)