from django.db import models
from formacion.models import Grupo
from formador.models import Formador
from region.models import Region
from django.utils.encoding import smart_unicode
from formacion.models import ParticipanteDocente

class CodigoMasivo(models.Model):
    codigo = models.BigIntegerField(unique=True)
    generado = models.BooleanField(editable=False,default=False)

    def __unicode__(self):
        return smart_unicode(self.codigo)


class CodigoMasivo_Docentes(models.Model):
    codigo = models.BigIntegerField(unique=True)
    departamento = models.CharField(max_length=200,blank=True,null=True)
    municipio = models.CharField(max_length=200,blank=True,null=True)
    formador = models.CharField(max_length=200,blank=True,null=True)
    cedula = models.CharField(max_length=200,blank=True,null=True)
    lugar = models.CharField(max_length=200,blank=True,null=True)
    region = models.ForeignKey(Region)


    def __unicode__(self):
        return smart_unicode(self.codigo)


class ParticipanteDocenteMasivo(models.Model):
    codigo_masivo = models.ForeignKey(CodigoMasivo_Docentes)
    nombre = models.CharField(max_length=200,blank=True,null=True)
    cedula = models.CharField(max_length=200,blank=True,null=True)
    institucion = models.CharField(max_length=200,blank=True,null=True)
    sede = models.CharField(max_length=200,blank=True,null=True)
    correo = models.CharField(max_length=200,blank=True,null=True)
    telefono = models.CharField(max_length=200,blank=True,null=True)


    def __unicode__(self):
        return smart_unicode(self.cedula)








class CodigoMasivo_Proyectoss(models.Model):
    codigo = models.BigIntegerField(unique=True)
    nombre_proyecto = models.CharField(max_length=200,blank=True,null=True)
    definicion_problema = models.TextField(max_length=10000,blank=True,null=True)
    pregunta_proyecto = models.CharField(max_length=200,blank=True,null=True)
    objetivos = models.TextField(max_length=10000,blank=True,null=True)
    secuencias = models.TextField(max_length=10000,blank=True,null=True)
    area = models.CharField(max_length=200,blank=True,null=True)
    competencia = models.CharField(max_length=200,blank=True,null=True)
    region = models.ForeignKey(Region)


    def __unicode__(self):
        return smart_unicode(self.codigo)


class ParticipanteProyectoMasivos(models.Model):
    codigo_masivo = models.ForeignKey(CodigoMasivo_Proyectos)
    nombre = models.CharField(max_length=200,blank=True,null=True)
    celular = models.CharField(max_length=200,blank=True,null=True)
    correo = models.CharField(max_length=200,blank=True,null=True)
    departamento = models.CharField(max_length=200,blank=True,null=True)
    municipio = models.CharField(max_length=200,blank=True,null=True)
    institucion = models.CharField(max_length=200,blank=True,null=True)
    sede = models.CharField(max_length=200,blank=True,null=True)
    dane = models.CharField(max_length=200,blank=True,null=True)
    direccion = models.CharField(max_length=200,blank=True,null=True)
    localidad = models.CharField(max_length=200,blank=True,null=True)


    def __unicode__(self):
        return smart_unicode(self.cedula)











class ParticipanteEscuelaTicTrucho(models.Model):
    codigo_masivo = models.ForeignKey(CodigoMasivo)
    region = models.ForeignKey(Region)
    departamento = models.CharField(max_length=200,blank=True,null=True)
    municipio = models.CharField(max_length=200,blank=True,null=True)
    institucion = models.CharField(max_length=200,blank=True,null=True)
    grupo = models.ForeignKey(Grupo)
    formador = models.ForeignKey(Formador)

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

    def __unicode__(self):
        return smart_unicode(self.cedula)


class CodigoMasivoN1_S2(models.Model):
    codigo = models.BigIntegerField(unique=True)

    def __unicode__(self):
        return smart_unicode(self.codigo)


class ParticipanteN1_S2(models.Model):
    codigo_masivo = models.ForeignKey(CodigoMasivoN1_S2)
    participante = models.ForeignKey(ParticipanteDocente)

    def __unicode__(self):
        return smart_unicode(self.participante.cedula)

class CargasMasivas(models.Model):
    archivo = models.FileField(upload_to="Cargas Masivas/Escuela TIC/Adicionales/")

    def __unicode__(self):
        return smart_unicode(self.id)

class Nivel1_Sesion1_1(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_2(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_3(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_4(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_5(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_6(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_7(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_8(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_9(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_10(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_11(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_12(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_REDA(models.Model):
    recurso = models.CharField(max_length=200)
    portal = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __unicode__(self):
        return smart_unicode(self.recurso)
class Nivel1_Sesion2(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion3(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel1_Sesion4_preguntas_aleatorias(models.Model):
    pregunta = models.CharField(max_length=1000)
    respuesta = models.CharField(max_length=1000)
    incorrecta_1 = models.CharField(max_length=1000)
    incorrecta_2 = models.CharField(max_length=1000)
    def __unicode__(self):
        return smart_unicode(self.pregunta)

class Nivel1_Sesion4_1(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel1_Sesion4_2(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel1_Sesion4_3(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel1_Sesion4_4(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel1_Sesion4_5(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel4_Sesion1_1(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel4_Sesion1_2(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)



class Nivel4_Sesion2_1(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel4_Sesion2_2(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel4_Sesion2_3(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)





class Nivel4_Sesion3_1(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel4_Sesion3_2(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel4_Sesion3_3(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel4_Sesion3_4(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel4_Sesion3_5(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel4_Sesion3_6(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)



class Nivel1_Sesion2_1(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel1_Sesion2_2(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel1_Sesion2_3(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel1_Sesion2_4(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel3_Sesion3_1(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)

class Nivel3_Sesion3_2(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)



class Nivel3_Sesion1_1(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)


class Nivel3_Sesion1_2(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)



class Nivel3_Sesion2_1(models.Model):
    respuesta = models.CharField(max_length=10000)
    def __unicode__(self):
        return smart_unicode(self.respuesta)