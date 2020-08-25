var limpiar_form = function(){
    $("#nombre_control").val("");
    $("#descripcion_txtarea").val("");
    $("#tipo_control").val("");
    $("#dueno_control").val("");
    $("#frecuencia_control").val("");
    $("#kt_select2_3").val("");
    $("#kt_consecuencia_modal").val("");

    $("#eficacia_control").val("");
    $("#eficiencia_control").val("");
    $("#efectividad_control").val("");
    $("#frecuencia_monitoreo").val("");
    $("#fecini_control").val("");
    $("#fecterm_control").val("");
    $("#link_evidencia").html("");

    $("#btn_eliminar_control").attr("disabled", true);
    $("#id_control_seleccionado").val("");
    $("#guardar_control").attr("disabled", false);
    $("#btn_asignar_actualizar").attr("disabled", true);

    $("#btn_asignar_actualizar").prop("value", "Asignar/Actualizar");            

    $("#valida_asignacion").val("");
    $("#valida_edit").val("");
    $("#kt_datepicker_1").val("");
    $("#kt_datepicker_2").val("");

    $("#kt_select2_3").val(null).trigger("change");
    $("#kt_consecuencia_modal").val(null).trigger("change");


}