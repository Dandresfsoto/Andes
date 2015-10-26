from django.db import models
from django.utils.encoding import smart_unicode
from departamento.models import Departamento

class Municipio(models.Model):
    nombre = models.CharField(max_length=100,blank=False)
    departamento = models.ForeignKey(Departamento)
    codigo = models.CharField(max_length=100,blank=True)

    class Meta:
        ordering = ['nombre']

    def __unicode__(self):
        return smart_unicode('%s - %s' % (self.nombre, self.departamento))