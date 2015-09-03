from django.views.generic import TemplateView
from django.views.generic import UpdateView
from region.models import Region

from gestor.models import Gestor
from gestor.forms import GestorSoporteForm, GestorSeguroForm

from formador.models import Formador
from formador.forms import FormadorSoporteForm, FormadorSeguroForm

from funcionario.models import Funcionario
from funcionario.forms import FuncionarioSoporteForm, FuncionarioSeguroForm, FuncionarioInformacionForm, FuncionarioFotoForm

class AdministrativoView(TemplateView):
    template_name = 'administrativo.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(AdministrativoView,self).get_context_data(**kwargs)

class GestorView(TemplateView):
    template_name = 'listado_gestores.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(GestorView,self).get_context_data(**kwargs)

class FormadorView(TemplateView):
    template_name = 'listado_formadores.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(FormadorView,self).get_context_data(**kwargs)

class FuncionarioView(TemplateView):
    template_name = 'listado_funcionarios.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(FuncionarioView,self).get_context_data(**kwargs)

class GestorActualizarSoporteView(UpdateView):
    model = Gestor
    form_class = GestorSoporteForm
    template_name = "update_gestor.html"

    pk_url_kwarg = "gestor_id"
    success_url = "../../../"


    def get_context_data(self, **kwargs):
        kwargs['actual_hv'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).hv
        kwargs['actual_certificacion'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).certificacion
        kwargs['actual_rut'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).rut
        kwargs['actual_contrato'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).contrato

        kwargs['nombre'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).nombre
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(GestorActualizarSoporteView,self).get_context_data(**kwargs)

class GestorActualizarSeguroView(UpdateView):
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
                              {'mes':"junlio",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_julio},
                              {'mes':"agosto",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_agosto},
                              {'mes':"septiembre",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_septiembre},
                              {'mes':"octubre",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_octubre},
                              {'mes':"noviembre",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_noviembre},
                              {'mes':"diciembre",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_diciembre},]

        kwargs['nombre'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).nombre
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(GestorActualizarSeguroView,self).get_context_data(**kwargs)

class FormadorActualizarSoporteView(UpdateView):
    model = Formador
    form_class = FormadorSoporteForm
    template_name = "update_gestor.html"

    pk_url_kwarg = "formador_id"
    success_url = "../../../"


    def get_context_data(self, **kwargs):
        kwargs['actual_hv'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).hv
        kwargs['actual_certificacion'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).certificacion
        kwargs['actual_rut'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).rut
        kwargs['actual_contrato'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).contrato

        kwargs['nombre'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).nombre
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(FormadorActualizarSoporteView,self).get_context_data(**kwargs)

class FormadorActualizarSeguroView(UpdateView):
    model = Formador
    form_class = FormadorSeguroForm
    template_name = "update_seguro_gestor.html"

    pk_url_kwarg = "formador_id"
    success_url = "../../../"


    def get_context_data(self, **kwargs):
        kwargs['soportes'] = [{'mes':"enero",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_enero},
                              {'mes':"febrero",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_febrero},
                              {'mes':"marzo",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_marzo},
                              {'mes':"abril",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_abril},
                              {'mes':"mayo",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_mayo},
                              {'mes':"junio",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_junio},
                              {'mes':"junlio",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_julio},
                              {'mes':"agosto",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_agosto},
                              {'mes':"septiembre",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_septiembre},
                              {'mes':"octubre",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_octubre},
                              {'mes':"noviembre",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_noviembre},
                              {'mes':"diciembre",'soporte':Gestor.objects.get(pk=self.kwargs['gestor_id']).seguro_diciembre},]

        kwargs['nombre'] = Gestor.objects.get(pk=self.kwargs['gestor_id']).nombre
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(FormadorActualizarSeguroView,self).get_context_data(**kwargs)


class FuncionarioActualizarSoporteView(UpdateView):
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

class FuncionarioActualizarInformacionView(UpdateView):
    model = Funcionario
    form_class = FuncionarioInformacionForm
    template_name = "update_funcionario_informacion.html"

    pk_url_kwarg = "funcionario_id"
    success_url = "../../../"


    def get_context_data(self, **kwargs):
        kwargs['informacion'] = [
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

class FuncionarioActualizarSeguroView(UpdateView):
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
                              {'mes':"junlio",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_julio},
                              {'mes':"agosto",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_agosto},
                              {'mes':"septiembre",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_septiembre},
                              {'mes':"octubre",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_octubre},
                              {'mes':"noviembre",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_noviembre},
                              {'mes':"diciembre",'soporte':Funcionario.objects.get(pk=self.kwargs['funcionario_id']).seguro_diciembre},]

        kwargs['nombre'] = Funcionario.objects.get(pk=self.kwargs['funcionario_id']).nombre
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(FuncionarioActualizarSeguroView,self).get_context_data(**kwargs)

class FuncionarioActualizarFotoView(UpdateView):
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