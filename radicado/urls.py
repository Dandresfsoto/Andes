from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from radicado import views

urlpatterns = [
    url(r'^lista/(?P<region>\w+)/(?P<id_municipio>\w+)/(?P<id_gestor>\w+)', login_required(views.RadicadoTableView.as_view())),
    url(r'^lista_apoyo/(?P<region>\w+)/(?P<id_municipio>\w+)/(?P<id_gestor>\w+)', login_required(views.RadicadoApoyoTableView.as_view())),
    url(r'^lista_total/(?P<region>\w+)', login_required(views.RadicadoTotalTableView.as_view())),
    url(r'^lista_total_apoyo/(?P<region>\w+)', login_required(views.RadicadoTotalApoyoTableView.as_view())),
    url(r'^reasignados/(?P<region>\w+)', login_required(views.RadicadoReasignadoView.as_view())),
]