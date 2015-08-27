
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from proyectos import views


urlpatterns = [
    url(r'^$', login_required(views.ProyectoView.as_view()),name="proyectos"),
]