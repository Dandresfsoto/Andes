from django.views.generic import TemplateView, CreateView
from mixins.mixins import FinancieroMixin
from region.models import Region
from gestor.models import Gestor
from gestor.forms import NuevoForm
from formador.models import Formador
from formador.forms import NuevoForm as NuevoFormFormador
from funcionario.forms import NuevoFuncionarioForm
from funcionario.models import Funcionario

class FinancieroView(FinancieroMixin,TemplateView):
    template_name = 'financiero.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(FinancieroView,self).get_context_data(**kwargs)

class GestorView(FinancieroMixin,TemplateView):
    template_name = 'listado_gestores_financiero.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(GestorView,self).get_context_data(**kwargs)

class FormadorView(FinancieroMixin,TemplateView):
    template_name = 'listado_formadores_financiero.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(FormadorView,self).get_context_data(**kwargs)

class FuncionarioView(FinancieroMixin,TemplateView):
    template_name = 'listado_funcionario_financiero.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(FuncionarioView,self).get_context_data(**kwargs)

class NuevoGestorView(FinancieroMixin, CreateView):
    model = Gestor
    form_class = NuevoForm
    success_url = "../"
    template_name = "nuevo_gestor.html"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(NuevoGestorView,self).get_context_data(**kwargs)

class NuevoFormadorView(FinancieroMixin, CreateView):
    model = Formador
    form_class = NuevoFormFormador
    success_url = "../"
    template_name = "nuevo_formador.html"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(NuevoFormadorView,self).get_context_data(**kwargs)

class NuevoFuncionarioView(FinancieroMixin, CreateView):
    model = Funcionario
    form_class = NuevoFuncionarioForm
    success_url = "../"
    template_name = "nuevo_funcionario.html"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(NuevoFuncionarioView,self).get_context_data(**kwargs)