from rest_framework import serializers
from .models import Evidencia
from radicado.models import Radicado

class RadicadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radicado
        fields = ('numero',)

class EvidenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evidencia
        fields = ('id','soporte')