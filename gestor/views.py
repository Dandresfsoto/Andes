from .models import Gestor
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q
from acceso.models import Evidencia

class GestorTableView(BaseDatatableView):
    model = Gestor
    columns = [
        'id',
        'nombre',
        'cedula',
        'celular',
        'correo',
        'cargo',
        'profesion',
        'banco',
        'tipo_cuenta',
        'numero_cuenta',
        'eps',
        'pension',
        'arl',
        'foto',
        'hv',
        'certificacion',
        'rut',
        'contrato',
        'fotocopia_cedula',
        'antecedentes_judiciales',
        'antecedentes_contraloria',
        'seguro_enero',
        'seguro_febrero',
        'seguro_marzo',
        'seguro_abril',
        'seguro_mayo',
        'seguro_junio',
        'seguro_julio',
        'seguro_agosto',
        'seguro_septiembre',
        'seguro_octubre',
        'seguro_noviembre',
        'seguro_diciembre',
        'fecha_contratacion',
        'fecha_terminacion',
    ]

    order_columns = [
        'nombre',
        'cedula',
        'celular',
        'correo',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        ''
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.all().filter(region__id=self.kwargs['region'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'nombre__icontains' : search})
            q |= Q(**{'cedula__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'hv':
            return str(row.hv)
        if column == 'certificacion':
            return str(row.certificacion)
        if column == 'rut':
            return str(row.rut)
        if column == 'contrato':
            return str(row.contrato)
        if column == 'seguro_enero':
            return str(row.seguro_enero)
        if column == 'seguro_febrero':
            return str(row.seguro_febrero)
        if column == 'seguro_marzo':
            return str(row.seguro_marzo)
        if column == 'seguro_abril':
            return str(row.seguro_abril)
        if column == 'seguro_mayo':
            return str(row.seguro_mayo)
        if column == 'seguro_junio':
            return str(row.seguro_junio)
        if column == 'seguro_julio':
            return str(row.seguro_julio)
        if column == 'seguro_agosto':
            return str(row.seguro_agosto)
        if column == 'seguro_septiembre':
            return str(row.seguro_septiembre)
        if column == 'seguro_octubre':
            return str(row.seguro_octubre)
        if column == 'seguro_noviembre':
            return str(row.seguro_noviembre)
        if column == 'seguro_diciembre':
            return str(row.seguro_diciembre)
        if column == 'fotocopia_cedula':
            return str(row.fotocopia_cedula)
        if column == 'antecedentes_judiciales':
            return str(row.antecedentes_judiciales)
        if column == 'antecedentes_contraloria':
            return str(row.antecedentes_contraloria)
        if column == 'foto':
            return str(row.foto)
        else:
            return super(GestorTableView,self).render_column(row,column)

class GestorCalificacionTableView(BaseDatatableView):
    model = Gestor
    columns = [
        'id',
        'nombre',
        'cedula',
        'celular',
        'correo',
        'cargo',
        'profesion',
        'foto',
    ]

    order_columns = [
        'nombre',
        'cedula',
        'celular',
        'correo',
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.all().filter(region__id=self.kwargs['region'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'nombre__icontains' : search})
            q |= Q(**{'cedula__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'foto':
            return str(row.foto)
        else:
            return super(GestorCalificacionTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            actividades = Evidencia.objects.all().filter(gestor__id=item.id)
            radicado = actividades.values_list('radicado',flat=True).distinct().count()
            actividades_ejecutadas = actividades.exclude(soporte = "")
            actividades_sinEjecutar = actividades.filter(soporte = "")
            if actividades.count() != 0:
                progreso = format(actividades_ejecutadas.count()*100/actividades.count(), '.2f')
            else:
                progreso = 0


            json_data.append([
                item.id,
                item.nombre,
                item.cedula,
                item.celular,
                item.correo,
                item.cargo,
                item.profesion,
                str(item.foto),
                actividades.count(),
                radicado,
                actividades_ejecutadas.count(),
                actividades_sinEjecutar.count(),
                progreso,
            ])
        return json_data