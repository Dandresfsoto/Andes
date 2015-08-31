from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode

class UserProfile(models.Model):
    usuario = models.OneToOneField(User,related_name='nombre_usuario')
    mail = models.EmailField(max_length=30)
    imagen = models.ImageField(upload_to="Usuarios/Imagenes/")

    def __unicode__(self):
        return smart_unicode(self.usuario)