function format ( d ) {
    var actividad = "";

    for(i=0;i<d[7].length;i++){
        var entregables = "";
        for(j=0;j<d[7][i].informacion.length;j++){
            if(d[7][i].informacion[j].link_soporte != "") {
                entregables += '<tr>' +
                    '<td colspan="4">' + d[7][i].informacion[j].entregable + ': <a href="actualizar/'+d[7][i].informacion[j].id_soporte+'" style="color:#004c99;">Actualizar</a> - <a href="asignar/'+d[7][i].informacion[j].id_soporte+'" style="color:#004c99;">Asignar</a></td>' +
                    '<td colspan="2"><a href="/media/'+d[7][i].informacion[j].link_soporte+'" target="_blank"><img src="/static/imagenes/pdf.png" height="40"><a></td>' +
                    '<td colspan="2">Participantes: '+d[7][i].informacion[j].cantidad+'</td>' +
                    '</tr>';
            }
            else{
                entregables += '<tr>' +
                    '<td colspan="4">' + d[7][i].informacion[j].entregable + ': <a href="actualizar/'+d[7][i].informacion[j].id_soporte+'" style="color:#004c99;">Actualizar</a> - <a href="asignar/'+d[7][i].informacion[j].id_soporte+'" style="color:#004c99;">Asignar</a></td>' +
                    '<td colspan="2"><img src="/static/imagenes/pdf-gris.png" height="40"></td>' +
                    '<td colspan="2">Participantes: '+d[7][i].informacion[j].cantidad+'</td>' +
                    '</tr>';
            }
        }
        actividad += '<tr><th colspan="8" class="text-center"><h4><b>'+d[7][i].nombre_actividad+'</b><h4></th></tr>'+entregables;
    }

    return '<div class="table-responsive"><table class="table table-striped" style="padding-left:50px;color:black;">'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>INFORMACIÓN</b></h4></th>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="4"><b>Dirección:</b> '+d[4]+'</td>'+
            '<td colspan="4"><b>Horario:</b> '+d[5]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="8"><b>Cantidad de Participantes:</b> '+d[6]+'</td>'+
        '</tr>'+
            actividad+

    '</table></div>';
}
$(document).ready(function() {

    var table = $('#table').DataTable({
        dom: 'Bfrtip',
        buttons: [
            {
                text: 'Nuevo Grupo',
                action: function ( e, dt, node, config ) {
                    location.replace(location.href+"nuevo");
                }
            }
        ],
        "searching": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/formador/grupo/"+ $('#id_region').val()+"/"+ $('#id_formador').val(),
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
                          return '<a href="grupo/'+row[0]+'" style="color:#004c99;">'+data+'</a>';
                },
                "orderable":false
            },
            {
                "data": 2,
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