from django.contrib import admin
from .models import Masivo, Actividad, Entregable, Grupo, SoporteEntregableEscuelaTic, ParticipanteEscuelaTic, EvidenciaEscuelaTic, Valor, Corte

admin.site.register(Masivo)
admin.site.register(Actividad)
admin.site.register(Entregable)
admin.site.register(Grupo)
admin.site.register(SoporteEntregableEscuelaTic)
admin.site.register(ParticipanteEscuelaTic)
admin.site.register(EvidenciaEscuelaTic)
admin.site.register(Valor)
admin.site.register(Corte)

# Register your models here.