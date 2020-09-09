$("#id-select-campos").change(function(){
    $("#id-div-grafico-1-eventos").css("display", "none");
    $("#id-div-grafico-2-eventos").css("display", "none");
    $("#id-sub-title-chart-cantidad").html("Cantidad de Eventos");
    $("#id-sub-title-chart-montokus").html("Montos Pérdidas KUS$");
    valor = $("#id-txt-gerencia-eventos").val();
    tipo = $("#id-tipo-nivel").val();
    $("#id-title-chart-cantidad").html("");
    $("#id-title-chart-montokus").html("");
    $("#id-select-datos-campos").html("<option value=''>Seleccione</option>");
    $.ajax({
        url:'/dashboard/datos-campos',
        type:"GET",
        dataType:"json",
        data:{"campo":this.value, 'tipo':tipo, 'valor':valor, },
        success:function(data){            
            var option = "";
            for(var i = 0; i<data.datos_campo.length; i++){
                option+="<option value='"+data.datos_campo[i]+"'>"+data.datos_campo[i]+"</option>";                
            }
            $("#id-select-datos-campos").append(option);


            objeto_cantidad = Object();
            objeto_monto = Object();
            objeto_cantidad['glosa'] = [];
            objeto_cantidad['cantidad'] = [];
            objeto_monto['glosa'] = [];
            objeto_monto['montokus'] = [];
            
            for(q in data.cantidad){
                objeto_cantidad['glosa'].push(q);
                objeto_cantidad['cantidad'].push(data.cantidad[q]); 
            }

            for(m in data.montokus){
                objeto_monto['glosa'].push(m);
                objeto_monto['montokus'].push(data.montokus[m]); 
            }
                        
            grafico_chart_js(objeto_cantidad, 'chart-area-cantidad', 'cantidad', 'id-div-canvas-cantidad');
            grafico_chart_js(objeto_monto, 'chart-area-montokus', 'montokus', 'id-div-canvas-montos');
            
            $("#id-div-grafico-1-eventos").css("display", "block");
            $("#id-div-grafico-2-eventos").css("display", "block");
            
            console.log(objeto_cantidad)
            console.log(objeto_monto)
        }, error:function(err){
            console.error(err);
        }
    })
})
