var usuarios = {};
var username = "";


if(localStorage.getItem("user") != null){
    $("#profile").attr('src',localStorage.getItem("user"));
}


$("#iniciar").click(function(){
    username = $("#idUsername").val();
    if(usuarios[username] != undefined){
        localStorage.setItem("user",usuarios[username]);
    }
});

$.ajax({
    url: '/usuarios/api/users_profile/',
    type: 'GET',
}).done(function( data ){
    data2 = {};
    for (index in data.results) {
                data2[data.results[index].usuario['username']] = data.results[index].imagen;
            }
    usuarios = data2;
});