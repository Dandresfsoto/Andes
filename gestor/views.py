from .models import Gestor
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q
from acceso.models import Evidencia, Corte, EvidenciaApoyo, CorteApoyo
from radicado.models import Radicado
from django.db.models import Sum

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
        'contrato_plan_choque',
        'liquidacion',
        'seguro_enero_1',
        'seguro_febrero_1',
        'seguro_marzo_1',
        'seguro_abril_1',
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
        return self.model.objects.all().filter(region__id=self.kwargs['region']).filter(tipo__id=self.kwargs['tipo'])

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
        if column == 'contrato_plan_choque':
            return str(row.contrato_plan_choque)
        if column == 'liquidacion':
            return str(row.liquidacion)
        if column == 'seguro_enero_1':
            return str(row.seguro_enero_1)
        if column == 'seguro_febrero_1':
            return str(row.seguro_febrero_1)
        if column == 'seguro_marzo_1':
            return str(row.seguro_marzo_1)
        if column == 'seguro_abril_1':
            return str(row.seguro_abril_1)
        if column == 'foto':
            return str(row.foto)
        else:
            return super(GestorTableView,self).render_column(row,column)

class GestorFinancieroTableView(BaseDatatableView):
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
            return Evidencia.objects.filter(gestor__id=row.id).exclude(corte=None).aggregate(Sum('valor__valor'))['valor__valor__sum']
        if column == 'certificacion':
            return Evidencia.objects.filter(gestor__id=row.id).aggregate(Sum('valor__valor'))['valor__valor__sum']
        if column == 'rut':
            cortes = Corte.objects.filter(region__id=self.kwargs['region'])
            json = []
            for corte in cortes:
                evidencias = Evidencia.objects.filter(gestor__id=row.id).filter(corte__id=corte.id)
                if evidencias.count() > 0:
                    fecha = corte.fecha
                    titulo = corte.titulo
                    descripcion = corte.descripcion
                    valor = round(int(evidencias.aggregate(Sum('valor__valor'))['valor__valor__sum']))
                    id_corte = corte.id
                    json.append([fecha,titulo,descripcion,valor,corte.id])
                else:
                    fecha = corte.fecha
                    titulo = corte.titulo
                    descripcion = corte.descripcion
                    json.append([fecha,titulo,descripcion,0,corte.id])
            return json
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
            return super(GestorFinancieroTableView,self).render_column(row,column)

class GestorFinancieroApoyoTableView(BaseDatatableView):
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
            return EvidenciaApoyo.objects.filter(gestor__id=row.id).exclude(corte=None).aggregate(Sum('valor__valor'))['valor__valor__sum']
        if column == 'certificacion':
            return EvidenciaApoyo.objects.filter(gestor__id=row.id).aggregate(Sum('valor__valor'))['valor__valor__sum']
        if column == 'rut':
            cortes = CorteApoyo.objects.filter(region__id=self.kwargs['region'])
            json = []
            for corte in cortes:
                evidencias = EvidenciaApoyo.objects.filter(gestor__id=row.id).filter(corte__id=corte.id)
                if evidencias.count() > 0:
                    fecha = corte.fecha
                    titulo = corte.titulo
                    descripcion = corte.descripcion
                    valor = round(int(evidencias.aggregate(Sum('valor__valor'))['valor__valor__sum']))
                    id_corte = corte.id
                    json.append([fecha,titulo,descripcion,valor,corte.id])
                else:
                    fecha = corte.fecha
                    titulo = corte.titulo
                    descripcion = corte.descripcion
                    json.append([fecha,titulo,descripcion,0,corte.id])
            return json
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
            return super(GestorFinancieroApoyoTableView,self).render_column(row,column)

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
        'nombre'
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.all().filter(region__id=self.kwargs['region']).filter(tipo__id=self.kwargs['tipo'])

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
            return super(GestorCalificacionTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            actividades = Evidencia.objects.filter(gestor__id=item.id)
            radicado = actividades.values_list('radicado',flat=True).distinct().count()
            actividades_ejecutadas = actividades.exclude(corte = None)
            actividades_sinEjecutar = actividades.filter(corte = None)
            actividades_sinReportar = actividades.filter(corte = None).exclude(soporte="")
            if actividades.count() != 0:
                progreso = format((actividades_ejecutadas.count()*100.0)/actividades.count(), '.2f')
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
                actividades_sinReportar.count()
            ])
        return json_data

class GestorCalificacionApoyoTableView(BaseDatatableView):
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
        'nombre'
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.all().filter(region__id=self.kwargs['region']).filter(tipo__id=self.kwargs['tipo'])

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
            return super(GestorCalificacionApoyoTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            actividades = EvidenciaApoyo.objects.filter(gestor__id=item.id)
            radicado = actividades.values_list('radicado',flat=True).distinct().count()
            actividades_ejecutadas = actividades.exclude(corte = None)
            actividades_sinEjecutar = actividades.filter(corte = None)
            actividades_sinReportar = actividades.filter(corte = None).exclude(soporte="")
            if actividades.count() != 0:
                progreso = format((actividades_ejecutadas.count()*100.0)/actividades.count(), '.2f')
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
                actividades_sinReportar.count()
            ])
        return json_data

class GestorCorteEvidenciasTableView(BaseDatatableView):
    model = Evidencia
    columns = [
        'id',
        'radicado',
        'gestor',
        'ciclo',
        'componente',
        'modulo',
        'actividad',
        'encargado',
        'valor',
        'soporte',
        'corte',
        'usuario',
        'modificacion',
    ]

    order_columns = [
        'radicado',
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(gestor__id=self.kwargs['gestor']).filter(corte__id=self.kwargs['corte']).values_list('radicado__numero',flat=True).distinct()

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'radicado__numero__icontains' : search.capitalize()})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'radicado':
            return row.radicado.numero
        if column == 'gestor':
            return row.gestor.nombre
        if column == 'ciclo':
            return row.ciclo.nombre
        if column == 'componente':
            return row.componente.nombre
        if column == 'modulo':
            return row.modulo.nombre
        if column == 'actividad':
            return row.actividad.nombre
        if column == 'encargado':
            return row.encargado.encargado
        if column == 'valor':
            return row.valor.valor
        if column == 'soporte':
            return str(row.soporte)
        if column == 'corte':
            return row.corte.titulo
        if column == 'usuario':
            return row.usuario.username
        if column == 'modificacion':
            return str(row.modificacion)
        else:
            return super(GestorCorteEvidenciasTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            radicado = Radicado.objects.get(numero=item)
            evidencias = Evidencia.objects.filter(radicado__numero=item).filter(corte__id=self.kwargs['corte'])
            evidencia_radicado = []
            for evidencia in evidencias:
                evidencia_radicado.append([
                    evidencia.ciclo.nombre,
                    evidencia.componente.nombre,
                    evidencia.modulo.nombre,
                    evidencia.actividad.nombre,
                    evidencia.actividad.descripcion,
                    evidencia.valor.valor,
                    str(evidencia.soporte),
                    evidencia.usuario.username,
                    evidencia.modificacion
                ])
            json_data.append([

                item,
                radicado.municipio.nombre,
                radicado.municipio.departamento.nombre,
                evidencias.count(),
                evidencia_radicado
            ])

        return json_data

class GestorCorteApoyoEvidenciasTableView(BaseDatatableView):
    model = EvidenciaApoyo
    columns = [
        'id',
        'radicado',
        'gestor',
        'ciclo',
        'componente',
        'modulo',
        'actividad',
        'encargado',
        'valor',
        'soporte',
        'corte',
        'usuario',
        'modificacion',
    ]

    order_columns = [
        'radicado',
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(gestor__id=self.kwargs['gestor']).filter(corte__id=self.kwargs['corte']).values_list('radicado__numero',flat=True).distinct()

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'radicado__numero__icontains' : search.capitalize()})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'radicado':
            return row.radicado.numero
        if column == 'gestor':
            return row.gestor.nombre
        if column == 'ciclo':
            return row.ciclo.nombre
        if column == 'componente':
            return row.componente.nombre
        if column == 'modulo':
            return row.modulo.nombre
        if column == 'actividad':
            return row.actividad.nombre
        if column == 'encargado':
            return row.encargado.encargado
        if column == 'valor':
            return row.valor.valor
        if column == 'soporte':
            return str(row.soporte)
        if column == 'corte':
            return row.corte.titulo
        if column == 'usuario':
            return row.usuario.username
        if column == 'modificacion':
            return str(row.modificacion)
        else:
            return super(GestorCorteApoyoEvidenciasTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            radicado = Radicado.objects.get(numero=item)
            evidencias = EvidenciaApoyo.objects.filter(radicado__numero=item).filter(corte__id=self.kwargs['corte'])
            evidencia_radicado = []
            for evidencia in evidencias:
                evidencia_radicado.append([
                    evidencia.ciclo.nombre,
                    evidencia.componente.nombre,
                    evidencia.modulo.nombre,
                    evidencia.actividad.nombre,
                    evidencia.actividad.descripcion,
                    evidencia.valor.valor,
                    str(evidencia.soporte),
                    evidencia.usuario.username,
                    evidencia.modificacion
                ])
            json_data.append([

                item,
                radicado.municipio.nombre,
                radicado.municipio.departamento.nombre,
                evidencias.count(),
                evidencia_radicado
            ])

        return json_data