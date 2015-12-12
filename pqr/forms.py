from django import forms
from .models import PqrRespuesta
from region.models import Region
from funcionario.models import Funcionario

class PqrRespuestaForm(forms.ModelForm):
    class Meta:
        region_choice = []
        for region in Region.objects.all():
            region_choice.append(tuple([region.id,region.nombre]))
        funcionario_choice = []
        for funcionario in Funcionario.objects.all():
            funcionario_choice.append(tuple([funcionario.id,funcionario.nombre]))
        model = PqrRespuesta
        fields = ['pqr','region','funcionario','mensaje']
        widgets = {
            'region': forms.Select(attrs={'style':'width:100%;','required':''},choices=(region_choice)),
            'funcionario': forms.Select(attrs={'style':'width:100%;','required':''},choices=(funcionario_choice)),
            'mensaje': forms.Textarea(attrs={'style':'width:100%;','rows':5}),
        }