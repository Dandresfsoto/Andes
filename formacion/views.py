from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from mixins.mixins import FormacionMixin
from region.models import Region
from formador.models import Formador
from formacion.models import Grupo, ParticipanteEscuelaTic
from formacion.forms import NuevoGrupoForm, NuevoParticipanteForm

class FormacionView(FormacionMixin,TemplateView):
    template_name = 'formacion.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(FormacionView,self).get_context_data(**kwargs)

class FormadorView(FormacionMixin,TemplateView):
    template_name = 'tipo2_formador_formacion.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(FormadorView,self).get_context_data(**kwargs)

class FormadorGrupoView(FormacionMixin,TemplateView):
    template_name = 'tipo2_formador_grupo.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['NOMBRE_FORMADOR'] = Formador.objects.get(pk=self.kwargs['formador_id']).nombre
        kwargs['ID_FORMADOR'] = self.kwargs['formador_id']
        return super(FormadorGrupoView,self).get_context_data(**kwargs)

class NuevoGrupoView(FormacionMixin,CreateView):
    model = Grupo
    form_class = NuevoGrupoForm
    template_name = "formulario_grupo.html"
    success_url = "../"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['NOMBRE_FORMADOR'] = Formador.objects.get(pk=self.kwargs['formador_id']).nombre
        kwargs['ID_FORMADOR'] = self.kwargs['formador_id']
        return super(NuevoGrupoView,self).get_context_data(**kwargs)

class ListadoGrupoView(FormacionMixin,TemplateView):
    template_name = 'tipo2_formador_listado.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['NOMBRE_FORMADOR'] = Formador.objects.get(pk=self.kwargs['formador_id']).nombre
        kwargs['ID_FORMADOR'] = self.kwargs['formador_id']
        kwargs['ID_GRUPO'] = self.kwargs['grupo_id']
        kwargs['NOMBRE_GRUPO'] = Grupo.objects.get(pk=self.kwargs['grupo_id']).nombre
        return super(ListadoGrupoView,self).get_context_data(**kwargs)

class NuevoParticipanteView(FormacionMixin,CreateView):
    model = ParticipanteEscuelaTic
    form_class = NuevoParticipanteForm
    template_name = "formulario_participante.html"
    success_url = "../../"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['NOMBRE_FORMADOR'] = Formador.objects.get(pk=self.kwargs['formador_id']).nombre
        kwargs['ID_FORMADOR'] = self.kwargs['formador_id']
        kwargs['ID_GRUPO'] = self.kwargs['grupo_id']
        kwargs['NOMBRE_GRUPO'] = Grupo.objects.get(pk=self.kwargs['grupo_id']).nombre
        return super(NuevoParticipanteView,self).get_context_data(**kwargs)