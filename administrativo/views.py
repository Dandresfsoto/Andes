#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.views.generic import UpdateView, CreateView, DeleteView
from region.models import Region

from gestor.models import Gestor
from gestor.forms import GestorSoporteForm, GestorSeguroForm, GestorInformacionForm, GestorFotoForm, NuevoForm

from formador.models import Formador
from formador.forms import FormadorSoporteForm, FormadorSeguroForm, FormadorInformacionForm, FormadorFotoForm
from formador.forms import NuevoForm as NuevoFormFormador

from funcionario.models import Funcionario
from funcionario.forms import FuncionarioSoporteForm, FuncionarioSeguroForm, FuncionarioInformacionForm, FuncionarioFotoForm

from mixins.mixins import AdministrativoMixin

from .models import Informes, Obligacion, SoporteObligacion
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q
from .forms import NuevoInformeForm, NuevaObligacionForm, NuevoSoporteObligacionForm
from formacion.models import EvidenciaDocentes, EntregableDocentes, EvidenciaEscuelaTic, Entregable, ParticipanteDocente, ParticipanteEscuelaTic


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
    template_name = 'tipo_gestor.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(GestorView,self).get_context_data(**kwargs)

class GestorTipoView(AdministrativoMixin,TemplateView):
    template_name = 'listado_gestores.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_TIPO'] = self.kwargs['tipo_id']
        return super(GestorTipoView,self).get_context_data(**kwargs)

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
                              {'nombre':'Contrato Plan Choque','soporte_id':"contrato_plan_choque",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).contrato_plan_choque},
                              {'nombre':'Fotocopia Cedula','soporte_id':"fotocopia_cedula",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).fotocopia_cedula},
                              {'nombre':'Ancedentes Judiciales','soporte_id':"antecedentes_judiciales",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).antecedentes_judiciales},
                              {'nombre':'Antecedentes Contraloria','soporte_id':"antecedentes_contraloria",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).antecedentes_contraloria},
                              {'nombre':'Liquidacion','soporte_id':"liquidacion",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).liquidacion},
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
                              {'mes':"diciembre",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).seguro_diciembre},
                              {'mes':"enero_1",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).seguro_enero_1},
                              {'mes':"febrero_1",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).seguro_febrero_1},
                              {'mes':"marzo_1",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).seguro_marzo_1},
                              {'mes':"abril_1",'soporte':Formador.objects.get(pk=self.kwargs['formador_id']).seguro_abril_1},
                              ]

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

class CpeObligacionesView(AdministrativoMixin,TemplateView):
    template_name = 'cpe_obligaciones_listado.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(CpeObligacionesView,self).get_context_data(**kwargs)

class CpeNuevaObligacionView(AdministrativoMixin, CreateView):
    model = Obligacion
    form_class = NuevaObligacionForm
    success_url = "../"
    template_name = "nueva_obligacion.html"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(CpeNuevaObligacionView,self).get_context_data(**kwargs)

class CpeEditarObligacion(AdministrativoMixin, UpdateView):
    model = Obligacion
    form_class = NuevaObligacionForm
    success_url = "../../"
    template_name = "editar_obligacion.html"
    pk_url_kwarg = 'obligacion_id'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_OBLIGACION'] = self.kwargs['obligacion_id']
        kwargs['OBLIGACION'] = Obligacion.objects.get(pk=self.kwargs['obligacion_id']).numero
        return super(CpeEditarObligacion,self).get_context_data(**kwargs)

class CpeObligacionTableView(BaseDatatableView):
    model = Obligacion
    columns = [
        'id',
        'region',
        'numero',
        'descripcion'
    ]

    order_columns = [
        'numero',
        'numero',
        'numero',
        'numero'
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.all().filter(region__id=self.kwargs['pk'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'numero__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'region':
            return row.region.nombre
        else:
            return super(CpeObligacionTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            meses = SoporteObligacion.objects.filter(obligacion__id=item.id).values_list('mes',flat=True).distinct()
            soportes = SoporteObligacion.objects.filter(obligacion__id=item.id).order_by('id')
            x=[]

            for mes in meses:
                x.append(mes)

            y=[]

            for soporte in soportes:
                y.append([
                    soporte.mes,
                    soporte.descripcion,
                    str(soporte.soporte),
                    soporte.id
                ])


            json_data.append([
                item.id,
                item.region.nombre,
                item.numero,
                item.descripcion,
                x,
                y
            ])
        return json_data

class CpeNuevoSoporteObligacion(AdministrativoMixin, CreateView):
    model = SoporteObligacion
    form_class = NuevoSoporteObligacionForm
    success_url = "../../"
    template_name = "nuevo_soporte_obligacion.html"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_OBLIGACION'] = self.kwargs['obligacion_id']
        kwargs['OBLIGACION'] = Obligacion.objects.get(pk=self.kwargs['obligacion_id']).numero
        return super(CpeNuevoSoporteObligacion,self).get_context_data(**kwargs)

class CpeEditarSoporteObligacion(AdministrativoMixin, UpdateView):
    model = SoporteObligacion
    form_class = NuevoSoporteObligacionForm
    success_url = "../../../"
    template_name = "nuevo_soporte_obligacion.html"
    pk_url_kwarg = 'soporte_id'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_OBLIGACION'] = self.kwargs['obligacion_id']
        kwargs['OBLIGACION'] = Obligacion.objects.get(pk=self.kwargs['obligacion_id']).numero
        return super(CpeEditarSoporteObligacion,self).get_context_data(**kwargs)


class CpeEliminarSoporteObligacion(AdministrativoMixin, DeleteView):
    model = SoporteObligacion
    form_class = NuevoSoporteObligacionForm
    success_url = "../../../"
    template_name = "eliminar_soporte_obligacion.html"
    pk_url_kwarg = 'soporte_id'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_OBLIGACION'] = self.kwargs['obligacion_id']
        kwargs['OBLIGACION'] = Obligacion.objects.get(pk=self.kwargs['obligacion_id']).numero
        return super(CpeEliminarSoporteObligacion,self).get_context_data(**kwargs)

class NuevoGestorView(AdministrativoMixin, CreateView):
    model = Gestor
    form_class = NuevoForm
    success_url = "../"
    template_name = "nuevo_gestor_administrativo.html"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_TIPO'] = self.kwargs['tipo_id']
        return super(NuevoGestorView,self).get_context_data(**kwargs)

class NuevoFormadorView(AdministrativoMixin, CreateView):
    model = Formador
    form_class = NuevoFormFormador
    success_url = "../"
    template_name = "nuevo_formador_administrativo.html"

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_TIPO'] = self.kwargs['tipo_id']
        return super(NuevoFormadorView,self).get_context_data(**kwargs)

class AuxiliaresView(AdministrativoMixin,TemplateView):
    template_name = 'auxiliares.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(AuxiliaresView,self).get_context_data(**kwargs)

class EstadisticasView(AdministrativoMixin,TemplateView):
    template_name = 'estadisticas.html'

    def get_context_data(self, **kwargs):
        r1_escuela_tic = []
        i = 0
        for entregable_escuela_tic in Entregable.objects.all():
            cantidad = EvidenciaEscuelaTic.objects.filter(participante__formador__region__id=1).filter(entregable__id=entregable_escuela_tic.id).exclude(soporte=None).exclude(soporte__soporte='').count()
            meta = 27834
            progreso = (cantidad*100.0)/meta
            i += 1
            if i%2 == 0:
                clase = "even"
            else:
                clase = "odd"
            r1_escuela_tic.append({'actividad':entregable_escuela_tic.actividad.nombre,'entregable':entregable_escuela_tic.nombre,'cantidad':cantidad,'meta':meta,'progreso':"{0:.2f}".format(progreso),'clase':clase})




        r1_docentes = []
        i = 0
        for entregable_docentes in EntregableDocentes.objects.all():
            cantidad = EvidenciaDocentes.objects.filter(participante__formador__region__id=1).filter(entregable__id=entregable_docentes.id).exclude(soporte=None).exclude(soporte__soporte='').count()
            meta = 6905
            progreso = (cantidad*100.0)/meta
            i += 1
            if i%2 == 0:
                clase = "even"
            else:
                clase = "odd"
            r1_docentes.append({'actividad':entregable_docentes.actividad.nombre,'entregable':entregable_docentes.nombre,'cantidad':cantidad,'meta':meta,'progreso':"{0:.2f}".format(progreso),'clase':clase})




        r4_escuela_tic = []
        i = 0
        for entregable_escuela_tic in Entregable.objects.all():
            cantidad = EvidenciaEscuelaTic.objects.filter(participante__formador__region__id=2).filter(entregable__id=entregable_escuela_tic.id).exclude(soporte=None).exclude(soporte__soporte='').count()
            meta = 67826
            progreso = (cantidad*100.0)/meta
            i += 1
            if i%2 == 0:
                clase = "even"
            else:
                clase = "odd"
            r4_escuela_tic.append({'actividad':entregable_escuela_tic.actividad.nombre,'entregable':entregable_escuela_tic.nombre,'cantidad':cantidad,'meta':meta,'progreso':"{0:.2f}".format(progreso),'clase':clase})

        r4_docentes = []
        i = 0
        for entregable_docentes in EntregableDocentes.objects.all():
            cantidad = EvidenciaDocentes.objects.filter(participante__formador__region__id=2).filter(entregable__id=entregable_docentes.id).exclude(soporte=None).exclude(soporte__soporte='').count()
            meta = 10932
            progreso = (cantidad*100.0)/meta
            i += 1
            if i%2 == 0:
                clase = "even"
            else:
                clase = "odd"
            r4_docentes.append({'actividad':entregable_docentes.actividad.nombre,'entregable':entregable_docentes.nombre,'cantidad':cantidad,'meta':meta,'progreso':"{0:.2f}".format(progreso),'clase':clase})



        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ESCUELA_TIC_R1'] = r1_escuela_tic
        kwargs['ESCUELA_TIC_R4'] = r4_escuela_tic
        kwargs['DOCENTES_R1'] = r1_docentes
        kwargs['DOCENTES_R4'] = r4_docentes
        return super(EstadisticasView,self).get_context_data(**kwargs)