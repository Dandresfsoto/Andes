from django.conf.urls import url, include
from pqr import views

urlpatterns = [
    url(r'^$', views.PqrView.as_view()),
]