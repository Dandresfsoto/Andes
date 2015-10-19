from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from acceso import views



urlpatterns = [
    url(r'^$', login_required(views.AccesoView.as_view()),name='acceso'),

    url(r'api/(?P<id_evidencia>\w+)/', login_required(views.EvidenciaViewSet.as_view())),

    url(r'^calificacion/$', login_required(views.AccesoCalificacionView.as_view())),
    url(r'^calificacion_total/$', login_required(views.AccesoCalificacionTotalView.as_view())),
    url(r'^reasignados/$', login_required(views.AccesoReasignadosView.as_view())),

    url(r'^calificacion/(?P<id_gestor>\w+)/$', login_required(views.AccesoListadoMunicipiosView.as_view())),
    url(r'^calificacion/reporte/(?P<id_gestor>\w+)/$', login_required(views.reporte_acceso)),
    url(r'^calificacion/(?P<id_gestor>\w+)/municipio/(?P<id_municipio>\w+)/$', login_required(views.AccesoListadoRadicadosView.as_view())),
    url(r'^calificacion/(?P<id_gestor>\w+)/municipio/(?P<id_municipio>\w+)/radicado/(?P<id_radicado>\w+)/$', login_required(views.evidencia_form)),
    url(r'^calificacion_total/radicado/(?P<id_radicado>\w+)/$', login_required(views.evidencia_total_form)),
    url(r'^calificacion/(?P<id_gestor>\w+)/municipio/(?P<id_municipio>\w+)/reasignar/(?P<id_radicado>\w+)/$', login_required(views.ReasignarView.as_view())),

    url(r'^administracion/$', login_required(views.AccesoView.as_view())),

    url(r'^masivo/$', login_required(views.MasivoView.as_view())),
    url(r'^masivo/listado/$', login_required(views.MasivoTableView.as_view())),
    url(r'^masivo/nuevo/$', login_required(views.MasivoNuevoView.as_view())),
]