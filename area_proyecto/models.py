from django.db import models
from django.utils.encoding import smart_unicode

class AreaProyecto(models.Model):
    nombre = models.CharField(max_length=100)
    homologacion = models.IntegerField()

    def __unicode__(self):
        return smart_unicode(self.nombre)