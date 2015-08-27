from django.views.generic import ListView
from django.views.generic import TemplateView
from braces.views import GroupRequiredMixin
from django.contrib.auth.models import User, Group

from .models import Region

class InicioView(ListView):
    template_name = 'inicio.html'
    model = Region

    def get_context_data(self, **kwargs):
        return super(InicioView,self).get_context_data(**kwargs)

class RegionView(ListView):
    template_name = 'region.html'
    model = Region

    def queryset(self):
        queryset = Region.objects.get(pk=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(RegionView,self).get_context_data(**kwargs)