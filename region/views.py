from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import Region
from eje.models import Eje
from formador.models import Formador
from mixins.mixins import RegionMixin, AndesMixin, CpeMixin

from django.http import HttpResponse
import os
import zipfile
import StringIO
from django.conf import settings

from funcionario.models import Funcionario
from gestor.models import Gestor

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
        kwargs['ID_TIPO'] = self.kwargs['tipo']
        return super(CpeGestorView,self).get_context_data(**kwargs)

class CpeFormadorView(CpeMixin,TemplateView):
    template_name = 'tipo_formador_cpe.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(CpeFormadorView,self).get_context_data(**kwargs)

class CpeFormadorTipoView(CpeMixin,TemplateView):
    template_name = 'listado_formadores_cpe.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_TIPO'] = self.kwargs['tipo']
        return super(CpeFormadorTipoView,self).get_context_data(**kwargs)

class CpeAdministrativoView(CpeMixin,TemplateView):
    template_name = 'administrativo_cpe.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(CpeAdministrativoView,self).get_context_data(**kwargs)

class CpeAdministrativoInformesView(CpeMixin,TemplateView):
    template_name = 'administrativo_cpe_listado.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(CpeAdministrativoInformesView,self).get_context_data(**kwargs)

class CpeAdministrativoObligacionesView(CpeMixin,TemplateView):
    template_name = 'administrativo_cpe_listado_obligaciones.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(CpeAdministrativoObligacionesView,self).get_context_data(**kwargs)

def hv(request,pk,tipo):
    formadores = Formador.objects.filter(region__id=pk).filter(tipo__id=tipo)
    zip_subdir = "Hojas de Vida"
    zip_filename = "%s.zip" % zip_subdir
    s = StringIO.StringIO()
    zf = zipfile.ZipFile(s, "w")

    for formador in formadores:
        soporte = settings.MEDIA_ROOT+'/'+str(formador.hv)
        if os.path.exists(soporte):
            fdir, fname = os.path.split(soporte)
            zf.write(soporte,os.path.join('Hoja de Vida',formador.nombre,fname))

    zf.close()
    resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
    return resp

def contratos(request,pk,tipo):
    formadores = Formador.objects.filter(region__id=pk).filter(tipo__id=tipo)
    zip_subdir = "Contratos"
    zip_filename = "%s.zip" % zip_subdir
    s = StringIO.StringIO()
    zf = zipfile.ZipFile(s, "w")

    for formador in formadores:
        soporte = settings.MEDIA_ROOT+'/'+str(formador.contrato)
        if os.path.exists(soporte):
            fdir, fname = os.path.split(soporte)
            zf.write(soporte,os.path.join('Contratos',formador.nombre,fname))

    zf.close()
    resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
    return resp

def hvFuncionarios(request,pk,eje):
    funcionarios = Funcionario.objects.filter(region__id=pk).filter(eje__nombre=eje)
    zip_subdir = "Hojas de Vida"
    zip_filename = "%s.zip" % zip_subdir
    s = StringIO.StringIO()
    zf = zipfile.ZipFile(s, "w")

    for funcionario in funcionarios:
        soporte = settings.MEDIA_ROOT+'/'+str(funcionario.hv)
        if os.path.exists(soporte):
            fdir, fname = os.path.split(soporte)
            zf.write(soporte,os.path.join('Hoja de Vida',funcionario.nombre,fname))

    zf.close()
    resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
    return resp

def contratosFuncionarios(request,pk,eje):
    funcionarios = Funcionario.objects.filter(region__id=pk).filter(eje__nombre=eje)
    zip_subdir = "Contratos"
    zip_filename = "%s.zip" % zip_subdir
    s = StringIO.StringIO()
    zf = zipfile.ZipFile(s, "w")

    for funcionario in funcionarios:
        soporte = settings.MEDIA_ROOT+'/'+str(funcionario.contrato)
        if os.path.exists(soporte):
            fdir, fname = os.path.split(soporte)
            zf.write(soporte,os.path.join('Contratos',funcionario.nombre,fname))

    zf.close()
    resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
    return resp

def hvGestores(request,pk,tipo):
    gestores = Gestor.objects.filter(region__id=pk).filter(tipo__id=tipo)
    zip_subdir = "Hojas de Vida"
    zip_filename = "%s.zip" % zip_subdir
    s = StringIO.StringIO()
    zf = zipfile.ZipFile(s, "w")

    for gestor in gestores:
        soporte = settings.MEDIA_ROOT+'/'+str(gestor.hv)
        if os.path.exists(soporte):
            fdir, fname = os.path.split(soporte)
            zf.write(soporte,os.path.join('Hoja de Vida',gestor.nombre,fname))

    zf.close()
    resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
    return resp

def contratosGestores(request,pk,tipo):
    gestores = Gestor.objects.filter(region__id=pk).filter(tipo__id=tipo)
    zip_subdir = "Contratos"
    zip_filename = "%s.zip" % zip_subdir
    s = StringIO.StringIO()
    zf = zipfile.ZipFile(s, "w")

    for gestor in gestores:
        soporte = settings.MEDIA_ROOT+'/'+str(gestor.contrato)
        if os.path.exists(soporte):
            fdir, fname = os.path.split(soporte)
            zf.write(soporte,os.path.join('Contratos',gestor.nombre,fname))

    zf.close()
    resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
    return resp