from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import ModelFormMixin
from mixins.mixins import FinancieroMixin
from region.models import Region
from gestor.models import Gestor
from gestor.forms import NuevoForm
from formador.models import Formador
from formador.forms import NuevoForm as NuevoFormFormador
from funcionario.forms import NuevoFuncionarioForm
from funcionario.models import Funcionario
from acceso.models import Corte
from acceso.forms import CorteForm
from acceso.models import Evidencia
from django.db.models import Sum

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

class NuevoCorteView(FinancieroMixin, CreateView):
    model = Corte
    form_class = CorteForm
    success_url = "../"
    template_name = "nuevo_corte.html"

    def get_context_data(self, **kwargs):
        reporte = Evidencia.objects.filter(radicado__region__id=self.kwargs['pk']).filter(corte=None).exclude(soporte="")
        kwargs['CANTIDAD'] = reporte.count()
        kwargs['VALOR'] = "$ "+str(reporte.aggregate(Sum('valor__valor'))['valor__valor__sum'])
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']

        return super(NuevoCorteView,self).get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        corte = self.object
        reporte = Evidencia.objects.filter(radicado__region__id=self.kwargs['pk']).filter(corte=None).exclude(soporte="")
        for evidencia in reporte:
            evidencia.corte = corte
            evidencia.save()
        return super(ModelFormMixin, self).form_valid(form)