from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from funcionario import views


urlpatterns = [
    url(r'^datatable/(?P<region>\w+)', login_required(views.FuncionarioTableView.as_view()),name='tabla_funcionarios'),
    url(r'^datatable_cpe/(?P<region>\w+)/(?P<eje>\w+)', login_required(views.FuncionarioTableEjeView.as_view())),
]