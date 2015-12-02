function format ( d ) {
    // `d` is the original data object for the row
    return '<div class="table-responsive"><table class="table table-striped" style="padding-left:50px;color:black;">'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>INFORMACIÓN</b></h4></th>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Formador:</b> '+d[1]+'</td>'+
            '<td colspan="2"><b>Grupo:</b> '+d[2]+'</td>'+
            '<td colspan="2"><b>Municipio:</b> '+""+'</td>'+
            '<td colspan="2"><b>Institución:</b> '+d[4]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Genero:</b> '+d[8]+'</td>'+
            '<td colspan="2"><b>Nivel Educativo:</b> '+d[9]+'</td>'+
            '<td colspan="2"><b>Telefono:</b> '+d[10]+'</td>'+
            '<td colspan="2"><b>Correo:</b> '+d[11]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Población:</b> '+d[12]+'</td>'+
            '<td colspan="2"><b>Código ANSPE:</b> '+d[13]+'</td>'+
            '<td colspan="2"><b>Tipo de Proyecto:</b> '+d[14]+'</td>'+
            '<td colspan="2"><b>Grupo de Conformación:</b> '+d[15]+'</td>'+
        '</tr>'+

    '</table></div>';
}

$(document).ready(function() {

    var table = $('#table').DataTable({
        "searching": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/formador/listado_total_participantes/"+ $('#id_region').val(),
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
                "data": 7,
                "render": function ( data, type, row, meta ) {
                          return '<a href="evidencias/'+row[0]+'" style="color:#004c99;">'+data+'</a>';
                },
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