from django import forms
from .models import Formador

class NuevoForm(forms.ModelForm):
    class Meta:
        CHOICES = Formador.objects.all().order_by('nombre')
        opciones = [("","")]
        for opcion in CHOICES:
            opciones.append((opcion.nombre,opcion.nombre))

        model = Formador
        fields = ['region','tipo','nombre','cedula','celular','correo','fecha_contratacion','reemplazo']
        widgets = {
            'reemplazo': forms.Select(choices=(opciones),attrs={'style':'width:100%;'}),
        }

class FormadorFotoForm(forms.ModelForm):
    class Meta:
        model = Formador
        fields = ['foto']

class FormadorSoporteForm(forms.ModelForm):
    class Meta:
        model = Formador
        fields = ['hv','certificacion','rut','contrato','contrato_plan_choque','fotocopia_cedula','antecedentes_judiciales','antecedentes_contraloria']

class FormadorInformacionForm(forms.ModelForm):
    class Meta:
        model = Formador
        fields = ['nombre',
                  'cedula',
                  'celular',
                  'correo',
                  'fecha_contratacion',
                  'fecha_terminacion',
                  'reemplazo',
                  'cargo',
                  'profesion',
                  'banco',
                  'tipo_cuenta',
                  'numero_cuenta',
                  'eps',
                  'pension',
                  'arl']
        widgets = {
            'nombre': forms.TextInput(attrs={'style':'width:100%;','required':''}),
            'cedula': forms.NumberInput(attrs={'style':'width:100%;','required':''}),
            'celular': forms.TextInput(attrs={'style':'width:100%;','required':''}),
            'correo': forms.EmailInput(attrs={'style':'width:100%;','required':''}),
            'fecha_contratacion': forms.TextInput(attrs={'style':'width:100%;','required':''}),
            'fecha_terminacion': forms.TextInput(attrs={'style':'width:100%;'}),
            'cargo': forms.TextInput(attrs={'style':'width:100%;'}),
            'profesion': forms.TextInput(attrs={'style':'width:100%;'}),
            'banco': forms.TextInput(attrs={'style':'width:100%;'}),
            'tipo_cuenta': forms.TextInput(attrs={'style':'width:100%;'}),
            'numero_cuenta': forms.TextInput(attrs={'style':'width:100%;'}),
            'eps': forms.TextInput(attrs={'style':'width:100%;'}),
            'pension': forms.TextInput(attrs={'style':'width:100%;'}),
            'arl': forms.TextInput(attrs={'style':'width:100%;'}),
        }

class FormadorSeguroForm(forms.ModelForm):
    class Meta:
        model = Formador
        fields = ['seguro_enero','seguro_febrero','seguro_marzo','seguro_abril',
                  'seguro_mayo','seguro_junio','seguro_julio','seguro_agosto',
                  'seguro_septiembre','seguro_octubre','seguro_noviembre','seguro_diciembre']