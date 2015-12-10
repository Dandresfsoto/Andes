function actualizar(){
    if(this.column != "") {
        this.content = '<td><a target="_blank" href="/media/' + this.column + '"><img src="/static/imagenes/pdf.png" height="48" width="48"></a></td>';
    }
}

function format ( d ) {
    // `d` is the original data object for the row
    var init = '<td><img src="/static/imagenes/pdf-gris.png" height="48" width="48"></td>';
    var imagen

    if(d[13] != ""){
        imagen = '<td rowspan="4" colspan="3" class="text-center"><img src="/media/'+d[13]+'" height="200"></td>'
    }
    else{
        imagen = '<td rowspan="4" colspan="3" class="text-center"><img src="/static/imagenes/user-unknown.png" height="200"></td>'
    }

    var hv = {content: init,
    actualizar: actualizar,
    column: d[14]};

    var certificacion = {content: init,
    actualizar: actualizar,
    column: d[15]};

    var rut = {content: init,
    actualizar: actualizar,
    column: d[16]};

    var contrato = {content: init,
    actualizar: actualizar,
    column: d[17]};

    var fotocopia_cedula = {content: init,
    actualizar: actualizar,
    column: d[18]};

    var antecedentes_judiciales = {content: init,
    actualizar: actualizar,
    column: d[19]};

    var antecedentes_contraloria = {content: init,
    actualizar: actualizar,
    column: d[20]};

    var enero = {content: init,
    actualizar: actualizar,
    column: d[21]};

    var febrero = {content: init,
    actualizar: actualizar,
    column: d[22]};

    var marzo = {content: init,
    actualizar: actualizar,
    column: d[23]};

    var abril = {content: init,
    actualizar: actualizar,
    column: d[24]};

    var mayo = {content: init,
    actualizar: actualizar,
    column: d[25]};

    var junio = {content: init,
    actualizar: actualizar,
    column: d[26]};

    var julio = {content: init,
    actualizar: actualizar,
    column: d[27]};

    var agosto = {content: init,
    actualizar: actualizar,
    column: d[28]};

    var septiembre = {content: init,
    actualizar: actualizar,
    column: d[29]};

    var octubre = {content: init,
    actualizar: actualizar,
    column: d[30]};

    var noviembre = {content: init,
    actualizar: actualizar,
    column: d[31]};

    var diciembre = {content: init,
    actualizar: actualizar,
    column: d[32]};



    hv.actualizar();
    certificacion.actualizar();
    rut.actualizar();
    contrato.actualizar();
    enero.actualizar();
    febrero.actualizar();
    marzo.actualizar();
    abril.actualizar();
    mayo.actualizar();
    junio.actualizar();
    julio.actualizar();
    agosto.actualizar();
    septiembre.actualizar();
    octubre.actualizar();
    noviembre.actualizar();
    diciembre.actualizar();
    fotocopia_cedula.actualizar();
    antecedentes_judiciales.actualizar();
    antecedentes_contraloria.actualizar();


    return '<div class="table-responsive"><table class="table table-striped" style="padding-left:50px;color:black;">'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>INFORMACIÓN</b></h4></th>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Cargo:</b> '+d[5]+'</td>'+
            '<td colspan="2"><b>Profesion:</b> '+d[6]+'</td>'+
            imagen+

        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Banco:</b> '+d[7]+'</td>'+
            '<td colspan="2"><b>Eps:</b> '+d[10]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Tipo de Cuenta:</b> '+d[8]+'</td>'+
            '<td colspan="2"><b>Pension:</b> '+d[11]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<td colspan="2"><b>Numero de Cuenta:</b> '+d[9]+'</td>'+
            '<td colspan="2"><b>Arl:</b> '+d[12]+'</td>'+
        '</tr>'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>SOPORTES</b></h4></th>'+
        '</tr>'+
        '<tr>'+
            '<td class="text-center">Hoja de Vida:</td>'+
            hv.content+
            '<td class="text-center">Certificación Bancaria:</td>'+
            certificacion.content+
            '<td class="text-center">Rut:</td>'+
            rut.content+
            '<td class="text-center">Contrato:</td>'+
            contrato.content+
        '</tr>'+

        '<tr>'+
            '<td class="text-center">Fotocopia Cedula:</td>'+
            fotocopia_cedula.content+
            '<td class="text-center">Antecedentes Judiciales:</td>'+
            antecedentes_judiciales.content+
            '<td class="text-center">Contraloria:</td>'+
            antecedentes_contraloria.content+
        '</tr>'+

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b>SEGURIDAD SOCIAL</b></h4></th>'+
        '</tr>'+

        '<tr>'+
            '<td class="text-center">Enero:</td>'+
            enero.content+
            '<td class="text-center">Febrero:</td>'+
            febrero.content+
            '<td class="text-center">Marzo:</td>'+
            marzo.content+
            '<td class="text-center">Abril:</td>'+
            abril.content+
        '</tr>'+

        '<tr>'+
            '<td class="text-center">Mayo:</td>'+
            mayo.content+
            '<td class="text-center">Junio:</td>'+
            junio.content+
            '<td class="text-center">Julio:</td>'+
            julio.content+
            '<td class="text-center">Agosto:</td>'+
            agosto.content+
        '</tr>'+

        '<tr>'+
            '<td class="text-center">Septiembre:</td>'+
            septiembre.content+
            '<td class="text-center">Octubre:</td>'+
            octubre.content+
            '<td class="text-center">Noviembre:</td>'+
            noviembre.content+
            '<td class="text-center">Diciembre:</td>'+
            diciembre.content+
        '</tr>'+
    '</table></div>';
}

$(document).ready(function() {

    var table = $('#table').DataTable({
        dom: 'Bfrtip',
        buttons: [
            {
                text: 'Hojas de Vida',
                action: function ( e, dt, node, config ) {
                    location.replace(location.href+"hv/"+$('#id_tipo').val());
                }
            },
            {
                text: 'Contratos',
                action: function ( e, dt, node, config ) {
                    location.replace(location.href+"contratos/"+$('#id_tipo').val());
                }
            },
            {
                text: 'Ruteo',
                action: function ( e, dt, node, config ) {
                    location.replace(location.href+"ruteo/"+$('#id_tipo').val());
                }
            }
        ],
        "searching": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/gestor/datatable/"+ $('#id_region').val()+"/"+$('#id_tipo').val(),
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
                "data": 4,
                "orderable":false,
            },
            {
                "data": 33,
                "orderable":false,
            },
            {
                "data": 34,
                "orderable":false,
            },
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