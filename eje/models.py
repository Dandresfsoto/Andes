from django.db import models
from django.utils.encoding import smart_unicode

class Eje(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return smart_unicode(self.nombre)
