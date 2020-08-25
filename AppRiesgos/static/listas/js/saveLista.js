$('#form-listas').submit(function(e){
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
            if(data.estado){
                alert(data.msg);
                location.reload();
                setTimeout(() => {
                    registros_listas();    

                }, 3000);
                
            }else{
                alert(data.msg);
                $("#id-nueva-lista").val("");
                $("#id-tipo-lista").focus().select();
            }                        
        }, error:function(err){
            alert("Ha ocurrido un error al almacenar los datos.");
            console.error(err);
        }
    });
});
    