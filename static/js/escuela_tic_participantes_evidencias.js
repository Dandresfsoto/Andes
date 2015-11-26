function format ( d ) {
    // `d` is the original data object for the row
    return '<div class="table-responsive"><table class="table table-striped" style="padding-left:50px;color:black;">'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>DESCRIPCIÓN</b></h4></th>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2">'+d[4]+'</td>'+
        '</tr>'+

    '</table></div>';
}

$(document).ready(function() {

    var table = $('#table').DataTable({
        "searching": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/formador/listado_evidencias/"+ $('#id_region').val()+"/"+ $('#id_participante').val(),
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
                "orderable":false
            },
            {
                "data": 2,
                "orderable":false,
            },
            {
                "data": 3,
                "render": function ( data, type, row, meta ) {
                            var soporte = "";
                            if(row[3] == ""){
                                soporte = "";
                            }
                            else{
                                soporte = '<a href="/media/'+row[3]+'" target="_blank"><img src="/static/imagenes/pdf.png" height="40" class="center-block"><a>';
                            }
                          return soporte;
                },
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