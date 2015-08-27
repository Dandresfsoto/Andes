from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from diplomado import views

urlpatterns = [
    url(r'^$', login_required(views.DiplomadosView.as_view()),name="diplomados"),
    url(r'^diplomado/(?P<diplomado>\w+)/$', login_required(views.DiplomadosInfoView.as_view()),name="diplomados_info"),
    url(r'^diplomado/(?P<diplomado>\w+)/participantes/', include('participantes.urls')),
    url(r'^diplomado/(?P<diplomado>\w+)/proyectos/', include('proyectos.urls')),
]