from acceso.models import Evidencia
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q

class RadicadoTableView(BaseDatatableView):
    model = Evidencia
    columns = [
        'radicado',
        'ciclo',
        'componente',
        'id'
    ]

    order_columns = [
        'radicado',
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.all().filter(gestor__id=self.kwargs['id_gestor']).values('radicado__id','radicado__numero','radicado__municipio__nombre','radicado__municipio__departamento__nombre').distinct()

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'radicado__numero__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'radicado':
            return str(row.radicado.numero)
        if column == 'ciclo':
            return str(row.ciclo.nombre)
        if column == 'componente':
            return str(row.componente.nombre)
        else:
            return super(RadicadoTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            json_data.append([
                item['radicado__id'],
                item['radicado__numero'],
                item['radicado__municipio__nombre'],
                item['radicado__municipio__departamento__nombre']
            ])
        return json_data