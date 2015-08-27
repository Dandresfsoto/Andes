from django.contrib import admin
from region import models
from guardian.admin import GuardedModelAdmin
from functools import partial

class RegionAdmin(GuardedModelAdmin):
    list_display = ('nombre',)
    @property
    def queryset(self):
        return partial(self.get_queryset)

admin.site.register(models.Region,RegionAdmin)
