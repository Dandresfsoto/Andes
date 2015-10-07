from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from region import views

urlpatterns = [
    url(r'^$', login_required(views.InicioView.as_view()),name="region"),
    url(r'^(?P<pk>\w+)/$', login_required(views.RegionView.as_view()),name="region_rol"),
    url(r'^(?P<pk>\w+)/cpe/$', login_required(views.CpeView.as_view())),

    url(r'^(?P<pk>\w+)/cpe/formacion/$', login_required(views.CpeFormacionView.as_view())),
    url(r'^(?P<pk>\w+)/cpe/formacion/funcionarios/(?P<eje>\w+)/$', login_required(views.CpeFuncionarioView.as_view())),
    url(r'^(?P<pk>\w+)/cpe/formacion/formadores/$', login_required(views.CpeFormadorView.as_view())),
    url(r'^(?P<pk>\w+)/cpe/formacion/formadores/(?P<tipo>\w+)/$', login_required(views.CpeFormadorTipoView.as_view())),
    url(r'^(?P<pk>\w+)/cpe/formacion/etic@/', include('diplomado.urls')),

    url(r'^(?P<pk>\w+)/cpe/acceso/$', login_required(views.CpeAccesoView.as_view())),
    url(r'^(?P<pk>\w+)/cpe/acceso/funcionarios/(?P<eje>\w+)/$', login_required(views.CpeFuncionarioView.as_view())),
    url(r'^(?P<pk>\w+)/cpe/acceso/gestores/$', login_required(views.CpeGestorView.as_view())),

    url(r'^(?P<pk>\w+)/andes/$', login_required(views.AndesView.as_view()),name="andes_rol"),
    url(r'^(?P<pk>\w+)/andes/administrativo/', include('administrativo.urls')),
    url(r'^(?P<pk>\w+)/andes/acceso/', include('acceso.urls')),
    url(r'^(?P<pk>\w+)/andes/financiero/', include('financiero.urls')),
    url(r'^(?P<pk>\w+)/andes/formacion/', include('formacion.urls')),
]