function format ( d ) {
    // `d` is the original data object for the row
    var uno, uno_calificar, dos, dos_calificar, tres, tres_calificar, cuatro, cuatro_calificar, cinco, cinco_calificar

    if(d[7][0] == ""){
        uno = 'Sin soporte'
        uno_calificar = '<td colspan="4"><b>Calificar:</b> Primero debes cargar el Soporte</td>'
    }
    else{
        uno = '<a href="/media/'+d[7][0]+'" style="color:#004c99;">Soporte</a>'
        uno_calificar = '<td colspan="4"><b>Calificar: </b><a href="uno/'+d[8][0]+'" style="color:#004c99;">Click aqui</a></td>'
    }

    if(d[7][1] == ""){
        dos = 'Sin soporte'
        dos_calificar = '<td colspan="4"><b>Calificar:</b> Primero debes cargar el Soporte</td>'
    }
    else{
        dos = '<a href="/media/'+d[7][1]+'">Soporte</a>'
    }

    if(d[7][2] == ""){
        tres = 'Sin soporte'
        tres_calificar = '<td colspan="4"><b>Calificar:</b> Primero debes cargar el Soporte</td>'
    }
    else{
        tres = '<a href="/media/'+d[7][2]+'" style="color:#004c99;">Soporte</a>'
    }

    if(d[7][3] == ""){
        cuatro = 'Sin soporte'
        cuatro_calificar = '<td colspan="4"><b>Calificar:</b> Primero debes cargar el Soporte</td>'
    }
    else{
        cuatro = '<a href="/media/'+d[7][3]+'" style="color:#004c99;">Soporte</a>'
    }

    if(d[7][4] == ""){
        cinco = 'Sin soporte'
        cinco_calificar = '<td colspan="4"><b>Calificar:</b> Primero debes cargar el Soporte</td>'
    }
    else{
        cinco = '<a href="/media/'+d[7][4]+'">Soporte</a>'
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
            '<td colspan="4"><b>Cantidad de Participantes:</b> '+d[6]+'</td>'+
            '<td colspan="4"><b>Actualizar Soportes:</b> <a href = "soportes/'+d[0]+' " style="color:#004c99;">Click aqui</a></td>'+
        '</tr>'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>Conformación escuela TIC</b></h4></th>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="4"><b>Acta de reunión:</b> '+uno+'</td>'+
            uno_calificar+
        '</tr>'+

        '</tr>'+
            '<td colspan="4"><b>Registro fotográfico:</b> '+dos+'</td>'+
            dos_calificar+
        '</tr>'+

        '<tr>'+
            '<td colspan="4"><b>Pantallazo de imagen en el grupo de Facebook ESCUELA TIC FAMILIA:</b> '+tres+'</td>'+
            tres_calificar+
        '</tr>'+

        '<tr>'+
            '<td colspan="4"><b>Pantallazo Hashtag a #ESCUELATICFAMILIA:</b> '+cuatro+'</td>'+
            cuatro_calificar+
        '</tr>'+

        '<tr>'+
            '<td colspan="4"><b>Mensaje en el grupo de Facebook ESCUELA TIC FAMILIA:</b> '+cinco+'</td>'+
            cinco_calificar+
        '</tr>'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>Sesión 1</b></h4></th>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="4"><b>Listado de Asistencia:</b> '+d[4]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="4"><b>Registro fotográfico del mural de los sueños:</b> '+d[5]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="4"><b>Publicación de una imagen o frase En TIC Confio y Redvolución:</b> '+d[4]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="4"><b>Pantallazo Hashtag a #ESCUELATICFAMILIA:</b> '+d[5]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>Sesión 2</b></h4></th>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="4"><b>Lista de asistencia:</b> '+d[4]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="4"><b>Registro fotográfico:</b> '+d[5]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="4"><b>Evidencia del Proyecto Familiar:</b> '+d[4]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="4"><b>Publicación de una imagen o frase en @compuparaeducar:</b> '+d[5]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="8"><b>Entrega de las constancias digitales:</b> '+d[4]+'</td>'+
        '</tr>'+


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