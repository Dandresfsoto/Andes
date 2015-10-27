from .models import Formador
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q
from formacion.models import Grupo,ParticipanteEscuelaTic, SoporteEntregableEscuelaTic

class FormadorTableView(BaseDatatableView):
    model = Formador
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
        return self.model.objects.filter(region__id=self.kwargs['region']).filter(tipo__id=self.kwargs['tipo'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'nombre__icontains' : search.capitalize()})
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
            return super(FormadorTableView,self).render_column(row,column)

class FormadorCalificacionTableView(BaseDatatableView):
    model = Formador
    columns = [
        'id',
        'nombre',
        'cedula',
        'celular',
        'correo',
        'cargo',
        'profesion',
        'foto',
        'fecha_contratacion',
        'fecha_terminacion',
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
        return self.model.objects.filter(region__id=self.kwargs['region']).filter(tipo__id=2)

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'nombre__icontains' : search.capitalize()})
            q |= Q(**{'cedula__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'foto':
            return str(row.foto)
        else:
            return super(FormadorCalificacionTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            grupos = Grupo.objects.filter(formador__id=item.id).count()
            participantes = ParticipanteEscuelaTic.objects.filter(formador__id=item.id).count()
            json_data.append([
                item.id,
                item.nombre,
                item.cedula,
                item.celular,
                item.correo,
                item.cargo,
                item.profesion,
                str(item.foto),
                item.fecha_contratacion,
                item.fecha_terminacion,
                grupos,
                participantes
            ])

        return json_data

class FormadorGrupoTableView(BaseDatatableView):
    model = Grupo
    columns = [
        'id',
        'formador',
        'municipio',
        'nombre',
        'direccion',
        'horario'
    ]

    order_columns = [
        'id',
        'formador',
        'municipio',
        'nombre',
        'direccion',
        'horario'
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(formador__id=self.kwargs['id_formador'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'nombre__icontains' : search.capitalize()})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'formador':
            return str(row.nombre)
        if column == 'municipio':
            return str(row.municipio.nombre)
        else:
            return super(FormadorGrupoTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            participantes = ParticipanteEscuelaTic.objects.filter(grupo__id=item.id).count()
            soportes = SoporteEntregableEscuelaTic.objects.filter(grupo__id=item.id).order_by('id')
            x=[]
            y=[]
            for soporte in soportes:
                x.append(str(soporte.soporte))
                y.append(soporte.id)
            json_data.append([
                item.id,
                item.nombre,
                item.municipio.nombre,
                item.municipio.departamento.nombre,
                item.direccion,
                item.horario,
                participantes,
                x,
                y
            ])

        return json_data

class FormadorListadoGrupoTableView(BaseDatatableView):
    model = ParticipanteEscuelaTic
    columns = [
        'id',
        'grupo',
        'formador',
        'poblacion',
        'genero',
        'nombres',
        'apellidos',
        'institucion',
        'correo',
        'telefono',
        'cedula'
    ]

    order_columns = [
        'id',
        'grupo',
        'formador',
        'poblacion',
        'genero',
        'nombres',
        'apellidos',
        'institucion',
        'correo',
        'telefono',
        'cedula'
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(formador__id=self.kwargs['id_formador']).filter(grupo__id=self.kwargs['id_grupo'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'nombres__icontains' : search.capitalize()})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'formador':
            return str(row.formador.nombre)
        if column == 'grupo':
            return str(row.grupo.nombre)
        else:
            return super(FormadorListadoGrupoTableView,self).render_column(row,column)