function actualizar(){
    if(this.column != "") {
        this.content = '<td><a target="_blank" href="/media/' + this.column + '"><img src="/static/imagenes/pdf.png" height="48" width="48"></a></td>';
    }
}

function format ( d ) {
    // `d` is the original data object for the row
    var init = '<td><img src="/static/imagenes/pdf-gris.png" height="48" width="48"></td>';
    var imagen

    if(d[33] != ""){
        imagen = '<td rowspan="4" colspan="3" class="text-center"><img src="/media/'+d[33]+'" height="200"></td>'
    }
    else{
        imagen = '<td rowspan="4" colspan="3" class="text-center"><img src="/static/imagenes/user-unknown.png" height="200"></td>'
    }


    return '<div class="table-responsive"><table class="table table-striped" style="padding-left:50px;color:black;">'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>INFORMACIÓN</b></h4></th>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Cargo:</b> '+d[26]+'</td>'+
            '<td colspan="2"><b>Profesion:</b> '+d[34]+'</td>'+
            imagen+

        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Banco:</b> '+d[27]+'</td>'+
            '<td colspan="2"><b>Eps:</b> '+d[30]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Tipo de Cuenta:</b> '+d[28]+'</td>'+
            '<td colspan="2"><b>Pension:</b> '+d[31]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Numero de Cuenta:</b> '+d[29]+'</td>'+
            '<td colspan="2"><b>Arl:</b> '+d[32]+'</td>'+
        '</tr>'+

    '</table></div>';
}

$(document).ready(function() {

    var table = $('#table').DataTable({
        dom: 'Bfrtip',
        buttons: [
            {
                text: 'Nuevo Funcionario',
                action: function ( e, dt, node, config ) {
                    location.replace(location.href+"nuevo");
                }
            }
        ],
        "searching": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/funcionario/datatable/"+ $('#id_region').val(),
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
                "orderable":false,
            },
            {
                "data": 1,
                "orderable":false,
            },
            {
                "data": 2,
                "orderable":false,
            },
            {
                "data": 3,
                "orderable":false,
            },
            {
                "data": 20,
                "orderable":false,
            },
            {
                "data": 21,
                "orderable":false,
            },
        ],
        "order": [[0, 'asc']],
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