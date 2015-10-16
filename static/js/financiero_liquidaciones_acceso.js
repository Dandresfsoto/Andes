function format ( d ) {
    // `d` is the original data object for the row
    return '<div class="table-responsive"><table class="table table-striped" style="padding-left:50px;color:black;">'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>INFORMACIÓN</b></h4></th>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Valor Inicial de Contrato:</b> $'+d[4].toLocaleString('es-CO')+'</td>'+
            '<td colspan="2"><b>Valor Ejecutado del Contrato:</b> $'+d[5].toLocaleString('es-CO')+'</td>'+
            '<td colspan="2"><b>Valor Pagado del Contrato:</b> $'+d[6].toLocaleString('es-CO')+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="8"><b>Descargar Liquidación:</b> <a href="descargar/'+d[0]+'" style="color:#004c99;">Click aqui</a></td>'+
        '</tr>'+

    '</table></div>';
}

$(document).ready(function() {

    var table = $('#table').DataTable({
        dom: 'Bfrtip',
        buttons: [
            {
                text: 'Nuevo',
                action: function ( e, dt, node, config ) {
                    location.replace(location.href+"nuevo");
                }
            }
        ],
        "searching": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/region/"+ $('#id_region').val()+"/andes/financiero/documental/liquidaciones/gestores/listado/",
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
                "data": 1,
                "render": function ( data, type, row, meta ) {
                          return '<a href="editar/'+row[0]+'" style="color:#004c99;">'+data+'</a>';
                },
                "orderable":      false,
            },
            { "data": 2,"orderable":false },
            { "data": 3,"orderable":false },
        ],
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