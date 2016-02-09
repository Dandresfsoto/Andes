from .models import Formador
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q
from formacion.models import Grupo,ParticipanteEscuelaTic, SoporteEntregableEscuelaTic, Masivo, Actividad, EvidenciaEscuelaTic, Entregable
from formacion.models import GrupoDocentes, ParticipanteDocente, EvidenciaDocentes, EntregableDocentes
from random import randrange

def unique(seq):
        seen = set()
        seen_add = seen.add
        return [x for x in seq if not (x in seen or seen_add(x))]

class FormadorTableView(BaseDatatableView):
    model = Formador
    columns = [
        'id',
        'nombre',
        'cedula',
        'celular',
        'correo',
        'cargo',
        'profesion',
        'banco',
        'tipo_cuenta',
        'numero_cuenta',
        'eps',
        'pension',
        'arl',
        'foto',
        'hv',
        'certificacion',
        'rut',
        'contrato',
        'fotocopia_cedula',
        'antecedentes_judiciales',
        'antecedentes_contraloria',
        'seguro_enero',
        'seguro_febrero',
        'seguro_marzo',
        'seguro_abril',
        'seguro_mayo',
        'seguro_junio',
        'seguro_julio',
        'seguro_agosto',
        'seguro_septiembre',
        'seguro_octubre',
        'seguro_noviembre',
        'seguro_diciembre',
        'fecha_contratacion',
        'fecha_terminacion',
    ]

    order_columns = [
        'nombre',
        'nombre',
        'nombre',
        'nombre',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        ''
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(region__id=self.kwargs['region']).filter(tipo__id=self.kwargs['tipo'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'nombre__icontains' : search.capitalize()})
            q |= Q(**{'cedula__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'hv':
            return str(row.hv)
        if column == 'certificacion':
            return str(row.certificacion)
        if column == 'rut':
            return str(row.rut)
        if column == 'contrato':
            return str(row.contrato)
        if column == 'seguro_enero':
            return str(row.seguro_enero)
        if column == 'seguro_febrero':
            return str(row.seguro_febrero)
        if column == 'seguro_marzo':
            return str(row.seguro_marzo)
        if column == 'seguro_abril':
            return str(row.seguro_abril)
        if column == 'seguro_mayo':
            return str(row.seguro_mayo)
        if column == 'seguro_junio':
            return str(row.seguro_junio)
        if column == 'seguro_julio':
            return str(row.seguro_julio)
        if column == 'seguro_agosto':
            return str(row.seguro_agosto)
        if column == 'seguro_septiembre':
            return str(row.seguro_septiembre)
        if column == 'seguro_octubre':
            return str(row.seguro_octubre)
        if column == 'seguro_noviembre':
            return str(row.seguro_noviembre)
        if column == 'seguro_diciembre':
            return str(row.seguro_diciembre)
        if column == 'fotocopia_cedula':
            return str(row.fotocopia_cedula)
        if column == 'antecedentes_judiciales':
            return str(row.antecedentes_judiciales)
        if column == 'antecedentes_contraloria':
            return str(row.antecedentes_contraloria)
        if column == 'foto':
            return str(row.foto)
        else:
            return super(FormadorTableView,self).render_column(row,column)

class FormadorCalificacionTableView(BaseDatatableView):
    model = Formador
    columns = [
        'id',
        'nombre',
        'cedula',
        'celular',
        'correo',
        'cargo',
        'profesion',
        'foto',
        'fecha_contratacion',
        'fecha_terminacion',
    ]

    order_columns = [
        'nombre',
        'nombre',
        'nombre',
        'nombre',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        ''
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(region__id=self.kwargs['region']).filter(tipo__id=self.kwargs['id_tipo'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'nombre__icontains' : search.capitalize()})
            q |= Q(**{'cedula__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'foto':
            return str(row.foto)
        else:
            return super(FormadorCalificacionTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        tipo = int(self.kwargs['id_tipo'])
        if tipo == 1:
            for item in qs:
                grupos = GrupoDocentes.objects.filter(formador__id=item.id).count()
                participantes = ParticipanteDocente.objects.filter(formador__id=item.id).count()
                json_data.append([
                    item.id,
                    item.nombre,
                    item.cedula,
                    item.celular,
                    item.correo,
                    item.cargo,
                    item.profesion,
                    str(item.foto),
                    item.fecha_contratacion,
                    item.fecha_terminacion,
                    grupos,
                    participantes
                ])
        if tipo == 2:
            for item in qs:
                grupos = Grupo.objects.filter(formador__id=item.id).count()
                participantes = ParticipanteEscuelaTic.objects.filter(formador__id=item.id).count()
                json_data.append([
                    item.id,
                    item.nombre,
                    item.cedula,
                    item.celular,
                    item.correo,
                    item.cargo,
                    item.profesion,
                    str(item.foto),
                    item.fecha_contratacion,
                    item.fecha_terminacion,
                    grupos,
                    participantes
                ])

        return json_data

class FormadorGrupoTableView(BaseDatatableView):
    model = Grupo
    columns = [
        'id',
        'formador',
        'municipio',
        'nombre',
        'direccion',
        'horario'
    ]

    order_columns = [
        'id',
        'formador',
        'municipio',
        'nombre',
        'direccion',
        'horario'
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(formador__id=self.kwargs['id_formador'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'nombre__icontains' : search.capitalize()})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'formador':
            return str(row.nombre)
        if column == 'municipio':
            return str(row.municipio.nombre)
        else:
            return super(FormadorGrupoTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            participantes = ParticipanteEscuelaTic.objects.filter(grupo__id=item.id).count()
            json_data.append([
                item.id,
                item.nombre,
                item.municipio.nombre,
                item.municipio.departamento.nombre,
                item.direccion,
                item.horario,
                participantes
            ])

        return json_data

class FormadorGrupoTipo1TableView(BaseDatatableView):
    model = GrupoDocentes
    columns = [
        'id',
        'formador',
        'municipio',
        'nombre',
        'direccion',
        'horario'
    ]

    order_columns = [
        'id',
        'formador',
        'municipio',
        'nombre',
        'direccion',
        'horario'
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(formador__id=self.kwargs['id_formador'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'nombre__icontains' : search.capitalize()})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'formador':
            return str(row.nombre)
        if column == 'municipio':
            return str(row.municipio.nombre)
        else:
            return super(FormadorGrupoTipo1TableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            participantes = ParticipanteDocente.objects.filter(grupo__id=item.id).count()
            json_data.append([
                item.id,
                item.nombre,
                item.municipio.nombre,
                item.municipio.departamento.nombre,
                item.direccion,
                item.horario,
                participantes
            ])

        return json_data

class FormadorListadoGrupoTableView(BaseDatatableView):
    model = ParticipanteEscuelaTic
    columns = [
        'id',
        'formador',
        'grupo',
        'numero',
        'institucion',
        'nombres',
        'apellidos',
        'cedula',
        'genero',
        'nivel_educativo',
        'telefono',
        'correo',
        'poblacion',
        'codigo_anspe',
        'tipo_proyecto',
        'grupo_conformacion'
    ]

    order_columns = [
        'nombres',
        'nombres',
        'nombres',
        'nombres',
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(formador__id=self.kwargs['id_formador']).filter(grupo__id=self.kwargs['id_grupo'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'nombres__icontains' : search})
            q |= Q(**{'apellidos__icontains' : search})
            q |= Q(**{'cedula__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'formador':
            return str(row.formador.nombre)
        if column == 'grupo':
            return str(row.grupo.nombre)
        else:
            return super(FormadorListadoGrupoTableView,self).render_column(row,column)

class FormadorListadoGrupoDocentesTableView(BaseDatatableView):
    model = ParticipanteDocente
    columns = [
        'id',
        'formador',
        'grupo',
        'radicado',
        'nombres',
        'apellidos',
        'cedula',
        'correo',
        'telefono_fijo',
        'celular',
        'area',
        'grado',
        'tipo_beneficiario',
        'genero',
        'nombre_proyecto',
        'definicion_problema',
        'area_proyecto',
        'competencia',
        'grupo_poblacional'
    ]

    order_columns = [
        'nombres',
        'nombres',
        'nombres',
        'nombres',
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(formador__id=self.kwargs['id_formador']).filter(grupo__id=self.kwargs['id_grupo'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'nombres__icontains' : search})
            q |= Q(**{'apellidos__icontains' : search})
            q |= Q(**{'cedula__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'formador':
            return unicode(row.formador.nombre)
        if column == 'grupo':
            return unicode(row.grupo.nombre)
        if column == 'radicado':
            return unicode(row.radicado.numero)
        if column == 'area':
            return unicode(row.area)
        if column == 'grado':
            return unicode(row.grado)
        if column == 'genero':
            return unicode(row.genero)
        if column == 'competencia':
            return unicode(row.competencia)
        if column == 'grupo_poblacional':
            return unicode(row.grupo_poblacional)
        else:
            return super(FormadorListadoGrupoDocentesTableView,self).render_column(row,column)

class FormadorListadoMasivoTableView(BaseDatatableView):
    model = Masivo
    columns = [
        'id',
        'fecha',
        'grupo',
        'archivo',
        'usuario',
        'resultado'
    ]

    order_columns = [
        'id',
        'fecha',
        'grupo',
        'archivo',
        'usuario',
        'resultado'
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(grupo__id=self.kwargs['id_grupo'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'grupo':
            return row.grupo.nombre
        if column == 'archivo':
            return str(row.archivo)
        if column == 'resultado':
            return str(row.resultado)
        if column == 'usuario':
            return row.usuario.username
        else:
            return super(FormadorListadoMasivoTableView,self).render_column(row,column)

class ParticipantesListadoTableView(BaseDatatableView):
    model = ParticipanteEscuelaTic
    columns = [
        'id',
        'formador',
        'grupo',
        'numero',
        'institucion',
        'nombres',
        'apellidos',
        'cedula',
        'genero',
        'nivel_educativo',
        'telefono',
        'correo',
        'poblacion',
        'codigo_anspe',
        'tipo_proyecto',
        'grupo_conformacion'
    ]

    order_columns = [
        'nombres',
        'nombres',
        'nombres',
        'nombres',
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(formador__region__id=self.kwargs['region'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'cedula__icontains' : search})
            q |= Q(**{'nombres__icontains' : search.capitalize()})
            q |= Q(**{'apellidos__icontains' : search.capitalize()})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'formador':
            return str(row.formador.nombre)
        if column == 'grupo':
            return str(row.grupo.nombre)
        else:
            return super(ParticipantesListadoTableView,self).render_column(row,column)

class DocentesListadoTableView(BaseDatatableView):
    model = ParticipanteDocente
    columns = [
        'id',
        'formador',
        'grupo',
        'radicado',
        'nombres',
        'apellidos',
        'cedula',
        'correo',
        'telefono_fijo',
        'celular',
        'area',
        'grado',
        'tipo_beneficiario',
        'genero',
        'nombre_proyecto',
        'definicion_problema',
        'area_proyecto',
        'competencia',
        'grupo_poblacional',
    ]

    order_columns = [
        'nombres',
        'nombres',
        'nombres',
        'nombres',
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(formador__region__id=self.kwargs['region'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'cedula__icontains' : search})
            q |= Q(**{'nombres__icontains' : search.capitalize()})
            q |= Q(**{'apellidos__icontains' : search.capitalize()})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'formador':
            return unicode(row.formador.nombre)
        if column == 'grupo':
            return unicode(row.grupo.nombre)
        if column == 'radicado':
            return unicode(row.radicado)
        if column == 'area':
            return unicode(row.area)
        if column == 'grado':
            return unicode(row.grado)
        if column == 'genero':
            return unicode(row.genero)
        if column == 'competencia':
            return unicode(row.competencia)
        if column == 'grupo_poblacional':
            return unicode(row.grupo_poblacional)
        else:
            return super(DocentesListadoTableView,self).render_column(row,column)

class EvidenciasDocentesListadoTableView(BaseDatatableView):
    model = EvidenciaDocentes
    columns = [
        'id',
        'soporte',
        'entregable',
        'participante'
    ]

    order_columns = [
        'id',
        'id',
        'id',
        'id'
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        x = self.kwargs
        y = x['participante__id']
        qs = self.model.objects.filter(participante__id=y).order_by('entregable')
        c = qs.values_list('entregable__id',flat=True)
        return qs

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'soporte':
            return str(row.soporte.soporte)
        if column == 'entregable':
            return row.entregable.nombre
        if column == 'participante':
            return str(row.participante.cedula)
        else:
            return super(EvidenciasDocentesListadoTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        d = qs.values_list('entregable__id',flat=True)
        for item in qs:
            if item.soporte == None:
                soporte = ""
                #soporte = EvidenciaDocentes.objects.exclude(soporte = None)
                #random = randrange(0,soporte.count()-1)
                #soporte = unicode(soporte[random].soporte.soporte)
            else:
                soporte = unicode(item.soporte.soporte)
            json_data.append([
                item.id,
                item.entregable.actividad.nombre,
                item.entregable.nombre,
                soporte,
                item.entregable.descripcion,
            ])

        return json_data

class EvidenciasListadoTableView(BaseDatatableView):
    model = EvidenciaEscuelaTic
    columns = [
        'id',
        'soporte',
        'entregable',
        'participante'
    ]

    order_columns = [
        'id',
        'id',
        'id',
        'id'
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        x = self.kwargs
        y = x['participante__id']
        return self.model.objects.filter(participante__id=y)

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'soporte':
            return str(row.soporte.soporte)
        if column == 'entregable':
            return row.entregable.nombre
        if column == 'participante':
            return str(row.participante.cedula)
        else:
            return super(EvidenciasListadoTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        qy = EvidenciaEscuelaTic.objects.filter(participante__id=self.kwargs['participante__id'])
        json_data = []
        for item in qy:
            if item.soporte == None:
                soporte = ""
            else:
                soporte = unicode(item.soporte.soporte)
            json_data.append([
                item.id,
                item.entregable.actividad.nombre,
                item.entregable.nombre,
                soporte,
                item.entregable.descripcion,
            ])

        return json_data

class ActividadesListadoTableView(BaseDatatableView):
    model = Entregable
    columns = [
        'id',
        'actividad',
        'nombre',
        'descripcion'
    ]

    order_columns = [
        'id',
        'actividad',
        'nombre',
        'descripcion'
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.all()

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'actividad':
            return str(row.actividad.nombre)
        else:
            return super(ActividadesListadoTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        filtro_region = EvidenciaEscuelaTic.objects.filter(participante__formador__region__id=self.kwargs['region'])
        for item in qs:
            cantidad = filtro_region.filter(entregable__id=item.id).exclude(soporte=None).exclude(soporte__soporte='').count()
            json_data.append([
                item.id,
                item.actividad.nombre,
                item.nombre,
                item.descripcion,
                cantidad
            ])

        return json_data

class ActividadesDocentesListadoTableView(BaseDatatableView):
    model = EntregableDocentes
    columns = [
        'id',
        'actividad',
        'nombre',
        'descripcion'
    ]

    order_columns = [
        'id',
        'actividad',
        'nombre',
        'descripcion'
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.all()

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'actividad':
            return str(row.actividad.nombre)
        else:
            return super(ActividadesDocentesListadoTableView,self).render_column(row,column)



    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            #cantidad = EvidenciaDocentes.objects.filter(participante__formador__region=self.kwargs['region']).filter(soporte__entregable__id=item.id).exclude(soporte__soporte="").values_list("participante__id",flat=True).distinct()
            json_data.append([
                item.id,
                item.actividad.nombre,
                item.nombre,
                item.descripcion,
                #cantidad.count()
            ])

        return json_data

class ParticipantesActividadListadoTableView(BaseDatatableView):
    model = ParticipanteEscuelaTic
    columns = [
        'id',
        'formador',
        'grupo',
        'numero',
        'institucion',
        'nombres',
        'apellidos',
        'cedula',
        'genero',
        'nivel_educativo',
        'telefono',
        'correo',
        'poblacion',
        'codigo_anspe',
        'tipo_proyecto',
        'grupo_conformacion'
    ]

    order_columns = [
        'nombres',
        'nombres',
        'nombres',
        'nombres',
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        x = EvidenciaEscuelaTic.objects.filter(soporte__entregable__id=self.kwargs['id_actividad']).exclude(soporte__soporte="").values_list("participante__id",flat=True)
        return self.model.objects.filter(formador__region__id=self.kwargs['region']).filter(id__in = x)

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'cedula__icontains' : search})
            q |= Q(**{'nombres__icontains' : search.capitalize()})
            q |= Q(**{'apellidos__icontains' : search.capitalize()})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'formador':
            return str(row.formador.nombre)
        if column == 'grupo':
            return str(row.grupo.nombre)
        else:
            return super(ParticipantesActividadListadoTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            soporte = EvidenciaEscuelaTic.objects.filter(participante__id=item.id).get(entregable__id=self.kwargs['id_actividad']).soporte
            json_data.append([
                item.id,
                item.formador.nombre,
                item.grupo.nombre,
                item.numero,
                item.grupo.municipio.departamento.nombre,
                item.grupo.municipio.nombre,
                item.institucion,
                item.nombres,
                item.apellidos,
                item.cedula,
                item.genero,
                item.nivel_educativo,
                item.telefono,
                item.correo,
                item.poblacion,
                item.codigo_anspe,
                item.tipo_proyecto,
                item.grupo_conformacion,
                unicode(soporte.soporte)
            ])

        return json_data

class ParticipantesDocentesActividadListadoTableView(BaseDatatableView):
    model = EvidenciaDocentes
    columns = [
        'id',
        'soporte',
        'entregable',
        'participante',
        'valor',
        'corte'
    ]

    order_columns = [
        'id',
        'id',
        'id',
        'id'
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(participante__formador__region__id=self.kwargs['region']).filter(soporte__entregable__id=self.kwargs['id_actividad']).exclude(soporte__soporte="")

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'participante__cedula__icontains' : search})
            q |= Q(**{'participante__nombres__icontains' : search})
            q |= Q(**{'participante__apellidos__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'soporte':
            return str(row.soporte)
        if column == 'entregable':
            return str(row.entregable)
        if column == 'participante':
            return str(row.participante)
        if column == 'valor':
            return str(row.valor)
        if column == 'corte':
            return str(row.corte)
        else:
            return super(ParticipantesDocentesActividadListadoTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            #soporte = EvidenciaDocentes.objects.filter(participante__id=item.id).get(entregable__id=self.kwargs['id_actividad']).soporte
            json_data.append([
                item.participante.id,
                unicode(item.participante.formador),
                unicode(item.participante.grupo),
                unicode(item.participante.radicado),
                item.participante.nombres,
                item.participante.apellidos,
                item.participante.cedula,
                item.participante.correo,
                item.participante.telefono_fijo,
                item.participante.celular,
                unicode(item.participante.area),
                unicode(item.participante.grado),
                item.participante.tipo_beneficiario,
                unicode(item.participante.genero),
                item.participante.nombre_proyecto,
                item.participante.definicion_problema,
                unicode(item.participante.area_proyecto),
                unicode(item.participante.competencia),
                unicode(item.participante.grupo_poblacional),
                unicode(item.soporte.soporte)
            ])

        return json_data