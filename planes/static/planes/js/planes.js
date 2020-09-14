var detalle_riesgo = function(id_riesgo){
    limpiar_plan();
    limpiar_detalle_plan();
    $("#id-riesgo-control-objetivo").val(id_riesgo);

    $.ajax({
        url:"trae-detalle-riesgo",
        type:"GET",
        dataType:"json",
        data:{"id_riesgo":id_riesgo},
        beforeSend:function(){
            // Loading ...
        },
        success:function(data){
            $("#descripcion_riesgo").html(data.detalle_riesgo[0].riesgo);
            $("#direccion_riesgo").html(data.detalle_riesgo[0].direccion);
            $("#estado_riesgo").html(data.detalle_riesgo[0].estado);
            $("#fase_riesgo").html(data.detalle_riesgo[0].fasedelriesgo);
            $("#proyecto_riesgo").html(data.detalle_riesgo[0].proyecto);
            $("#dueno_riesgo").html(data.detalle_riesgo[0].dueño);

            $("#id_riesgo_plan").val(id_riesgo);
            getDetallePlanes();

            
            /*
            cuerpo_causas_riesgo_actividad
            cuerpo_consecuencias_riesgo_actividad
             */
            var tbody_causas = "";
            if(data.causas.length>0){
                for(var i = 0; i<data.causas.length; i++){
                    tbody_causas += "<tr>";
                    tbody_causas += "<td>"+data.causas[i].CAUSA+"</td>"
                    tbody_causas += "</tr>";
                }
            }else{
                tbody_causas = "Riesgo No Posee Causas.";
            }
            $("#cuerpo_causas_riesgo_actividad").html(tbody_causas);

            var tbody_consecuencias = "";
            if(data.consecuencias.length>0){
                for(var j = 0; j<data.consecuencias.length; j++){
                    tbody_consecuencias += "<tr>";
                    tbody_consecuencias += "<td>"+data.consecuencias[j].CONSECUENCIA+"</td>"
                    tbody_consecuencias += "</tr>";
                }
            }else{
                tbody_consecuencias = "Riesgo No Posee Consecuencias.";
            }
            $("#cuerpo_consecuencias_riesgo_actividad").html(tbody_consecuencias);

            $("#btn_agregar_plan").attr("disabled", false);

            goTo("id-div-creacion-plan-accion");            

            

        }, error:function(err){
            console.error(err);
        }
    });
}



$( ".input-objetivo, #txt_obj_probabilidad" ).keypress(function() {
    $(".r-circle").css("display", "none");

      setTimeout(() => {
        var probabilidad = $("#txt_obj_probabilidad").val();
        if(probabilidad > 0 || probabilidad <= 7 || probabilidad != ""){
        arreglo_valores_objetivos = []      
          $( ".input-objetivo" ).each(function( index ) {
              if($(this).val() == ""){
                valor = 0;
              }else{
                valor = $(this).val();
              }
              if(valor<=7 || valor<0){
                arreglo_valores_objetivos.push(parseInt(valor));
              }else{
                $("#"+this.id).val("");
              }
            });            
            var max = Math.max.apply(null, arreglo_valores_objetivos);                      
            $("#txt_obj_impacto").val(max);

            $("#obj_label_"+max+"_"+probabilidad).css("display","block");
          }
      }, 100);
    
});


$( ".input-objetivo, #txt_obj_probabilidad" ).keypress(function() {
    arreglo_valores_objetivos = []      
              
        setTimeout(() => {
            $( ".input-objetivo" ).each(function( index ) {            
                if($(this).val() == ""){
                valor = 0;
                }else{
                valor = $(this).val();
                }
                if(valor<=7 || valor<0){
                    arreglo_valores_objetivos.push(parseInt(valor));
                }else{
                $("#"+this.id).val("");
                }
            });            
            var impacto = Math.max.apply(null, arreglo_valores_objetivos);  
            var probabilidad = $("#txt_obj_probabilidad").val();
            $.ajax({
                url:'../controles-riesgo/magnitud-nivel',
                type:"GET",
                dataType:"json",
                data:{'probabilidad':probabilidad, 'impacto':impacto},
                success:function(data){                    
                    $("#txt_obj_magnitud").val(data.magnitud);
                    $("#txt_obj_nivel").val(data.nivel);
                }, error:function(err){
                    console.error(err);
                }
            })
        }, 1000);
        });


var formulario_objetivo = $('#id-form-riesgos-objetivo');
var accion = function(){
    formulario_objetivo.submit();
}
formulario_objetivo.submit(function () {
    $("#btn-guardar-riesgo-objetivo")  .attr("disabled", true);
    $("#btn-cancelar-riesgo-objetivo").attr("disabled", true);
    $( ".input-objetivo" ).each(function( index ) {
        if($(this).val() == ""){                        
            $("#"+this.id).val(0)          
        }else{
            valor = $(this).val();
        }        
    });  
    $.ajax({
        type: formulario_objetivo.attr('method'),
        url: formulario_objetivo.attr('action'),
        data: formulario_objetivo.serialize(),
        beforeSend:function(){
            $("#save-actions-objetivo").html('<div style="float: right;display: block;margin-top: -3%;margin-right: 4%;" id="loading-right-save-riesgos" class="kt-spinner kt-spinner--sm kt-spinner--success"></div>');
        },
        success: function (data) {            
            if(data){                
                $("#save-actions-objetivo").html('<i class="flaticon2-check-mark" style="font-size: 35px;float: right;color: #2de02d;margin-top: -8%;"></i>');
                setTimeout(() => {
                    $("#save-actions-objetivo").html("");
                    $("#btn-guardar-riesgo-objetivo")  .attr("disabled", false);
                }, 3000);
            }
        },
        error: function(data) {
            alert("ha ocurrido un error al almacenar.-");
            location.reload();
        }
    });

    return false;
});
