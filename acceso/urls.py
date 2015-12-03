from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from acceso import views



urlpatterns = [
    url(r'^$', login_required(views.AccesoView.as_view()),name='acceso'),
    url(r'^territoriales/$', login_required(views.AccesoTipoView.as_view())),
    url(r'^territoriales/calificacion/$', login_required(views.AccesoCalificacionView.as_view())),
    url(r'^territoriales/calificacion_total/$', login_required(views.AccesoCalificacionTotalView.as_view())),

    url(r'^territoriales/calificacion/(?P<id_gestor>\w+)/$', login_required(views.AccesoListadoMunicipiosView.as_view())),
    url(r'^territoriales/calificacion/reporte/(?P<id_gestor>\w+)/$', login_required(views.reporte_acceso)),
    url(r'^territoriales/calificacion/(?P<id_gestor>\w+)/municipio/(?P<id_municipio>\w+)/$', login_required(views.AccesoListadoRadicadosView.as_view())),
    url(r'^territoriales/calificacion/(?P<id_gestor>\w+)/municipio/(?P<id_municipio>\w+)/radicado/(?P<id_radicado>\w+)/$', login_required(views.evidencia_form)),
    url(r'^territoriales/calificacion_total/radicado/(?P<id_radicado>\w+)/$', login_required(views.evidencia_total_form)),
    url(r'^territoriales/calificacion_total/reporte/$', login_required(views.reporte_total)),
    url(r'^territoriales/administracion/$', login_required(views.AccesoView.as_view())),

    url(r'^territoriales/masivo/$', login_required(views.MasivoView.as_view())),
    url(r'^territoriales/masivo/listado/$', login_required(views.MasivoTableView.as_view())),
    url(r'^territoriales/masivo/nuevo/$', login_required(views.MasivoNuevoView.as_view())),
    url(r'^territoriales/masivo/ejecutar/(?P<id_masivo>\w+)/$', login_required(views.ejecutar_masivo)),


    url(r'^apoyo/$', login_required(views.AccesoTipoApoyoView.as_view())),
    url(r'^apoyo/calificacion/$', login_required(views.AccesoCalificacionApoyoView.as_view())),
    #url(r'^apoyo/calificacion_total/$', login_required(views.AccesoCalificacionTotalApoyoView.as_view())),

    url(r'^apoyo/calificacion/(?P<id_gestor>\w+)/$', login_required(views.AccesoListadoMunicipiosApoyoView.as_view())),
    #url(r'^apoyo/calificacion/reporte/(?P<id_gestor>\w+)/$', login_required(views.reporte_acceso_apoyo)),
    #url(r'^apoyo/calificacion/(?P<id_gestor>\w+)/municipio/(?P<id_municipio>\w+)/$', login_required(views.AccesoListadoRadicadosApoyoView.as_view())),
    #url(r'^apoyo/calificacion/(?P<id_gestor>\w+)/municipio/(?P<id_municipio>\w+)/radicado/(?P<id_radicado>\w+)/$', login_required(views.evidencia_form_apoyo)),
    #url(r'^apoyo/calificacion_total/radicado/(?P<id_radicado>\w+)/$', login_required(views.evidencia_total_form_apoyo)),
    #url(r'^apoyo/calificacion_total/reporte/$', login_required(views.reporte_total_apoyo)),
    #url(r'^apoyo/administracion/$', login_required(views.AccesoApoyoView.as_view())),

    #url(r'^apoyo/masivo/$', login_required(views.MasivoApoyoView.as_view())),
    #url(r'^apoyo/masivo/listado/$', login_required(views.MasivoTableApoyoView.as_view())),
    #url(r'^apoyo/masivo/nuevo/$', login_required(views.MasivoNuevoApoyoView.as_view())),
    #url(r'^apoyo/masivo/ejecutar/(?P<id_masivo>\w+)/$', login_required(views.ejecutar_masivo_apoyo)),
]