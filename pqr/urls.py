from django.conf.urls import url, include
from pqr import views

urlpatterns = [
    url(r'^(?P<region>\w+)/$', views.PqrView.as_view()),
]