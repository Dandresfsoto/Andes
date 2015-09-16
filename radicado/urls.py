from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from radicado import views

urlpatterns = [
    url(r'^lista/(?P<region>\w+)/(?P<id_gestor>\w+)', login_required(views.RadicadoTableView.as_view())),
]