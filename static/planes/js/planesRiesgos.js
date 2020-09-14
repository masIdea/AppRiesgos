var getDetallePlanes = function(){
    var id_riesgo = $("#id_riesgo_plan").val();    
    $.ajax({        
        url:'detalle-planes-riesgo',
        type:"GET",
        dataType:"json",
        data:{'id_riesgo':id_riesgo},
        success:function(data){            
            var tbody = "";
            for(var i = 0; i<data.detalle_plan_riesgo.length; i++){                
                tbody+='<tr class="tr_plan" id="tr_plan_'+i+'" onclick="detallePlanRespuesta(this.id, \''+data.detalle_plan_riesgo[i].idplanrespuesta+'\');">'
                tbody+="<td>"+data.detalle_plan_riesgo[i].descripcion+"</td>"
                tbody+="</tr>"
            }

            $("#cuerpo_planes_riesgo").html(tbody);
        }, error:function(err){
            console.error(err);
        }
    })
}


var detallePlanRespuesta = function(id_tr, id_plan){
    limpiar_detalle_plan();
    limpiar_datos_actividad();
    goTo("id-form-plan-accion");
    trClickActividad(id_tr);
    $("#actividad_descripcion_riesgo").html($("#descripcion_riesgo").html());
    $("#id-txt-id-plan").val(id_plan)
    $("#editar-detalle-plan").attr("disabled", false);
    $("#btn_eliminar_plan").attr("disabled", false);
    $.ajax({
        url:'detalle-plan-respuesta',
        type:"GET",
        dataType:"json",
        data:{'id_plan':id_plan},
        success:function(data){
            console.log(data);
            var fecterm = "";
            var fecini = "";
            $("#cuerpo_actividades_plan").html("");
            $("#estrategia_plan").html(data.detalle_plan_respuesta[0].estrategia);
            $("#trigger_plan").html(data.detalle_plan_respuesta[0].trigger);
            $("#descripcion_plan").html(data.detalle_plan_respuesta[0].descripcion);
            $("#dueno_plan").html(data.detalle_plan_respuesta[0].dueñoplanderespuesta);
            $("#cargo_dueno_plan").html(data.detalle_plan_respuesta[0].cargodueñoplan);
            $("#plan-seleccionado").html(data.detalle_plan_respuesta[0].descripcion);
            $("#id-plan").val(id_plan);

            
            var tbody = "";
            var costo = 0;
            var avance_real = 0;        
            
            for(var i=0; i<data.actividades_plan_respuesta.length; i++){
                console.log(typeof(data.actividades_plan_respuesta[i]));
                costo += parseFloat(data.actividades_plan_respuesta[i].costo);
                avance_real += (parseFloat(data.actividades_plan_respuesta[i].avancereal) * parseFloat(data.actividades_plan_respuesta[i].pesoespecifico))/100;
                tbody+='<tr class="tr_plan_actividad" id="tr_actividad_plan_'+i+'" onclick="detalleActividad(this.id, \''+ data.actividades_plan_respuesta[i].idactividad+'\');">'
                tbody+="<td>"+data.actividades_plan_respuesta[i].nombreactividad+"</td>"
                tbody+="</tr>"
            }
            if(data.inicio_termino.inicio != null){
                fecini = data.inicio_termino.inicio.split("T")[0]
                fecini = fecini.split("-")[2] + '-' + fecini.split("-")[1] + '-' + fecini.split("-")[0]
            }
            
            if(data.inicio_termino.termino != null){
                fecterm = data.inicio_termino.termino.split("T")[0]
                fecterm = fecterm.split("-")[2] + '-' + fecterm.split("-")[1] + '-' + fecterm.split("-")[0]
            }
            

            $("#costo_detalle_plan").html(costo);
            if(avance_real>=0){
                $("#avance_real").html(avance_real+" %");    
            }else{
                $("#avance_real").html("0%");
            }
            
            $("#avance_planificado").html(data.programado.toFixed(1)+" %");
            $("#fec_ini_detalle_plan").html(fecini);
            $("#fec_ter_detalle_plan").html(fecterm);            
            $("#cuerpo_actividades_plan").html(tbody);
        }
    })
}

var detalleActividad = function(id_tr, id_actividad){    
    trClick(id_tr);
    $("#editar-actividad-plan").attr("disabled", false);
    $("#eliminar-actividad-plan").attr("disabled", false);
    $("#id-txt-id-actividad").val(id_actividad);
}

$("#editar-actividad-plan").click(function(){
    $("#id-href-actividad-evidencia").html("");
    id_actividad = $("#id-txt-id-actividad").val();    
    $.ajax({
        url:"detalle-actividad",
        type:"GET",
        dataType:"json",
        data:{'id_actividad':id_actividad},
        success:function(data){
            console.log(data)
            fecini = data.actividad[0].inicio.split("T")[0]
            fecterm = data.actividad[0].termino.split("T")[0]
            fecini = fecini.split("-")[2] + '-' + fecini.split("-")[1] + '-' + fecini.split("-")[0]
            fecterm = fecterm.split("-")[2] + '-' + fecterm.split("-")[1] + '-' + fecterm.split("-")[0]

            $("#id-actividad-responsable").val(data.actividad[0].responsable);
            $("#id-actividad-estrategia").val(data.actividad[0].estrategia);
            $("#id-actividad-costo").val(data.actividad[0].costo);
            $("#kt_datepicker_2").val(fecini);
            $("#kt_datepicker_1").val(fecterm);
            $("#id-actividad-estado").val(data.actividad[0].estadoactividad);
            $("#id-actividad-peso-especifico").val(data.actividad[0].pesoespecifico);
            $("#id-actividad-avance-real").val(data.actividad[0].avancereal);
            $("#id-actividad-nombre").val(data.actividad[0].nombreactividad);
            $("#id-actividad-detalle-actividad").val(data.actividad[0].detalleactividad);

            $("#id-actividad-responsable").prop('readonly', true);
            $("#id-actividad-estrategia").prop('readonly', true);
            $("#id-actividad-costo").prop('readonly', true);
            $("#kt_datepicker_2").prop('readonly', true);
            $("#kt_datepicker_1").prop('readonly', true);
            $("#id-actividad-estado").prop('readonly', true);
            $("#id-actividad-peso-especifico").prop('readonly', true);
            $("#id-actividad-nombre").prop('readonly', true);
            $("#id-actividad-detalle-actividad").prop('readonly', true);
            $("#modal_detalle_plan_actividad").modal("show");

            $("#btn_registrar_actividad").prop("value", "Modificar Actividad");
            $("#id-actividad-avance-real").css({"border-color": "#60cf65", 
            "border-width":"2px", 
            "border-style":"solid"});
            $("#id-txt-edit-actividad").val(1);
            $("#id-evidencia-actividad").html("");
            console.log(data)
            console.log(data.archivo);
            if(data.archivo != ""){
                $("#id-href-actividad-evidencia").html("<a download style='margin-left: 3%;font-weight: 700;font-style: italic;' href='"+data.archivo+"'> Evidencia Cargada &nbsp; <i class='fa fa-download' aria-hidden='true'></i> </a>");
            }            

        }, error:function(err){
            console.error(err);
        }
    })
});

$("#btn_agregar_detalle").click(function(){    
    $("#id-href-actividad-evidencia").html("");
    limpiar_actividad();
    $("#btn_registrar_actividad").prop("value", "Registrar Actividad");
    $("#modal_detalle_plan_actividad").modal("show");
    $("#id-txt-edit-actividad").val(0);
    $("#id-evidencia-actividad").html('<input required type="file" class="custom-file-input" name="evidencia" id="customFile"><label class="custom-file-label" style="font-size: 9px;" for="customFile">Evidencia</label>');
})

var trClick = function(id_tr){
    //$("#"+id_tr).css("font-weight", "800");
    $(".tr_plan_actividad").css("background-color", "transparent");
    $(".tr_plan_actividad").css({"border-width":"0px"});
    $(".tr_plan_actividad").css("font-weight", "100");
    $("#"+id_tr).css("background-color", "#f7f8fa");
    $("#"+id_tr).css({//"border-color": "#00BCD4", 
                                        //"border-width":"1px", 
                                        "border-style":"solid"});
    
    

}

var trClickActividad = function(id_tr){    
    $(".tr_plan").css("background-color", "transparent");
    $(".tr_plan").css({"border-width":"0px"});    
    $(".tr_plan").css("font-weight", "100");
    $("#"+id_tr).css("background-color", "#f7f8fa");
    $("#"+id_tr).css({//"border-color": "#00BCD4", 
                                        //"border-width":"1px", 
                                        "border-style":"solid"});
    
                                        
    //$("#"+id_tr).css("font-weight", "800");

}
