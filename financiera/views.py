from django.views.generic import TemplateView
from region.models import Region

class GestorView(TemplateView):
    template_name = 'listado_gestores.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(GestorView,self).get_context_data(**kwargs)