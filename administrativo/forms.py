from django import forms
from .models import Informes, Obligacion, SoporteObligacion

class NuevoInformeForm(forms.ModelForm):
    class Meta:
        model = Informes
        fields = ['region','nombre','mes','excel_acceso','soporte_acceso','excel_formacion','soporte_formacion']
        widgets = {
            'nombre': forms.TextInput(attrs={'style':'width:100%;','required':''}),
            'mes': forms.Select(attrs={'style':'width:100%;','required':''}, choices=(('Enero','Enero'),('Febrero','Febrero'),
                                                                                      ('Marzo','Marzo'),('Abril','Abril'),
                                                                                      ('Mayo','Mayo'),('Junio','Junio'),
                                                                                      ('Julio','Julio'),('Agosto','Agosto'),
                                                                                      ('Septiembre','Septiembre'),('Octubre','Octubre'),
                                                                                      ('Noviembre','Noviembre'),('Diciembre','Diciembre'))),
        }

class NuevaObligacionForm(forms.ModelForm):
    class Meta:
        model = Obligacion
        fields = ['region','numero','descripcion']
        widgets = {
            'numero': forms.NumberInput(attrs={'style':'width:100%;','required':''}),
            'descripcion': forms.Textarea(attrs={'style':'width:100%;','required':''}),
        }

class NuevoSoporteObligacionForm(forms.ModelForm):
    class Meta:
        model = SoporteObligacion
        fields = ['mes','obligacion','descripcion','soporte']
        widgets = {
            'mes': forms.Select(attrs={'style':'width:100%;','required':''}, choices=(('Enero','Enero'),('Febrero','Febrero'),
                                                                                      ('Marzo','Marzo'),('Abril','Abril'),
                                                                                      ('Mayo','Mayo'),('Junio','Junio'),
                                                                                      ('Julio','Julio'),('Agosto','Agosto'),
                                                                                      ('Septiembre','Septiembre'),('Octubre','Octubre'),
                                                                                      ('Noviembre','Noviembre'),('Diciembre','Diciembre'))),
            'descripcion': forms.TextInput(attrs={'style':'width:100%;','required':''}),
        }