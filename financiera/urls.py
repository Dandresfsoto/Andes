from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from financiera import views


urlpatterns = [
    url(r'^$', login_required(views.GestorView.as_view()),name='gestores'),
]