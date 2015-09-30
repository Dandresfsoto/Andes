from django import forms
from .models import Gestor

class NuevoForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['region','nombre','cedula','celular','correo','fecha_contratacion']

class GestorFotoForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['foto']

class GestorSoporteForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['hv','certificacion','rut','contrato','fotocopia_cedula','antecedentes_judiciales','antecedentes_contraloria']

class GestorInformacionForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['celular','correo','cargo','profesion','banco','tipo_cuenta','numero_cuenta','eps','pension','arl']

class GestorSeguroForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['seguro_enero','seguro_febrero','seguro_marzo','seguro_abril',
                  'seguro_mayo','seguro_junio','seguro_julio','seguro_agosto',
                  'seguro_septiembre','seguro_octubre','seguro_noviembre','seguro_diciembre']