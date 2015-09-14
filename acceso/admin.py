from django.contrib import admin
from .models import Ciclo,Componente, Modulo, Actividad, Encargado, Entregables, Valor, Evidencia, Corte

class ModuloAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')

admin.site.register(Ciclo)
admin.site.register(Componente)
admin.site.register(Modulo,ModuloAdmin)
admin.site.register(Actividad)
admin.site.register(Encargado)
admin.site.register(Entregables)
admin.site.register(Valor)
admin.site.register(Evidencia)
admin.site.register(Corte)