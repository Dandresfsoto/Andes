#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import ParticipanteEscuelaTicTrucho, CargasMasivas
from formador.models import Formador
from municipio.models import Municipio
from django.http import HttpResponse
from conf import settings
import openpyxl
from formacion.models import ParticipanteEscuelaTic, Grupo
import time
import datetime
from openpyxl.styles import Style, PatternFill, Border, Side, Alignment, Protection, Font
from .models import CodigoMasivo
from region.models import Region
from formador.models import Formador
import pythoncom
from win32com import client
from win32com.client import DispatchEx
from win32com import *
from django.shortcuts import HttpResponseRedirect

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

def carga_participantes(modeladmin,request,queryset):
    for archivo_queryset in queryset:
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Carga Masiva.xlsx'
        archivo = openpyxl.load_workbook(settings.STATICFILES_DIRS[0]+'/formatos/base.xlsx')

        logo = openpyxl.drawing.Image(settings.STATICFILES_DIRS[0]+'/formatos/logo.png')
        logo.drawing.top = 10
        logo.drawing.left = 25

        hoja1 = archivo.get_sheet_by_name('hoja1')
        hoja1.title = "Carga Masiva Participantes"
        hoja1.add_image(logo)

        celda = hoja1.cell('E2')
        celda.value = 'Formacion'

        celda = hoja1.cell('E3')
        celda.value = 'Carga Masiva Participantes'

        celda = hoja1.cell('I3')
        celda.value = time.strftime("%d/%m/%y")

        celda = hoja1.cell('I4')
        celda.value = time.strftime("%I:%M:%S %p")

        row_num = 5

        columns = [tuple(['CODIGO MASIVO',30]),
                   tuple(['REGION',30]),
                   tuple(['DEPARTAMENTO',30]),
                   tuple(['MUNICIPIO',30]),
                   tuple(['INSTITUCION',30]),
                   tuple(['GRUPO',30]),
                   tuple(['GRUPO',30]),
                   tuple(['NOMBRE FORMADOR',30]),
                   tuple(['CEDULA FORMADOR',30]),
                   tuple(['NOMBRES',30]),
                   tuple(['APELLIDOS',30]),
                   tuple(['CEDULA',60]),
                   tuple(['GENERO',30]),
                   tuple(['NIVEL EDUCATIVO',60]),
                   tuple(['CELULAR',30]),
                   tuple(['CORREO',30]),
                   tuple(['TIPO POBLACION',30]),
                   tuple(['CODIGO ANSPE',30]),
                   tuple(['TIPO PROYECTO',30]),
                   tuple(['GRUPO DE CONFORMACION',30]),
                   tuple(['RESULTADO',30]),
                   ]

        for col_num in xrange(len(columns)):
            c = hoja1.cell(row=row_num, column=col_num+1)
            c.value = columns[col_num][0]
            c.style = t
            hoja1.column_dimensions[openpyxl.cell.get_column_letter(col_num+1)].width = columns[col_num][1]


        archivo_masivo = openpyxl.load_workbook(settings.MEDIA_ROOT+'/'+unicode(archivo_queryset.archivo))

        hoja1_masivo = archivo_masivo.get_sheet_by_name('MATRIZ PADRES DE FAMILIA-INTERV')

        i = 0

        for fila in hoja1_masivo.rows:
            i += 1
            if i > 3:
                proceso =""
                try:
                    cedula = fila[10].value.replace('.','').replace(',','')
                except:
                    cedula = fila[10].value

                nombres = fila[8].value
                apellidos = fila[9].value

                if CodigoMasivo.objects.filter(codigo=int(fila[0].value)).count() == 0:
                    x = CodigoMasivo(codigo=int(fila[0].value))
                    x.save()

                codigo_masivo = CodigoMasivo.objects.get(codigo=int(fila[0].value))
                cantidad = ParticipanteEscuelaTicTrucho.objects.filter(codigo_masivo__codigo=int(fila[0].value)).count()

                if codigo_masivo.generado == False and cantidad <= 20:
                    if cedula == "" or cedula == None:
                        proceso = "El campo de cedula esta vacio"
                    else:
                        try:
                            long(cedula)
                        except ValueError:
                            proceso = "El numero de cedula es invalido"
                        else:
                            if ParticipanteEscuelaTic.objects.filter(cedula=cedula).count() != 0:
                                proceso = "La Cedula ya se encuentra registrada (Modulo Principal)"
                            else:
                                if ParticipanteEscuelaTicTrucho.objects.filter(cedula=cedula).count() != 0:
                                    proceso = "La Cedula ya se encuentra registrada (Modulo Actual)"
                                else:
                                    if nombres == "" or nombres == None:
                                        proceso = "El campo de nombres esta vacio"
                                    else:
                                        if apellidos == "" or apellidos == None:
                                            proceso = "El campo de apellidos esta vacio"
                                        else:
                                            if Formador.objects.filter(cedula=fila[7].value).count() == 0:
                                                proceso = "No existe el formador"
                                            else:
                                                formador = Formador.objects.get(cedula=fila[7].value)
                                                if Grupo.objects.filter(formador__id=formador.id).count() == 0:
                                                    proceso = "El formador no tiene grupos asignados"
                                                else:
                                                    grupo = Grupo.objects.filter(formador__id=formador.id)[0]
                                                    proceso = "Registrado Correctamente"
                                                    nuevo = ParticipanteEscuelaTicTrucho()
                                                    nuevo.codigo_masivo = codigo_masivo

                                                    if fila[1].value == 1:
                                                        nuevo.region = Region.objects.get(id=1)
                                                    if fila[1].value == 4:
                                                        nuevo.region = Region.objects.get(id=2)

                                                    nuevo.departamento = fila[2].value
                                                    nuevo.municipio = fila[3].value
                                                    nuevo.institucion = fila[4].value
                                                    nuevo.grupo = grupo
                                                    nuevo.formador = grupo.formador

                                                    nuevo.nombres = fila[8].value
                                                    nuevo.apellidos = fila[9].value
                                                    nuevo.cedula = long(cedula)
                                                    if fila[11].value == None or fila[11].value == "":
                                                        nuevo.genero = "Masculino"
                                                        proceso = "Registrado Correctamente - Genero Masculino por defecto"
                                                    else:
                                                        nuevo.genero = fila[11].value
                                                    nuevo.nivel_educativo = fila[12].value
                                                    nuevo.telefono = fila[13].value
                                                    if validateEmail(fila[14].value):
                                                        nuevo.correo = fila[14].value
                                                    nuevo.poblacion = fila[15].value
                                                    nuevo.codigo_anspe = fila[16].value
                                                    nuevo.tipo_proyecto = fila[17].value
                                                    nuevo.grupo_conformacion = fila[18].value
                                                    nuevo.save()

                elif codigo_masivo.generado == True:
                    proceso = "El listado ya fue generado y no se pueden agregar mas participantes"
                else:
                    proceso = "Hay mas de 20 participantes en el listado"

                row_num += 1
                row = [
                    fila[0].value,
                    fila[1].value,
                    fila[2].value,
                    fila[3].value,
                    fila[4].value,
                    fila[5].value,
                    fila[6].value,
                    fila[7].value,
                    fila[8].value,
                    fila[9].value,
                    fila[10].value,
                    fila[11].value,
                    fila[12].value,
                    fila[13].value,
                    fila[14].value,
                    fila[15].value,
                    fila[16].value,
                    fila[17].value,
                    fila[18].value,
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

        archivo.save(response)
        return response
carga_participantes.short_description = "Cargar participantes"


class CargasMasivasAdmin(admin.ModelAdmin):
    list_display = ['id','archivo']
    ordering = ['archivo']
    actions = [carga_participantes]
admin.site.register(CargasMasivas, CargasMasivasAdmin)
admin.site.register(ParticipanteEscuelaTicTrucho)


def generar_listas(modeladmin,request,queryset):
    pythoncom.CoInitializeEx(pythoncom.COINIT_MULTITHREADED)
    xl = win32com.client.dynamic.Dispatch('Excel.Application')
    xl.DisplayAlerts = True
    xl.Visible = 0

    lista = xl.Workbooks.Open(settings.STATICFILES_DIRS[0]+'/formatos/Lista Padres.xlsx')

    i = 2

    for codigo_masivo in queryset:
        participantes = ParticipanteEscuelaTicTrucho.objects.filter(codigo_masivo__id=codigo_masivo.id)
        for sesion_numero in range(1,3):
            fila = 0
            if sesion_numero == 1:
                lista.Worksheets("Sesion").Copy(lista.Worksheets(lista.Worksheets.Count))
                sesion = lista.Worksheets('Sesion ('+str(i)+')')
                i += 1
                sesion.Cells(5,3).Value = "Sesión 1:______X_______".encode("latin1")
                sesion.Cells(5,5).Value = "Sesión 2:______________".encode("latin1")
                departamento = participantes[0].departamento
                municipio = participantes[0].municipio
                formador = participantes[0].formador.nombre
                sesion.Cells(6,1).Value = "Departamento: "+departamento.encode("latin1")+"                         "+"Municipio: "+municipio.encode("latin1")
                sesion.Cells(5,7).Value = "Formador: "+formador.encode("latin1")
                for participante in participantes:
                    sesion.Cells(10+fila,2).Value = participante.nombres.encode("latin1")
                    sesion.Cells(10+fila,3).Value = participante.apellidos.encode("latin1")
                    sesion.Cells(10+fila,4).Value = participante.cedula
                    sesion.Cells(10+fila,5).Value = participante.correo
                    sesion.Cells(10+fila,6).Value = participante.telefono
                    fila += 1
            if sesion_numero == 2:
                lista.Worksheets("Sesion").Copy(lista.Worksheets(lista.Worksheets.Count))
                sesion = lista.Worksheets('Sesion ('+str(i)+')')
                i += 1
                sesion.Cells(5,3).Value = "Sesión 1:______________".encode("latin1")
                sesion.Cells(5,5).Value = "Sesión 2:______X_______".encode("latin1")
                departamento = participantes[0].departamento
                municipio = participantes[0].municipio
                formador = participantes[0].formador.nombre
                sesion.Cells(6,1).Value = "Departamento: "+departamento.encode("latin1")+"                         "+"Municipio: "+municipio.encode("latin1")
                sesion.Cells(5,7).Value = "Formador: "+formador.encode("latin1")
                for participante in participantes:
                    sesion.Cells(10+fila,2).Value = participante.nombres.encode("latin1")
                    sesion.Cells(10+fila,3).Value = participante.apellidos.encode("latin1")
                    sesion.Cells(10+fila,4).Value = participante.cedula
                    sesion.Cells(10+fila,5).Value = participante.correo
                    sesion.Cells(10+fila,6).Value = participante.telefono
                    fila += 1

    lista.Worksheets('Sesion').Delete()
    lista.ExportAsFixedFormat(0,settings.MEDIA_ROOT+'/Listados Escuela Tic/Padres.pdf')
    lista.Close(SaveChanges=False)

    xl.Quit()
    pythoncom.CoUninitialize()

    for codigo_masivo in queryset:
        codigo_masivo.generado = True
        codigo_masivo.save()

    return HttpResponseRedirect('/media/Listados Escuela Tic/Padres.pdf')
generar_listas.short_description = "Generar Listas"


class CodigoMasivoAdmin(admin.ModelAdmin):
    list_display = ['id','generado']
    list_filter = ['generado']
    ordering = ['id']
    actions = [generar_listas]
admin.site.register(CodigoMasivo,CodigoMasivoAdmin)