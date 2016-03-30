from django.db import models
from formador.models import Formador
from municipio.models import Municipio
from django.utils.encoding import smart_unicode
from region.models import Region
from django.contrib.auth.models import User
import os
from time import localtime, strftime
from departamento.models import Departamento
from django.contrib.auth.models import User

def content_file_name(instance, filename):
    path = os.path.join('Formacion', 'Formadores Tipo 2', smart_unicode(instance.grupo.formador.region),'Archivos Masivos',smart_unicode(instance.grupo.formador.nombre),smart_unicode(instance.grupo.nombre),strftime("%d-%m-%Y %H-%M-%S", localtime()))
    path = path.replace(' \\','\\').replace('\\ ','\\')
    if not os.path.exists(path):
        os.makedirs(path)
    return '/'.join([path,filename])

def upload_soporte_escuela(instance, filename):
    path = os.path.join('Formacion', 'Formadores Tipo 2', smart_unicode(instance.grupo.formador.region),smart_unicode(instance.grupo.formador.nombre),smart_unicode(instance.grupo.nombre),smart_unicode(instance.entregable.actividad.nombre),smart_unicode(instance.entregable.id))
    path = path.replace(' \\','\\').replace('\\ ','\\')
    if not os.path.exists(path):
        os.makedirs(path)
    file = filename.split("//")
    return '/'.join([path,file[len(file)-1]])

def content_file_name_tipo1(instance, filename):
    path = os.path.join('Formacion', 'Formadores Tipo 1', smart_unicode(instance.grupo.formador.region),'Archivos Masivos',smart_unicode(instance.grupo.formador.nombre),smart_unicode(instance.grupo.nombre),strftime("%d-%m-%Y %H-%M-%S", localtime()))
    path = path.replace(' \\','\\').replace('\\ ','\\')
    if not os.path.exists(path):
        os.makedirs(path)
    return '/'.join([path,filename])

def upload_soporte_escuela_tipo1(instance, filename):
    path = os.path.join('Formacion', 'Formadores Tipo 1', smart_unicode(instance.grupo.formador.region),smart_unicode(instance.grupo.formador.nombre),smart_unicode(instance.grupo.nombre),smart_unicode(instance.entregable.actividad.nombre),smart_unicode(instance.entregable.id))
    path = path.replace(' \\','\\').replace('\\ ','\\')
    if not os.path.exists(path):
        os.makedirs(path)
    file = filename.split("//")
    return '/'.join([path,file[len(file)-1]])

class Grupo(models.Model):
    formador = models.ForeignKey(Formador)
    municipio = models.ForeignKey(Municipio)
    nombre = models.CharField(blank=True,max_length=1000)
    direccion = models.TextField(blank=True,max_length=1000)
    horario = models.TextField(blank=True,max_length=2000)

    def __unicode__(self):
        return smart_unicode("%s - %s" % (self.formador,self.nombre))


    def save(self, *args, **kwargs):
        super(Grupo,self).save(*args, **kwargs)
        entregables = Entregable.objects.all()
        grupo = Grupo.objects.get(pk=self.pk)
        if SoporteEntregableEscuelaTic.objects.filter(grupo__pk=self.pk).count() == 0:
            for entregable in entregables:
                nuevo = SoporteEntregableEscuelaTic(grupo=grupo,entregable=entregable)
                nuevo.save()

class GrupoDocentes(models.Model):
    formador = models.ForeignKey(Formador)
    municipio = models.ForeignKey(Municipio)
    nombre = models.CharField(blank=True,max_length=1000)
    direccion = models.TextField(blank=True,max_length=1000,null=True)
    horario = models.TextField(blank=True,max_length=2000,null=True)

    def __unicode__(self):
        return smart_unicode("%s - %s" % (self.formador,self.nombre))

    def save(self, *args, **kwargs):
        super(GrupoDocentes,self).save(*args, **kwargs)
        entregables = EntregableDocentes.objects.all()
        grupo = GrupoDocentes.objects.get(pk=self.pk)
        if SoporteEntregableDocente.objects.filter(grupo__pk=self.pk).count() == 0:
            for entregable in entregables:
                nuevo = SoporteEntregableDocente(grupo=grupo,entregable=entregable)
                nuevo.save()

class ParticipanteEscuelaTic(models.Model):
    formador = models.ForeignKey(Formador)
    grupo = models.ForeignKey(Grupo)

    numero = models.BigIntegerField(blank=True,null=True)

    institucion = models.CharField(max_length=200,blank=True,null=True)

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.BigIntegerField(unique=True,error_messages={'unique':"Este numero de identificacion ya ha sido registrado"})
    genero = models.CharField(max_length=100)
    nivel_educativo = models.CharField(max_length=100,blank=True,null=True)
    telefono = models.CharField(blank=True,max_length=100,null=True)
    correo = models.EmailField(blank=True,max_length=200,null=True)
    poblacion = models.CharField(blank=True,max_length=200,null=True)
    codigo_anspe = models.CharField(blank=True,max_length=200,null=True)
    tipo_proyecto = models.CharField(blank=True,max_length=200,null=True)
    grupo_conformacion = models.CharField(blank=True,max_length=200,null=True)

    aprobado = models.BooleanField(default=True)

    def __unicode__(self):
        return smart_unicode(self.cedula)


    def save(self, *args, **kwargs):
        super(ParticipanteEscuelaTic,self).save(*args, **kwargs)
        entregables = Entregable.objects.all()
        participante = ParticipanteEscuelaTic.objects.get(pk=self.pk)
        individuales = [5,9,11]
        if participante.formador.region.id == 1:
            valor = Valor.objects.get(pk=1)
        else:
            valor = Valor.objects.get(pk=2)
        if EvidenciaEscuelaTic.objects.filter(participante__pk=self.pk).count() == 0:
            for entregable in entregables:
                nuevo = EvidenciaEscuelaTic(entregable=entregable,participante=participante,valor=valor)
                if entregable.id not in individuales:
                    pass
                    #nuevo.soporte = SoporteEntregableEscuelaTic.objects.filter(grupo__id=self.grupo.id).get(entregable__id=entregable.id)
                nuevo.save()

class RadicadoFormacion(models.Model):
    numero = models.BigIntegerField()
    dane_ie = models.CharField(max_length=100,blank=True,null=True)
    nombre_ie = models.CharField(max_length=500,blank=True,null=True)
    dane_sede = models.CharField(max_length=100,blank=True,null=True)
    nombre_sede = models.CharField(max_length=500,blank=True,null=True)

    def __unicode__(self):
        return smart_unicode(self.numero)

class AreaCurricular(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return smart_unicode(self.nombre)

class Grado(models.Model):
    grado = models.CharField(max_length=100)

    def __unicode__(self):
        return smart_unicode(self.grado)

class Genero(models.Model):
    genero = models.CharField(max_length=100)

    def __unicode__(self):
        return smart_unicode(self.genero)

class Competencias(models.Model):
    competencia = models.CharField(max_length=100)

    def __unicode__(self):
        return smart_unicode(self.competencia)

class GrupoPoblacional(models.Model):
    grupo_poblacional = models.CharField(max_length=100)

    def __unicode__(self):
        return smart_unicode(self.grupo_poblacional)

class ParticipanteDocente(models.Model):
    formador = models.ForeignKey(Formador)
    grupo = models.ForeignKey(GrupoDocentes)
    radicado = models.ForeignKey(RadicadoFormacion)

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.BigIntegerField(unique=True,error_messages={'unique':"Este numero de identificacion ya ha sido registrado"})
    correo = models.EmailField(blank=True,max_length=200,null=True)
    telefono_fijo = models.CharField(blank=True,max_length=100,null=True)
    celular = models.CharField(blank=True,max_length=100,null=True)

    area = models.ForeignKey(AreaCurricular,blank=True,null=True)
    grado = models.ForeignKey(Grado,blank=True,null=True)
    tipo_beneficiario = models.CharField(blank=True,max_length=100,null=True)
    genero = models.ForeignKey(Genero,blank=True,null=True)

    nombre_proyecto = models.CharField(blank=True,max_length=500,null=True)
    definicion_problema = models.TextField(blank=True,max_length=1000,null=True)
    area_proyecto = models.CharField(blank=True,max_length=500,null=True)
    competencia = models.ForeignKey(Competencias,blank=True,null=True)
    grupo_poblacional = models.ForeignKey(GrupoPoblacional,blank=True,null=True)

    def __unicode__(self):
        return smart_unicode(self.cedula)


    def save(self, *args, **kwargs):
        super(ParticipanteDocente,self).save(*args, **kwargs)
        entregables = EntregableDocentes.objects.all()
        participante = ParticipanteDocente.objects.get(pk=self.pk)
        if EvidenciaDocentes.objects.filter(participante__pk=self.pk).count() == 0:
            for entregable in entregables:
                valor = ValorDocente.objects.get(id=1)
                nuevo = EvidenciaDocentes(entregable=entregable,participante=participante,valor=valor)
                nuevo.save()

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return smart_unicode(self.nombre)

class ActividadDocentes(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return smart_unicode(self.nombre)

class EntregableDocentes(models.Model):
    actividad = models.ForeignKey(ActividadDocentes)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=2000)

    def __unicode__(self):
        return smart_unicode("%s - %s" % (self.actividad.nombre,self.nombre))

class Entregable(models.Model):
    actividad = models.ForeignKey(Actividad)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=2000)

    def __unicode__(self):
        return smart_unicode("%s - %s" % (self.actividad.nombre,self.nombre))

class Valor(models.Model):
    valor = models.FloatField()

    def __str__(self):
        return "%i" %self.valor

class ValorDocente(models.Model):
    region = models.ForeignKey(Region)
    entregable = models.ForeignKey(EntregableDocentes)
    valor = models.FloatField()

    def __str__(self):
        return "%s - %s - %i" % (self.region,self.entregable,self.valor)

class Corte(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    region = models.ForeignKey(Region,related_name='corte_formacion')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.titulo)

class CorteDocente(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    region = models.ForeignKey(Region,related_name='corte_formacion_docente')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.titulo)

class Masivo(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    grupo = models.ForeignKey(Grupo)
    archivo = models.FileField(upload_to=content_file_name,max_length=2000)
    usuario = models.ForeignKey(User,blank=True,null=True)
    resultado = models.FileField(upload_to=content_file_name,blank=True,max_length=2000)

    def __unicode__(self):
        return smart_unicode(self.fecha)

class MasivoDocente(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    grupo = models.ForeignKey(GrupoDocentes)
    archivo = models.FileField(upload_to=content_file_name,max_length=2000)
    usuario = models.ForeignKey(User,blank=True,null=True)
    resultado = models.FileField(upload_to=content_file_name,blank=True,max_length=2000)

    def __unicode__(self):
        return smart_unicode(self.fecha)

class SoporteEntregableEscuelaTic(models.Model):
    grupo = models.ForeignKey(Grupo)
    entregable = models.ForeignKey(Entregable)
    soporte = models.FileField(upload_to=upload_soporte_escuela,blank=True,null=True,max_length=2000)

    def __unicode__(self):
        return smart_unicode("%s - %s - %s" % (self.grupo.formador.nombre,self.grupo,self.entregable))

class SoporteEntregableDocente(models.Model):
    grupo = models.ForeignKey(GrupoDocentes)
    entregable = models.ForeignKey(EntregableDocentes)
    soporte = models.FileField(upload_to=upload_soporte_escuela_tipo1,blank=True,null=True,max_length=2000)
    def __unicode__(self):
        return smart_unicode("%s - %s - %s" % (self.grupo.formador.nombre,self.grupo,self.entregable))

class EvidenciaEscuelaTic(models.Model):
    soporte = models.ForeignKey(SoporteEntregableEscuelaTic,null=True,blank=True)
    entregable = models.ForeignKey(Entregable)
    participante = models.ForeignKey(ParticipanteEscuelaTic)
    valor = models.ForeignKey(Valor)
    corte = models.ForeignKey(Corte, null=True,blank=True)
    usuario = models.ForeignKey(User, null=True,blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return smart_unicode(self.participante)

class EvidenciaDocentes(models.Model):
    soporte = models.ForeignKey(SoporteEntregableDocente,null=True,blank=True)
    entregable = models.ForeignKey(EntregableDocentes)
    participante = models.ForeignKey(ParticipanteDocente)
    valor = models.ForeignKey(ValorDocente)
    corte = models.ForeignKey(CorteDocente, null=True,blank=True)
    usuario = models.ForeignKey(User, null=True,blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return smart_unicode(self.participante)

class CargasMasivas(models.Model):
    archivo = models.FileField(upload_to="Cargas Masivas/Escuela TIC/")

    def __unicode__(self):
        return smart_unicode(self.id)

class RevisionInterventoriaDocente(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User)
    ip = models.IPAddressField(null=True,blank=True)
    region = models.ForeignKey(Region)
    participante = models.ForeignKey(ParticipanteDocente)
    registrado = models.BooleanField(default=False)

    def __unicode__(self):
        return smart_unicode(self.fecha)

class RevisionInterventoriaDocenteSoporte(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User)
    ip = models.IPAddressField(null=True,blank=True)
    evidencia = models.ForeignKey(EvidenciaDocentes,null=True,blank=True)

    def __unicode__(self):
        return smart_unicode(self.fecha)

class RevisionInterventoriaDocenteSoporteActividades(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User)
    ip = models.IPAddressField(null=True,blank=True)
    path = models.CharField(max_length=500,blank=True,null=True)

    def __unicode__(self):
        return smart_unicode(self.fecha)

class RevisionInterventoriaEscuelaTic(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User)
    ip = models.IPAddressField(null=True,blank=True)
    region = models.ForeignKey(Region)
    participante = models.ForeignKey(ParticipanteEscuelaTic)
    registrado = models.BooleanField(default=False)

    def __unicode__(self):
        return smart_unicode(self.fecha)

class RevisionInterventoriaEscuelaTicSoporte(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User)
    ip = models.IPAddressField(null=True,blank=True)
    evidencia = models.ForeignKey(EvidenciaEscuelaTic,blank=True,null=True)

    def __unicode__(self):
        return smart_unicode(self.fecha)

class RevisionInterventoriaEscuelaTicSoporteActividades(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User)
    ip = models.IPAddressField(null=True,blank=True)
    path = models.CharField(max_length=500,blank=True,null=True)

    def __unicode__(self):
        return smart_unicode(self.fecha)

class CargaMasivaListados(models.Model):
    archivo = models.FileField(upload_to='Carga Masiva Listados')
    soportes = models.FileField(upload_to='Carga Masiva Listados')
    resultado = models.FileField(upload_to='Carga Masiva Listados',null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.archivo)