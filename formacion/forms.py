#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import Select,SelectMultiple
from django.utils.encoding import force_unicode
from django.utils.html import escape, conditional_escape
from formacion.models import Grupo, ParticipanteEscuelaTic, Masivo, SoporteEntregableEscuelaTic, EvidenciaEscuelaTic, GrupoDocentes, ParticipanteDocente
from formacion.models import EntregableDocentes, SoporteEntregableDocente, EvidenciaDocentes, ParticipanteDocente
from departamento.models import Departamento
from municipio.models import Municipio

class SelectWithDisabled(SelectMultiple):
    """
    Subclass of Django's select widget that allows disabling options.
    To disable an option, pass a dict instead of a string for its label,
    of the form: {'label': 'option label', 'disabled': True}
    """
    def render_option(self, selected_choices, option_value, option_label):
        option_value = force_unicode(option_value)
        if (option_value in selected_choices):
            selected_html = u' selected="selected"'
        else:
            selected_html = ''
        disabled_html = ''
        if isinstance(option_label, dict):
            if dict.get(option_label, 'disabled'):
                disabled_html = u' disabled="disabled"'
            option_label = option_label['label']
        return u'<option value="%s"%s%s>%s</option>' % (
            escape(option_value), selected_html, disabled_html,
            conditional_escape(force_unicode(option_label)))

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

class NuevoGrupoDocenteForm(forms.ModelForm):
    class Meta:
        model = GrupoDocentes
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
        fields = ['formador','grupo','numero','institucion','nombres','apellidos','cedula','genero','nivel_educativo','telefono','correo','poblacion','codigo_anspe','tipo_proyecto','grupo_conformacion']
        widgets = {
            'numero': forms.NumberInput(attrs={'style':'width:100%;'}),
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

class NuevoDocenteForm(forms.ModelForm):
    class Meta:
        secretaria_choice = []
        for secretaria in Municipio.objects.all():
            secretaria_choice.append(tuple([secretaria.nombre+" - "+secretaria.departamento.nombre,secretaria.nombre+" - "+secretaria.departamento.nombre]))
        model = ParticipanteDocente
        fields = ['formador','grupo','radicado',
                  'nombres','apellidos','cedula','correo','telefono_fijo','celular',
                  'area','grado','tipo_beneficiario','genero','nombre_proyecto',
                  'definicion_problema','area_proyecto','competencia','grupo_poblacional']
        widgets = {
            'secretaria': forms.Select(attrs={'style':'width:100%;','required':''}, choices=(secretaria_choice)),
            'radicado': forms.Select(attrs={'style':'width:100%;'}),
            'nombres': forms.TextInput(attrs={'style':'width:100%;','required':''}),
            'apellidos': forms.TextInput(attrs={'style':'width:100%;','required':''}),
            'cedula': forms.NumberInput(attrs={'style':'width:100%;','required':''}),
            'correo': forms.EmailInput(attrs={'style':'width:100%;'}),
            'telefono_fijo': forms.TextInput(attrs={'style':'width:100%;'}),
            'celular': forms.TextInput(attrs={'style':'width:100%;'}),
            'area': forms.Select(attrs={'style':'width:100%;'}),
            'grado': forms.Select(attrs={'style':'width:100%;'}),
            'tipo_beneficiario': forms.TextInput(attrs={'style':'width:100%;'}),
            'genero': forms.Select(attrs={'style':'width:100%;'}),
            'nombre_proyecto': forms.TextInput(attrs={'style':'width:100%;'}),
            'definicion_problema': forms.Textarea(attrs={'style':'width:100%;'}),
            'area_proyecto': forms.TextInput(attrs={'style':'width:100%;'}),
            'competencia': forms.Select(attrs={'style':'width:100%;'}),
            'grupo_poblacional': forms.Select(attrs={'style':'width:100%;'}),
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

class NuevoSoporteDocenteForm(forms.ModelForm):
    class Meta:
        model = SoporteEntregableDocente
        fields = ['soporte']

class AsignarForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.soporte = kwargs.pop('soporte_id', None)
        self.grupo = SoporteEntregableEscuelaTic.objects.get(pk=self.soporte).grupo.id
        super(AsignarForm, self).__init__(*args, **kwargs)
        self.id_entregable = SoporteEntregableEscuelaTic.objects.get(pk=self.soporte).entregable.id

        x = SoporteEntregableEscuelaTic.objects.filter(grupo__id=self.grupo).filter(entregable__id=self.id_entregable).values_list("id",flat=True)

        x = list(x)

        x.pop(x.index(long(self.soporte)))

        if not isinstance(x,list):
            x = [x]

        y = EvidenciaEscuelaTic.objects.filter(soporte__in=x).values_list("participante__id",flat=True)
        participantes = ParticipanteEscuelaTic.objects.filter(grupo__id=self.grupo)
        choices = []
        for participante in participantes:
            if participante.pk in y:
                choices.append((participante.pk,{'label':participante.nombres+" "+participante.apellidos+" - "+str(participante.cedula),'disabled': True}))
            else:
                choices.append((participante.pk,participante.nombres+" "+participante.apellidos+" - "+str(participante.cedula)))

        self.fields['participantes'] = forms.MultipleChoiceField(choices=choices,widget=SelectWithDisabled())
        self.initial['participantes'] = [c.participante.id for c in EvidenciaEscuelaTic.objects.filter(soporte__id=self.soporte)]
        self.fields['participantes'].widget.attrs['class'] = 'form-control'
        self.fields['participantes'].widget.attrs['data-placeholder'] = 'Seleccione los participantes'

class AsignarDocenteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.soporte = kwargs.pop('soporte_id', None)
        self.grupo = SoporteEntregableDocente.objects.get(pk=self.soporte).grupo.id
        super(AsignarDocenteForm, self).__init__(*args, **kwargs)
        self.id_entregable = SoporteEntregableDocente.objects.get(pk=self.soporte).entregable.id
        soporte = SoporteEntregableDocente.objects.get(pk=self.soporte)

        x = SoporteEntregableDocente.objects.filter(grupo__formador__id=soporte.grupo.formador.id).filter(entregable__id=self.id_entregable).values_list("id",flat=True)

        x = list(x)

        x.pop(x.index(long(self.soporte)))

        if not isinstance(x,list):
            x = [x]

        y = EvidenciaDocentes.objects.filter(soporte__in=x).values_list("participante__id",flat=True)
        participantes = ParticipanteDocente.objects.filter(grupo__id=self.grupo)
        choices = []
        for participante in participantes:
            if participante.pk in y:
                choices.append((participante.pk,{'label':participante.nombres+" "+participante.apellidos+" - "+str(participante.cedula),'disabled': True}))
            else:
                choices.append((participante.pk,participante.nombres+" "+participante.apellidos+" - "+str(participante.cedula)))

        self.fields['participantes'] = forms.MultipleChoiceField(choices=choices,widget=SelectWithDisabled())
        self.initial['participantes'] = [c.participante.id for c in EvidenciaDocentes.objects.filter(soporte__id=self.soporte)]
        self.fields['participantes'].widget.attrs['class'] = 'form-control'
        self.fields['participantes'].widget.attrs['data-placeholder'] = 'Seleccione los participantes'

class AgregarSoporteForm(forms.ModelForm):
    class Meta:
        model = SoporteEntregableEscuelaTic
        fields = ['grupo','entregable']
        widgets = {
            'entregable': forms.Select(attrs={'style':'width:100%;'}),
        }

class AgregarSoporteDocenteForm(forms.ModelForm):
    class Meta:
        model = SoporteEntregableDocente
        fields = ['grupo','entregable']
        widgets = {
            'entregable': forms.Select(attrs={'style':'width:100%;'}),
        }