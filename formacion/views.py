from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from mixins.mixins import FormacionMixin
from region.models import Region
from formador.models import Formador
from formacion.models import Grupo, ParticipanteEscuelaTic, Entregable, SoporteEntregableEscuelaTic
from formacion.forms import NuevoGrupoForm, NuevoParticipanteForm
from django.http import HttpResponseRedirect
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

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

    def form_valid(self, form):
        self.object = form.save()
        entregables = Entregable.objects.all()
        for entregable in entregables:
            soporte = SoporteEntregableEscuelaTic()
            soporte.grupo = self.object
            soporte.entregable = entregable
            soporte.save()

        return HttpResponseRedirect(self.get_success_url())

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

def soporte_form(request,pk,grupo_id,formador_id):
    SoporteFormSet = modelformset_factory(SoporteEntregableEscuelaTic, fields=('soporte',),extra=0)
    if request.method == "POST":
        formset = SoporteFormSet(request.POST, request.FILES, queryset=SoporteEntregableEscuelaTic.objects.filter(grupo__id=grupo_id))
        if formset.is_valid():
            formset.save()
    else:
        formset = SoporteFormSet(queryset=SoporteEntregableEscuelaTic.objects.filter(grupo__id=grupo_id),)
    return render_to_response("soportes_escuelaTIC.html",{"formset":formset,"user":request.user,"REGION":Region.objects.get(pk=pk).nombre},context_instance=RequestContext(request))