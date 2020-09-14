$("#btn_agregar_plan").click(function(){    
    $("#id-estrategia-plan").val("");
    $("#id-descripcion-plan").val("");
    $("#id-dueno-plan").val("");
    $("#id-cargo-dueno-plan").val("");
    $("#id-trigger-plan").val("");
    $("#modal_creacion_plan").modal("show");
    $("#id-edit-plan").val(0);
    $("#btn_crear_plan_respuesta").prop("value", "Crear Plan de Respuesta");
});

$('#form-plan-respuesta').submit(function(e){
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
            console.log(data.valida);
            if(data.valida){
                limpiar_detalle_plan();
                detallePlanRespuesta("1", $("#id-txt-id-plan").val());
                $("#contenedor-check-plan-respuesta").html('<i class="flaticon2-check-mark" style="font-size: 35px;color: #2de02d;"></i>');
                setTimeout(() => {
                    $("#contenedor-check-plan-respuesta").html("");                    
                }, 1000);

                setTimeout(() => {
                    $("#modal_creacion_plan").modal("hide");
                }, 1500);
                getDetallePlanes();
                detalle_riesgo($("#id_riesgo_plan").val());

            }else{
                limpiar_detalle_plan();
                $("#contenedor-check-plan-respuesta").html('<i class="flaticon2-cross" style="font-size: 35px;color: red;"></i>');
                setTimeout(() => {
                    $("#contenedor-check-plan-respuesta").html("");                    
                }, 1000);

                setTimeout(() => {
                    $("#modal_creacion_plan").modal("hide");
                }, 1500);
            }
            
            
        },
    });
});
    


$("#editar-detalle-plan").click(function(){
    $("#btn_crear_plan_respuesta").prop("value", "Modificar Plan");
    $("#id-edit-plan").val(1);
    $("#id-estrategia-plan").val($("#estrategia_plan").html());
    $("#id-descripcion-plan").val($("#descripcion_plan").html());
    $("#id-dueno-plan").val($("#dueno_plan").html());
    $("#id-cargo-dueno-plan").val($("#cargo_dueno_plan").html());
    $("#id-trigger-plan").val($("#trigger_plan").html());

    $("#modal_creacion_plan").modal("show");
});


$("#btn_eliminar_plan").click(function(){
    cfm = confirm("Esta seguro que desea eliminar el plan seleccionado?");
    if(cfm == true){
        var id_plan = $("#id-plan").val()
        $.ajax({
            url:"eliminar-plan",
            type:"GET",
            dataType:"json",
            data:{"id_plan":id_plan},
            success:function(data){
                if(data){
                    alert("Eliminado correctamente.");
                    $("#editar-detalle-plan").attr("disabled", true);
                    $("#btn_eliminar_plan").attr("disabled", true);
                    detalle_riesgo($("#id_riesgo_plan").val());
                }
            }, error:function(err){
                alert("Ha ocurrido un error al eliminar el plan seleccionado.");
                console.error(err);
            }
        });
    }

})