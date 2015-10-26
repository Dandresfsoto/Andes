#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from formacion.models import Grupo, ParticipanteEscuelaTic
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
        model = ParticipanteEscuelaTic
        fields = ['formador','grupo','numero','departamento','municipio','institucion','nombres','apellidos','cedula','genero','nivel_educativo','telefono','correo','poblacion','codigo_anspe']
        widgets = {
            'numero': forms.NumberInput(attrs={'style':'width:100%;'}),
            'departamento': forms.Select(attrs={'style':'width:100%;','required':''}, choices=(Departamento.objects.all().values_list('nombre','nombre'))),
            'municipio': forms.Select(attrs={'style':'width:100%;','required':''}, choices=(Municipio.objects.all().values_list('nombre','nombre'))),
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
        }