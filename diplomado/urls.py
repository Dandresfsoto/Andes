from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from diplomado import views

urlpatterns = [
    url(r'^$', login_required(views.DiplomadosView.as_view()),name="diplomados"),

    url(r'^escuela_tic/$', login_required(views.EscuelaTicView.as_view())),
    url(r'^docentes/$', login_required(views.DocentesView.as_view())),

    url(r'^escuela_tic/participantes/$', login_required(views.EscuelaTicParticipantesListadoView.as_view())),
    url(r'^docentes/participantes/$', login_required(views.DocentesListadoView.as_view())),

    url(r'^escuela_tic/participantes/evidencias/(?P<participante_id>\w+)/$', login_required(views.EscuelaTicEvidenciasListadoView.as_view())),
    url(r'^docentes/participantes/evidencias/(?P<participante_id>\w+)/$', login_required(views.DocentesEvidenciasListadoView.as_view())),

    url(r'^escuela_tic/actividades/$', login_required(views.EscuelaTicActividadesListadoView.as_view())),
    url(r'^docentes/actividades/$', login_required(views.DocentesActividadesListadoView.as_view())),

    url(r'^escuela_tic/actividades/(?P<actividad_id>\w+)/$', login_required(views.EscuelaTicActividadesListadoFiltroView.as_view())),
    url(r'^docentes/actividades/(?P<actividad_id>\w+)/$', login_required(views.DocentesActividadesListadoFiltroView.as_view())),

    url(r'^diplomado/(?P<diplomado>\w+)/participantes/', include('participantes.urls')),
    url(r'^diplomado/(?P<diplomado>\w+)/proyectos/', include('proyectos.urls')),
]