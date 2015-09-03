# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_unicode
from departamento.models import Departamento

class Region(models.Model):
    nombre = models.CharField(max_length=100,blank=False)
    departamentos = models.ManyToManyField(Departamento)
    imagen = models.ImageField(upload_to='Region/Mapa')

    def __unicode__(self):
        return smart_unicode(self.nombre)

    class Meta:
        permissions = (
            ('region_acceso', 'Acceso a region'),
            ('region_acceso_cpe','Acceso a region cpe'),
            ('region_acceso_andes','Acceso a region andes'),
            ('acceso', 'Rol asignado al eje de Acceso'),
            ('formacion','Rol asignado al eje de formacion'),
            ('administrativo','Rol asignado al eje Administrativo'),
            ('financiero','Rol asignado al eje Financiero'),
        )