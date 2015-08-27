/* Formatting function for row details - modify as you need */
function format ( d ) {
    // `d` is the original data object for the row
    return '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;color:black;">'+
        '<tr>'+
            '<td>Nombre del Proyecto:</td>'+
            '<td>'+d[2]+'</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Definicion del Problema:</td>'+
            '<td>'+d[3]+'</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Area:</td>'+
            '<td>'+d[4]+'</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Competencia:</td>'+
            '<td>'+d[5]+'</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Grupo Poblacional:</td>'+
            '<td>'+d[6]+'</td>'+
        '</tr>'+
            '<tr>'+
            '<td>Archivo:</td>'+
            '<td>'+'<p><b><a class="link-tabla" href="/media/'+d[7]+'" target="_blank">Link</a></b></p>'+'</td>'+
        '</tr>'
    '</table>';
}

$(document).ready(function() {

    var table = $('#table').DataTable({
        "searching": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/participantes/proyecto/"+ $('#id_diplomado').val(),
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
            { "data": 1 }
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