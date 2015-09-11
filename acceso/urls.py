from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from acceso import views


urlpatterns = [
    url(r'^$', login_required(views.AccesoView.as_view()),name='acceso'),

    url(r'^calificacion/$', login_required(views.AccesoCalificacionView.as_view())),

    url(r'^administracion/$', login_required(views.AccesoView.as_view())),
]