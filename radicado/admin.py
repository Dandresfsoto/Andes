from django.contrib import admin
from .models import Radicado
# Register your models here.

class RadicadoAdmin(admin.ModelAdmin):
    list_display = ('numero','municipio')
    search_fields = ['numero']
    list_filter = ('municipio__departamento',)

admin.site.register(Radicado,RadicadoAdmin)