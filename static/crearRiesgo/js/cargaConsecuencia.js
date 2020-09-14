

var cargaConsecuenciasFiltradas = function(){
    var id_riesgo = $("#identificador-riesgo-creado").html();    
    $.ajax({
        url:'/crea-riesgo/trae-consecuencias',
        type:"GET",
        dataType:"json",
        data:{'id_riesgo':id_riesgo},
        beforeSend:function(){
            $("#consecuencias-actions").html('<div style="float: right;display: block;margin-top: -3%;margin-right: 4%;" id="loading-right-save-riesgos" class="kt-spinner kt-spinner--sm kt-spinner--success"></div>');
        },
        success:function(data){
            $("#select_consecuencias").html("");
            var options = "";
            for(var i = 0; i<data.consecuencias.length; i++){
                options += "<option value='"+data.consecuencias[i].idconsecuencia+"'>"+data.consecuencias[i].consecuencia+"</option>";
            }
            
            $("#consecuencias-actions").html("");

            $("#select_consecuencias").html(options);

            
            console.log(data);
        }, error(err){
            console.error(err);
        }
    })
}
