from django.views.generic import ListView
from .models import Region
from mixins.mixins import RegionMixin

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