from region.models import Region
from django.views.generic import ListView
from .models import Diplomado
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView
from participantes.models import Participante
from mixins.mixins import CpeMixin
from formacion.models import ParticipanteEscuelaTic, ParticipanteDocente

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
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(DiplomadosView,self).get_context_data(**kwargs)

class EscuelaTicView(TemplateView):
    template_name = 'escuela_tic.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(EscuelaTicView,self).get_context_data(**kwargs)

class DocentesView(TemplateView):
    template_name = 'docentes.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(DocentesView,self).get_context_data(**kwargs)

class EscuelaTicParticipantesListadoView(TemplateView):
    template_name = 'escuela_tic_participantes.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(EscuelaTicParticipantesListadoView,self).get_context_data(**kwargs)

class DocentesListadoView(TemplateView):
    template_name = 'docentes_participantes.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(DocentesListadoView,self).get_context_data(**kwargs)

class EscuelaTicEvidenciasListadoView(TemplateView):
    template_name = 'escuela_tic_participantes_evidencias.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        participante = ParticipanteEscuelaTic.objects.get(id=self.kwargs['participante_id'])
        kwargs['PARTICIPANTE'] = participante.nombres+" "+participante.apellidos+" - "+str(participante.cedula)
        kwargs['ID_PARTICIPANTE'] = participante.id
        return super(EscuelaTicEvidenciasListadoView,self).get_context_data(**kwargs)

class DocentesEvidenciasListadoView(TemplateView):
    template_name = 'docentes_participantes_evidencias.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        participante = ParticipanteDocente.objects.get(id=self.kwargs['participante_id'])
        kwargs['PARTICIPANTE'] = participante.nombres+" "+participante.apellidos+" - "+str(participante.cedula)
        kwargs['ID_PARTICIPANTE'] = participante.id
        return super(DocentesEvidenciasListadoView,self).get_context_data(**kwargs)

class EscuelaTicActividadesListadoView(TemplateView):
    template_name = 'escuela_tic_actividades.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(EscuelaTicActividadesListadoView,self).get_context_data(**kwargs)

class DocentesActividadesListadoView(TemplateView):
    template_name = 'docentes_actividades.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(DocentesActividadesListadoView,self).get_context_data(**kwargs)

class EscuelaTicActividadesListadoFiltroView(TemplateView):
    template_name = 'escuela_tic_actividades_filtro.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_ACTIVIDAD'] = self.kwargs['actividad_id']
        return super(EscuelaTicActividadesListadoFiltroView,self).get_context_data(**kwargs)

class DocentesActividadesListadoFiltroView(TemplateView):
    template_name = 'docentes_actividades_filtro.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_ACTIVIDAD'] = self.kwargs['actividad_id']
        return super(DocentesActividadesListadoFiltroView,self).get_context_data(**kwargs)