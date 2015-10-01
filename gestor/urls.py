from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from gestor import views


urlpatterns = [
    url(r'^datatable/(?P<region>\w+)', login_required(views.GestorTableView.as_view()),name='tabla_gestores'),
    url(r'^financiero/(?P<region>\w+)', login_required(views.GestorFinancieroTableView.as_view())),
    url(r'^calificacion/(?P<region>\w+)', login_required(views.GestorCalificacionTableView.as_view())),
]