$("#id-select-datos-campos").change(function(){        
    datos_graficos();
});

var datos_graficos = function(){
    valor = $("#id-txt-gerencia-eventos").val();
    tipo = $("#id-tipo-nivel").val();
    dato_campo = $("#id-select-datos-campos").val()
    $("#id-title-chart-cantidad").html(dato_campo);
    $("#id-title-chart-montokus").html(dato_campo);
    $("#id-sub-title-chart-cantidad").html("Cantidad de Eventos");
    $("#id-sub-title-chart-montokus").html("Montos Pérdidas KUS$");
    campo = $("#id-select-campos").val()
    datos = $("#id-select-datos-campos").val()
    if(campo !="" && datos != ""){
        $.ajax({
            url:'/dashboard/datos-clasificacion-eventos',
            type:"GET",
            dataType:"json",
            data:{"glosa":dato_campo, 'tipo':tipo, 'valor':valor, 'campo':$("#id-select-campos").val()},
            success:function(data){            
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
                //grafico_chart_js(objeto, 'chart-area-montokus', this.value, 'Cantidad', 'cantidad');

            }, error:function(err){
                console.error(err);
            }
        })
    }
}

var grafico_chart_js = function(objeto, id, llave, idDivParent){
    resetCanvas(id, idDivParent);        
    var config = {
        data: {
            datasets: [{
                data: objeto[llave],
                backgroundColor: [
                    "#997300",
                    "#ED7D31",
                    "#FFC000",
                    "#70AD47",
                    "#9E480E",
                    "#43682B",
                    "#0D88B3",
                    "#A5A5A5",
                    "#333F50",
                    "#7030A0",
                ],
                label: ' ' // for legend
            }],
            labels: objeto['glosa']
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            legend: {
                position: 'bottom',
            },
            title: {
                display: false,
                text: ' '
            },
            scale: {
                ticks: {
                    beginAtZero: true
                },
                reverse: false
            },
            animation: {
                animateRotate: false,
                animateScale: true
            },
            
        }
    };
    
        var ctx = document.getElementById(id);                
        console.log("EL CTX ", ctx);
        window.myPolarArea = Chart.PolarArea(ctx, config);        

}
