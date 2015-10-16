from django import forms
from django.forms.models import modelformset_factory
from .models import LiquidacionGestor, LiquidacionFormador

class LiquidacionGestorForm(forms.ModelForm):
    class Meta:
        model = LiquidacionGestor
        fields = ['gestor','fecha_terminacion','contrato','valor_inicial','valor_ejecutado','valor_pagado']
        widgets = {
            'gestor': forms.Select(attrs={'style':'width:100%;'}),
            'fecha_terminacion': forms.TextInput(attrs={'style':'width:100%;'}),
            'contrato': forms.TextInput(attrs={'style':'width:100%;'}),
            'valor_inicial': forms.NumberInput(attrs={'style':'width:100%;'}),
            'valor_ejecutado': forms.NumberInput(attrs={'style':'width:100%;'}),
            'valor_pagado': forms.NumberInput(attrs={'style':'width:100%;'}),
        }

class LiquidacionFormadorForm(forms.ModelForm):
    class Meta:
        model = LiquidacionFormador
        fields = ['formador','fecha_terminacion','contrato','valor_inicial','valor_ejecutado','valor_pagado']
        widgets = {
            'formador': forms.Select(attrs={'style':'width:100%;'}),
            'fecha_terminacion': forms.TextInput(attrs={'style':'width:100%;'}),
            'contrato': forms.TextInput(attrs={'style':'width:100%;'}),
            'valor_inicial': forms.NumberInput(attrs={'style':'width:100%;'}),
            'valor_ejecutado': forms.NumberInput(attrs={'style':'width:100%;'}),
            'valor_pagado': forms.NumberInput(attrs={'style':'width:100%;'}),
        }