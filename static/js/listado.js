/* Formatting function for row details - modify as you need */
function format ( d ) {
    // `d` is the original data object for the row
    return '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;color:black;">'+
        '<tr>'+
            '<td>Email:</td>'+
            '<td>'+d[4]+'</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Telefono:</td>'+
            '<td>'+d[5]+'</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Area:</td>'+
            '<td>'+d[6]+'</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Grado:</td>'+
            '<td>'+d[7]+'</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Beneficiario:</td>'+
            '<td>'+d[8]+'</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Genero:</td>'+
            '<td>'+d[9]+'</td>'+
        '</tr>'
    '</table>';
}

$(document).ready(function() {

    var table = $('#table').DataTable({
        "searching": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/participantes/datatable/"+ $('#id_diplomado').val(),
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
            { "data": 0 },
            { "data": 1 },
            { "data": 2 },
            { "data": 3 }
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