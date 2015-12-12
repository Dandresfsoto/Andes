#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from .models import PqrRespuesta, Llamadas, LlamadasRespuesta
from region.models import Region
from funcionario.models import Funcionario
from municipio.models import Municipio

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

class LlamadaForm(forms.ModelForm):
    class Meta:

        region_choice = []
        for region in Region.objects.all():
            region_choice.append(tuple([region.id,region.nombre]))

        secretaria_choice = []
        for secretaria in Municipio.objects.all():
            secretaria_choice.append(tuple([secretaria.nombre+" - "+secretaria.departamento.nombre,secretaria.nombre+" - "+secretaria.departamento.nombre]))

        eje_choice = [tuple(['Administrativo','Administrativo']),tuple(['Formación','Formación']),tuple(['Acceso','Acceso'])]
        model = Llamadas
        fields = ['region','eje','nombre','email','telefono','municipio','mensaje']
        widgets = {
            'region': forms.Select(attrs={'style':'width:100%;','required':''},choices=(region_choice)),
            'eje': forms.Select(attrs={'style':'width:100%;','required':''},choices=(eje_choice)),
            'nombre': forms.TextInput(attrs={'style':'width:100%;','required':''}),
            'email': forms.EmailInput(attrs={'style':'width:100%;','required':''}),
            'telefono': forms.TextInput(attrs={'style':'width:100%;','required':''}),
            'municipio': forms.Select(attrs={'style':'width:100%;','required':''}, choices=(secretaria_choice)),
            'mensaje': forms.Textarea(attrs={'style':'width:100%;','rows':5}),
        }

class LlamadaRespuestaForm(forms.ModelForm):
    class Meta:
        region_choice = []
        for region in Region.objects.all():
            region_choice.append(tuple([region.id,region.nombre]))
        funcionario_choice = []
        for funcionario in Funcionario.objects.all():
            funcionario_choice.append(tuple([funcionario.id,funcionario.nombre]))
        model = LlamadasRespuesta
        fields = ['llamada','region','funcionario','mensaje']
        widgets = {
            'region': forms.Select(attrs={'style':'width:100%;','required':''},choices=(region_choice)),
            'funcionario': forms.Select(attrs={'style':'width:100%;','required':''},choices=(funcionario_choice)),
            'mensaje': forms.Textarea(attrs={'style':'width:100%;','rows':5}),
        }