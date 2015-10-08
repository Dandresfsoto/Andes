function format ( d ) {
    // `d` is the original data object for the row
    var excel_acceso
    var soporte_acceso
    var excel_formacion
    var soporte_formacion

    if(d[4] != ""){
        excel_acceso = '<td colspan="2"><b>Archivo: </b><a href="/media/'+d[4]+'" style="color:#004c99;" target="_blank">Informe</a></td>'
    }
    else{
        excel_acceso = '<td colspan="2"><b>Archivo:</b> Sin archivo</td>'
    }

    if(d[5] != ""){
        soporte_acceso = '<td colspan="2"><b>Soporte: </b><a href="/media/'+d[5]+'" style="color:#004c99;" target="_blank">Informe</a></td>'
    }
    else{
        soporte_acceso = '<td colspan="2"><b>Soporte:</b> Sin soporte</td>'
    }

    if(d[6] != ""){
        excel_formacion = '<td colspan="2"><b>Archivo: </b><a href="/media/'+d[6]+'" style="color:#004c99;" target="_blank">Informe</a></td>'
    }
    else{
        excel_formacion = '<td colspan="2"><b>Archivo:</b> Sin archivo</td>'
    }

    if(d[7] != ""){
        soporte_formacion = '<td colspan="2"><b>Soporte: </b><a href="/media/'+d[7]+'" style="color:#004c99;" target="_blank">Informe</a></td>'
    }
    else{
        soporte_formacion = '<td colspan="2"><b>Soporte:</b> Sin soporte</td>'
    }

    return '<div class="table-responsive"><table class="table table-striped" style="padding-left:50px;color:black;">'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>INFORMACIÓN</b></h4></th>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Eje:</b> Acceso</td>'+
            excel_acceso+
            soporte_acceso+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Eje:</b> Formación</td>'+
            excel_formacion+
            soporte_formacion+
        '</tr>'+

    '</table></div>';
}

$(document).ready(function() {

    var table = $('#table').DataTable({
        dom: 'Bfrtip',
        buttons: [
            {
                text: 'Nuevo Informe',
                action: function ( e, dt, node, config ) {
                    location.replace(location.href+"nuevo");
                }
            }
        ],
        "searching": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/region/"+ $('#id_region').val()+"/andes/administrativo/cpe/informes/listado/",
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
                "render": function ( data, type, row, meta ) {
                          return '<a href="actualizar/'+row[0]+'" style="color:#004c99;">'+data+'</a>';
                },
                "orderable":false,
            },
            {
                "data": 3,
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