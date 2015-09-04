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
        imagen = '<td rowspan="4" colspan="3" class="text-center"><a href="actualizar/foto/'+d[22]+'/"><img src="/media/'+d[33]+'" height="200"></a></td>'
    }
    else{
        imagen = '<td rowspan="4" colspan="3" class="text-center"><a href="actualizar/foto/'+d[22]+'/"><img src="/static/imagenes/user-unknown.png" height="200"></a></td>'
    }

    var hv = {content: init,
    actualizar: actualizar,
    column: d[4]};

    var certificacion = {content: init,
    actualizar: actualizar,
    column: d[5]};

    var rut = {content: init,
    actualizar: actualizar,
    column: d[6]};

    var contrato = {content: init,
    actualizar: actualizar,
    column: d[7]};

    var fotocopia_cedula = {content: init,
    actualizar: actualizar,
    column: d[23]};

    var antecedentes_judiciales = {content: init,
    actualizar: actualizar,
    column: d[24]};

    var antecedentes_contraloria = {content: init,
    actualizar: actualizar,
    column: d[25]};

    var enero = {content: init,
    actualizar: actualizar,
    column: d[8]};

    var febrero = {content: init,
    actualizar: actualizar,
    column: d[9]};

    var marzo = {content: init,
    actualizar: actualizar,
    column: d[10]};

    var abril = {content: init,
    actualizar: actualizar,
    column: d[11]};

    var mayo = {content: init,
    actualizar: actualizar,
    column: d[12]};

    var junio = {content: init,
    actualizar: actualizar,
    column: d[13]};

    var julio = {content: init,
    actualizar: actualizar,
    column: d[14]};

    var agosto = {content: init,
    actualizar: actualizar,
    column: d[15]};

    var septiembre = {content: init,
    actualizar: actualizar,
    column: d[16]};

    var octubre = {content: init,
    actualizar: actualizar,
    column: d[17]};

    var noviembre = {content: init,
    actualizar: actualizar,
    column: d[18]};

    var diciembre = {content: init,
    actualizar: actualizar,
    column: d[19]};



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
            '<th colspan="8" class="text-center"><h4><b><a href="actualizar/informacion/'+d[22]+'/" style="color:#004c99;">INFORMACIÓN<a></b></h4></th>'+
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

        '<tr>'+
            '<th colspan="8" class="text-center"><h4><b><a href="actualizar/soportes/'+d[22]+'/" style="color:#004c99;">SOPORTES<a></b></h4></th>'+
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
            '<th colspan="8" class="text-center"><h4><b><a href="actualizar/seguro/'+d[22]+'/" style="color:#004c99;">SEGURIDAD SOCIAL</b></h4></th>'+
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
        "searching": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/funcionario/datatable_cpe/"+ $('#id_region').val()+"/"+$('#id_eje').val(),
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