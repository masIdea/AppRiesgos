$(".tipo-riesgos").click(function(){
    console.log(this.id);
    var valor1 = "";
    var valor2 = "";
    var valor3 = "";
    var valor4 = "";
    var valor5 = "";
    var filtro = $("#filtro").val();
    if(this.id == "id-check-eventos"){
        $("#id-txt-tipo").val("eventos");
        valor1 = "Causas de Eventos Materializados";
        valor2 = "Causas Valorizadas";
        valor3 = "Direcciones/SuperIntendecias Con Más Eventos Materializados";
        valor4 = "Eventos Materializados";
        valor5 = "Direcciones/SuperIntendecias Con Mayores Gastos Por Eventos";
        trae_causas_riesgos_criticos(filtro);
        trae_riesgos_por_gerencia(filtro);
        trae_riesgos_por_direccion_valorizados(filtro);
    }else if(this.id == "id-check-riesgos"){
        $("#id-txt-tipo").val("riesgos");
        valor1 = "Causas de Riesgos Críticos"
        valor2 = "Causas Valorizadas"
        valor3 = "Direcciones/SuperIntendencias Con Más Riesgos"
        valor4 = "Riesgos Críticos"
        valor5 = "Direcciones/SuperIntendencias Con Mayores Gastos por Riesgos"
        trae_causas_riesgos_criticos(filtro);
        trae_riesgos_por_gerencia(filtro);
        trae_riesgos_por_direccion_valorizados(filtro);
    }else if(this.id == "id-check-directic"){
        $("#id-txt-tipo").val("directic");
        valor1 = "Causas de Riesgos Críticos Directic"
        valor2 = "Causas Valorizadas Directic"
        valor3 = "Direcciones/SuperIntendencias Con Más Riesgos Directic"
        valor4 = "Riesgos Críticos Directic"
        valor5 = "Direcciones/SuperIntendencias Con Mayores Gastos por Riesgos Directic"
        trae_causas_riesgos_criticos(filtro);
        trae_riesgos_por_gerencia(filtro);
        trae_riesgos_por_direccion_valorizados(filtro);
    }    
    $("#id-gerencia-h3-criticos").html(valor1);
    $("#id-gerencia-h3-valorizadas").html(valor2);
    $("#id-gerencia-h3-sup-dir").html(valor3);
    $("#id-gerencia-h3-sub-sup-dir").html(valor4);
    $("#id-gerencia-h3-sup-dir-gastos").html(valor5);
})
