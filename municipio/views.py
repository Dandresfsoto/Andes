from acceso.models import Evidencia, EvidenciaApoyo
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q

class MunicipioTableView(BaseDatatableView):
    model = Evidencia
    columns = [
        'radicado',
    ]

    order_columns = [
        'radicado',
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(gestor__id=self.kwargs['id_gestor']).values('radicado__municipio__id',
                                                                                     'radicado__municipio__nombre',
                                                                                     'radicado__municipio__departamento__nombre').distinct()

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'radicado__municipio__nombre__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'radicado':
            return str(row.radicado.municipio.nombre)
        else:
            return super(MunicipioTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        qs = Evidencia.objects.filter(gestor__id=self.kwargs['id_gestor']).values('radicado__municipio__id',
                                                                                  'radicado__municipio__nombre',
                                                                                  'radicado__municipio__departamento__nombre',
                                                                                  'radicado__municipio__codigo',
                                                                                  'radicado__municipio__departamento__codigo').distinct()
        for item in qs:
            actividades = Evidencia.objects.all().filter(gestor__id=self.kwargs['id_gestor']).filter(radicado__municipio__id=item['radicado__municipio__id'])
            ejecutadas = actividades.exclude(corte=None).count()
            sin_ejecutar = actividades.filter(corte=None).count()
            sin_reportar = actividades.filter(corte=None).exclude(soporte="").count()

            if actividades.count() != 0:
                progreso = format((ejecutadas*100.0)/actividades.count(), '.2f')
            else:
                progreso = 0
            json_data.append([
                item['radicado__municipio__id'],
                item['radicado__municipio__nombre'],
                item['radicado__municipio__departamento__nombre'],
                item['radicado__municipio__codigo'],
                item['radicado__municipio__departamento__codigo'],
                ejecutadas,
                sin_ejecutar,
                sin_reportar,
                progreso,
                actividades.count()
            ])
        return json_data

class MunicipioTableApoyoView(BaseDatatableView):
    model = EvidenciaApoyo
    columns = [
        'radicado',
    ]

    order_columns = [
        'radicado',
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(gestor__id=self.kwargs['id_gestor']).values('radicado__municipio__id',
                                                                                     'radicado__municipio__nombre',
                                                                                     'radicado__municipio__departamento__nombre').distinct()

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'radicado__municipio__nombre__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'radicado':
            return str(row.radicado.municipio.nombre)
        else:
            return super(MunicipioTableApoyoView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        qs = EvidenciaApoyo.objects.filter(gestor__id=self.kwargs['id_gestor']).values('radicado__municipio__id',
                                                                                  'radicado__municipio__nombre',
                                                                                  'radicado__municipio__departamento__nombre',
                                                                                  'radicado__municipio__codigo',
                                                                                  'radicado__municipio__departamento__codigo').distinct()
        for item in qs:
            actividades = EvidenciaApoyo.objects.all().filter(gestor__id=self.kwargs['id_gestor']).filter(radicado__municipio__id=item['radicado__municipio__id'])
            ejecutadas = actividades.exclude(corte=None).count()
            sin_ejecutar = actividades.filter(corte=None).count()
            sin_reportar = actividades.filter(corte=None).exclude(soporte="").count()

            if actividades.count() != 0:
                progreso = format((ejecutadas*100.0)/actividades.count(), '.2f')
            else:
                progreso = 0
            json_data.append([
                item['radicado__municipio__id'],
                item['radicado__municipio__nombre'],
                item['radicado__municipio__departamento__nombre'],
                item['radicado__municipio__codigo'],
                item['radicado__municipio__departamento__codigo'],
                ejecutadas,
                sin_ejecutar,
                sin_reportar,
                progreso,
                actividades.count()
            ])
        return json_data