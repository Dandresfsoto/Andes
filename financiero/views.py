#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import ModelFormMixin
from mixins.mixins import FinancieroMixin
from region.models import Region
from gestor.models import Gestor
from gestor.forms import NuevoForm
from formador.models import Formador
from formador.forms import NuevoForm as NuevoFormFormador
from funcionario.forms import NuevoFuncionarioForm
from funcionario.models import Funcionario
from acceso.models import Corte
from acceso.forms import CorteForm
from acceso.models import Evidencia,Actividad
from django.db.models import Sum
from django.core.mail import EmailMessage
import StringIO

from django.http import HttpResponse
import time
from conf import settings
import openpyxl
from django.utils.encoding import smart_unicode

from openpyxl.styles import Style, PatternFill, Border, Side, Alignment, Protection, Font

t = Style(font=Font(name='Calibri',size=12,bold=True,italic=False,vertAlign=None,underline='none',strike=False,color='FF000000'),
       fill=PatternFill(fill_type='solid',start_color='C9C9C9',end_color='FF000000'),
       alignment=Alignment(horizontal='center',vertical='center',wrap_text=True),
     number_format='General')

co = Style(font=Font(name='Calibri',size=11),
       alignment=Alignment(horizontal='center',vertical='center',wrap_text=True),
     number_format='General')

co_money = Style(font=Font(name='Calibri',size=11),
       alignment=Alignment(horizontal='center',vertical='center',wrap_text=True),
     number_format='Money')

v = Style(font=Font(name='Calibri',size=12,bold=True,italic=False,vertAlign=None,underline='none',strike=False,color='FF000000'),
       fill=PatternFill(fill_type='solid',start_color='E4F5E1',end_color='FF000000'),
       alignment=Alignment(horizontal='center',vertical='center',wrap_text=True),
     number_format='General')

vc = Style(font=Font(name='Calibri',size=12,bold=False,italic=False,vertAlign=None,underline='none',strike=False,color='FF000000'),
       fill=PatternFill(fill_type='solid',start_color='D4F5CE',end_color='FF000000'),
       alignment=Alignment(horizontal='center',vertical='center',wrap_text=True),
     number_format='General')

class FinancieroView(FinancieroMixin,TemplateView):
    template_name = 'financiero.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(FinancieroView,self).get_context_data(**kwargs)

class GestorView(FinancieroMixin,TemplateView):
    template_name = 'listado_gestores_financiero.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(GestorView,self).get_context_data(**kwargs)

class GestorCorteEvidenciaView(FinancieroMixin,TemplateView):
    template_name = 'listado_gestores_evidencia_corte.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_CORTE'] = self.kwargs['corte_id']
        kwargs['ID_GESTOR'] = self.kwargs['gestor_id']
        kwargs['CORTE'] = Corte.objects.get(pk=self.kwargs['corte_id']).titulo
        kwargs['GESTOR'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).nombre
        return super(GestorCorteEvidenciaView,self).get_context_data(**kwargs)

class FormadorView(FinancieroMixin,TemplateView):
    template_name = 'tipo_formador_financiero.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(FormadorView,self).get_context_data(**kwargs)

class FormadorTipoView(FinancieroMixin,TemplateView):
    template_name = 'listado_formadores_financiero.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_TIPO'] = self.kwargs['tipo_id']
        return super(FormadorTipoView,self).get_context_data(**kwargs)

class FuncionarioView(FinancieroMixin,TemplateView):
    template_name = 'listado_funcionario_financiero.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(FuncionarioView,self).get_context_data(**kwargs)

class NuevoGestorView(FinancieroMixin, CreateView):
    model = Gestor
    form_class = NuevoForm
    success_url = "../"
    template_name = "nuevo_gestor.html"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(NuevoGestorView,self).get_context_data(**kwargs)

class NuevoFormadorView(FinancieroMixin, CreateView):
    model = Formador
    form_class = NuevoFormFormador
    success_url = "../"
    template_name = "nuevo_formador.html"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_TIPO'] = self.kwargs['tipo_id']
        return super(NuevoFormadorView,self).get_context_data(**kwargs)

class NuevoFuncionarioView(FinancieroMixin, CreateView):
    model = Funcionario
    form_class = NuevoFuncionarioForm
    success_url = "../"
    template_name = "nuevo_funcionario.html"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(NuevoFuncionarioView,self).get_context_data(**kwargs)

class NuevoCorteView(FinancieroMixin, CreateView):
    model = Corte
    form_class = CorteForm
    success_url = "../"
    template_name = "nuevo_corte.html"

    def get_context_data(self, **kwargs):
        reporte = Evidencia.objects.filter(radicado__region__id=self.kwargs['pk']).filter(corte=None).exclude(soporte="")
        kwargs['CANTIDAD'] = reporte.count()
        kwargs['VALOR'] = "$ "+str(reporte.aggregate(Sum('valor__valor'))['valor__valor__sum'])
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']

        return super(NuevoCorteView,self).get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        corte = self.object
        reporte = Evidencia.objects.filter(radicado__region__id=self.kwargs['pk']).filter(corte=None).exclude(soporte="")
        for evidencia in reporte:
            evidencia.corte = corte
            evidencia.save()
        return super(ModelFormMixin, self).form_valid(form)

def reporte_quincenal_financiero(request,pk):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Reporte de Quincenas.xlsx'
    archivo = openpyxl.load_workbook(settings.STATICFILES_DIRS[0]+'/formatos/base.xlsx')

    logo = openpyxl.drawing.Image(settings.STATICFILES_DIRS[0]+'/formatos/logo.png')
    logo.drawing.top = 10
    logo.drawing.left = 25

    hoja1 = archivo.get_sheet_by_name('hoja1')
    hoja1.title = "Informe Quincenas Gestores"
    hoja1.add_image(logo)

    celda = hoja1.cell('E2')
    celda.value = 'ADMINISTRATIVO Y FINANCIERO'

    celda = hoja1.cell('E3')
    celda.value = 'REPORTE QUINCENAS GESTORES'

    celda = hoja1.cell('I3')
    celda.value = time.strftime("%d/%m/%y")

    celda = hoja1.cell('I4')
    celda.value = time.strftime("%I:%M:%S %p")

    row_num = 5

    cortes = Corte.objects.filter(region__id=pk)

    columns = [tuple(['Nombre Gestor',60]),
               tuple(['Banco',30]),
               tuple(['Tipo de Cuenta',30]),
               tuple(['Numero de Cuenta',30])
               ]
    for corte in cortes:
        columns.append(tuple([corte.titulo+" - "+str(corte.fecha),90]))



    for col_num in xrange(len(columns)):
        c = hoja1.cell(row=row_num, column=col_num+1)
        c.value = columns[col_num][0]
        c.style = t
        hoja1.column_dimensions[openpyxl.cell.get_column_letter(col_num+1)].width = columns[col_num][1]


    gestores = Gestor.objects.filter(region__id=pk)

    for gestor in gestores:
        row_num += 1
        row = [
            gestor.nombre,
            gestor.banco,
            gestor.tipo_cuenta,
            gestor.numero_cuenta,
        ]

        for corte in cortes:
            row.append(Evidencia.objects.filter(gestor__id=gestor.id).exclude(corte=None).filter(corte=corte).aggregate(Sum('valor__valor'))['valor__valor__sum'])

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

        c = hoja1.cell(row=6, column=6)
        c.style = co_money

    archivo.save(response)
    return response

def reporte_gestor(request,pk,corte_id,gestor_id):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    gestor = Gestor.objects.get(id=gestor_id)
    corte = Corte.objects.get(id=corte_id)
    response['Content-Disposition'] = 'attachment; filename='+smart_unicode(gestor.nombre)+'.xlsx'
    archivo = openpyxl.load_workbook(settings.STATICFILES_DIRS[0]+'/formatos/base.xlsx')

    logo = openpyxl.drawing.Image(settings.STATICFILES_DIRS[0]+'/formatos/logo.png')
    logo.drawing.top = 10
    logo.drawing.left = 25

    hoja1 = archivo.get_sheet_by_name('hoja1')
    hoja1.title = smart_unicode(gestor.nombre)
    hoja1.add_image(logo)

    celda = hoja1.cell('E2')
    celda.value = 'ACCESO'

    celda = hoja1.cell('E3')
    celda.value = 'REPORTE QUINCENAL - '+smart_unicode(gestor.nombre)

    celda = hoja1.cell('I3')
    celda.value = time.strftime("%d/%m/%y")

    celda = hoja1.cell('I4')
    celda.value = time.strftime("%I:%M:%S %p")

    row_num = 5

    columnas = Actividad.objects.order_by('id').values('nombre','titulo')
    columns = [tuple(['Radicado',30]),
               tuple(['Departamento',30]),
               tuple(['Municipio',30]),
               tuple(['Ciclo',30]),
               tuple(['Componente',30]),
               tuple(['Modulo',30]),
               tuple(['Actividad',30]),
               tuple(['Valor',30]),
               tuple(['Corte',30]),
               ]



    for col_num in xrange(len(columns)):
        c = hoja1.cell(row=row_num, column=col_num+1)
        c.value = columns[col_num][0]
        c.style = t
        hoja1.column_dimensions[openpyxl.cell.get_column_letter(col_num+1)].width = columns[col_num][1]


    evidencias = Evidencia.objects.filter(gestor__id=gestor_id).filter(corte_id=corte.id)

    for evidencia in evidencias:
        row_num += 1
        row = [
            evidencia.radicado.numero,
            evidencia.radicado.municipio.departamento.nombre,
            evidencia.radicado.municipio.nombre,
            evidencia.ciclo.nombre,
            evidencia.componente.nombre,
            evidencia.modulo.nombre,
            str(evidencia.actividad.nombre)+" - "+str(evidencia.actividad.titulo),
            evidencia.valor.valor,
            str(evidencia.corte.fecha)+" - "+str(evidencia.corte.titulo) if evidencia.corte != None else "",
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

def reporte_gestor_email(request,pk,corte_id,gestor_id):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    gestor = Gestor.objects.get(id=gestor_id)
    corte = Corte.objects.get(id=corte_id)
    response['Content-Disposition'] = 'attachment; filename='+smart_unicode(gestor.nombre)+'.xlsx'
    archivo = openpyxl.load_workbook(settings.STATICFILES_DIRS[0]+'/formatos/base.xlsx')

    logo = openpyxl.drawing.Image(settings.STATICFILES_DIRS[0]+'/formatos/logo.png')
    logo.drawing.top = 10
    logo.drawing.left = 25

    hoja1 = archivo.get_sheet_by_name('hoja1')
    hoja1.title = smart_unicode(gestor.nombre)
    hoja1.add_image(logo)

    celda = hoja1.cell('E2')
    celda.value = 'ACCESO'

    celda = hoja1.cell('E3')
    celda.value = 'REPORTE QUINCENAL - '+smart_unicode(gestor.nombre)

    celda = hoja1.cell('I3')
    celda.value = time.strftime("%d/%m/%y")

    celda = hoja1.cell('I4')
    celda.value = time.strftime("%I:%M:%S %p")

    row_num = 5

    columnas = Actividad.objects.order_by('id').values('nombre','titulo')
    columns = [tuple(['Radicado',30]),
               tuple(['Departamento',30]),
               tuple(['Municipio',30]),
               tuple(['Ciclo',30]),
               tuple(['Componente',30]),
               tuple(['Modulo',30]),
               tuple(['Actividad',30]),
               tuple(['Valor',30]),
               tuple(['Corte',30]),
               ]



    for col_num in xrange(len(columns)):
        c = hoja1.cell(row=row_num, column=col_num+1)
        c.value = columns[col_num][0]
        c.style = t
        hoja1.column_dimensions[openpyxl.cell.get_column_letter(col_num+1)].width = columns[col_num][1]


    evidencias = Evidencia.objects.filter(gestor__id=gestor_id).filter(corte_id=corte.id)
    valor = evidencias.aggregate(Sum('valor__valor'))['valor__valor__sum']

    for evidencia in evidencias:
        row_num += 1
        row = [
            evidencia.radicado.numero,
            evidencia.radicado.municipio.departamento.nombre,
            evidencia.radicado.municipio.nombre,
            evidencia.ciclo.nombre,
            evidencia.componente.nombre,
            evidencia.modulo.nombre,
            str(evidencia.actividad.nombre)+" - "+str(evidencia.actividad.titulo),
            evidencia.valor.valor,
            str(evidencia.corte.fecha)+" - "+str(evidencia.corte.titulo) if evidencia.corte != None else "",
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

    f = StringIO.StringIO()
    archivo.save(f)

    contenido = '<b>Apreciado(a) Gestor(a): '+gestor.nombre+'</b><br><br>'+'<p>Cordial saludo,</p>'+'<br>'+\
                '<p>Para la <b>Asociación Nacional para el Desarrollo Social - ANDES</b> y el programa <b>Computadores para Educar</b> es ' \
                'un placer contar con Gestores tan comprometidos con su trabajo, te informamos que adjunto puedes encontrar el reporte detallado con las' \
                ' actividades cargadas en el sistema SICAN con corte: <b>'+str(corte.fecha)+'</b> por un valor total de' \
                ' <b>$'+str(int(valor))+'</b>.</p>'+'<br>'
    email = EmailMessage("Reporte Quincena - "+corte.titulo+" - "+str(corte.fecha),contenido,to=["dandresfsoto@gmail.com"],from_email='sistemas@asoandes.org')
    email.attach('Reporte.xlsx', f.getvalue(), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    email.content_subtype = "html"
    email.send()

    archivo.save(response)
    return response