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
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                exportOptions: {
                    columns: [1, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9,10]
                },
                title: 'Participantes',
            }
        ],
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
            { "data": 3 },
            { "data": 4, "visible": false, "title": "Email"},
            { "data": 5, "visible": false, "title": "Telefono"},
            { "data": 6, "visible": false, "title": "Area"},
            { "data": 7, "visible": false, "title": "Grado"},
            { "data": 8, "visible": false, "title": "Beneficiario"},
            { "data": 9, "visible": false, "title": "Genero"}
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