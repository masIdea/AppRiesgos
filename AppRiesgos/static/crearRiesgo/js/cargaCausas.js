

var cargaCausasFiltradas = function(){
    var id_riesgo = $("#identificador-riesgo-creado").html();    
    $.ajax({
        url:'/crea-riesgo/trae-causas',
        type:"GET",
        dataType:"json",
        data:{'id_riesgo':id_riesgo},
        beforeSend:function(){
            $("#causas-actions").html('<div style="float: right;display: block;margin-top: -3%;margin-right: 4%;" id="loading-right-save-riesgos" class="kt-spinner kt-spinner--sm kt-spinner--success"></div>');
        },
        success:function(data){
            $("#select_causas").html("");
            var options = "";
            for(var i = 0; i<data.causas.length; i++){
                options += "<option value='"+data.causas[i].idcausa+"'>"+data.causas[i].causa+"</option>";
            }            
            $("#causas-actions").html("");
            $("#select_causas").html(options);


            //select_causas
            console.log(data);
        }, error(err){
            console.error(err);
        }
    })
}
