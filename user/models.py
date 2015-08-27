from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    usuario = models.OneToOneField(User,related_name='nombre_usuario')
    imagen = models.ImageField(upload_to="Usuarios/Imagenes/")

    def __unicode__(self):
        return '%d: %s' % (self.id,self.usuario.username)