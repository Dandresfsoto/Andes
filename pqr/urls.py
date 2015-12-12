from django.conf.urls import url, include
from pqr import views

urlpatterns = [
    url(r'^$', views.PqrView.as_view()),
    url(r'^listado_pqr/(?P<region>\w+)/$', views.PqrListadoView.as_view()),
    url(r'^listado_pqr_respuestas/(?P<codigo>\w+)/$', views.PqrListadoRespuestasView.as_view()),
]