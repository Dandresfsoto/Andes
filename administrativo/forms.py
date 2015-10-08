from django import forms
from .models import Informes

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