from django.views.generic import TemplateView
from region.models import Region
from diplomado.models import Diplomado
from .models import Participante
from proyectos.models import Proyecto


# Create your views here.

class ParticipantesView(TemplateView):
    template_name = 'listado.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['DIPLOMADO'] = Diplomado.objects.get(pk=self.kwargs['diplomado']).tag
        kwargs['DIPLOMADO_ID'] = self.kwargs['diplomado']
        return super(ParticipantesView,self).get_context_data(**kwargs)


from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q

class ParticipanteTableView(BaseDatatableView):
    model = Participante
    columns = [
        'radicado',
        'cedula',
        'nombres',
        'apellidos',
        'email',
        'telefono',
        'area',
        'grado',
        'beneficiario',
        'genero'
    ]

    order_columns = [
        'radicado',
        'cedula',
        'nombres',
        'apellidos',
        'email',
        'telefono',
        'area',
        'grado',
        'beneficiario',
        'genero'
    ]

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'radicado__numero__contains' : search})
            q |= Q(**{'cedula__contains' : search})
            q |= Q(**{'nombres__contains' : search})
            q |= Q(**{'apellidos__contains' : search})
            qs = qs.filter(q)
        return qs

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.all().filter(diplomado__id=self.kwargs['diplomado'])

    def render_column(self, row, column):
        if column == 'radicado':
            return row.radicado.numero
        elif column == 'area':
            return row.area.nombre
        elif column == 'grado':
            return row.grado.grado
        elif column == 'beneficiario':
            return row.beneficiario.beneficiario
        elif column == 'genero':
            return row.genero.genero
        else:
            return super(ParticipanteTableView,self).render_column(row,column)

class ProyectoTableView(BaseDatatableView):
    model = Proyecto
    columns = [
        'radicado',
        'participante',
        'nombre',
        'problema',
        'area',
        'competencia',
        'poblacion',
        'archivo'
    ]

    order_columns = [
        'radicado',
        'participante',
        'nombre',
        'problema',
        'area',
        'competencia',
        'poblacion',
        'archivo'
    ]


    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'radicado__numero__contains' : search})
            q |= Q(**{'participante__cedula__contains' : search})
            qs = qs.filter(q)
        return qs

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.all().filter(diplomado__id=self.kwargs['diplomado'])

    def render_column(self, row, column):
        if column == 'radicado':
            return row.radicado.numero
        if column == 'participante':
            return row.participante.cedula
        if column == 'nombre':
            return row.nombre
        if column == 'problema':
            return row.problema
        if column == 'area':
            return row.area.nombre
        if column == 'competencia':
            return row.competencia.nombre
        if column == 'poblacion':
            return row.poblacion.nombre
        if column == 'archivo':
            return str(row.archivo)
        else:
            return super(ProyectoTableView,self).render_column(row,column)