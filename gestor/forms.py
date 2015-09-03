from django import forms
from .models import Gestor

class GestorSoporteForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['hv','certificacion','rut','contrato']

class GestorSeguroForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['seguro_enero','seguro_febrero','seguro_marzo','seguro_abril',
                  'seguro_mayo','seguro_junio','seguro_julio','seguro_agosto',
                  'seguro_septiembre','seguro_octubre','seguro_noviembre','seguro_diciembre']