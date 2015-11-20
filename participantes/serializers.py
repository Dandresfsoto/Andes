from rest_framework import serializers
from formacion.models import ParticipanteEscuelaTic

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipanteEscuelaTic
        fields = ('cedula','nombres','apellidos','departamento','municipio')