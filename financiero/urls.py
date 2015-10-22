from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from financiero import views

urlpatterns = [
    url(r'^$', login_required(views.FinancieroView.as_view())),

    url(r'^gestores/corte/(?P<corte_id>\w+)/gestor/(?P<gestor_id>\w+)/$', login_required(views.GestorCorteEvidenciaView.as_view())),
    url(r'^gestores/corte/(?P<corte_id>\w+)/gestor/(?P<gestor_id>\w+)/reporte/$', login_required(views.reporte_gestor)),
    url(r'^gestores/corte/(?P<corte_id>\w+)/gestor/(?P<gestor_id>\w+)/email/$', login_required(views.reporte_gestor_email)),

    url(r'^gestores/$', login_required(views.GestorView.as_view())),
    url(r'^gestores/(?P<tipo_id>\w+)/$', login_required(views.GestorTipoView.as_view())),
    url(r'^gestores/(?P<tipo_id>\w+)/nuevo/$', login_required(views.NuevoGestorView.as_view())),

    url(r'^gestores/(?P<tipo_id>\w+)/corte/$', login_required(views.NuevoCorteView.as_view())),
    url(r'^gestores/(?P<tipo_id>\w+)/reporte/$', login_required(views.reporte_quincenal_financiero)),

    url(r'^formadores/$', login_required(views.FormadorView.as_view())),
    url(r'^formadores/(?P<tipo_id>\w+)/$', login_required(views.FormadorTipoView.as_view())),
    url(r'^formadores/(?P<tipo_id>\w+)/nuevo/$', login_required(views.NuevoFormadorView.as_view())),

    url(r'^funcionarios/$', login_required(views.FuncionarioView.as_view())),
    url(r'^funcionarios/nuevo/$', login_required(views.NuevoFuncionarioView.as_view())),

    url(r'^documental/$', login_required(views.DocumentalView.as_view())),
    url(r'^documental/liquidaciones/$', login_required(views.LiquidacionesView.as_view())),

    url(r'^documental/liquidaciones/gestores/$', login_required(views.LiquidacionAccesoView.as_view())),
    url(r'^documental/liquidaciones/gestores/nuevo/$', login_required(views.LiquidacionAccesoNuevoView.as_view())),
    url(r'^documental/liquidaciones/gestores/editar/(?P<id_liquidacion>\w+)/$', login_required(views.LiquidacionAccesoEditarView.as_view())),
    url(r'^documental/liquidaciones/gestores/listado/$', login_required(views.LiquidacionAccesoTableView.as_view())),
    url(r'^documental/liquidaciones/gestores/descargar/(?P<id_liquidacion>\w+)/$', login_required(views.liquidacion_acceso)),

    url(r'^documental/liquidaciones/formadores/$', login_required(views.LiquidacionFormacionView.as_view())),
    url(r'^documental/liquidaciones/formadores/nuevo/$', login_required(views.LiquidacionFormacionNuevoView.as_view())),
    url(r'^documental/liquidaciones/formadores/editar/(?P<id_liquidacion>\w+)/$', login_required(views.LiquidacionFormacionEditarView.as_view())),
    url(r'^documental/liquidaciones/formadores/listado/$', login_required(views.LiquidacionFormacionTableView.as_view())),
    url(r'^documental/liquidaciones/formadores/descargar/(?P<id_liquidacion>\w+)/$', login_required(views.liquidacion_formacion)),
]