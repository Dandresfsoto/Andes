from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from municipio import views

urlpatterns = [
    url(r'^lista/(?P<region>\w+)/(?P<id_gestor>\w+)', login_required(views.MunicipioTableView.as_view())),
    url(r'^lista_apoyo/(?P<region>\w+)/(?P<id_gestor>\w+)', login_required(views.MunicipioTableApoyoView.as_view())),
]