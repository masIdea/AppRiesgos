var limpiar_plan = function(){
    $("#descripcion_riesgo").html("");
    $("#direccion_riesgo").html("");
    $("#estado_riesgo").html("");
    $("#fase_riesgo").html("");
    $("#proyecto_riesgo").html("");
    $("#dueno_riesgo").html("");
}

var limpiar_detalle_plan = function(){
    $("#id-estrategia-plan").val("");
    $("#id-descripcion-plan").val("");
    $("#id-dueno-plan").val("");
    $("#id-cargo-dueno-plan").val("");
    $("#id-trigger-plan").val("");

    $("#estrategia_plan").html("");
    $("#trigger_plan").html("");
    $("#descripcion_plan").html("");
    $("#dueno_plan").html("");
    $("#cargo_dueno_plan").html("");

    $("#costo_detalle_plan").html("");
    $("#fec_ini_detalle_plan").html("");
    $("#fec_ter_detalle_plan").html("");
    $("#costo_detalle_plan").html("");
    $("#fec_ini_detalle_plan").html("");
}

var limpiar_detalle_actividad = function(){
    $("#id-actividad-responsable").val("");
    $("#id-actividad-estrategia").val("");
    $("#id-actividad-costo").val("");
    $("#kt_datepicker_2").val("");
    $("#kt_datepicker_1").val("");
    $("#id-actividad-estado").val("");
    $("#id-actividad-nombre").val("");
    $("#id-actividad-peso-especifico").val("");
    $("#id-actividad-avance-real").val("");
    $("#id-actividad-detalle-actividad").val("");    
}

var limpiar_datos_actividad = function(){
    $("#avance_real").html("");
    $("#avance_planificado").html("");
    $("#costo_detalle_plan").html("");
    $("#fec_ini_detalle_plan").html("");
    $("#fec_ter_detalle_plan").html("");
}

var limpiar_actividad = function(){
    $("#id-actividad-responsable").prop('readonly', false);
    $("#id-actividad-estrategia").prop('readonly', false);
    $("#id-actividad-costo").prop('readonly', false);
    $("#kt_datepicker_2").prop('readonly', false);
    $("#kt_datepicker_1").prop('readonly', false);
    $("#id-actividad-estado").prop('readonly', false);
    $("#id-actividad-peso-especifico").prop('readonly', false);
    $("#id-actividad-nombre").prop('readonly', false);
    $("#id-actividad-detalle-actividad").prop('readonly', false);

    $("#id-actividad-responsable").val("");
    $("#id-actividad-estrategia").val("");
    $("#id-actividad-costo").val("");
    $("#kt_datepicker_2").val("");
    $("#kt_datepicker_1").val("");
    $("#id-actividad-estado").val("");
    $("#id-actividad-peso-especifico").val("");
    $("#id-actividad-nombre").val("");
    $("#id-actividad-detalle-actividad").val("");
    $("#id-actividad-avance-real").val("");    
}