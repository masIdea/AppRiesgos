$(".tipo-riesgos-dashboard").click(function(){
    console.log(this.id);
    var valor1 = "";
    var valor2 = "";
    var valor3 = "";
    var valor4 = "";
    var valor5 = "";
    if(this.id == "id-check-eventos-dashboard"){
        $("#id-h3-titulo-dashboard").html("Eventos Materializados");
        datos_dashboard_tipo('eventos');
    }else if(this.id == "id-check-riesgos-dashboard"){
        $("#id-h3-titulo-dashboard").html("Riesgos Críticos");
        datos_dashboard_tipo('riesgos');
    }    

})

var datos_dashboard_tipo = function(tipo){
    $.ajax({
        url:'/dashboard/datos-dashboard-tipo-riesgo',
        type:"GET",
        dataType:"json",
        data:{'tipo':tipo},
        success:function(data){
            console.log(data);
            $("#id-riesgos-acumulados").html(data.cantidad_riesgos_acumulados)
            $("#id-riesgos-mensuales").html(data.cantidad_riesgos_mes)
            $("#id-spn-acum-atraso-proyecto").html("Acumulado " + data.atraso_proyecto.num_acumulado + " - KUS$ " + numberWithCommas(data.atraso_proyecto.suma_acum));
            $("#id-spn-mes-atraso-proyecto").html("En el mes " + data.atraso_proyecto.num_mes + " - KUS$ " + numberWithCommas(data.atraso_proyecto.num_acumulado));
            $("#id-spn-acum-probidad").html("Acumulado " + data.probidad_transparencia.num_acumulado + " - KUS$ " + numberWithCommas(data.probidad_transparencia.suma_acum));
            $("#id-spn-mes-probidad").html("En el mes " + data.probidad_transparencia.num_mes + " - KUS$ " + numberWithCommas(data.probidad_transparencia.num_acumulado));
            $("#id-spn-acum-falta-agua").html("Acumulado " + data.falta_agua.num_acumulado + " - KUS$ " + numberWithCommas(data.falta_agua.suma_acum));
            $("#id-spn-mes-falta-agua").html("En el mes " + data.falta_agua.num_mes + " - KUS$ " + numberWithCommas(data.falta_agua.num_acumulado));
            $("#id-spn-acum-equipo").html("Acumulado " + data.falla_equipo_critico.num_acumulado + " - KUS$ " + numberWithCommas(data.falla_equipo_critico.suma_acum));
            $("#id-spn-mes-equipo").html("En el mes " + data.falla_equipo_critico.num_mes + " - KUS$ " + numberWithCommas(data.falla_equipo_critico.num_acumulado));
            $("#id-spn-acum-incendio").html("Acumulado " + data.incendio.num_acumulado + " - KUS$ " + numberWithCommas(data.incendio.suma_acum));
            $("#id-spn-mes-incendio").html("En el mes " + data.incendio.num_mes + " - KUS$ " + numberWithCommas(data.incendio.num_acumulado));

        },error:function(err){
            console.error(err);
        }
    })
}

