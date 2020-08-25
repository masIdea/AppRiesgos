var trae_matrices = function(valor, tipo, directic=1){    
    $(".r-circle").css("display", "none");
    $(".r-circle").html("");
    $.ajax({
        url:'trae-matrices',
        type:"GET",
        dataType:"json",
        data:{'valor':valor, 'tipo':tipo, 'directic':directic},
        beforeSend:function(){
            $(".loading-matrices").css("display", "block");
        },
        success:function(data){                                              
            for(key_inh in data.matriz_inherente){                                
                $("#inhe_label_"+key_inh+"").html(data.matriz_inherente[key_inh]);                
                $("#inhe_label_"+key_inh+"").css("display", "block");                
            }
            console.log("---------->")
            for(key_res in data.matriz_residual){                                
                $("#res_label_"+key_res+"").html(data.matriz_residual[key_res]);
                $("#res_label_"+key_res+"").css("display", "block");                
                
            }
            console.log("---------->")
            for(key_obj in data.matriz_objetivo){                                
                $("#obj_label_"+key_obj+"").html(data.matriz_objetivo[key_obj]);
                $("#obj_label_"+key_obj+"").css("display", "block");                
                
            }                        
            
            $("#id-lbl-cant-objetivo").html("&nbsp;("+data.suma_objetivo+")");
            $("#id-lbl-cant-inherente").html("&nbsp;("+data.suma_inherente+")");
            $("#id-lbl-cant-residual").html("&nbsp;("+data.suma_residual+")");

            $(".loading-matrices").css("display", "none");

        }, error:function(err){
            console.error(err);
        }
    });
}
