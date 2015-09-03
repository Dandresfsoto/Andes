from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from formador import views


urlpatterns = [
    url(r'^datatable/(?P<region>\w+)', login_required(views.FormadorTableView.as_view()),name='tabla_formadores'),
]