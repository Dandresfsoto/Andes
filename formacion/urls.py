from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from formacion import views

urlpatterns = [
    url(r'^$', login_required(views.FormacionView.as_view())),

    url(r'^tipo2/$', login_required(views.FormadorView.as_view())),
    url(r'^tipo2/(?P<formador_id>\w+)/$', login_required(views.FormadorGrupoView.as_view())),

    url(r'^tipo2/(?P<formador_id>\w+)/actualizar/(?P<soporte_id>\w+)/$', login_required(views.FormSoporteGrupoView.as_view())),
    url(r'^tipo2/(?P<formador_id>\w+)/asignar/(?P<soporte_id>\w+)/$', login_required(views.FormAsignarSoporteView.as_view())),

    url(r'^tipo2/(?P<formador_id>\w+)/nuevo/$', login_required(views.NuevoGrupoView.as_view())),
    url(r'^tipo2/(?P<formador_id>\w+)/grupo/(?P<grupo_id>\w+)/$', login_required(views.ListadoGrupoView.as_view())),
    url(r'^tipo2/(?P<formador_id>\w+)/grupo/(?P<grupo_id>\w+)/editar/(?P<participante_id>\w+)/$', login_required(views.EditarParticipanteView.as_view())),
    url(r'^tipo2/(?P<formador_id>\w+)/grupo/(?P<grupo_id>\w+)/nuevo/participante/$', login_required(views.NuevoParticipanteView.as_view())),
    url(r'^tipo2/(?P<formador_id>\w+)/soportes/(?P<grupo_id>\w+)/$', login_required(views.soporte_form)),

    url(r'^tipo2/(?P<formador_id>\w+)/grupo/(?P<grupo_id>\w+)/masivo/$', login_required(views.ListadoMasivoView.as_view())),
    url(r'^tipo2/(?P<formador_id>\w+)/grupo/(?P<grupo_id>\w+)/masivo/nuevo/$', login_required(views.NuevoMasivoView.as_view())),
]