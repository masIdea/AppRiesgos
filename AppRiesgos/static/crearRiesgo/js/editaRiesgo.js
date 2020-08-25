var edita_riesgo = function(id_riesgo){    
    $(".r-circle").css("display", "none");
    $.ajax({
        url:'../datos-edita-riesgo',
        type:'GET',
        dataType:'json',
        data:{'id_riesgo':id_riesgo},
        success:function(data){
            $("#txt_inhe_probabilidad").val("");
            $("#txt_inhe_capex").val("");
            $("#txt_inhe_plazo").val("");
            $("#txt_inhe_economico").val("");
            $("#txt_inhe_sso").val("");
            $("#txt_inhe_medioambiente").val("");
            $("#txt_inhe_comunitario").val("");
            $("#txt_inhe_reputacional").val("");
            $("#txt_inhe_legal").val("");
            $("#txt_inhe_impacto").val("");
            $("#txt_inhe_magnitud").val("");
            $("#txt_inhe_nivel").val("");
            $("#id-txt-idRiesgo").val(id_riesgo);
            $("#identificador-riesgo-creado").html(id_riesgo);

            $("#identificador-riesgo-creado-inherente").val(id_riesgo);    

            $("#riesgo_gerencia").val(data.datos_riesgo[0].gerencia);
            $("#riesgo_direccion").val(data.datos_riesgo[0].direccion);
            $("#riesgo_proyecto").val(data.datos_riesgo[0].proyecto);                                                

            $("#riesgo_clasificacion").val(data.datos_riesgo[0].clasificacion);
            $("#riesgo_fase").val(data.datos_riesgo[0].fasedelriesgo);
            $("#riesgo_dueno").val(data.datos_riesgo[0].dueño);
            $("#riesgo_cargo").val(data.datos_riesgo[0].cargodeldueño);
            $("#riesgo_estado").val(data.datos_riesgo[0].estado);
            $("#id-riesgo-descripcion").val(data.datos_riesgo[0].descripcionriesgo);
            console.log("Esta es la fecha ", data.datos_riesgo[0].fechadigita)
            if(data.datos_riesgo[0].fechadigita != "" && data.datos_riesgo[0].fechadigita != null){
                if(data.datos_riesgo[0].fechadigita.split("T")){
                    fecha = data.datos_riesgo[0].fechadigita.split("T");
                    fecha = fecha[0].split("-");
                    fecha = fecha[1]+'/'+fecha[2]+'/'+fecha[0];
                }else{                
                    fecha = fecha[0].split("-");
                    fecha = fecha[1]+'/'+fecha[2]+'/'+fecha[0];
                }
            }else{
                fecha = ""
            }

            $("#kt_datepicker_1").val(fecha);

            $("#riesgo_descripcion_riesgo").val(data.datos_riesgo[0].riesgo);
            $("#riesgo_familia").val(data.familia);
            $("#riesgo_subproceso").val(data.subproceso);
            $("#riesgo-creado").html(data.datos_riesgo[0].riesgo);

            $("#id-maxima-perdida-mus").val(data.datos_riesgo[0].maximaperdidamus);
            $("#id-maxima-perdida-meses").val(data.datos_riesgo[0].maximaperdidameses);
            console.log("el directic ", data.datos_riesgo[0].directic)
            if(data.datos_riesgo[0].directic == true || data.datos_riesgo[0].directic == "b'\x01'"){
                $("#id-chk-directic").prop("checked", true);
            }else{
                $("#id-chk-directic").prop("checked", false);
            }

            //causas_asociadas
            //consecuencias_asociadas
            options_causas = ""
            for(var i = 0; i<data.causas_asociadas.length; i++){
                options_causas+="<option value='"+data.causas_asociadas[i].idcausa+"'>"+data.causas_asociadas[i].causa+"</option>";
            }
            $("#select_causas").html(options_causas);
            
            
            options_consecuencias = ""
            for(var i = 0; i<data.consecuencias_asociadas.length; i++){
                console.log(data.consecuencias_asociadas[i]);
                options_consecuencias+="<option value='"+data.consecuencias_asociadas[i].idconsecuencia+"'>"+data.consecuencias_asociadas[i].consecuencia+"</option>";
            }
            $("#select_consecuencias").html(options_consecuencias);

            console.log("LAS CONSECUENCIAS --> ", data.consecuencias_asociadas);

            if(data.inherente.length > 0){
                probabilidad = parseInt(data.inherente[0].probabilidad);
                impacto = parseInt(data.inherente[0].impacto);            
    
                $("#txt_inhe_probabilidad").val(probabilidad);
                $("#txt_inhe_capex").val(parseInt(data.inherente[0].impactocapex));
                $("#txt_inhe_plazo").val(parseInt(data.inherente[0].impactoplazo));
                $("#txt_inhe_economico").val(parseInt(data.inherente[0].impactoeconomico));
                $("#txt_inhe_sso").val(parseInt(data.inherente[0].impactosso));
                $("#txt_inhe_medioambiente").val(parseInt(data.inherente[0].impactomedioambiente));
                $("#txt_inhe_comunitario").val(parseInt(data.inherente[0].impactocomunitario));
                $("#txt_inhe_reputacional").val(parseInt(data.inherente[0].impactoreputacional));
                $("#txt_inhe_legal").val(parseInt(data.inherente[0].impactolegal));
                $("#txt_inhe_impacto").val(impacto);
                $("#txt_inhe_magnitud").val(parseInt(data.inherente[0].magnitudriesgo));
                $("#txt_inhe_nivel").val(data.inherente[0].nivelriesgo);
                            
                $("#inhe_label_"+impacto+"_"+probabilidad).css("display","block");
            }

            goTo("id-div-datos-riesgo");
            $("#btn-registrar-riesgo").attr("disabled", false);
            
        }
        
    })
}


var formulario = $('#form_riesgo_inherente');
formulario.submit(function () {    
    $("#btn-editar-riesgo-inherente").attr("disabled", true);
    $("#btn-cancelar").attr("disabled", true);    
    $.ajax({
        type: formulario.attr('method'),
        url: formulario.attr('action'),
        data: formulario.serialize(),
        beforeSend:function(){
            $("#save-actions-inherente").html('<div style="float: right;display: block;margin-top: -3%;margin-right: 4%;" id="loading-right-save-riesgos" class="kt-spinner kt-spinner--sm kt-spinner--success"></div>');
        },
        success: function (data) {            
            if(data){                
                $("#btn-editar-riesgo-inherente").attr("disabled", false);
                $("#save-actions-inherente").html('<i class="flaticon2-check-mark" style="font-size: 35px;float: right;color: #2de02d;margin-top: -8%;"></i>');
                setTimeout(() => {
                    $("#save-actions-inherente").html("");
                }, 3000);
            }
        },
        error: function(data) {
           alert("ha ocurrido un error al editar.-") ;
        }
    });

    return false;
});
