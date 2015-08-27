from django.db import models
from region.models import Region
from django.utils.encoding import smart_unicode


class Diplomado(models.Model):
    nombre = models.CharField(max_length=200)
    tag = models.CharField(max_length=50)
    region = models.ForeignKey(Region)
    imagen = models.ImageField(upload_to="Region/Diplomado/")

    def __unicode__(self):
        return smart_unicode(self.tag)

    class Meta:
        permissions = (
            ('r1', 'Region 1'),
            ('r4', 'Region 4'),
        )