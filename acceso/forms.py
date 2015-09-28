from django import forms
from django.forms.models import modelformset_factory
from .models import Evidencia, Reasignados

EvidenciaFormSetBase = modelformset_factory(Evidencia,extra=0,fields=('soporte',))

class EvidenciaFormSet(EvidenciaFormSetBase):
    def add_fields(self, form, index):
        super(EvidenciaFormSet, self).add_fields(form, index)
        form.fields['is_checked'] = forms.BooleanField(required=False)
        form.fields['somefield'].widget.attrs['class'] = 'somefieldclass'

class ReasignacionForm(forms.ModelForm):
    class Meta:
        model = Reasignados
        fields = ['gestor_origen','gestor_destino']