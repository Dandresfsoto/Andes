from django.contrib import admin
from .models import Masivo, Actividad, Entregable, Grupo, SoporteEntregableEscuelaTic, ParticipanteEscuelaTic

admin.site.register(Masivo)
admin.site.register(Actividad)
admin.site.register(Entregable)
admin.site.register(Grupo)
admin.site.register(SoporteEntregableEscuelaTic)
admin.site.register(ParticipanteEscuelaTic)

# Register your models here.
