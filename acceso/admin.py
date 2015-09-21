from django.contrib import admin
from .models import Ciclo,Componente, Modulo, Actividad, Encargado, Entregables, Valor, Evidencia, Corte

class ModuloAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')

class EvidenciaAdmin(admin.ModelAdmin):
    list_display = ('radicado','ciclo','componente','modulo','actividad','encargado')
    search_fields = ('radicado__numero',)

admin.site.register(Ciclo)
admin.site.register(Componente)
admin.site.register(Modulo,ModuloAdmin)
admin.site.register(Actividad)
admin.site.register(Encargado)
admin.site.register(Entregables)
admin.site.register(Valor)
admin.site.register(Evidencia,EvidenciaAdmin)
admin.site.register(Corte)