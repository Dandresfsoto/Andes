from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from region import views

urlpatterns = [
    url(r'^$', login_required(views.InicioView.as_view()),name="region"),
    url(r'^(?P<pk>\w+)/$', login_required(views.RegionView.as_view()),name="region_rol"),
    url(r'^(?P<pk>\w+)/cpe/', include('diplomado.urls')),
    url(r'^(?P<pk>\w+)/andes/$', login_required(views.AndesView.as_view()),name="andes_rol"),
    url(r'^(?P<pk>\w+)/andes/administrativo/', include('administrativo.urls')),
]