from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm


#----------------------------------------------- API USERS -------------------------------------------------------------

from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from user import serializers
from user import models



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [ permissions.IsAuthenticatedOrReadOnly ]

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    permission_classes = [ permissions.IsAuthenticatedOrReadOnly ]
