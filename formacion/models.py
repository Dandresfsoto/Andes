from django.db import models
from formador.models import Formador
from municipio.models import Municipio
from django.utils.encoding import smart_unicode
from region.models import Region
from django.contrib.auth.models import User

def content_file_name(instance, filename):
    return '/'.join(['Formacion', 'Formadores Tipo 2', smart_unicode(instance.grupo.formador.region),'Archivos Masivos',smart_unicode(instance.grupo.formador.nombre),smart_unicode(instance.grupo.nombre),filename])

def upload_soporte_escuela(instance, filename):
    return '/'.join(['Formacion', 'Formadores Tipo 2', smart_unicode(instance.grupo.formador.region),smart_unicode(instance.grupo.formador.nombre),smart_unicode(instance.entregable.actividad.nombre),filename])

class Grupo(models.Model):
    formador = models.ForeignKey(Formador)
    municipio = models.ForeignKey(Municipio)
    nombre = models.CharField(blank=True,max_length=1000)
    direccion = models.TextField(blank=True,max_length=1000)
    horario = models.TextField(blank=True,max_length=2000)

    def __unicode__(self):
        return smart_unicode("%s - %s" % (self.formador,self.nombre))

class ParticipanteEscuelaTic(models.Model):
    formador = models.ForeignKey(Formador)
    grupo = models.ForeignKey(Grupo)

    numero = models.BigIntegerField(blank=True)
    departamento = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)

    institucion = models.CharField(max_length=200,blank=True)

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.BigIntegerField(unique=True,error_messages={'unique':"Este numero de identificacion ya ha sido registrado"})
    genero = models.CharField(max_length=100)
    nivel_educativo = models.CharField(max_length=100)
    telefono = models.CharField(blank=True,max_length=100)
    correo = models.EmailField(blank=True,max_length=200)
    poblacion = models.CharField(blank=True,max_length=200)
    codigo_anspe = models.CharField(blank=True,max_length=200)



    def __unicode__(self):
        return smart_unicode(self.cedula)

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return smart_unicode(self.nombre)

class Entregable(models.Model):
    actividad = models.ForeignKey(Actividad)
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return smart_unicode(self.nombre)

class Valor(models.Model):
    valor = models.FloatField()

    def __str__(self):
        return "%i" %self.valor

class Corte(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    region = models.ForeignKey(Region,related_name='corte_formacion')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.titulo)

class Masivo(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    grupo = models.ForeignKey(Grupo)
    archivo = models.FileField(upload_to=content_file_name,blank=True)
    usuario = models.ForeignKey(User,blank=True,null=True)

    def __unicode__(self):
        return smart_unicode(self.fecha)

class EvidenciaEscuelaTic(models.Model):
    entregable = models.ForeignKey(Entregable)
    participante = models.ForeignKey(ParticipanteEscuelaTic)
    valor = models.ForeignKey(Valor)
    corte = models.ForeignKey(Corte, null=True)

    def __unicode__(self):
        return smart_unicode("%s - %s" % (self.participante,self.entregable.actividad))

class SoporteEntregableEscuelaTic(models.Model):
    grupo = models.ForeignKey(Grupo)
    entregable = models.ForeignKey(Entregable)
    soporte = models.FileField(upload_to=upload_soporte_escuela,blank=True,null=True)

    def __unicode__(self):
        return smart_unicode("%s - %s - %s" % (self.grupo.formador.nombre,self.grupo,self.entregable))