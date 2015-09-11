from django.contrib import admin
from .models import Municipio

class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_filter = ('departamento',)


admin.site.register(Municipio,MunicipioAdmin)
