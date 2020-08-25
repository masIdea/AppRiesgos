var control = function(id_riesgo){       
    matriz_residual(id_riesgo);
    limpiar_form();
    $("#descripcion_riesgo").val("");
    $("#direccion_riesgo").val("");
    $("#estado_riesgo").val("");
    $("#fase_riesgo").val("");
    $("#proyecto_riesgo").val("");
    $("#dueno_riesgo").val("");
    $.ajax({
        url:"trae-detalle-riesgo",
        type:"GET",
        dataType:"json",
        data:{"id_riesgo":id_riesgo},
        beforeSend:function(){
            // Loading ...
        },
        success:function(data){            
            var tbody_causas = ""
            var select_causas = '<select required class="form-control kt-select2" style="height: 30px;" id="kt_select2_3" name="causas_asociadas_al_control" multiple="multiple">';
            for(var i = 0; i<data.causas.length; i++){
                tbody_causas+="<tr>"
                tbody_causas+="<td>"+data.causas[i].CAUSA+"</td>"
                tbody_causas+="</tr>"
                select_causas+='<option value="'+data.causas[i].IdCausa+'">'+data.causas[i].CAUSA+'</option>';
            }
            select_causas+='</select>';
            $("#contenedor_select_causas").html(select_causas);
            $("#cuerpo_causas").html(tbody_causas);

            transform_select2('kt_select2_3', 'Seleccione una Causa');


            var tbody_consecuencias = ""
            var select_consecuencias = '<select class="form-control kt-select2" style="height: 30px !important;" id="kt_consecuencia_modal" name="consecuencias_asociadas_al_control" multiple="multiple">';
            
            for(var j=0; j<data.consecuencias.length; j++){                
                tbody_consecuencias+="<tr>"
                tbody_consecuencias+="<td>"+data.consecuencias[j].CONSECUENCIA+"</td>"
                tbody_consecuencias+="</tr>"
                select_consecuencias+='<option value="'+data.consecuencias[j].IdConsecuencia+'">'+data.consecuencias[j].CONSECUENCIA+'</option>';
            }

            $("#contenedor_select_consecuencias").html(select_consecuencias);
            

            transform_select2('kt_consecuencia_modal', 'Seleccione una Consecuencia');

            
            $("#cuerpo_consecuencias").html(tbody_consecuencias);

            $("#descripcion_riesgo").val(data.detalle_riesgo[0].riesgo);
            $("#direccion_riesgo").val(data.detalle_riesgo[0].direccion);
            $("#estado_riesgo").val(data.detalle_riesgo[0].estado);
            $("#fase_riesgo").val(data.detalle_riesgo[0].fasedelriesgo);
            $("#proyecto_riesgo").val(data.detalle_riesgo[0].proyecto);
            $("#dueno_riesgo").val(data.detalle_riesgo[0].dueño);

            $("#id_riesgo_control").val(id_riesgo);
            $("#id-riesgo-control-residual").val(id_riesgo);            
            $("#btn-guardar-riesgo-residual").html("Editar");
            $('#id-form-riesgos-residual').attr('action', "/controles-riesgo/editar-matriz-residual/");

            controles_riesgo();

        }, error:function(err){
            console.error(err);
        }
    })
}

var matriz_residual = function(id_riesgo){
    $.ajax({
        url:"get-matriz-residual",
        type:"GET",
        dataType:"json",
        data:{'id_riesgo':id_riesgo, },
        beforeSend:function(){

        },
        success:function(data){
            $(".r-circle").css("display", "none");
            $(".input-residual").val("");
            $("#txt_res_probabilidad").val("");
            $("#txt_res_impacto").val("");
            $("#txt_res_magnitud").val("");
            $("#txt_res_nivel").val("");
            if(data.length > 0){
                $("#res_label_"+data[0].impactoresidual+"_"+data[0].probabilidadresidual+"").css("display", "block");
                $("#txt_res_probabilidad").val(data[0].probabilidadresidual);
                $("#txt_res_capex").val(data[0].impactocapexresidual);
                $("#txt_res_plazo").val(data[0].probabilidadresidual);
                $("#txt_res_economico").val(data[0].impactoeconomicoresidual);
                $("#txt_res_sso").val(data[0].impactossoresidual);
                $("#txt_res_medioambiente").val(data[0].impactomedioambienteresidual);
                $("#txt_res_comunitario").val(data[0].impactocomunitarioresidual);
                $("#txt_res_reputacional").val(data[0].impactoreputacionalresidual);
                $("#txt_res_legal").val(data[0].impactolegalresidual);
                $("#txt_res_impacto").val(data[0].impactoresidual);
                $("#txt_res_magnitud").val(data[0].magnitudriesgoresidual);
                $("#txt_res_nivel").val(data[0].nivelriesgoresidual);
            }

                                                
        }, error:function(err){
            console.error(err);
        }
    })
}

$( ".input-residual, #txt_res_probabilidad" ).keypress(function() {
    $(".r-circle").css("display", "none");

      setTimeout(() => {
        var probabilidad = $("#txt_res_probabilidad").val();
        if(probabilidad > 0 || probabilidad <= 7 || probabilidad != ""){
        arreglo_valores_residuales = []      
          $( ".input-residual" ).each(function( index ) {
              if($(this).val() == ""){
                valor = 0;
              }else{
                valor = $(this).val();
              }
              if(valor<=7 || valor<0){
                arreglo_valores_residuales.push(parseInt(valor));
              }else{
                $("#"+this.id).val("");
              }
            });            
            var max = Math.max.apply(null, arreglo_valores_residuales);                      
            $("#txt_res_impacto").val(max);

            $("#res_label_"+max+"_"+probabilidad).css("display","block");
          }
      }, 100);
    
});

var controles_riesgo = function(){
    descr_riesgo = $("#descripcion_riesgo").val();
    id_riesgo = $("#id_riesgo_control").val();
    $.ajax({
        url:"get-controles-riesgo",
        type:"GET",
        dataType:"json",
        data:{'id_riesgo':id_riesgo, 'descr_riesgo':descr_riesgo},
        beforeSend:function(){

        },
        success:function(data){            
            var options_controles_asociados = "";
            for(var i = 0; i<data.controles_asociados.length; i++){
                options_controles_asociados += "<option value="+data.controles_asociados[i].IDCONTROL+">"+data.controles_asociados[i].NOMBRECONTROL+"</option>";
            }
            $("#select_controles_asociados_riesgo").html(options_controles_asociados);

            var options_controles_creados = "";            
            for(var j = 0; j<data.controles_creados.length; j++){
                options_controles_creados += "<option value="+data.controles_creados[j].IDCONTROL+">"+data.controles_creados[j].NOMBRECONTROL+"</option>";
            }
            $("#select_controles_creados_riesgo").html(options_controles_creados);
                        
        }, error:function(err){
            console.error(err);
        }
    })
}

$("#select_controles_asociados_riesgo").click(function(){    
    $("#id_control_seleccionado").val(this.value);
    $.ajax({
        url:"get-datos-control",
        type:"GET",
        dataType:"json",
        data:{'id_control':this.value},
        beforeSend:function(){

        }, success:function(data){          
            $("#guardar_control").attr("disabled", true);
            $("#btn_eliminar_control").attr("disabled", false);              
            $("#link_evidencia").html("");
            $("#nombre_control").val(data.datos_control[0].NombreControl);
            $("#descripcion_txtarea").val(data.datos_control[0].DescripcionControl);
            $("#tipo_control").val(data.datos_control[0].TipoControl);
            $("#dueno_control").val(data.datos_control[0].DuenoControl);
            $("#frecuencia_control").val(data.datos_control[0].FrecuenciaControl);
            
            $("#eficacia_control").val(data.autoevaluacion[0].eficacia);            
            $("#efectividad_control").val(data.autoevaluacion[0].efectividad);
            $("#eficiencia_control").val(data.autoevaluacion[0].eficiencia);

            $("#fecini_control").val(data.monitoreo[0].inicio);
            $("#fecterm_control").val(data.monitoreo[0].fin);
            $("#frecuencia_monitoreo").val(data.monitoreo[0].frecuencia);

            evidencia = data.evidencia[0].archivo;            
            $("#link_evidencia").html("<a download style='margin-left: 3%;font-weight: 700;font-style: italic;' href='"+evidencia+"'> Evidencia Subida &nbsp; <i class='fa fa-download' aria-hidden='true'></i> </a>");


            var select_causas = '<select required class="form-control kt-select2" style="height: 30px;" id="kt_select2_3" name="causas_asociadas_al_control" multiple="multiple">';
            for(var i = 0; i<data.causas.length; i++){
                select_causas+='<option selected="selected" value="'+data.causas[i].IdCausa+'">'+data.causas[i].Causa+'</option>';
            }
            select_causas+='</select>';
            $("#contenedor_select_causas").html(select_causas);            

            transform_select2('kt_select2_3', 'Seleccione una Causa');

            
            var select_consecuencias = '<select class="form-control kt-select2" style="height: 30px !important;" id="kt_consecuencia_modal" name="consecuencias_asociadas_al_control" multiple="multiple">';
            
            for(var j=0; j<data.consecuencias.length; j++){                
                select_consecuencias+='<option selected="selected" value="'+data.consecuencias[j].IdConsecuencia+'">'+data.consecuencias[j].Consecuencia+'</option>';
            }
            $("#contenedor_select_consecuencias").html(select_consecuencias);
            transform_select2('kt_consecuencia_modal', 'Seleccione una Causa');



        }, error:function(err){
            console.error(err);
        }
    })
});

$("#select_controles_creados_riesgo").click(function(){    
    $("#id_control_seleccionado").val(this.value);
    $.ajax({
        url:"get-datos-control",
        type:"GET",
        dataType:"json",
        data:{'id_control':this.value},
        beforeSend:function(){

        }, success:function(data){                        
            $("#link_evidencia").html("");
            $("#nombre_control").val(data.datos_control[0].NombreControl);
            $("#descripcion_txtarea").val(data.datos_control[0].DescripcionControl);
            $("#tipo_control").val(data.datos_control[0].TipoControl);
            $("#dueno_control").val(data.datos_control[0].DuenoControl);
            $("#frecuencia_control").val(data.datos_control[0].FrecuenciaControl);
            
            $("#eficacia_control").val(data.autoevaluacion[0].eficacia);            
            $("#efectividad_control").val(data.autoevaluacion[0].efectividad);
            $("#eficiencia_control").val(data.autoevaluacion[0].eficiencia);

            $("#fecini_control").val(data.monitoreo[0].inicio);
            $("#fecterm_control").val(data.monitoreo[0].fin);
            $("#frecuencia_monitoreo").val(data.monitoreo[0].frecuencia);
            $("#valida_asignacion").val(true);
            $("#valida_edit").val(false);

            $("#btn_asignar_actualizar").prop("value", "Asignar Control");
            $("#btn_asignar_actualizar").attr("disabled", false);          

            transform_select2('kt_consecuencia_modal', 'Seleccione una Consecuencia');
            
            

        }, error:function(err){
            console.error(err);
        }
    })
});

var eliminar_control = function(){
    id_control = $("#id_control_seleccionado").val();
    id_riesgo = $("#id_riesgo_control").val();
    if($("#id_control_seleccionado").val() != ""){
        cfm = confirm("¿Está seguro de eliminar el control seleccionado?");
        if(cfm == true){
            $.ajax({
                url:'eliminar-control',
                data:{'id_control':id_control, 'id_riesgo':id_riesgo},
                type:'GET',
                dataType:'json',
                success:function(data){
                    alert("Control eliminado satisfactoriamente.-");
                    controles_riesgo();
                    limpiar_form();
                },error:function(err){
                    console.error(err);
                }
            });
        }

    }else{
        alert("Seleccione un control.-");
    }

}

var transform_select2 = function(id_select, placeholder){
    $('#'+id_select).select2({
        placeholder: placeholder,
    });
}

$("#eficiencia_control").change(function(){
    eficacia = $("#eficacia_control").val();
    eficiencia = $("#eficiencia_control").val();
    if(eficacia == ""){
        alert("Primero Seleccione una eficacia");
        $("#eficiencia_control").val("");
    }else{
        if(eficiencia == "Alta" && eficacia == "Alta"){
            efectividad = "Alta";
        }else if(eficiencia == "Alta" && eficacia == "Media"){
            efectividad = "Alta";
        }else if(eficiencia == "Alta" && eficacia == "Baja"){
            efectividad = "Media";
        }else if(eficiencia == "Media" && eficacia == "Media"){
            efectividad = "Media";
        }else if(eficiencia == "Media" && eficacia == "Baja"){
            efectividad = "Baja";
        }else if(eficiencia == "Baja" && eficacia == "Baja"){
            efectividad = "Baja";
        }
        $("#efectividad_control").val(efectividad);

    }
});

$("#eficacia_control").change(function(){
    $("#eficiencia_control").val("");
})


var formulario_residual = $('#id-form-riesgos-residual');
var accion = function(){
    formulario_residual.submit();
}
formulario_residual.submit(function () {
    $("#btn-guardar-riesgo-residual")  .attr("disabled", true);
    $("#btn-cancelar-riesgo-residual").attr("disabled", true);
    $( ".input-residual" ).each(function( index ) {
        if($(this).val() == ""){                        
          $("#"+this.id).val(0)          
        }else{
          valor = $(this).val();
        }        
    });  
    $.ajax({
        type: formulario_residual.attr('method'),
        url: formulario_residual.attr('action'),
        data: formulario_residual.serialize(),
        beforeSend:function(){
            $("#save-actions-residual").html('<div style="float: right;display: block;margin-top: -3%;margin-right: 4%;" id="loading-right-save-riesgos" class="kt-spinner kt-spinner--sm kt-spinner--success"></div>');
        },
        success: function (data) {            
            if(data){                
                $("#save-actions-residual").html('<i class="flaticon2-check-mark" style="font-size: 35px;float: right;color: #2de02d;margin-top: -8%;"></i>');
                setTimeout(() => {
                    $("#save-actions-residual").html("");
                    $("#btn-guardar-riesgo-residual")  .attr("disabled", false);
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
