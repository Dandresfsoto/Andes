function change(){
        $('#nameCategoryChange').text( $('#nameCategory').val() );
    }
$(document).ready(function(){

    $.background = $(" #colorCategory ").val();
    $.icono = $(" #id_icon ").val();
    $(" .categoryPreview ").css('background-color', $.background);
    $('#nameCategoryChange').text( $('#nameCategory').val() );
    $('.icono').removeClass("fa-question-circle");

    $('.icono').addClass($.icono);

    $(" #colorCategory ").change( function(){
        $.background = $(" #colorCategory ").val();
        $(" .categoryPreview ").css('background-color', $.background);
    });


    $('.icp-auto').iconpicker();

    $('.icp').on('iconpickerSelected', function(e) {
                    $('.icono').get(0).className = 'icono ' +
                            e.iconpickerInstance.options.fullClassFormatter(e.iconpickerValue)+' fa-5x';
                });

    $(' #nameCategory ').keyup(function(){
       $('#nameCategoryChange').text( $(this).val() );
    });


});