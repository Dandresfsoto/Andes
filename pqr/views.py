from .models import Pqr
from .serializers import PqrSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

class PqrView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        x = request._request.GET
        data = {}
        data['region'] = self.kwargs['region']
        data['eje'] = x['eje']
        data['nombre'] = x['nombre']
        data['email'] = x['email']
        data['telefono'] = x['telefono']
        data['municipio'] = x['municipio']
        data['mensaje'] = x['mensaje']
        serializer = PqrSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)