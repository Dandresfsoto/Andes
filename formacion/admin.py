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


class CargasMasivasAdmin(admin.ModelAdmin):
    list_display = ['id','archivo']
    ordering = ['archivo']
    actions = [carga_grupos]

admin.site.register(CargasMasivas, CargasMasivasAdmin)


# Register your models here.