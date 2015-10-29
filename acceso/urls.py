from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from acceso import views



urlpatterns = [
    url(r'^$', login_required(views.AccesoView.as_view()),name='acceso'),
    url(r'^(?P<tipo_gestor>\w+)/$', login_required(views.AccesoTipoView.as_view())),
    url(r'^(?P<tipo_gestor>\w+)/calificacion/$', login_required(views.AccesoCalificacionView.as_view())),
    url(r'^(?P<tipo_gestor>\w+)/calificacion_total/$', login_required(views.AccesoCalificacionTotalView.as_view())),

    url(r'^(?P<tipo_gestor>\w+)/calificacion/(?P<id_gestor>\w+)/$', login_required(views.AccesoListadoMunicipiosView.as_view())),
    url(r'^(?P<tipo_gestor>\w+)/calificacion/reporte/(?P<id_gestor>\w+)/$', login_required(views.reporte_acceso)),
    url(r'^(?P<tipo_gestor>\w+)/calificacion/(?P<id_gestor>\w+)/municipio/(?P<id_municipio>\w+)/$', login_required(views.AccesoListadoRadicadosView.as_view())),
    url(r'^(?P<tipo_gestor>\w+)/calificacion/(?P<id_gestor>\w+)/municipio/(?P<id_municipio>\w+)/radicado/(?P<id_radicado>\w+)/$', login_required(views.evidencia_form)),
    url(r'^(?P<tipo_gestor>\w+)/calificacion_total/radicado/(?P<id_radicado>\w+)/$', login_required(views.evidencia_total_form)),
    url(r'^(?P<tipo_gestor>\w+)/calificacion_total/reporte/$', login_required(views.reporte_total)),
    url(r'^(?P<tipo_gestor>\w+)/administracion/$', login_required(views.AccesoView.as_view())),

    url(r'^(?P<tipo_gestor>\w+)/masivo/$', login_required(views.MasivoView.as_view())),
    url(r'^(?P<tipo_gestor>\w+)/masivo/listado/$', login_required(views.MasivoTableView.as_view())),
    url(r'^(?P<tipo_gestor>\w+)/masivo/nuevo/$', login_required(views.MasivoNuevoView.as_view())),
    url(r'^(?P<tipo_gestor>\w+)/masivo/ejecutar/(?P<id_masivo>\w+)/$', login_required(views.ejecutar_masivo)),
]