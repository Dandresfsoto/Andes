from django import forms
from .models import Formador

class FormadorSoporteForm(forms.ModelForm):
    class Meta:
        model = Formador
        fields = ['hv','certificacion','rut','contrato']

class FormadorSeguroForm(forms.ModelForm):
    class Meta:
        model = Formador
        fields = ['seguro_enero','seguro_febrero','seguro_marzo','seguro_abril',
                  'seguro_mayo','seguro_junio','seguro_julio','seguro_agosto',
                  'seguro_septiembre','seguro_octubre','seguro_noviembre','seguro_diciembre']