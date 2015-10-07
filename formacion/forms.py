from django import forms
from formacion.models import Grupo, ParticipanteEscuelaTic

class NuevoGrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['formador','municipio','nombre','direccion','horario']
        widgets = {
            'municipio': forms.Select(attrs={'style':'width:100%;','required':''}),
            'nombre': forms.TextInput(attrs={'style':'width:100%;','required':''}),
            'direccion': forms.Textarea(attrs={'style':'width:100%;','rows':5}),
            'horario': forms.Textarea(attrs={'style':'width:100%;','rows':5}),
        }

class NuevoParticipanteForm(forms.ModelForm):
    class Meta:
        model = ParticipanteEscuelaTic
        fields = ['formador','grupo','poblacion','genero','nombres','apellidos','institucion','correo','telefono','cedula']
        widgets = {
            'poblacion': forms.Select(attrs={'style':'width:100%;','required':''}, choices=(('Padre de familia','Padre de familia'),('Acudiente','Acudiente'))),
            'genero': forms.Select(attrs={'style':'width:100%;','required':''}, choices=(('Masculino','Masculino'),('Femenino','Femenino'))),
            'nombres': forms.TextInput(attrs={'style':'width:100%;','required':''}),
            'apellidos': forms.TextInput(attrs={'style':'width:100%;','required':''}),
            'institucion': forms.TextInput(attrs={'style':'width:100%;','required':''}),
            'correo': forms.EmailInput(attrs={'style':'width:100%;'}),
            'telefono': forms.TextInput(attrs={'style':'width:100%;'}),
            'cedula': forms.NumberInput(attrs={'style':'width:100%;','required':''}),
        }