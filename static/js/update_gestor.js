$(document).ready(function() {
    $('input[type="file"]').ezdz({
        text: 'Seleccionar archivo'
    });

    setInterval(function(){
        if($('#progressBar').prop("hidden")){
            var porcentaje = $('#progressBar').val();
            $('#porcentaje').text(porcentaje.toFixed(2)+'%');
        }
    }, 50);
});