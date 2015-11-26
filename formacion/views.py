#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, FormView
from mixins.mixins import FormacionMixin
from region.models import Region
from formador.models import Formador
from formacion.models import Grupo, ParticipanteEscuelaTic, Entregable, SoporteEntregableEscuelaTic, Masivo, EvidenciaEscuelaTic
from formacion.forms import NuevoGrupoForm, NuevoParticipanteForm, NuevoMasivoForm, NuevoSoporteForm, AsignarForm
from django.http import HttpResponseRedirect
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import openpyxl
from django.utils.encoding import smart_unicode
from conf import settings
from django.core.files.base import ContentFile
from StringIO import StringIO
import time
from openpyxl.styles import Style, PatternFill, Border, Side, Alignment, Protection, Font

t = Style(font=Font(name='Calibri',size=12,bold=True,italic=False,vertAlign=None,underline='none',strike=False,color='FF000000'),
       fill=PatternFill(fill_type='solid',start_color='C9C9C9',end_color='FF000000'),
       alignment=Alignment(horizontal='center',vertical='center',wrap_text=True),
     number_format='General')

co = Style(font=Font(name='Calibri',size=11),
       alignment=Alignment(horizontal='center',vertical='center',wrap_text=True),
     number_format='General')

v = Style(font=Font(name='Calibri',size=12,bold=True,italic=False,vertAlign=None,underline='none',strike=False,color='FF000000'),
       fill=PatternFill(fill_type='solid',start_color='E4F5E1',end_color='FF000000'),
       alignment=Alignment(horizontal='center',vertical='center',wrap_text=True),
     number_format='General')

vc = Style(font=Font(name='Calibri',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color='FF000000'),
       fill=PatternFill(fill_type='solid',start_color='D4F5CE',end_color='FF000000'),
       alignment=Alignment(horizontal='center',vertical='center',wrap_text=True),
     number_format='General')

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False

class FormacionView(FormacionMixin,TemplateView):
    template_name = 'formacion.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(FormacionView,self).get_context_data(**kwargs)

class FormadorView(FormacionMixin,TemplateView):
    template_name = 'tipo2_formador_formacion.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(FormadorView,self).get_context_data(**kwargs)

class FormadorGrupoView(FormacionMixin,TemplateView):
    template_name = 'tipo2_formador_grupo.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['NOMBRE_FORMADOR'] = Formador.objects.get(pk=self.kwargs['formador_id']).nombre
        kwargs['ID_FORMADOR'] = self.kwargs['formador_id']
        return super(FormadorGrupoView,self).get_context_data(**kwargs)

class NuevoGrupoView(FormacionMixin,CreateView):
    model = Grupo
    form_class = NuevoGrupoForm
    template_name = "formulario_grupo.html"
    success_url = "../"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['NOMBRE_FORMADOR'] = Formador.objects.get(pk=self.kwargs['formador_id']).nombre
        kwargs['ID_FORMADOR'] = self.kwargs['formador_id']
        return super(NuevoGrupoView,self).get_context_data(**kwargs)

class FormSoporteGrupoView(FormacionMixin,UpdateView):
    pk_url_kwarg = 'soporte_id'
    model = SoporteEntregableEscuelaTic
    form_class = NuevoSoporteForm
    template_name = "formulario_soporte_tipo2.html"
    success_url = "../../"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['NOMBRE_FORMADOR'] = Formador.objects.get(pk=self.kwargs['formador_id']).nombre
        kwargs['ID_FORMADOR'] = self.kwargs['formador_id']
        kwargs['NOMBRE_SOPORTE'] = SoporteEntregableEscuelaTic.objects.get(pk=self.kwargs['soporte_id']).entregable.nombre + " - " + SoporteEntregableEscuelaTic.objects.get(pk=self.kwargs['soporte_id']).grupo.nombre
        return super(FormSoporteGrupoView,self).get_context_data(**kwargs)

class FormAsignarSoporteView(FormacionMixin,FormView):
    form_class = AsignarForm
    template_name = "formulario_asignar_soporte_tipo2.html"
    success_url = "../../"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['NOMBRE_FORMADOR'] = Formador.objects.get(pk=self.kwargs['formador_id']).nombre
        kwargs['ID_FORMADOR'] = self.kwargs['formador_id']
        kwargs['NOMBRE_SOPORTE'] = SoporteEntregableEscuelaTic.objects.get(pk=self.kwargs['soporte_id']).entregable.nombre + " - " + SoporteEntregableEscuelaTic.objects.get(pk=self.kwargs['soporte_id']).grupo.nombre
        return super(FormAsignarSoporteView,self).get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
            'soporte_id': self.kwargs['soporte_id'],
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def form_valid(self, form):
        super(FormAsignarSoporteView, self).form_valid(form)
        participantes = form.cleaned_data['participantes']
        soporte = SoporteEntregableEscuelaTic.objects.get(pk=self.kwargs['soporte_id'])
        participantes_total = ParticipanteEscuelaTic.objects.filter(grupo__id=soporte.grupo.id).values_list("id",flat=True)
        for participante in participantes_total:
            evidencia = EvidenciaEscuelaTic.objects.filter(participante__id=participante).get(entregable__id=soporte.entregable.id)
            if unicode(participante) in participantes:
                evidencia.soporte = soporte
            else:
                evidencia.soporte = None
            evidencia.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        soporte = SoporteEntregableEscuelaTic.objects.get(pk=self.kwargs['soporte_id'])
        participantes_total = ParticipanteEscuelaTic.objects.filter(grupo__id=soporte.grupo.id).values_list("id",flat=True)
        for participante in participantes_total:
            evidencia = EvidenciaEscuelaTic.objects.filter(participante__id=participante).get(entregable__id=soporte.entregable.id)
            evidencia.soporte = None
            evidencia.save()
        return HttpResponseRedirect(self.get_success_url())

class ListadoGrupoView(FormacionMixin,TemplateView):
    template_name = 'tipo2_formador_listado.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['NOMBRE_FORMADOR'] = Formador.objects.get(pk=self.kwargs['formador_id']).nombre
        kwargs['ID_FORMADOR'] = self.kwargs['formador_id']
        kwargs['ID_GRUPO'] = self.kwargs['grupo_id']
        kwargs['NOMBRE_GRUPO'] = Grupo.objects.get(pk=self.kwargs['grupo_id']).nombre
        return super(ListadoGrupoView,self).get_context_data(**kwargs)

class NuevoParticipanteView(FormacionMixin,CreateView):
    model = ParticipanteEscuelaTic
    form_class = NuevoParticipanteForm
    template_name = "formulario_participante.html"
    success_url = "../../"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['NOMBRE_FORMADOR'] = Formador.objects.get(pk=self.kwargs['formador_id']).nombre
        kwargs['ID_FORMADOR'] = self.kwargs['formador_id']
        kwargs['ID_GRUPO'] = self.kwargs['grupo_id']
        kwargs['NOMBRE_GRUPO'] = Grupo.objects.get(pk=self.kwargs['grupo_id']).nombre
        kwargs['ACCION'] = "Nuevo"
        return super(NuevoParticipanteView,self).get_context_data(**kwargs)

class EditarParticipanteView(FormacionMixin,UpdateView):
    model = ParticipanteEscuelaTic
    form_class = NuevoParticipanteForm
    template_name = "formulario_participante.html"
    success_url = "../../"
    pk_url_kwarg = "participante_id"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['NOMBRE_FORMADOR'] = Formador.objects.get(pk=self.kwargs['formador_id']).nombre
        kwargs['ID_FORMADOR'] = self.kwargs['formador_id']
        kwargs['ID_GRUPO'] = self.kwargs['grupo_id']
        kwargs['NOMBRE_GRUPO'] = Grupo.objects.get(pk=self.kwargs['grupo_id']).nombre
        kwargs['ACCION'] = "Editar: "+ParticipanteEscuelaTic.objects.get(pk=self.kwargs['participante_id']).nombres
        return super(EditarParticipanteView,self).get_context_data(**kwargs)

def soporte_form(request,pk,grupo_id,formador_id):
    SoporteFormSet = modelformset_factory(SoporteEntregableEscuelaTic, fields=('soporte',),extra=0)
    if request.method == "POST":
        formset = SoporteFormSet(request.POST, request.FILES, queryset=SoporteEntregableEscuelaTic.objects.filter(grupo__id=grupo_id))
        if formset.is_valid():
            formset.save()
    else:
        formset = SoporteFormSet(queryset=SoporteEntregableEscuelaTic.objects.filter(grupo__id=grupo_id),)
    return render_to_response("soportes_escuelaTIC.html",{"formset":formset,"user":request.user,"REGION":Region.objects.get(pk=pk).nombre},context_instance=RequestContext(request))

class ListadoMasivoView(FormacionMixin,TemplateView):
    template_name = 'tipo2_formador_listado_masivo.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['NOMBRE_FORMADOR'] = Formador.objects.get(pk=self.kwargs['formador_id']).nombre
        kwargs['ID_FORMADOR'] = self.kwargs['formador_id']
        kwargs['ID_GRUPO'] = self.kwargs['grupo_id']
        kwargs['NOMBRE_GRUPO'] = Grupo.objects.get(pk=self.kwargs['grupo_id']).nombre
        return super(ListadoMasivoView,self).get_context_data(**kwargs)

class NuevoMasivoView(FormacionMixin,CreateView):
    model = Masivo
    form_class = NuevoMasivoForm
    template_name = "formulario_masivo.html"
    success_url = "../"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['NOMBRE_FORMADOR'] = Formador.objects.get(pk=self.kwargs['formador_id']).nombre
        kwargs['ID_FORMADOR'] = self.kwargs['formador_id']
        kwargs['ID_GRUPO'] = self.kwargs['grupo_id']
        return super(NuevoMasivoView,self).get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        path = smart_unicode(self.object.archivo)
        archivo = openpyxl.load_workbook(settings.MEDIA_ROOT+'/'+path)
        try:
            hoja1 = archivo.get_sheet_by_name('BasePadresFamilia')
        except KeyError:
            self.object.delete()
            return self.render_to_response(self.get_context_data(form=form,ERROR="El Archivo no tiene ninguna hoja con el nombre 'BasePadresFamilia'"))
        else:
            r = StringIO()
            resultado = openpyxl.load_workbook(settings.STATICFILES_DIRS[0]+'/formatos/base.xlsx')

            logo = openpyxl.drawing.Image(settings.STATICFILES_DIRS[0]+'/formatos/logo.png')
            logo.drawing.top = 10
            logo.drawing.left = 25

            hoja1 = resultado.get_sheet_by_name('hoja1')
            hoja1.title = "ESCUELATIC"
            hoja1.add_image(logo)

            celda = hoja1.cell('E2')
            celda.value = 'FORMACIÓN'

            celda = hoja1.cell('E3')
            celda.value = 'ESCUELATIC'

            celda = hoja1.cell('I3')
            celda.value = time.strftime("%d/%m/%y")

            celda = hoja1.cell('I4')
            celda.value = time.strftime("%I:%M:%S %p")

            row_num = 5

            columns = [tuple(['NOMBRES',30]),
               tuple(['APELLIDOS',30]),
               tuple(['CEDULA',30]),
               tuple(['RESULTADO',50]),
               ]

            for col_num in xrange(len(columns)):
                c = hoja1.cell(row=row_num, column=col_num+1)
                c.value = columns[col_num][0]
                c.style = t
                hoja1.column_dimensions[openpyxl.cell.get_column_letter(col_num+1)].width = columns[col_num][1]

            i=0

            grupo = Grupo.objects.get(pk=self.kwargs['grupo_id'])
            formador = Formador.objects.get(pk=self.kwargs['formador_id'])

            archivo_hoja = archivo.get_sheet_by_name('BasePadresFamilia')
            for fila in archivo_hoja.rows:
                i += 1
                if i > 3:
                    proceso =""
                    try:
                        cedula = fila[6].value.replace('.','').replace(',','')
                    except:
                        cedula = fila[6].value
                    nombres = fila[4].value
                    apellidos = fila[5].value


                    if cedula == "" or cedula == None:
                        proceso = "El campo de cedula esta vacio"
                    else:
                        try:
                            long(cedula)
                        except ValueError:
                            proceso = "El numero de cedula es invalido"
                        else:
                            if ParticipanteEscuelaTic.objects.filter(cedula=cedula).count() != 0:
                                proceso = "La Cedula ya se encuentra registrada"
                            else:
                                if nombres == "" or nombres == None:
                                    proceso = "El campo de nombres esta vacio"
                                else:
                                    if apellidos == "" or apellidos == None:
                                        proceso = "El campo de apellidos esta vacio"
                                    else:
                                        proceso = "Registrado Correctamente"
                                        nuevo = ParticipanteEscuelaTic()
                                        nuevo.grupo = grupo
                                        nuevo.formador = formador
                                        nuevo.numero = fila[0].value
                                        nuevo.departamento = grupo.municipio.departamento.nombre
                                        nuevo.municipio = grupo.municipio.nombre
                                        nuevo.institucion = fila[3].value
                                        nuevo.nombres = fila[4].value
                                        nuevo.apellidos = fila[5].value
                                        nuevo.cedula = long(cedula)
                                        if fila[7].value == None or fila[7].value == "":
                                            nuevo.genero = "Masculino"
                                            proceso = "Registrado Correctamente - Genero Masculino por defecto"
                                        else:
                                            nuevo.genero = fila[7].value
                                        nuevo.nivel_educativo = fila[8].value
                                        nuevo.telefono = fila[9].value
                                        if validateEmail(fila[10].value):
                                            nuevo.correo = fila[10].value
                                        nuevo.poblacion = fila[11].value
                                        nuevo.codigo_anspe = fila[12].value
                                        nuevo.tipo_proyecto = fila[13].value
                                        nuevo.grupo_conformacion = fila[14].value
                                        nuevo.save()


                    row_num += 1
                    row = [
                        fila[4].value,
                        fila[5].value,
                        fila[6].value,
                        proceso
                    ]

                    for col_num in xrange(len(row)):
                        c = hoja1.cell(row=row_num, column=col_num+1)
                        if row[col_num] == True:
                            c.value = "SI"
                        if row[col_num] == False:
                            c.value = "NO"
                        if row[col_num] == None:
                            c.value = ""
                        else:
                            c.value = row[col_num]
                        c.style = co

            resultado.save(r)
            self.object.resultado.save('Resultado.xlsx', ContentFile(r.getvalue()))
            self.object.save()
        return HttpResponseRedirect(self.get_success_url())