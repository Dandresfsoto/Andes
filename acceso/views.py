from django.views.generic import TemplateView
from mixins.mixins import AccesoMixin
from region.models import Region
from gestor.models import Gestor

class AccesoView(AccesoMixin,TemplateView):
    template_name = 'acceso.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(AccesoView,self).get_context_data(**kwargs)


class AccesoCalificacionView(AccesoMixin,TemplateView):
    template_name = 'acceso_gestores.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(AccesoCalificacionView,self).get_context_data(**kwargs)

class AccesoListadoRadicadosView(AccesoMixin,TemplateView):
    template_name = 'acceso_radicados.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['NOMBRE'] = Gestor.objects.get(pk=self.kwargs['id_gestor']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_GESTOR'] = self.kwargs['id_gestor']
        return super(AccesoListadoRadicadosView,self).get_context_data(**kwargs)


