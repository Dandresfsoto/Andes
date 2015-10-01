from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import Region
from eje.models import Eje
from mixins.mixins import RegionMixin, AndesMixin, CpeMixin

class InicioView(ListView):
    template_name = 'inicio.html'
    model = Region

    def get_context_data(self, **kwargs):
        return super(InicioView,self).get_context_data(**kwargs)

class RegionView(RegionMixin, ListView):
    template_name = 'region.html'
    model = Region

    def queryset(self):
        queryset = Region.objects.get(pk=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(RegionView,self).get_context_data(**kwargs)

class AndesView(AndesMixin, ListView):
    template_name = 'andes.html'
    model = Region

    def queryset(self):
        queryset = Region.objects.get(pk=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(AndesView,self).get_context_data(**kwargs)

class CpeView(CpeMixin,ListView):
    template_name = 'cpe.html'
    model = Region

    def queryset(self):
        queryset = Region.objects.get(pk=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(CpeView,self).get_context_data(**kwargs)


class CpeFormacionView(CpeMixin,ListView):
    template_name = 'formacion_cpe.html'
    model = Region

    def queryset(self):
        queryset = Region.objects.get(pk=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(CpeFormacionView,self).get_context_data(**kwargs)

class CpeAccesoView(CpeMixin,ListView):
    template_name = 'acceso_cpe.html'
    model = Region

    def queryset(self):
        queryset = Region.objects.get(pk=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(CpeAccesoView,self).get_context_data(**kwargs)

class CpeFuncionarioView(CpeMixin,TemplateView):
    template_name = 'listado_funcionarios_cpe.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['EJE'] = Eje.objects.all().filter(nombre=self.kwargs['eje'])[0].nombre
        kwargs['ID_EJE'] = Eje.objects.all().filter(nombre=self.kwargs['eje'])[0].id
        return super(CpeFuncionarioView,self).get_context_data(**kwargs)

class CpeGestorView(CpeMixin,TemplateView):
    template_name = 'listado_gestores_cpe.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(CpeGestorView,self).get_context_data(**kwargs)

class CpeFormadorView(CpeMixin,TemplateView):
    template_name = 'listado_formadores_cpe.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(CpeFormadorView,self).get_context_data(**kwargs)