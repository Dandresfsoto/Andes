from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from formacion import views

urlpatterns = [
    url(r'^$', login_required(views.FormacionView.as_view())),

    url(r'^tipo2/$', login_required(views.FormadorView.as_view())),
    url(r'^tipo2/(?P<formador_id>\w+)/$', login_required(views.FormadorGrupoView.as_view())),

    url(r'^tipo2/(?P<formador_id>\w+)/calificar/(?P<grupo_id>\w+)/actualizar/(?P<soporte_id>\w+)/$', login_required(views.FormSoporteGrupoView.as_view())),
    url(r'^tipo2/(?P<formador_id>\w+)/calificar/(?P<grupo_id>\w+)/asignar/(?P<soporte_id>\w+)/$', login_required(views.FormAsignarSoporteView.as_view())),
    url(r'^tipo2/(?P<formador_id>\w+)/calificar/(?P<grupo_id>\w+)/agregar/$', login_required(views.FormAgregarSoporteView.as_view())),

    url(r'^tipo2/(?P<formador_id>\w+)/calificar/(?P<grupo_id>\w+)/$', login_required(views.CalificarGrupoView.as_view())),

    url(r'^tipo2/(?P<formador_id>\w+)/nuevo/$', login_required(views.NuevoGrupoView.as_view())),
    url(r'^tipo2/(?P<formador_id>\w+)/grupo/(?P<grupo_id>\w+)/$', login_required(views.ListadoGrupoView.as_view())),
    url(r'^tipo2/(?P<formador_id>\w+)/grupo/(?P<grupo_id>\w+)/editar/(?P<participante_id>\w+)/$', login_required(views.EditarParticipanteView.as_view())),
    url(r'^tipo2/(?P<formador_id>\w+)/grupo/(?P<grupo_id>\w+)/nuevo/participante/$', login_required(views.NuevoParticipanteView.as_view())),
    url(r'^tipo2/(?P<formador_id>\w+)/soportes/(?P<grupo_id>\w+)/$', login_required(views.soporte_form)),

    url(r'^tipo2/(?P<formador_id>\w+)/grupo/(?P<grupo_id>\w+)/masivo/$', login_required(views.ListadoMasivoView.as_view())),
    url(r'^tipo2/(?P<formador_id>\w+)/grupo/(?P<grupo_id>\w+)/masivo/nuevo/$', login_required(views.NuevoMasivoView.as_view())),


    url(r'^tipo1/$', login_required(views.FormadorTipo1View.as_view())),
    url(r'^tipo1/(?P<formador_id>\w+)/$', login_required(views.FormadorTipo1GrupoView.as_view())),
    url(r'^tipo1/(?P<formador_id>\w+)/nuevo/$', login_required(views.NuevoGrupoDocenteView.as_view())),
    url(r'^tipo1/(?P<formador_id>\w+)/grupo/(?P<grupo_id>\w+)/$', login_required(views.ListadoGrupoDocentesView.as_view())),
    url(r'^tipo1/(?P<formador_id>\w+)/grupo/(?P<grupo_id>\w+)/editar/(?P<participante_id>\w+)/$', login_required(views.EditarDocenteView.as_view())),
    url(r'^tipo1/(?P<formador_id>\w+)/grupo/(?P<grupo_id>\w+)/nuevo/docente/$', login_required(views.NuevoDocenteView.as_view())),

    url(r'^tipo1/(?P<formador_id>\w+)/calificar/(?P<grupo_id>\w+)/$', login_required(views.TipoEvidenciaView.as_view())),
    url(r'^tipo1/(?P<formador_id>\w+)/calificar/(?P<grupo_id>\w+)/(?P<tipo_evidencia>\w+)/$', login_required(views.NivelEvidenciaView.as_view())),
    url(r'^tipo1/(?P<formador_id>\w+)/calificar/(?P<grupo_id>\w+)/(?P<tipo_evidencia>\w+)/(?P<nivel>\w+)/$', login_required(views.SesionEvidenciaView.as_view())),
    url(r'^tipo1/(?P<formador_id>\w+)/calificar/(?P<grupo_id>\w+)/(?P<tipo_evidencia>\w+)/(?P<nivel>\w+)/(?P<sesion>\w+)/$', login_required(views.CalificarGrupoDocentesView.as_view())),
    url(r'^tipo1/(?P<formador_id>\w+)/calificar/(?P<grupo_id>\w+)/(?P<tipo_evidencia>\w+)/(?P<nivel>\w+)/(?P<sesion>\w+)/actualizar/(?P<soporte_id>\w+)/$', login_required(views.FormSoporteGrupoDocenteView.as_view())),
    url(r'^tipo1/(?P<formador_id>\w+)/calificar/(?P<grupo_id>\w+)/(?P<tipo_evidencia>\w+)/(?P<nivel>\w+)/(?P<sesion>\w+)/asignar/(?P<soporte_id>\w+)/$', login_required(views.FormAsignarSoporteDocenteView.as_view())),
    url(r'^tipo1/(?P<formador_id>\w+)/calificar/(?P<grupo_id>\w+)/(?P<tipo_evidencia>\w+)/(?P<nivel>\w+)/(?P<sesion>\w+)/agregar/$', login_required(views.FormAgregarSoporteDocenteView.as_view())),

    url(r'^map/$', login_required(views.MapView.as_view())),
    url(r'^map/(?P<codigo>\w+)/$', login_required(views.MapRespuestaView.as_view())),
    url(r'^map/(?P<codigo>\w+)/nuevo/$', login_required(views.MapNuevaRespuestaView.as_view())),
    url(r'^map/(?P<codigo>\w+)/editar/(?P<codigo_respuesta>\w+)/$', login_required(views.MapEditarRespuestaView.as_view())),

    url(r'^llamadas/$', login_required(views.LlamadasView.as_view())),
    url(r'^llamadas/nuevo/$', login_required(views.LlamadasNuevoView.as_view())),
    url(r'^llamadas/(?P<codigo>\w+)/$', login_required(views.LlamadasRespuestaView.as_view())),
    url(r'^llamadas/(?P<codigo>\w+)/nuevo/$', login_required(views.LlamadasNuevaRespuestaView.as_view())),
    url(r'^llamadas/(?P<codigo>\w+)/editar/(?P<codigo_respuesta>\w+)/$', login_required(views.MapEditarRespuestaView.as_view())),
    url(r'^lista_auxiliares/$', login_required(views.ListaAuxiliaresView.as_view())),
]