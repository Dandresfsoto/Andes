from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from formador import views


urlpatterns = [
    url(r'^datatable/(?P<region>\w+)/(?P<tipo>\w+)', login_required(views.FormadorTableView.as_view()),name='tabla_formadores'),
    url(r'^calificacion/(?P<region>\w+)', login_required(views.FormadorCalificacionTableView.as_view())),
    url(r'^grupo/(?P<region>\w+)/(?P<id_formador>\w+)', login_required(views.FormadorGrupoTableView.as_view())),
    url(r'^listado/(?P<region>\w+)/(?P<id_formador>\w+)/(?P<id_grupo>\w+)', login_required(views.FormadorListadoGrupoTableView.as_view())),
    url(r'^masivo/(?P<region>\w+)/(?P<id_formador>\w+)/(?P<id_grupo>\w+)', login_required(views.FormadorListadoMasivoTableView.as_view())),
    url(r'^listado_total_participantes/(?P<region>\w+)/', login_required(views.ParticipantesListadoTableView.as_view())),
    url(r'^listado_evidencias/(?P<region>\w+)/(?P<participante__id>\w+)/', login_required(views.EvidenciasListadoTableView.as_view())),
    url(r'^listado_actividades/(?P<region>\w+)/', login_required(views.ActividadesListadoTableView.as_view())),
    url(r'^listado_participantes_actividad/(?P<region>\w+)/(?P<id_actividad>\w+)/', login_required(views.ParticipantesActividadListadoTableView.as_view())),
]