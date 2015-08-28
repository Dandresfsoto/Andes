from region.models import Region
from django.views.generic import ListView
from .models import Diplomado
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView
from participantes.models import Participante
from mixins.mixins import CpeMixin

class ParticipantesDatatablesView(BaseDatatableView):
    model = Participante
    columns = ['radicado','cedula','nombres','apellidos','email','telefono','area','grado','beneficiario','genero']
    order_columns = ['radicado','cedula','nombres','apellidos','email','telefono','area','grado','beneficiario','genero']

    max_display_length = 25



class DiplomadosView(CpeMixin,ListView):
    template_name = 'diplomados.html'
    model = Diplomado

    def get_queryset(self):
        queryset = Diplomado.objects.all().filter(region__id=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(DiplomadosView,self).get_context_data(**kwargs)

class DiplomadosInfoView(TemplateView):
    template_name = 'diplomados_informacion.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['DIPLOMADO'] = Diplomado.objects.get(pk=self.kwargs['diplomado']).tag
        return super(DiplomadosInfoView,self).get_context_data(**kwargs)