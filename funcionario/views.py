from .models import Funcionario
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q

class FuncionarioTableView(BaseDatatableView):
    model = Funcionario
    columns = [
        'nombre',
        'cedula',
        'celular',
        'correo',
        'hv',
        'certificacion',
        'rut',
        'contrato',
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
        'id',
        'fotocopia_cedula',
        'antecedentes_judiciales',
        'antecedentes_contraloria',
        'cargo',
        'banco',
        'tipo_cuenta',
        'numero_cuenta',
        'eps',
        'pension',
        'arl',
        'foto',
        'profesion',
    ]

    order_columns = [
        'nombre',
        'nombre',
        'nombre',
        'nombre',
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
            return super(FuncionarioTableView,self).render_column(row,column)

class FuncionarioTableEjeView(BaseDatatableView):
    model = Funcionario
    columns = [
        'nombre',
        'cedula',
        'celular',
        'correo',
        'hv',
        'certificacion',
        'rut',
        'contrato',
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
        'id',
        'fotocopia_cedula',
        'antecedentes_judiciales',
        'antecedentes_contraloria',
        'cargo',
        'banco',
        'tipo_cuenta',
        'numero_cuenta',
        'eps',
        'pension',
        'arl',
        'foto',
        'profesion',
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
        return self.model.objects.all().filter(region__id=self.kwargs['region']).filter(eje__id=self.kwargs['eje'])

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
            return super(FuncionarioTableEjeView,self).render_column(row,column)