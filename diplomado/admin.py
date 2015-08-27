from django.contrib import admin
from .models import Diplomado
from guardian.admin import GuardedModelAdmin
from functools import partial

class DiplomadoAdmin(GuardedModelAdmin):
    list_display = ('tag','region')
    @property
    def queryset(self):
        return partial(self.get_queryset)


admin.site.register(Diplomado,DiplomadoAdmin)