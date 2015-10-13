function format ( d ) {
    // `d` is the original data object for the row
    var mes = '';
    var contenido = [];

    for(i=0;i<d[4].length;i++) {
        contenido[i]='';
        for (j = 0; j < d[5].length; j++) {
            if(d[4][i]==d[5][j][0]) {
                contenido[i] += '<tr><td colspan="4"><b>'+d[5][j][1]+'</b>: <a href="/media/'+d[5][j][2]+'" style="color:#004c99;" target="_blank"> Soporte</a>'+
                    '</td></tr>';
            }
        }
    }

    for(i=0;i<d[4].length;i++){
        mes += '<tr><th colspan="8" class="text-center"><h4><b>'+d[4][i]+'</b></h4></th></tr>'+contenido[i];
    }

    return '<div class="table-responsive"><table class="table table-striped" style="padding-left:50px;color:black;">'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>OBLIGACIÓN '+d[2]+'</b></h4></th>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="8">'+d[3]+'</td>'+
        '</tr>'+
        mes+
    '</table></div>';
}

$(document).ready(function() {

    var table = $('#table').DataTable({
        "searching": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/region/"+ $('#id_region').val()+"/andes/administrativo/cpe/obligaciones/listado/",
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
                "data": 2,
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