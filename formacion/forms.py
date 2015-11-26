#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from formacion.models import Grupo, ParticipanteEscuelaTic, Masivo, SoporteEntregableEscuelaTic, EvidenciaEscuelaTic
from departamento.models import Departamento
from municipio.models import Municipio

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
        municipio_choice = []
        for municipio in Municipio.objects.all():
            municipio_choice.append(tuple([municipio.nombre+" - "+municipio.departamento.nombre,municipio.nombre+" - "+municipio.departamento.nombre]))
        model = ParticipanteEscuelaTic
        fields = ['formador','grupo','numero','departamento','municipio','institucion','nombres','apellidos','cedula','genero','nivel_educativo','telefono','correo','poblacion','codigo_anspe','tipo_proyecto','grupo_conformacion']
        widgets = {
            'numero': forms.NumberInput(attrs={'style':'width:100%;'}),
            'departamento': forms.Select(attrs={'style':'width:100%;','required':''}, choices=(Departamento.objects.all().values_list('nombre','nombre'))),
            'municipio': forms.Select(attrs={'style':'width:100%;','required':''}, choices=(municipio_choice)),
            'institucion': forms.TextInput(attrs={'style':'width:100%;'}),
            'nombres': forms.TextInput(attrs={'style':'width:100%;','required':''}),
            'apellidos': forms.TextInput(attrs={'style':'width:100%;','required':''}),
            'cedula': forms.NumberInput(attrs={'style':'width:100%;','required':''}),
            'genero': forms.Select(attrs={'style':'width:100%;','required':''}, choices=(('Masculino','Masculino'),('Femenino','Femenino'))),
            'nivel_educativo': forms.Select(attrs={'style':'width:100%;','required':''}, choices=(('Escolar Sin terminar','Escolar Sin terminar'),('Escolar Terminado','Escolar Terminado'),('Técnico','Técnico'),('Profesional sin terminar','Profesional sin terminar'),('Profesional terminado','Profesional terminado'),('Postgrado','Postgrado'))),
            'telefono': forms.TextInput(attrs={'style':'width:100%;'}),
            'correo': forms.EmailInput(attrs={'style':'width:100%;'}),
            'poblacion': forms.Select(attrs={'style':'width:100%;','required':''}, choices=(('ANSPE','ANSPE'),('RED UNIDOS','RED UNIDOS'),('RED PAPAZ','RED PAPAZ'),('COMUNIDAD EDUCATIVA','COMUNIDAD EDUCATIVA'),('OTROS','OTROS'))),
            'codigo_anspe': forms.TextInput(attrs={'style':'width:100%;'}),
            'tipo_proyecto': forms.Select(attrs={'style':'width:100%;','required':''}, choices=(('P.F. Conocer un lugar en el mundo','P.F. Conocer un lugar en el mundo'),('P. F. Mejorar la productividad de un negocio','P. F. Mejorar la productividad de un negocio'),('P. F. Informarse sobre las redes sociales y compartir con los hijos','P. F. Informarse sobre las redes sociales y compartir con los hijos'))),
            'grupo_conformacion': forms.TextInput(attrs={'style':'width:100%;'}),
        }

class NuevoMasivoForm(forms.ModelForm):
    class Meta:
        model = Masivo
        fields = ['grupo','archivo','usuario']
        widgets = {
            'archivo': forms.FileInput(attrs={'accept':'.xlsx'}),
        }

class NuevoSoporteForm(forms.ModelForm):
    class Meta:
        model = SoporteEntregableEscuelaTic
        fields = ['soporte']

class AsignarForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.soporte = kwargs.pop('soporte_id', None)
        self.grupo = SoporteEntregableEscuelaTic.objects.get(pk=self.soporte).grupo.id
        super(AsignarForm, self).__init__(*args, **kwargs)
        self.fields['participantes'] = forms.MultipleChoiceField(choices=[(c.pk,c.nombres+" "+c.apellidos+" - "+str(c.cedula)) for c in ParticipanteEscuelaTic.objects.filter(grupo__id=self.grupo)])
        self.initial['participantes'] = [c.participante.id for c in EvidenciaEscuelaTic.objects.filter(soporte__id=self.soporte)]
        self.fields['participantes'].widget.attrs['class'] = 'form-control'
        self.fields['participantes'].widget.attrs['data-placeholder'] = 'Seleccione los participantes'