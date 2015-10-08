#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.views.generic import UpdateView, CreateView
from region.models import Region

from gestor.models import Gestor
from gestor.forms import GestorSoporteForm, GestorSeguroForm, GestorInformacionForm, GestorFotoForm

from formador.models import Formador
from formador.forms import FormadorSoporteForm, FormadorSeguroForm, FormadorInformacionForm, FormadorFotoForm

from funcionario.models import Funcionario
from funcionario.forms import FuncionarioSoporteForm, FuncionarioSeguroForm, FuncionarioInformacionForm, FuncionarioFotoForm

from mixins.mixins import AdministrativoMixin

from .models import Informes
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q
from .forms import NuevoInformeForm


class AdministrativoView(AdministrativoMixin,TemplateView):
    template_name = 'administrativo.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(AdministrativoView,self).get_context_data(**kwargs)

class FuncionarioView(AdministrativoMixin,TemplateView):
    template_name = 'listado_funcionarios.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(FuncionarioView,self).get_context_data(**kwargs)

class FuncionarioActualizarInformacionView(AdministrativoMixin,UpdateView):
    model = Funcionario
    form_class = FuncionarioInformacionForm
    template_name = "update_funcionario_informacion.html"

    pk_url_kwarg = "funcionario_id"
    success_url = "../../../"


    def get_context_data(self, **kwargs):
        kwargs['informacion'] = [
        {'nombre':"Celular",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).celular,'id':'celular','longitud': Funcionario._meta.get_field('celular').max_length},
        {'nombre':"Correo",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).correo,'id':'correo','longitud': Funcionario._meta.get_field('correo').max_length},
        {'nombre':"Cargo",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).cargo,'id':'cargo','longitud': Funcionario._meta.get_field('cargo').max_length},
        {'nombre':"Profesion",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).profesion,'id':'profesion','longitud': Funcionario._meta.get_field('profesion').max_length},
        {'nombre':"Banco",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).banco,'id':'banco','longitud': Funcionario._meta.get_field('banco').max_length},
        {'nombre':"Tipo de Cuenta",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).tipo_cuenta,'id':'tipo_cuenta','longitud': Funcionario._meta.get_field('tipo_cuenta').max_length},
        {'nombre':"Numero de Cuenta",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).numero_cuenta,'id':'numero_cuenta','longitud': Funcionario._meta.get_field('numero_cuenta').max_length},
        {'nombre':"Eps",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).eps,'id':'eps','longitud':Funcionario._meta.get_field('eps').max_length},
        {'nombre':"Pension",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).pension,'id':'pension','longitud':Funcionario._meta.get_field('pension').max_length},
        {'nombre':"Arl",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).arl,'id':'arl','longitud':Funcionario._meta.get_field('arl').max_length}
        ]

        kwargs['nombre'] = Funcionario.objects.get(pk=self.kwargs['funcionario_id']).nombre
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(FuncionarioActualizarInformacionView,self).get_context_data(**kwargs)

class FuncionarioActualizarSoporteView(AdministrativoMixin,UpdateView):
    model = Funcionario
    form_class = FuncionarioSoporteForm
    template_name = "update_funcionario_soporte.html"

    pk_url_kwarg = "funcionario_id"
    success_url = "../../../"


    def get_context_data(self, **kwargs):
        kwargs['soportes'] = [{'nombre':'Hoja de Vida','soporte_id':"hv",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).hv},
                              {'nombre':'Certificacion Bancaria','soporte_id':"certificacion",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).certificacion},
                              {'nombre':'Rut','soporte_id':"rut",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).rut},
                              {'nombre':'Contrato','soporte_id':"contrato",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).contrato},
                              {'nombre':'Fotocopia Cedula','soporte_id':"fotocopia_cedula",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).fotocopia_cedula},
                              {'nombre':'Ancedentes Judiciales','soporte_id':"antecedentes_judiciales",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).antecedentes_judiciales},
                              {'nombre':'Antecedentes Contraloria','soporte_id':"antecedentes_contraloria",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).antecedentes_contraloria},
                              ]

        kwargs['nombre'] = Funcionario.objects.get(pk=self.kwargs['funcionario_id']).nombre
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(FuncionarioActualizarSoporteView,self).get_context_data(**kwargs)

class FuncionarioActualizarSeguroView(AdministrativoMixin,UpdateView):
    model = Funcionario
    form_class = FuncionarioSeguroForm
    template_name = "update_seguro_funcionario.html"

    pk_url_kwarg = "funcionario_id"
    success_url = "../../../"


    def get_context_data(self, **kwargs):
        kwargs['soportes'] = [{'mes':"enero",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_enero},
                              {'mes':"febrero",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_febrero},
                              {'mes':"marzo",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_marzo},
                              {'mes':"abril",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_abril},
                              {'mes':"mayo",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_mayo},
                              {'mes':"junio",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_junio},
                              {'mes':"julio",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_julio},
                              {'mes':"agosto",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_agosto},
                              {'mes':"septiembre",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_septiembre},
                              {'mes':"octubre",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_octubre},
                              {'mes':"noviembre",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_noviembre},
                              {'mes':"diciembre",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_diciembre},]

        kwargs['nombre'] = Funcionario.objects.get(pk=self.kwargs['funcionario_id']).nombre
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(FuncionarioActualizarSeguroView,self).get_context_data(**kwargs)

class FuncionarioActualizarFotoView(AdministrativoMixin,UpdateView):
    model = Funcionario
    form_class = FuncionarioFotoForm
    template_name = "update_foto_funcionario.html"

    pk_url_kwarg = "funcionario_id"
    success_url = "../../../"


    def get_context_data(self, **kwargs):
        kwargs['soporte'] = Funcionario.objects.get(pk=self.kwargs['funcionario_id']).foto
        kwargs['nombre'] = Funcionario.objects.get(pk=self.kwargs['funcionario_id']).nombre
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(FuncionarioActualizarFotoView,self).get_context_data(**kwargs)



class GestorView(AdministrativoMixin,TemplateView):
    template_name = 'listado_gestores.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(GestorView,self).get_context_data(**kwargs)

class GestorActualizarInformacionView(AdministrativoMixin,UpdateView):
    model = Gestor
    form_class = GestorInformacionForm
    template_name = "update_informacion_gestor.html"

    pk_url_kwarg = "gestor_id"
    success_url = "../../../"


    def get_context_data(self, **kwargs):
        kwargs['informacion'] = [
        {'nombre':"Nombre",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).nombre,'id':'nombre','longitud': Gestor._meta.get_field('nombre').max_length},
        {'nombre':"Cedula",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).cedula,'id':'cedula','longitud': Gestor._meta.get_field('cedula').max_length},
        {'nombre':"Celular",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).celular,'id':'celular','longitud': Gestor._meta.get_field('celular').max_length},
        {'nombre':"Correo",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).correo,'id':'correo','longitud': Gestor._meta.get_field('correo').max_length},
        {'nombre':"Cargo",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).cargo,'id':'cargo','longitud': Gestor._meta.get_field('cargo').max_length},
        {'nombre':"Profesion",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).profesion,'id':'profesion','longitud': Gestor._meta.get_field('profesion').max_length},
        {'nombre':"Banco",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).banco,'id':'banco','longitud': Gestor._meta.get_field('banco').max_length},
        {'nombre':"Tipo de Cuenta",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).tipo_cuenta,'id':'tipo_cuenta','longitud': Gestor._meta.get_field('tipo_cuenta').max_length},
        {'nombre':"Numero de Cuenta",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).numero_cuenta,'id':'numero_cuenta','longitud': Gestor._meta.get_field('numero_cuenta').max_length},
        {'nombre':"Eps",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).eps,'id':'eps','longitud':Gestor._meta.get_field('eps').max_length},
        {'nombre':"Pension",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).pension,'id':'pension','longitud':Gestor._meta.get_field('pension').max_length},
        {'nombre':"Arl",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).arl,'id':'arl','longitud':Gestor._meta.get_field('arl').max_length},
        ]

        kwargs['nombre'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).nombre
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(GestorActualizarInformacionView,self).get_context_data(**kwargs)

class GestorActualizarSoporteView(AdministrativoMixin,UpdateView):
    model = Gestor
    form_class = GestorSoporteForm
    template_name = "update_gestor_soporte.html"

    pk_url_kwarg = "gestor_id"
    success_url = "../../../"


    def get_context_data(self, **kwargs):
        kwargs['soportes'] = [{'nombre':'Hoja de Vida','soporte_id':"hv",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).hv},
                              {'nombre':'Certificacion Bancaria','soporte_id':"certificacion",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).certificacion},
                              {'nombre':'Rut','soporte_id':"rut",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).rut},
                              {'nombre':'Contrato','soporte_id':"contrato",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).contrato},
                              {'nombre':'Fotocopia Cedula','soporte_id':"fotocopia_cedula",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).fotocopia_cedula},
                              {'nombre':'Ancedentes Judiciales','soporte_id':"antecedentes_judiciales",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).antecedentes_judiciales},
                              {'nombre':'Antecedentes Contraloria','soporte_id':"antecedentes_contraloria",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).antecedentes_contraloria},
                              ]

        kwargs['nombre'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).nombre
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(GestorActualizarSoporteView,self).get_context_data(**kwargs)

class GestorActualizarSeguroView(AdministrativoMixin,UpdateView):
    model = Gestor
    form_class = GestorSeguroForm
    template_name = "update_seguro_gestor.html"

    pk_url_kwarg = "gestor_id"
    success_url = "../../../"


    def get_context_data(self, **kwargs):
        kwargs['soportes'] = [{'mes':"enero",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_enero},
                              {'mes':"febrero",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_febrero},
                              {'mes':"marzo",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_marzo},
                              {'mes':"abril",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_abril},
                              {'mes':"mayo",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_mayo},
                              {'mes':"junio",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_junio},
                              {'mes':"julio",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_julio},
                              {'mes':"agosto",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_agosto},
                              {'mes':"septiembre",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_septiembre},
                              {'mes':"octubre",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_octubre},
                              {'mes':"noviembre",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_noviembre},
                              {'mes':"diciembre",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_diciembre},]

        kwargs['nombre'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).nombre
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(GestorActualizarSeguroView,self).get_context_data(**kwargs)

class GestorActualizarFotoView(AdministrativoMixin,UpdateView):
    model = Gestor
    form_class = GestorFotoForm
    template_name = "update_foto_gestor.html"

    pk_url_kwarg = "gestor_id"
    success_url = "../../../"


    def get_context_data(self, **kwargs):
        kwargs['soporte'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).foto
        kwargs['nombre'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).nombre
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(GestorActualizarFotoView,self).get_context_data(**kwargs)


class FormadorView(AdministrativoMixin,TemplateView):
    template_name = 'tipo_formador.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(FormadorView,self).get_context_data(**kwargs)

class FormadorTipoView(AdministrativoMixin,TemplateView):
    template_name = 'listado_formadores.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_TIPO'] = self.kwargs['tipo_id']
        return super(FormadorTipoView,self).get_context_data(**kwargs)

class FormadorActualizarInformacionView(AdministrativoMixin,UpdateView):
    model = Formador
    form_class = FormadorInformacionForm
    template_name = "update_informacion_formador.html"

    pk_url_kwarg = "formador_id"
    success_url = "../../../"


    def get_context_data(self, **kwargs):
        kwargs['informacion'] = [
        {'nombre':"Celular",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).celular,'id':'celular','longitud': Formador._meta.get_field('celular').max_length},
        {'nombre':"Correo",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).correo,'id':'correo','longitud': Formador._meta.get_field('correo').max_length},
        {'nombre':"Cargo",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).cargo,'id':'cargo','longitud': Formador._meta.get_field('cargo').max_length},
        {'nombre':"Profesion",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).profesion,'id':'profesion','longitud': Formador._meta.get_field('profesion').max_length},
        {'nombre':"Banco",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).banco,'id':'banco','longitud': Formador._meta.get_field('banco').max_length},
        {'nombre':"Tipo de Cuenta",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).tipo_cuenta,'id':'tipo_cuenta','longitud': Formador._meta.get_field('tipo_cuenta').max_length},
        {'nombre':"Numero de Cuenta",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).numero_cuenta,'id':'numero_cuenta','longitud': Formador._meta.get_field('numero_cuenta').max_length},
        {'nombre':"Eps",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).eps,'id':'eps','longitud':Formador._meta.get_field('eps').max_length},
        {'nombre':"Pension",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).pension,'id':'pension','longitud':Formador._meta.get_field('pension').max_length},
        {'nombre':"Arl",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).arl,'id':'arl','longitud':Formador._meta.get_field('arl').max_length}
        ]

        kwargs['nombre'] = Formador.objects.get(pk=self.kwargs['formador_id']).nombre
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(FormadorActualizarInformacionView,self).get_context_data(**kwargs)

class FormadorActualizarSoporteView(AdministrativoMixin,UpdateView):
    model = Formador
    form_class = FormadorSoporteForm
    template_name = "update_formador_soporte.html"

    pk_url_kwarg = "formador_id"
    success_url = "../../../"


    def get_context_data(self, **kwargs):
        kwargs['soportes'] = [{'nombre':'Hoja de Vida','soporte_id':"hv",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).hv},
                              {'nombre':'Certificacion Bancaria','soporte_id':"certificacion",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).certificacion},
                              {'nombre':'Rut','soporte_id':"rut",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).rut},
                              {'nombre':'Contrato','soporte_id':"contrato",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).contrato},
                              {'nombre':'Fotocopia Cedula','soporte_id':"fotocopia_cedula",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).fotocopia_cedula},
                              {'nombre':'Ancedentes Judiciales','soporte_id':"antecedentes_judiciales",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).antecedentes_judiciales},
                              {'nombre':'Antecedentes Contraloria','soporte_id':"antecedentes_contraloria",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).antecedentes_contraloria},
                              ]

        kwargs['nombre'] = Formador.objects.get(pk=self.kwargs['formador_id']).nombre
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(FormadorActualizarSoporteView,self).get_context_data(**kwargs)

class FormadorActualizarSeguroView(AdministrativoMixin,UpdateView):
    model = Formador
    form_class = FormadorSeguroForm
    template_name = "update_seguro_formador.html"

    pk_url_kwarg = "formador_id"
    success_url = "../../../"


    def get_context_data(self, **kwargs):
        kwargs['soportes'] = [{'mes':"enero",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).seguro_enero},
                              {'mes':"febrero",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).seguro_febrero},
                              {'mes':"marzo",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).seguro_marzo},
                              {'mes':"abril",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).seguro_abril},
                              {'mes':"mayo",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).seguro_mayo},
                              {'mes':"junio",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).seguro_junio},
                              {'mes':"julio",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).seguro_julio},
                              {'mes':"agosto",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).seguro_agosto},
                              {'mes':"septiembre",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).seguro_septiembre},
                              {'mes':"octubre",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).seguro_octubre},
                              {'mes':"noviembre",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).seguro_noviembre},
                              {'mes':"diciembre",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).seguro_diciembre},]

        kwargs['nombre'] = Formador.objects.get(pk=self.kwargs['formador_id']).nombre
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(FormadorActualizarSeguroView,self).get_context_data(**kwargs)

class FormadorActualizarFotoView(AdministrativoMixin,UpdateView):
    model = Formador
    form_class = FormadorFotoForm
    template_name = "update_foto_formador.html"

    pk_url_kwarg = "formador_id"
    success_url = "../../../"


    def get_context_data(self, **kwargs):
        kwargs['soporte'] = Formador.objects.get(pk=self.kwargs['formador_id']).foto
        kwargs['nombre'] = Formador.objects.get(pk=self.kwargs['formador_id']).nombre
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(FormadorActualizarFotoView,self).get_context_data(**kwargs)

class CpeView(AdministrativoMixin,TemplateView):
    template_name = 'cpe_administrativo.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(CpeView,self).get_context_data(**kwargs)

class CpeInformeView(AdministrativoMixin,TemplateView):
    template_name = 'cpe_administrativo_listado.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(CpeInformeView,self).get_context_data(**kwargs)

class CpeInformeTableView(BaseDatatableView):
    model = Informes
    columns = [
        'id',
        'fecha',
        'nombre',
        'mes',
        'excel_acceso',
        'soporte_acceso',
        'excel_formacion',
        'soporte_formacion'
    ]

    order_columns = [
        'id',
        'fecha',
        'nombre',
        'mes',
        'excel_acceso',
        'soporte_acceso',
        'excel_formacion',
        'soporte_formacion'
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.all().filter(region__id=self.kwargs['pk'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'nombre__icontains' : search.capitalize()})
            q |= Q(**{'mes__icontains' : search.capitalize()})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'excel_acceso':
            return str(row.excel_acceso)
        if column == 'soporte_acceso':
            return str(row.soporte_acceso)
        if column == 'excel_formacion':
            return str(row.excel_formacion)
        if column == 'soporte_formacion':
            return str(row.soporte_formacion)
        else:
            return super(CpeInformeTableView,self).render_column(row,column)

class CpeInformeNuevoView(AdministrativoMixin, CreateView):
    model = Informes
    form_class = NuevoInformeForm
    success_url = "../"
    template_name = "nuevo_informe.html"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(CpeInformeNuevoView,self).get_context_data(**kwargs)

class CpeInformeUpdateView(AdministrativoMixin,UpdateView):
    model = Informes
    form_class = NuevoInformeForm
    template_name = "nuevo_informe.html"

    pk_url_kwarg = "informe_id"
    success_url = "../../"


    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(CpeInformeUpdateView,self).get_context_data(**kwargs)