# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_unicode

class Departamento(models.Model):
    nombre = models.CharField(max_length=100,blank=False)
    codigo = models.CharField(max_length=100,blank=True)

    class Meta:
        ordering = ['nombre']

    def __unicode__(self):
        return smart_unicode(self.nombre)