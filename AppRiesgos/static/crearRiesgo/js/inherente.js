$('form').on('focus', 'input[type=number]', function (e) {
  $(this).on('wheel.disableScroll', function (e) {
    e.preventDefault()
  })
})
$('form').on('blur', 'input[type=number]', function (e) {
  $(this).off('wheel.disableScroll')
})


$( ".input-inherente, #txt_inhe_probabilidad" ).keypress(function() {
    $(".r-circle").css("display", "none");

      setTimeout(() => {
        var probabilidad = $("#txt_inhe_probabilidad").val();
        if(probabilidad > 0 || probabilidad <= 7 || probabilidad != ""){
        arreglo_valores_inherentes = []      
          $( ".input-inherente" ).each(function( index ) {
              if($(this).val() == ""){
                valor = 0;
              }else{
                valor = $(this).val();
              }
              if(valor<=7 || valor<0){
                arreglo_valores_inherentes.push(parseInt(valor));
              }else{
                $("#"+this.id).val("");
              }
            });            
            var max = Math.max.apply(null, arreglo_valores_inherentes);                      
            $("#txt_inhe_impacto").val(max);

            $("#inhe_label_"+max+"_"+probabilidad).css("display","block");
          }
      }, 100);
    
});


var formulario_inherente = $('#form_riesgo_inherente');
formulario_inherente.submit(function () {    
    $("#btn-guardar-riesgo-inherente").attr("disabled", true);
    $("#btn-cancelar-riesgo-inherente").attr("disabled", true);
    
    $.ajax({
        type: formulario_inherente.attr('method'),
        url: formulario_inherente.attr('action'),
        data: formulario_inherente.serialize(),
        beforeSend:function(){
            $("#save-actions-inherente").html('<div style="float: right;display: block;margin-top: -3%;margin-right: 4%;" id="loading-right-save-riesgos" class="kt-spinner kt-spinner--sm kt-spinner--success"></div>');
        },
        success: function (data) {            
            if(data.valida){
                let descr_riesgo = $("#riesgo_descripcion_riesgo").val();
                $("#riesgo-creado").html(descr_riesgo);
                $("#identificador-riesgo-creado").html(data.identificador);
                $("#riesgo-creado").css("font-size", "20px");
                $("#div-riesgos-similares").css("display", "none");
                $("#riesgo_gerencia").attr("disabled", true);

                $("#txt_inhe_capex").attr("disabled", true);
                $("#txt_inhe_probabilidad").attr("disabled", true);
                $("#txt_inhe_plazo").attr("disabled", true);
                $("#txt_inhe_economico").attr("disabled", true);
                $("#txt_inhe_sso").attr("disabled", true);
                $("#txt_inhe_medioambiente").attr("disabled", true);
                $("#txt_inhe_comunitario").attr("disabled", true);
                $("#txt_inhe_reputacional").attr("disabled", true);
                $("#txt_inhe_legal").attr("disabled", true);
                $("#txt_inhe_impacto").attr("disabled", true);
                $("#txt_inhe_magnitud").attr("disabled", true);
                $("#txt_inhe_nivel").attr("disabled", true);

                $("#causas_consecuencias").fadeIn("slow");
                $("#save-actions-inherente").html('<i class="flaticon2-check-mark" style="font-size: 35px;float: right;color: #2de02d;margin-top: -8%;"></i>');
                setTimeout(() => {
                    $("#save-actions-inherente").html("");
                }, 3000);
            }
        },
        error: function(data) {
           alert("ha ocurrido un error al almacenar, por favor reintente.-") ;
           $("#btn-guardar-riesgo-inherente").attr("disabled", false);
           $("#btn-cancelar-riesgo-inherente").attr("disabled", false);
           $("#save-actions-inherente").html("");
        }
    });

    return false;
});