from .models import Gestor
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q

class GestorTableView(BaseDatatableView):
    model = Gestor
    columns = [
        'nombre',
        'cedula',
        'celular',
        'correo',
    ]

    order_columns = [
        'nombre',
        'cedula',
        'celular',
        'correo',
    ]

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'nombre__contains' : search})
            q |= Q(**{'cedula__contains' : search})
            qs = qs.filter(q)
        return qs