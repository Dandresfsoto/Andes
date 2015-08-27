from django.views.generic import TemplateView
from region.models import Region
from diplomado.models import Diplomado


# Create your views here.

class ProyectoView(TemplateView):
    template_name = 'listado_proyectos.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['DIPLOMADO'] = Diplomado.objects.get(pk=self.kwargs['diplomado']).tag
        kwargs['DIPLOMADO_ID'] = self.kwargs['diplomado']
        return super(ProyectoView,self).get_context_data(**kwargs)

