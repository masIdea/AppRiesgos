var goTo = function(id_contenido){
    var jump = "#"+id_contenido
    var new_position = $(jump).offset();
    $('html, body').stop().animate({ scrollTop: new_position.top }, 400);
    //e.preventDefault();
}