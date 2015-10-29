function format ( d ) {
    // `d` is the original data object for the row
    return '<div class="table-responsive"><table class="table table-striped" style="padding-left:50px;color:black;">'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>INFORMACIÓN</b></h4></th>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Formador:</b> '+d[1]+'</td>'+
            '<td colspan="2"><b>Grupo:</b> '+d[2]+'</td>'+
            '<td colspan="2"><b>Municipio:</b> '+d[5]+'</td>'+
            '<td colspan="2"><b>Institución:</b> '+d[6]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Genero:</b> '+d[10]+'</td>'+
            '<td colspan="2"><b>Nivel Educativo:</b> '+d[11]+'</td>'+
            '<td colspan="2"><b>Telefono:</b> '+d[12]+'</td>'+
            '<td colspan="2"><b>Correo:</b> '+d[13]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Población:</b> '+d[14]+'</td>'+
            '<td colspan="2"><b>Código ANSPE:</b> '+d[15]+'</td>'+
            '<td colspan="2"><b>Tipo de Proyecto:</b> '+d[16]+'</td>'+
            '<td colspan="2"><b>Grupo de Conformación:</b> '+d[17]+'</td>'+
        '</tr>'+

    '</table></div>';
}

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
                text: 'Carga Masiva',
                action: function ( e, dt, node, config ) {
                    location.replace(location.href+"masivo/");
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
                "data": 9,
                "render": function ( data, type, row, meta ) {
                          return '<a href="editar/'+row[0]+'" style="color:#004c99;">'+data+'</a>';
                },
                "orderable":false
            },
            {
                "data": 7,
                "orderable":false,
            },
            {
                "data": 8,
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