function format ( d ) {
    // `d` is the original data object for the row
    return '<div class="table-responsive"><table class="table table-striped" style="padding-left:50px;color:black;">'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>INFORMACIÓN</b></h4></th>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Zona:</b> '+d[4]+'</td>'+
            '<td colspan="2"><b>Matricula:</b> '+d[5]+'</td>'+

        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Nombre institucion:</b> '+d[6]+'</td>'+
            '<td colspan="2"><b>Dane institucion:</b> '+d[7]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Nombre sede:</b> '+d[8]+'</td>'+
            '<td colspan="2"><b>Dane sede:</b> '+d[9]+'</td>'+
        '</tr>'+

         '<tr>'+
            '<td colspan="2"><b>Actividades ejecutadas:</b> '+d[10]+'</td>'+
            '<td colspan="2"><b>Actividades pendientes:</b> '+d[11]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="4"><b>Progreso: </b>'+d[12]+'%<progress value="'+d[10]+'" max="90" style="width:100%;"></progress></td>'+
        '</tr>'+

    '</table></div>';
}

$(document).ready(function() {

    var table = $('#table').DataTable({
        dom: 'Bfrtip',
        buttons: [
            {
                text: 'Reporte Total',
                action: function ( e, dt, node, config ) {
                    location.replace(location.href+"reporte");
                }
            }
        ],
        "searching": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/radicado/lista_total_apoyo/"+ $('#id_region').val(),
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
                          return '<a href="radicado/'+row[0]+'" style="color:#004c99;" target="_blank">'+data+'</a>';
                },
                "orderable":      false,
            },
            { "data": 2,"orderable":false },
            { "data": 3,"orderable":false }
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