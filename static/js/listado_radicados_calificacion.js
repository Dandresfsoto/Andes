$(document).ready(function() {

    var table = $('#table').DataTable({
        "searching": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/radicado/lista/"+ $('#id_region').val()+"/"+$('#id_gestor').val(),
        "language":{
            "url": "//cdn.datatables.net/plug-ins/1.10.8/i18n/Spanish.json"
        },
        "columns": [
            {
                "className":      'details-control',
                "orderable":      false,
                "data":           null,
                "defaultContent": ''
            },
            { "data": 1 },
            { "data": 2 },
            { "data": 3 }
        ],
    });

});