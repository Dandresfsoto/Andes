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
        fields = ['hv','certificacion','rut','contrato','fotocopia_cedula','antecedentes_judiciales','antecedentes_contraloria']

class FormadorInformacionForm(forms.ModelForm):
    class Meta:
        model = Formador
        fields = ['celular','correo','cargo','profesion','banco','tipo_cuenta','numero_cuenta','eps','pension','arl']

class FormadorSeguroForm(forms.ModelForm):
    class Meta:
        model = Formador
        fields = ['seguro_enero','seguro_febrero','seguro_marzo','seguro_abril',
                  'seguro_mayo','seguro_junio','seguro_julio','seguro_agosto',
                  'seguro_septiembre','seguro_octubre','seguro_noviembre','seguro_diciembre']