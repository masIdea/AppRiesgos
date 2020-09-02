$(".tipo-riesgos-dashboard").click(function(){
    console.log(this.id);
    if(this.id == "id-check-eventos-dashboard"){
        $("#id-h3-titulo-dashboard").html("Eventos Materializados");
        $("#id-spn-acumulado-dashboard").html("Acumulados - Valorizados");
        $("#id-spn-acumulado-dashboard").css("margin-left", "-12%");
        $("#id-div-num-general").css("left", "11%");
        $("#id-div-num-general").css("top", "-11%");
        $("#id-div-indicadores-1").css("display", "none");
        $("#id-div-indicadores-2").css("display", "block");
        $("#id-div-indicadores-3").css("display", "block");
        $("#id-spn-mensual").css("display", "none");
        datos_dashboard_tipo('eventos');
    }else if(this.id == "id-check-riesgos-dashboard"){
        $("#id-h3-titulo-dashboard").html("Riesgos Críticos");
        $("#id-spn-acumulado-dashboard").html("Acumulados");
        $("#id-spn-acumulado-dashboard").css("margin-left", "10%");
        $("#id-div-num-general").css("left", "35%");
        $("#id-div-num-general").css("top", "7%");
        $("#id-div-indicadores-2").css("display", "none");
        $("#id-div-indicadores-1").css("display", "block");
        $("#id-div-indicadores-3").css("display", "none");
        
        datos_dashboard_tipo('riesgos');
    }else if(this.id == "id-check-directi-dashboard"){
        $("#id-h3-titulo-dashboard").html("Riesgos Directic");
        $("#id-spn-acumulado-dashboard").html("Acumulados");
        $("#id-spn-acumulado-dashboard").css("margin-left", "10%");
        $("#id-div-num-general").css("left", "35%");
        $("#id-div-num-general").css("top", "7%");
        $("#id-div-indicadores-2").css("display", "none");
        $("#id-div-indicadores-1").css("display", "block");
        $("#id-div-indicadores-3").css("display", "none");
        
        datos_dashboard_tipo('directi');
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
            $("#id-spn-total").html("Cantidad de "+data.glosa+": "+data.cantidad_total_registros);
            $("#id-riesgos-acumulados").html(data.cantidad_riesgos_acumulados)
            $("#id-riesgos-mensuales").html(data.cantidad_riesgos_mes)
            $("#id-spn-acum-atraso-proyecto").html("Acumulado " + data.atraso_proyecto.num_acumulado + " - KUS$ " + numberWithCommas(data.atraso_proyecto.suma_acum));
            $("#id-spn-mes-atraso-proyecto").html("En el mes " + data.atraso_proyecto.num_mes + " - KUS$ " + numberWithCommas(data.atraso_proyecto.suma_mes));
            $("#id-spn-tmf-atraso-proyecto").html("TMF En el mes " + data.atraso_proyecto.suma_mes_tmf + " - TMF Acumulado " + numberWithCommas(data.atraso_proyecto.suma_tmf_total));        
            $("#id-spn-acum-probidad").html("Acumulado " + data.probidad_transparencia.num_acumulado + " - KUS$ " + numberWithCommas(data.probidad_transparencia.suma_acum));
            $("#id-spn-mes-probidad").html("En el mes " + data.probidad_transparencia.num_mes + " - KUS$ " + numberWithCommas(data.probidad_transparencia.suma_mes));
            $("#id-spn-tmf-probidad").html("TMF En el mes " + data.probidad_transparencia.suma_mes_tmf + " - TMF Acumulado " + numberWithCommas(data.probidad_transparencia.suma_tmf_total));
            $("#id-spn-acum-falta-agua").html("Acumulado " + data.falta_agua.num_acumulado + " - KUS$ " + numberWithCommas(data.falta_agua.suma_acum));
            $("#id-spn-mes-falta-agua").html("En el mes " + data.falta_agua.num_mes + " - KUS$ " + numberWithCommas(data.falta_agua.suma_mes));
            $("#id-spn-tmf-agua").html("TMF En el mes " + data.falta_agua.suma_mes_tmf + " - TMF Acumulado " + numberWithCommas(data.falta_agua.suma_tmf_total));
            $("#id-spn-acum-equipo").html("Acumulado " + data.falla_equipo_critico.num_acumulado + " - KUS$ " + numberWithCommas(data.falla_equipo_critico.suma_acum));
            $("#id-spn-mes-equipo").html("En el mes " + data.falla_equipo_critico.num_mes + " - KUS$ " + numberWithCommas(data.falla_equipo_critico.suma_mes));
            $("#id-spn-tmf-equipo").html("TMF En el mes " + data.falla_equipo_critico.suma_mes_tmf + " - TMF Acumulado " + numberWithCommas(data.falla_equipo_critico.suma_tmf_total));

            $("#id-spn-acum-incendio").html("Acumulado " + data.incendio.num_acumulado + " - KUS$ " + numberWithCommas(data.incendio.suma_acum));
            $("#id-spn-mes-incendio").html("En el mes " + data.incendio.num_mes + " - KUS$ " + numberWithCommas(data.incendio.suma_mes));
            $("#id-spn-tmf-incendio").html("TMF En el mes " + data.incendio.suma_mes_tmf + " - TMF Acumulado  " + numberWithCommas(data.incendio.suma_tmf_total));

            $("#id-spn-acum-pandemia").html("Acumulado " + data.pandemia.num_acumulado + " - KUS$ " + numberWithCommas(data.pandemia.suma_acum));
            $("#id-spn-mes-pandemia").html("En el mes " + data.pandemia.num_mes + " - KUS$ " + numberWithCommas(data.pandemia.suma_mes));
            $("#id-spn-tmf-pandemia").html("TMF En el mes " + data.pandemia.suma_mes_tmf + " - TMF Acumulado  " + numberWithCommas(data.pandemia.suma_tmf_total));

            $("#id-spn-acum-otros").html("Acumulado " + data.otro.num_acumulado + " - KUS$ " + numberWithCommas(data.otro.suma_acum));
            $("#id-spn-mes-otros").html("En el mes " + data.otro.num_mes + " - KUS$ " + numberWithCommas(data.otro.suma_mes));
            $("#id-spn-tmf-otros").html("TMF En el mes " + data.otro.suma_mes_tmf + " - TMF Acumulado  " + numberWithCommas(data.otro.suma_tmf_total));

            


        },error:function(err){
            console.error(err);
        }
    })
}

