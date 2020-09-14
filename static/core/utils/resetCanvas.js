var resetCanvas = function(idCanvas, idParentDiv){
    $('#'+idCanvas).remove();
    $('#'+idParentDiv).append('<canvas id="'+idCanvas+'"><canvas>');
}