from django.contrib.auth.models import User, Group
from rest_framework import serializers
from user import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class UserProfileSerializer(serializers.ModelSerializer):
    usuario = UserSerializer()
    class Meta:
        model = models.UserProfile
        fields = ('usuario','imagen')