from django.contrib import admin
from .models import Masivo, Actividad, Entregable, Grupo, SoporteEntregableEscuelaTic, ParticipanteEscuelaTic, EvidenciaEscuelaTic, Valor, Corte
from .models import RadicadoFormacion, ParticipanteDocente, ActividadDocentes, EntregableDocentes, GrupoDocentes, SoporteEntregableDocente, EvidenciaDocentes, ValorDocente, CorteDocente
from .models import CargasMasivas
from formador.models import Formador
from municipio.models import Municipio
from django.http import HttpResponse
from conf import settings
import openpyxl
import time
import datetime
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

admin.site.register(Masivo)
admin.site.register(Actividad)
admin.site.register(ActividadDocentes)
admin.site.register(Entregable)
admin.site.register(EntregableDocentes)
admin.site.register(Grupo)
admin.site.register(GrupoDocentes)
admin.site.register(SoporteEntregableEscuelaTic)
admin.site.register(SoporteEntregableDocente)
admin.site.register(ParticipanteEscuelaTic)
admin.site.register(ParticipanteDocente)
admin.site.register(EvidenciaEscuelaTic)
admin.site.register(EvidenciaDocentes)
admin.site.register(Valor)
admin.site.register(ValorDocente)
admin.site.register(Corte)
admin.site.register(CorteDocente)
admin.site.register(RadicadoFormacion)

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False

def carga_grupos(modeladmin,request,queryset):
    for archivo_queryset in queryset:
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Carga Masiva.xlsx'
        archivo = openpyxl.load_workbook(settings.STATICFILES_DIRS[0]+'/formatos/base.xlsx')

        logo = openpyxl.drawing.Image(settings.STATICFILES_DIRS[0]+'/formatos/logo.png')
        logo.drawing.top = 10
        logo.drawing.left = 25

        hoja1 = archivo.get_sheet_by_name('hoja1')
        hoja1.title = "Reporte Carga Masiva Grupos"
        hoja1.add_image(logo)

        celda = hoja1.cell('E2')
        celda.value = 'Formacion'

        celda = hoja1.cell('E3')
        celda.value = 'Reporte Carga Masiva Grupos'

        celda = hoja1.cell('I3')
        celda.value = time.strftime("%d/%m/%y")

        celda = hoja1.cell('I4')
        celda.value = time.strftime("%I:%M:%S %p")

        row_num = 5

        columns = [tuple(['REGION',30]),
                   tuple(['DEPARTAMENTO',30]),
                   tuple(['MUNICIPIO',30]),
                   tuple(['LUGAR DE REUNION',60]),
                   tuple(['CODIGO GRUPO',30]),
                   tuple(['NOMBRE FORMADOR',60]),
                   tuple(['CEDULA',30]),
                   tuple(['RESULTADO CARGA',30]),
                   ]

        for col_num in xrange(len(columns)):
            c = hoja1.cell(row=row_num, column=col_num+1)
            c.value = columns[col_num][0]
            c.style = t
            hoja1.column_dimensions[openpyxl.cell.get_column_letter(col_num+1)].width = columns[col_num][1]


        archivo_masivo = openpyxl.load_workbook(settings.MEDIA_ROOT+'/'+unicode(archivo_queryset.archivo))

        hoja1_masivo = archivo_masivo.get_sheet_by_name('Hoja1')

        i = 0

        for fila in hoja1_masivo.rows:
            i += 1
            if i > 1:
                proceso =""

                if fila[6].value != None:
                    try:
                        cedula = long(fila[6].value)
                    except ValueError:
                        proceso = "El numero de cedula solo debe contener numeros"
                    else:
                        if Formador.objects.filter(cedula=cedula).count() == 1:
                            formador = Formador.objects.get(cedula=cedula)
                            if Municipio.objects.filter(nombre=fila[2].value).count() == 1:
                                municipio = Municipio.objects.get(nombre=fila[2].value)
                                if fila[4].value != None:
                                    if Grupo.objects.filter(nombre=fila[4].value).count() == 0:
                                        grupo = Grupo(formador=formador,nombre=fila[4].value,municipio=municipio,direccion=fila[3].value)
                                        grupo.save()
                                        proceso = "Grupo creado correctamente"
                                    else:
                                        proceso = "El grupo ya existe"
                                else:
                                    proceso = "Esta vacio el codigo de grupo"
                            else:
                                proceso = "No existe el municipio"
                        else:
                            proceso = "No hay un solo formador registrado con el numero de cedula"
                else:
                    proceso = "No hay numero de cedula valido"

                row_num += 1
                row = [
                    fila[0].value,
                    fila[1].value,
                    fila[2].value,
                    fila[3].value,
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

        archivo.save(response)
        return response
carga_grupos.short_description = "Cargar grupos"

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

        columns = [tuple(['CODIGO GRUPO',30]),
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
                   ]

        for col_num in xrange(len(columns)):
            c = hoja1.cell(row=row_num, column=col_num+1)
            c.value = columns[col_num][0]
            c.style = t
            hoja1.column_dimensions[openpyxl.cell.get_column_letter(col_num+1)].width = columns[col_num][1]


        archivo_masivo = openpyxl.load_workbook(settings.MEDIA_ROOT+'/'+unicode(archivo_queryset.archivo))

        hoja1_masivo = archivo_masivo.get_sheet_by_name('Hoja1')

        i = 0

        for fila in hoja1_masivo.rows:
            i += 1
            if i > 1:
                proceso =""
                try:
                    cedula = fila[3].value.replace('.','').replace(',','')
                except:
                    cedula = fila[3].value
                nombres = fila[1].value
                apellidos = fila[2].value


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
                                    if fila[0].value == "" or fila[3].value == None:
                                        proceso = "El Codigo de grupo no es valido"
                                    else:
                                        if Grupo.objects.filter(nombre=fila[0].value).count() != 1:
                                            proceso = "No hay un solo grupo registrado con el codigo de grupo"
                                        else:
                                            grupo = Grupo.objects.get(nombre=fila[0].value)
                                            proceso = "Registrado Correctamente"
                                            nuevo = ParticipanteEscuelaTic()
                                            nuevo.grupo = grupo
                                            nuevo.formador = grupo.formador
                                            nuevo.nombres = fila[1].value
                                            nuevo.apellidos = fila[2].value
                                            nuevo.cedula = long(cedula)
                                            if fila[4].value == None or fila[4].value == "":
                                                nuevo.genero = "Masculino"
                                                proceso = "Registrado Correctamente - Genero Masculino por defecto"
                                            else:
                                                nuevo.genero = fila[4].value
                                            nuevo.nivel_educativo = fila[5].value
                                            nuevo.telefono = fila[6].value
                                            if validateEmail(fila[7].value):
                                                nuevo.correo = fila[7].value
                                            nuevo.poblacion = fila[8].value
                                            nuevo.codigo_anspe = fila[9].value
                                            nuevo.tipo_proyecto = fila[10].value
                                            nuevo.grupo_conformacion = fila[11].value
                                            nuevo.save()

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

def carga_radicados(modeladmin,request,queryset):
    for archivo_queryset in queryset:
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Carga Masiva.xlsx'
        archivo = openpyxl.load_workbook(settings.STATICFILES_DIRS[0]+'/formatos/base.xlsx')

        logo = openpyxl.drawing.Image(settings.STATICFILES_DIRS[0]+'/formatos/logo.png')
        logo.drawing.top = 10
        logo.drawing.left = 25

        hoja1 = archivo.get_sheet_by_name('hoja1')
        hoja1.title = "Carga Masiva Radicados"
        hoja1.add_image(logo)

        celda = hoja1.cell('E2')
        celda.value = 'Formacion'

        celda = hoja1.cell('E3')
        celda.value = 'Carga Masiva Radicados'

        celda = hoja1.cell('I3')
        celda.value = time.strftime("%d/%m/%y")

        celda = hoja1.cell('I4')
        celda.value = time.strftime("%I:%M:%S %p")

        row_num = 5

        columns = [tuple(['RADICADO',30]),
                   tuple(['CODIGO DANE INSTITUCION',30]),
                   tuple(['NOMBRE INSTITUCION',30]),
                   tuple(['CODIGO DANE SEDE EDUCATIVA',30]),
                   tuple(['NOMBRE DE LA SEDE EDUCATIVA',30]),
                   ]

        for col_num in xrange(len(columns)):
            c = hoja1.cell(row=row_num, column=col_num+1)
            c.value = columns[col_num][0]
            c.style = t
            hoja1.column_dimensions[openpyxl.cell.get_column_letter(col_num+1)].width = columns[col_num][1]


        archivo_masivo = openpyxl.load_workbook(settings.MEDIA_ROOT+'/'+unicode(archivo_queryset.archivo))

        hoja1_masivo = archivo_masivo.get_sheet_by_name('Hoja1')

        i = 0

        for fila in hoja1_masivo.rows:
            i += 1
            if i > 1:
                proceso =""
                if fila[0].value != None:
                    try:
                        radicado = int(fila[0].value)
                    except ValueError:
                        proceso = "El numero de radicado solo debe contener numeros"
                    else:
                        if RadicadoFormacion.objects.filter(numero=radicado).count() == 0:
                            nuevo = RadicadoFormacion()
                            nuevo.numero = radicado
                            if fila[1].value != None:
                                nuevo.dane_ie = fila[1].value
                            if fila[2].value != None:
                                nuevo.nombre_ie = fila[2].value
                            if fila[3].value != None:
                                nuevo.dane_sede = fila[3].value
                            if fila[4].value != None:
                                nuevo.nombre_sede = fila[4].value
                            nuevo.save()
                            proceso = "Radicado creado satisfactoriamente"
                        else:
                            proceso = "Ya existe el radicado"
                else:
                    proceso = "No hay numero de radicado valido"

                row_num += 1
                row = [
                    fila[0].value,
                    fila[1].value,
                    fila[2].value,
                    fila[3].value,
                    fila[4].value,
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
carga_radicados.short_description = "Cargar radicados"

def carga_grupos_docentes(modeladmin,request,queryset):
    for archivo_queryset in queryset:
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Carga Masiva.xlsx'
        archivo = openpyxl.load_workbook(settings.STATICFILES_DIRS[0]+'/formatos/base.xlsx')

        logo = openpyxl.drawing.Image(settings.STATICFILES_DIRS[0]+'/formatos/logo.png')
        logo.drawing.top = 10
        logo.drawing.left = 25

        hoja1 = archivo.get_sheet_by_name('hoja1')
        hoja1.title = "Reporte Carga Masiva Grupos"
        hoja1.add_image(logo)

        celda = hoja1.cell('E2')
        celda.value = 'Formacion'

        celda = hoja1.cell('E3')
        celda.value = 'Reporte Carga Masiva Grupos'

        celda = hoja1.cell('I3')
        celda.value = time.strftime("%d/%m/%y")

        celda = hoja1.cell('I4')
        celda.value = time.strftime("%I:%M:%S %p")

        row_num = 5

        columns = [tuple(['REGION',30]),
                   tuple(['DEPARTAMENTO',30]),
                   tuple(['SECRETARIA',30]),
                   tuple(['LUGAR DE REUNION',60]),
                   tuple(['CODIGO GRUPO',30]),
                   tuple(['NOMBRE FORMADOR',60]),
                   tuple(['CEDULA',30]),
                   tuple(['RESULTADO CARGA',30]),
                   ]

        for col_num in xrange(len(columns)):
            c = hoja1.cell(row=row_num, column=col_num+1)
            c.value = columns[col_num][0]
            c.style = t
            hoja1.column_dimensions[openpyxl.cell.get_column_letter(col_num+1)].width = columns[col_num][1]


        archivo_masivo = openpyxl.load_workbook(settings.MEDIA_ROOT+'/'+unicode(archivo_queryset.archivo))

        hoja1_masivo = archivo_masivo.get_sheet_by_name('Hoja1')

        i = 0

        for fila in hoja1_masivo.rows:
            i += 1
            if i > 1:
                proceso =""

                if fila[6].value != None:
                    try:
                        cedula = long(fila[6].value)
                    except ValueError:
                        proceso = "El numero de cedula solo debe contener numeros"
                    else:
                        if Formador.objects.filter(cedula=cedula).count() == 1:
                            formador = Formador.objects.get(cedula=cedula)
                            if Municipio.objects.filter(nombre=fila[2].value).count() == 1:
                                municipio = Municipio.objects.get(nombre=fila[2].value)
                                if fila[4].value != None:
                                    if GrupoDocentes.objects.filter(nombre=fila[4].value).count() == 0:
                                        grupo = GrupoDocentes(formador=formador,nombre=fila[4].value,municipio=municipio,direccion=fila[3].value)
                                        grupo.save()
                                        proceso = "Grupo creado correctamente"
                                    else:
                                        proceso = "El grupo ya existe"
                                else:
                                    proceso = "Esta vacio el codigo de grupo"
                            else:
                                proceso = "No existe la secretaria"
                        else:
                            proceso = "No hay un solo formador registrado con el numero de cedula"
                else:
                    proceso = "No hay numero de cedula valido"

                row_num += 1
                row = [
                    fila[0].value,
                    fila[1].value,
                    fila[2].value,
                    fila[3].value,
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

        archivo.save(response)
        return response
carga_grupos_docentes.short_description = "Cargar grupos de Docentes"

class CargasMasivasAdmin(admin.ModelAdmin):
    list_display = ['id','archivo']
    ordering = ['archivo']
    actions = [carga_grupos,carga_participantes,carga_radicados,carga_grupos_docentes]

admin.site.register(CargasMasivas, CargasMasivasAdmin)


# Register your models here.