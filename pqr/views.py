from .models import Pqr
from .serializers import PqrSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jsonp.renderers import JSONPRenderer
from django_datatables_view.base_datatable_view import BaseDatatableView
from .models import Pqr, PqrRespuesta
from django.db.models import Q

class PqrView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONPRenderer,)

    def get(self, request, format=None):
        x = request._request.GET
        data = {}
        data['region'] = x['region']
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

class PqrListadoView(BaseDatatableView):
    model = Pqr
    columns = [
        'id',
        'fecha_recepcion',
        'eje',
        'nombre',
        'email',
        'telefono',
        'municipio',
        'mensaje'
    ]

    order_columns = [
        '-id',
        '-id',
        '-id',
        '-id',
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        if self.kwargs['region'] == '2':
            return self.model.objects.filter(region='Region 4')
        if self.kwargs['region'] == '1':
            return self.model.objects.filter(region='Region 1').order_by('-id')

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'nombre__icontains' : search})
            q |= Q(**{'municipio__icontains' : search})
            qs = qs.filter(q)
        return qs

class PqrListadoRespuestasView(BaseDatatableView):
    model = PqrRespuesta
    columns = [
        'id',
        'fecha',
        'pqr',
        'region',
        'funcionario',
        'mensaje'
    ]

    order_columns = [
        '-id',
        '-id',
        '-id',
        '-id',
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(pqr__id=self.kwargs['codigo']).order_by('-id')

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'funcionario__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'pqr':
            return str(row.pqr.nombre)
        if column == 'region':
            return str(row.region.nombre)
        if column == 'funcionario':
            return str(row.funcionario.nombre)
        else:
            return super(PqrListadoRespuestasView,self).render_column(row,column)