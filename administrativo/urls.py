from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from administrativo import views


urlpatterns = [
    url(r'^$', login_required(views.AdministrativoView.as_view()),name='administrativo'),

    url(r'^gestores/$', login_required(views.GestorView.as_view()),name='gestores'),
    url(r'^gestores/actualizar/soportes/(?P<gestor_id>\w+)/$', login_required(views.GestorActualizarSoporteView.as_view())),
    url(r'^gestores/actualizar/seguro/(?P<gestor_id>\w+)/$', login_required(views.GestorActualizarSeguroView.as_view())),
    url(r'^gestores/actualizar/informacion/(?P<gestor_id>\w+)/$', login_required(views.GestorActualizarInformacionView.as_view())),
    url(r'^gestores/actualizar/foto/(?P<gestor_id>\w+)/$', login_required(views.GestorActualizarFotoView.as_view())),

    url(r'^formadores/$', login_required(views.FormadorView.as_view()),name='formadores'),
    url(r'^formadores/actualizar/soportes/(?P<formador_id>\w+)/$', login_required(views.GestorActualizarSoporteView.as_view())),
    url(r'^formadores/actualizar/seguro/(?P<formador_id>\w+)/$', login_required(views.GestorActualizarSeguroView.as_view())),

    url(r'^funcionarios/$', login_required(views.FuncionarioView.as_view()),name='formadores'),
    url(r'^funcionarios/actualizar/soportes/(?P<funcionario_id>\w+)/$', login_required(views.FuncionarioActualizarSoporteView.as_view())),
    url(r'^funcionarios/actualizar/seguro/(?P<funcionario_id>\w+)/$', login_required(views.FuncionarioActualizarSeguroView.as_view())),
    url(r'^funcionarios/actualizar/informacion/(?P<funcionario_id>\w+)/$', login_required(views.FuncionarioActualizarInformacionView.as_view())),
    url(r'^funcionarios/actualizar/foto/(?P<funcionario_id>\w+)/$', login_required(views.FuncionarioActualizarFotoView.as_view())),
]