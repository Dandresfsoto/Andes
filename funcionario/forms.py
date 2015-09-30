from django import forms
from .models import Funcionario

class NuevoFuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['region','nombre','cedula','celular','correo','fecha_contratacion','eje']

class FuncionarioFotoForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['foto']

class FuncionarioSoporteForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['hv','certificacion','rut','contrato','fotocopia_cedula','antecedentes_judiciales','antecedentes_contraloria']

class FuncionarioInformacionForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['celular','correo','cargo','profesion','banco','tipo_cuenta','numero_cuenta','eps','pension','arl']

class FuncionarioSeguroForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['seguro_enero','seguro_febrero','seguro_marzo','seguro_abril',
                  'seguro_mayo','seguro_junio','seguro_julio','seguro_agosto',
                  'seguro_septiembre','seguro_octubre','seguro_noviembre','seguro_diciembre']