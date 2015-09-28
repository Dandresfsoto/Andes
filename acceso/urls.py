from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from acceso import views



urlpatterns = [
    url(r'^$', login_required(views.AccesoView.as_view()),name='acceso'),

    url(r'api/(?P<id_evidencia>\w+)/', login_required(views.EvidenciaViewSet.as_view())),

    url(r'^calificacion/$', login_required(views.AccesoCalificacionView.as_view())),

    url(r'^calificacion/(?P<id_gestor>\w+)/$', login_required(views.AccesoListadoMunicipiosView.as_view())),
    url(r'^calificacion/reporte/(?P<id_gestor>\w+)/$', login_required(views.reporte_acceso)),
    url(r'^calificacion/(?P<id_gestor>\w+)/municipio/(?P<id_municipio>\w+)/$', login_required(views.AccesoListadoRadicadosView.as_view())),
    url(r'^calificacion/(?P<id_gestor>\w+)/municipio/(?P<id_municipio>\w+)/radicado/(?P<id_radicado>\w+)/$', login_required(views.evidencia_form)),

    url(r'^administracion/$', login_required(views.AccesoView.as_view())),
]