from django.utils.encoding import smart_unicode
from django.db import models
from diplomado.models import Diplomado
from radicado.models import Radicado
from participantes.models import Participante
from area_proyecto.models import AreaProyecto
from competencia.models import Competencia
from poblacion.models import Poblacion

class Proyecto(models.Model):
    diplomado = models.ForeignKey(Diplomado)
    radicado = models.ForeignKey(Radicado)
    participante = models.ForeignKey(Participante)
    nombre = models.TextField(max_length=320)
    problema = models.TextField(max_length=1000)
    area = models.ForeignKey(AreaProyecto)
    competencia = models.ForeignKey(Competencia)
    poblacion = models.ForeignKey(Poblacion)
    archivo = models.FileField(upload_to="Participantes/Proyectos/")

    def __unicode__(self):
        return smart_unicode(self.nombre)