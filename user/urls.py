from django.conf.urls import url, include
from django.conf.urls import url
from user import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'users_profile', views.UserProfileViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]