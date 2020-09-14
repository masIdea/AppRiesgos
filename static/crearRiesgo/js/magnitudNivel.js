$( ".input-inherente, #txt_inhe_probabilidad" ).keypress(function() {
    arreglo_valores_residuales = []      
              
        setTimeout(() => {
            $( ".input-inherente" ).each(function( index ) {            
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
            var impacto = Math.max.apply(null, arreglo_valores_residuales);  
            var probabilidad = $("#txt_inhe_probabilidad").val();
            $.ajax({
                url:'/controles-riesgo/magnitud-nivel',
                type:"GET",
                dataType:"json",
                data:{'probabilidad':probabilidad, 'impacto':impacto},
                success:function(data){
                    console.log(data);
                    $("#txt_inhe_magnitud").val(data.magnitud);
                    $("#txt_inhe_nivel").val(data.nivel);
                }, error:function(err){
                    console.error(err);
                }
            })
        }, 1000);
        });
