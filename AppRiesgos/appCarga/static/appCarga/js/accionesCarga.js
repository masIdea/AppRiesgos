$('#form-carga-datos').submit(function(e){
    e.preventDefault();
    $form = $(this)
    var formData = new FormData(this);
    $.ajax({
        url: $(this).attr('action'),
        type: $(this).attr('method'),
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        beforeSend:function(){            

        },
        success: function (data) {
            console.log(data);
            if(data){
                alert("Datos Cargados Exitosamente.");
                location.reload();
            }else{
                alert("Ha ocurrido un error al cargar el archivo, asegure que los datos sean validos.");
            }
        }, error:function(err){
            alert("Ha ocurrido un error al cargar el archivo, asegurese de que el archivo corresponde a la opción seleccionada.");
            console.error(err);
        }
    });
});