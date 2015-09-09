from rest_framework import serializers
from .models import Pqr

class PqrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pqr
        fields = ('region','eje','nombre','email','telefono','municipio','mensaje')