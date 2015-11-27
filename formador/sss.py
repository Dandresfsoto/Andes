class FormadorGrupoTableView(BaseDatatableView):
    model = Grupo
    columns = [
        'id',
        'formador',
        'municipio',
        'nombre',
        'direccion',
        'horario'
    ]

    order_columns = [
        'id',
        'formador',
        'municipio',
        'nombre',
        'direccion',
        'horario'
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(formador__id=self.kwargs['id_formador'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'nombre__icontains' : search.capitalize()})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'formador':
            return str(row.nombre)
        if column == 'municipio':
            return str(row.municipio.nombre)
        else:
            return super(FormadorGrupoTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:

            json_data.append([
                item.id,
                item.nombre,
                item.municipio.nombre,
                item.municipio.departamento.nombre,
                item.direccion,
                item.horario,
                participantes,
                y
            ])

        return json_data