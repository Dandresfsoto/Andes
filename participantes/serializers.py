from rest_framework import serializers
from formacion.models import ParticipanteEscuelaTic, Grupo
from municipio.models import Municipio
from departamento.models import Departamento

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('nombre',)

class MunicipioSerializer(serializers.ModelSerializer):
    departamento = DepartamentoSerializer()
    class Meta:
        model = Municipio
        fields = ('nombre','departamento')

class GrupoSerializer(serializers.ModelSerializer):
    municipio = MunicipioSerializer()
    class Meta:
        model = Grupo
        fields = ('municipio',)

class ParticipanteSerializer(serializers.ModelSerializer):
    grupo = GrupoSerializer()
    class Meta:
        model = ParticipanteEscuelaTic
        fields = ('cedula','nombres','apellidos','grupo')