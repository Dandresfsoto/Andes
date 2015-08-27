from rest_framework import serializers
from .models import Participante

class ParticipanteSerializer(serializers.ModelSerializer):
    area = serializers.SlugRelatedField(read_only=True,slug_field="homologacion")
    grado = serializers.SlugRelatedField(read_only=True,slug_field="homologacion")
    beneficiario = serializers.SlugRelatedField(read_only=True,slug_field="homologacion")
    genero = serializers.SlugRelatedField(read_only=True,slug_field="homologacion")
    class Meta:
        model = Participante
        fields = ('radicado','cedula','nombres','apellidos','email','telefono','area','grado','beneficiario','genero')