$('#form-control').submit(function(e){
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
        success: function (response) {
            controles_riesgo();
            limpiar_form();
            
        },
    });
});


