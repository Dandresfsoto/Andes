function format ( d ) {
    // `d` is the original data object for the row
    return '<div class="table-responsive"><table class="table table-striped" style="padding-left:50px;color:black;">'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>MENSAJE</b></h4></th>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2">'+d[7]+'</td>'+
        '</tr>'+

    '</table></div>';
}

$(document).ready(function() {

    var table = $('#table').DataTable({
        dom: 'Bfrtip',
        buttons: [
            {
                text: 'Nueva',
                action: function ( e, dt, node, config ) {
                    location.replace(location.href+"nuevo/");
                }
            }
        ],
        "searching": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/pqr/listado_llamadas/"+ $('#id_region').val(),
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
                "render": function ( data, type, row, meta ) {
                          return '<a href="'+row[0]+'" style="color:#004c99;">MAP-'+data+'</a>';
                },
                "orderable":false,
            },
            {
                "data": 1,
                "render": function ( data, type, row, meta ) {
                          return data.replace('T',' ').replace('Z','');
                },
                "orderable":false,
            },
            {
                "data": 3,
                "orderable":false,
            },
            {
                "data": 4,
                "orderable":false,
            },
            {
                "data": 5,
                "orderable":false,
            },
            {
                "data": 6,
                "orderable":false,
            }
        ]
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