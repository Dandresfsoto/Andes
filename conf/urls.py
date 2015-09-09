"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib.auth.decorators import login_required
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from conf import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','django.contrib.auth.views.login',{'template_name':'login.html'}, name='login'),
    url(r'^cerrar/$','django.contrib.auth.views.logout_then_login',name='logout'),
    url(r'^region/',include('region.urls')),
    url(r'^usuarios/',include('user.urls')),
    url(r'^participantes/',include('participantes.urls')),
    url(r'^gestor/',include('gestor.urls')),
    url(r'^formador/',include('formador.urls')),
    url(r'^funcionario/',include('funcionario.urls')),
    url(r'^progressbarupload/', include('progressbarupload.urls')),
    url(r'^pqr/', include('pqr.urls')),
    url(r'^password/cambiar/$', login_required(views.CambiarPassword.as_view())),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT,}),
]