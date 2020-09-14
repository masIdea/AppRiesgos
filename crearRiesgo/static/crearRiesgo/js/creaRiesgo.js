$("#riesgo_descripcion_riesgo").on("keydown", function(e){          
    //var value = this.value;     
    //var valor_riesgo = (value + String.fromCharCode(e.which))        
    setTimeout(() => {        
        var valor_riesgo = $("#riesgo_descripcion_riesgo").val();
        $.ajax({
            url:"trae-riesgos-similares",
            type:"GET",
            dataType:"json",
            data:{'desc_riesgo':valor_riesgo},
            beforeSend: function() {
                $("#loading-right-riesgos-similares").show();            
            },        
            success:function(data){
                console.log(data);
                var options = ""
                for(var i = 0; i<data.riesgos_simialres.length; i++){
                    options += "<option>"+data.riesgos_simialres[i].RIESGO+"</option>";
                }
                $("#select_multiple_riesgos_similares").html(options);
                $("#loading-right-riesgos-similares").hide();
                
            }, error(err){
                console.error(err);
            }
        })
    }, 1000);
});

$("#select_multiple_riesgos_similares").click(function(){
    valor = this.value;    
    $("#riesgo_descripcion_riesgo").val(valor);
});

var formulario = $('#form_riesgos');
formulario.submit(function () {
    $("#btn-registrar-riesgo")  .attr("disabled", true);
    $("#btn-cancelar")  .attr("disabled", true);    
    $.ajax({
        type: formulario.attr('method'),
        url: formulario.attr('action'),
        data: formulario.serialize(),
        beforeSend:function(){
            $("#save-actions").html('<div style="float: right;display: block;margin-top: -3%;margin-right: 4%;" id="loading-right-save-riesgos" class="kt-spinner kt-spinner--sm kt-spinner--success"></div>');
        },
        success: function (data) {            
            if(data.valida){
                let descr_riesgo = $("#riesgo_descripcion_riesgo").val();
                $("#riesgo-creado").html(descr_riesgo);
                $("#identificador-riesgo-creado").html(data.identificador);
                $("#identificador-riesgo-creado-inherente").val(data.identificador);
                $("#riesgo-creado").css("font-size", "20px");
                $("#div-riesgos-similares").css("display", "none");
                $("#riesgo_gerencia").attr("disabled", true);

                $("#riesgo_direccion").attr("disabled", true);
                $("#riesgo_proyecto").attr("disabled", true);
                $("#riesgo_fase").attr("disabled", true);
                $("#riesgo_cargo").attr("disabled", true);
                $("#riesgo_estado").attr("disabled", true);
                $("#kt_datepicker_7").attr("disabled", true);
                $("#riesgo_descripcion_riesgo").attr("disabled", true);

                $("#causas_consecuencias").fadeIn("slow");
                $("#riesgo-inherente").fadeIn("slow");

                $("#btn-registrar-riesgo").attr("disabled", true);
                $("#save-actions").html('<i class="flaticon2-check-mark" style="font-size: 35px;float: right;color: #2de02d;margin-top: -8%;"></i>');
                setTimeout(() => {
                    $("#save-actions").html("");
                }, 3000);
            }
        },
        error: function(data) {
           alert("ha ocurrido un error al almacenar.-") ;
        }
    });

    return false;
});


$("#riesgo_gerencia").change(function(){    
    $("#riesgo_direccion").html("<option value=''>Seleccione</option>");
    $.ajax({
        url:'direcciones-gerencia',
        type:"GET",
        dataType:"json",
        data:{'id_gerencia':this.value},
        beforeSend:function(){
            $("#loading-right-direcciones").css("display", "block");
        }, success:function(data){
            console.log(data);            
            var option = ""
            for(var i = 0; i<data.direcciones.length; i++){
                option+="<option value='"+data.direcciones[i].sigla+"'>"+data.direcciones[i].direccion+"</option>";
            }
            $("#riesgo_direccion").append(option);
            $("#loading-right-direcciones").css("display", "none");
        }, error:function(err){
            console.error(err);
        }
    })
});