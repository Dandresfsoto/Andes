from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from participantes import views

urlpatterns = [
    url('^api/(?P<cedula>\w+)/$', views.ParticipanteViewSet.as_view()),
    url(r'^$', login_required(views.ParticipantesView.as_view()),name="participantes"),
    url(r'^datatable/(?P<diplomado>\w+)', login_required(views.ParticipanteTableView.as_view()),name='tabla_participantes'),
    url(r'^proyecto/(?P<diplomado>\w+)', login_required(views.ProyectoTableView.as_view()),name='tabla_proyectos'),
]