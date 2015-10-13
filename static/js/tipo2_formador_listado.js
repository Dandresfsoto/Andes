$(document).ready(function() {

    var table = $('#table').DataTable({
        dom: 'Bfrtip',
        buttons: [
            {
                text: 'Nuevo Participante',
                action: function ( e, dt, node, config ) {
                    location.replace(location.href+"nuevo/participante/");
                }
            },
            {
                text: 'Cargar Archivo',
                action: function ( e, dt, node, config ) {
                    location.replace(location.href+"nuevo/archivo/");
                }
            }
        ],
        "searching": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/formador/listado/"+ $('#id_region').val()+"/"+ $('#id_formador').val()+"/"+ $('#id_grupo').val(),
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
            {
                "data": 10,
                "orderable":false
            },
            {
                "data": 5,
                "orderable":false,
            },
            {
                "data": 6,
                "orderable":false,
            }
        ],
        "order": [[1, 'asc']],
    });


    // Add event listener for opening and closing details
    $('#table tbody').on('click', 'td.details-control', function () {
        var tr = $(this).closest('tr');
        var row = table.row( tr );

        if ( row.child.isShown() ) {
            // This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
        }
        else {
            // Open this row
            row.child( format(row.data()) ).show();
            tr.addClass('shown');
        }
    } );

});