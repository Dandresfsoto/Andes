#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from mixins.mixins import AccesoMixin
from region.models import Region
from django.views.generic import CreateView
from gestor.models import Gestor
from radicado.models import Radicado
from municipio.models import Municipio
from acceso.models import Actividad, Reasignados, CargaMasiva
from conf import settings
import openpyxl

from acceso.forms import ReasignacionForm, CargaMasivaForm
from .models import Evidencia
from rest_framework import mixins
from rest_framework import generics
from .serializers import EvidenciaSerializer
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import time
import datetime
from openpyxl.styles import Style, PatternFill, Border, Side, Alignment, Protection, Font

from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q

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

class EvidenciaViewSet(mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = Evidencia.objects.all()
    serializer_class = EvidenciaSerializer
    lookup_url_kwarg = 'id_evidencia'


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class AccesoView(AccesoMixin,TemplateView):
    template_name = 'acceso.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(AccesoView,self).get_context_data(**kwargs)

class AccesoCalificacionView(AccesoMixin,TemplateView):
    template_name = 'acceso_gestores.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(AccesoCalificacionView,self).get_context_data(**kwargs)

class AccesoCalificacionTotalView(AccesoMixin,TemplateView):
    template_name = 'acceso_radicados_total.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(AccesoCalificacionTotalView,self).get_context_data(**kwargs)

class AccesoReasignadosView(AccesoMixin,TemplateView):
    template_name = 'acceso_reasignados.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(AccesoReasignadosView,self).get_context_data(**kwargs)

class AccesoListadoRadicadosView(AccesoMixin,TemplateView):
    template_name = 'acceso_radicados.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['NOMBRE'] = Gestor.objects.get(pk=self.kwargs['id_gestor']).nombre
        kwargs['MUNICIPIO'] = Municipio.objects.get(pk=self.kwargs['id_municipio']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_GESTOR'] = self.kwargs['id_gestor']
        kwargs['ID_MUNICIPIO'] = self.kwargs['id_municipio']
        return super(AccesoListadoRadicadosView,self).get_context_data(**kwargs)

class AccesoListadoMunicipiosView(AccesoMixin,TemplateView):
    template_name = 'acceso_municipios.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['NOMBRE'] = Gestor.objects.get(pk=self.kwargs['id_gestor']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_GESTOR'] = self.kwargs['id_gestor']
        return super(AccesoListadoMunicipiosView,self).get_context_data(**kwargs)

def evidencia_form(request,id_radicado,pk,id_gestor,id_municipio):
    EvidenciaFormSet = modelformset_factory(Evidencia, fields=('soporte',),extra=0)
    if request.method == "POST":
        formset = EvidenciaFormSet(request.POST, request.FILES, queryset=Evidencia.objects.filter(radicado__id=id_radicado))
        if formset.is_valid():
            formset.save()
            for form in formset.forms:
                if form.cleaned_data['soporte'] != None:
                    obj = Evidencia.objects.get(pk=form.instance.id)
                    obj.usuario = request.user
                    obj.modificacion = datetime.datetime.now()
                    obj.save()
    else:
        formset = EvidenciaFormSet(queryset=Evidencia.objects.filter(radicado__id=id_radicado),)
    return render_to_response("evidencias_radicado.html",{"formset":formset,"user":request.user,"REGION":Region.objects.get(pk=pk).nombre,
                                                          "gestor":Gestor.objects.get(pk=id_gestor).nombre,
                                                          "radicado":Radicado.objects.get(pk=id_radicado),
                                                          "municipio":Municipio.objects.get(pk=id_municipio)},
                              context_instance=RequestContext(request))

def evidencia_total_form(request,id_radicado,pk):
    EvidenciaFormSet = modelformset_factory(Evidencia, fields=('soporte',),extra=0)
    if request.method == "POST":
        formset = EvidenciaFormSet(request.POST, request.FILES, queryset=Evidencia.objects.filter(radicado__id=id_radicado))
        if formset.is_valid():
            formset.save()
            for form in formset.forms:
                if form.cleaned_data['soporte'] != None:
                    obj = Evidencia.objects.get(pk=form.instance.id)
                    obj.usuario = request.user
                    obj.modificacion = datetime.datetime.now()
                    obj.save()
    else:
        formset = EvidenciaFormSet(queryset=Evidencia.objects.filter(radicado__id=id_radicado),)
    return render_to_response("evidencias_radicado_total.html",{"formset":formset,"user":request.user,"REGION":Region.objects.get(pk=pk).nombre,"radicado":Radicado.objects.get(pk=id_radicado)},context_instance=RequestContext(request))

def reporte_acceso(request,pk,id_gestor):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Actividades Gestores.xlsx'
    archivo = openpyxl.load_workbook(settings.STATICFILES_DIRS[0]+'/formatos/base.xlsx')

    logo = openpyxl.drawing.Image(settings.STATICFILES_DIRS[0]+'/formatos/logo.png')
    logo.drawing.top = 10
    logo.drawing.left = 25

    hoja1 = archivo.get_sheet_by_name('hoja1')
    hoja1.title = "Informe Gestores"
    hoja1.add_image(logo)

    celda = hoja1.cell('E2')
    celda.value = 'ACCESO'

    celda = hoja1.cell('E3')
    celda.value = 'REPORTE GESTORES'

    celda = hoja1.cell('I3')
    celda.value = time.strftime("%d/%m/%y")

    celda = hoja1.cell('I4')
    celda.value = time.strftime("%I:%M:%S %p")

    row_num = 5

    columnas = Actividad.objects.order_by('id').values('nombre','titulo')
    columns = [tuple(['Radicado',30]),
               tuple(['Departamento',30]),
               tuple(['Municipio',30]),
               tuple(['Gestor',30]),
               tuple(['Ciclo',30]),
               tuple(['Componente',30]),
               tuple(['Modulo',30]),
               tuple(['Actividad',30]),
               tuple(['Encargado',30]),
               tuple(['Valor',30]),
               tuple(['Soporte',30]),
               tuple(['Corte',30]),
               tuple(['Usuario',30]),
               tuple(['Modificación',30]),
               ]



    for col_num in xrange(len(columns)):
        c = hoja1.cell(row=row_num, column=col_num+1)
        c.value = columns[col_num][0]
        c.style = t
        hoja1.column_dimensions[openpyxl.cell.get_column_letter(col_num+1)].width = columns[col_num][1]


    evidencias = Evidencia.objects.filter(radicado__region__id=pk).filter(gestor__id=id_gestor)

    for evidencia in evidencias:
        row_num += 1
        row = [
            evidencia.radicado.numero,
            evidencia.radicado.municipio.departamento.nombre,
            evidencia.radicado.municipio.nombre,
            evidencia.gestor.nombre,
            evidencia.ciclo.nombre,
            evidencia.componente.nombre,
            evidencia.modulo.nombre,
            str(evidencia.actividad.nombre)+" - "+str(evidencia.actividad.titulo),
            evidencia.encargado.encargado,
            evidencia.valor.valor,
            str(evidencia.soporte),
            str(evidencia.corte.fecha)+" - "+str(evidencia.corte.titulo) if evidencia.corte != None else "",
            evidencia.usuario.username,
            evidencia.modificacion
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



    archivo.save(response)
    return response

class ReasignarView(AccesoMixin,CreateView):
    model = Reasignados
    form_class = ReasignacionForm
    template_name = "formulario_reasignados.html"
    success_url = "../../../"

class MasivoView(AccesoMixin,TemplateView):
    template_name = 'acceso_masivo.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(MasivoView,self).get_context_data(**kwargs)

class MasivoTableView(BaseDatatableView):
    model = CargaMasiva
    columns = [
        'id',
        'region',
        'fecha',
        'usuario',
        'excel',
        'archivo',
    ]

    order_columns = [
        'id',
        'region',
        'fecha',
        'usuario',
        'excel',
        'archivo',
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.all().filter(region__id=self.kwargs['pk'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'usuario__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'region':
            return row.region.nombre
        if column == 'fecha':
            return row.fecha.strftime('%d/%m/%Y --- %I:%M:%S %p')
        if column == 'usuario':
            return row.usuario.username
        if column == 'excel':
            return str(row.excel)
        if column == 'archivo':
            return str(row.archivo)
        else:
            return super(MasivoTableView,self).render_column(row,column)

class MasivoNuevoView(AccesoMixin,CreateView):
    model = CargaMasiva
    form_class = CargaMasivaForm
    template_name = "formulario_carga_masiva.html"
    success_url = "../"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(MasivoNuevoView,self).get_context_data(**kwargs)