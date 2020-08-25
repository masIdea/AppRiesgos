$('#form-actividad-plan').submit(function(e){
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
            if(data.valida){       
                limpiar_detalle_actividad();         
                $("#contenedor-check-actividad").html('<i class="flaticon2-check-mark" style="font-size: 35px;color: #2de02d;"></i>');

                setTimeout(() => {
                    $("#contenedor-check-actividad").html("");
                }, 1000);

                setTimeout(() => {
                    $("#modal_detalle_plan_actividad").modal("hide");
                    detallePlanRespuesta("1", $("#id-txt-id-plan").val());
                }, 1500);

                


            }else{
                limpiar_detalle_actividad();
                $("#contenedor-check-actividad").html('<i class="flaticon2-cross" style="font-size: 35px;color: red;"></i>');
                alert(data.mensaje);
                setTimeout(() => {
                    $("#contenedor-check-actividad").html("");
                }, 1000);

                setTimeout(() => {
                    $("#modal_detalle_plan_actividad").modal("hide");
                }, 1500);


            }
            
            
        },
    });
});
    

$("#eliminar-actividad-plan").click(function(){
    cfm = confirm("Desea eliminar la actividad seleccionada?");
    if(cfm == true){
        id_actividad = $("#id-txt-id-actividad").val();
        $.ajax({
            url:"eliminar-actividad",
            type:"GET",
            dateType:"json",
            data:{"id_actividad":id_actividad},
            success:function(data){
                alert(data.info);
                detallePlanRespuesta("1", $("#id-txt-id-plan").val());
                $("#editar-actividad-plan").attr("disabled", true);
                $("#eliminar-actividad-plan").attr("disabled", true);
            }, error:function(err){
                console.error(err);            
                alert("Ha ocurrido un error al eliminar el registro.")
            }
        });
    }

})