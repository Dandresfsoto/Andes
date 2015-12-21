function format ( d ) {
    // `d` is the original data object for the row
    var actividades
    var soporte


    for (i = 0; i < d[4].length; i++) {
        if(d[4][i][6] != ""){
            soporte = '<td rowspan="1" colspan="1" class="text-center"><a href="/media/'+d[4][i][6]+'"><img src="/static/imagenes/pdf.png" height="40"></a></td>'
        }
        else{
            soporte = '<td rowspan="1" colspan="1" class="text-center"><img src="/static/imagenes/pdf-gris.png" height="40"></td>'
        }
        actividades += '<tr>' +
            '<td colspan="1"><b>Ciclo:</b> '+ d[4][i][0]+'</td>+' +
            '<td colspan="1"><b>Actividad:</b> '+ d[4][i][3]+' - '+d[4][i][4]+'</td>'+
            '<td colspan="1"><b>Valor:</b> $'+ d[4][i][5].toLocaleString('es-CO')+'</td>'+
            '<td colspan="1"><b>Usuario:</b> '+ d[4][i][7]+'</td>'+
            '<td colspan="1"><b>Fecha:</b> '+ d[4][i][8]+'</td>'+
             soporte+
            '</tr>';
    }


    return '<div class="table-responsive"><table class="table table-striped" style="padding-left:50px;color:black;">'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>ACTIVIDADES</b></h4></th>'+
        '</tr>'+

        '<tr>'+
            actividades+
        '</tr>'+


    '</table></div>';
}

$(document).ready(function() {

    var table = $('#table').DataTable({
        dom: 'Bfrtip',
        buttons: [
            {
                text: 'Reporte',
                action: function ( e, dt, node, config ) {
                    location.replace(location.href+"reporte");
                }
            },
            {
                text: 'Enviar a Email',
                action: function ( e, dt, node, config ) {
                    location.replace(location.href+"email");
                }
            }
        ],
        "searching": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/gestor/corte_apoyo/"+ $('#id_region').val()+"/"+ $('#id_corte').val()+"/"+ $('#id_gestor').val(),
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
                "data": 0,
                "orderable":false,
            },
            {
                "data": 1,
                "orderable":false,
            },
            {
                "data": 2,
                "orderable":false,
            },
            {
                "data": 3,
                "orderable":false,
            },
        ],
        "order": [[0, 'asc']],
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