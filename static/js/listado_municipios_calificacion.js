function format ( d ) {
    // `d` is the original data object for the row
    return '<div class="table-responsive"><table class="table table-striped" style="padding-left:50px;color:black;">'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>INFORMACIÓN</b></h4></th>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Codigo municipio:</b> '+d[3]+'</td>'+
            '<td colspan="2"><b>Codigo departamento:</b> '+d[4]+'</td>'+

        '</tr>'+


         '<tr>'+
            '<td colspan="2"><b>Actividades ejecutadas:</b> '+d[5]+'</td>'+
            '<td colspan="2"><b>Actividades pendientes:</b> '+d[6]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Actividades quincena:</b> '+d[7]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="4"><b>Progreso: </b>'+d[8]+'%<progress value="'+d[8]+'" max="100" style="width:100%;"></progress></td>'+
        '</tr>'+

    '</table></div>';
}

$(document).ready(function() {

    var table = $('#table').DataTable({
        "searching": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/municipio/lista/"+ $('#id_region').val()+"/"+$('#id_gestor').val(),
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
                          return '<a href="municipio/'+row[0]+'" style="color:#004c99;">'+data+'</a>';
                },
                "orderable":false
            },
            { "data": 2,"orderable":false}
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