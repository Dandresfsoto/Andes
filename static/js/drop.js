$(document).ready(function() {
    $('input[type="file"]').ezdz({
        text: 'Seleccionar archivo',
        previewImage: false,
    });

    setInterval(function(){
        if($('#progressBar').prop("hidden") == false ){
            var porcentaje = $('#progressBar').val();
            $('#porcentaje').text(porcentaje.toFixed(2)+'%');
        }
    }, 50);
});