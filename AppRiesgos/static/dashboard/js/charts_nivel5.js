var graficosDetalle_5 = function(api) {
    $('#grafico_111').html("");
    $('#grafico_222').html("");
    if(api == "T18M400"){
        data_1=[42, 23, 21, 12, 10]
        data_2=[23, 24, 54, 12, 36]                
    }
    if(api == "T18M401"){
        data_1=[23, 34, 56, 54, 12]
        data_2=[36, 24, 54, 56, 36]                
    }
    if(api == "T18M402"){
        data_1=[34, 56,23,15, 12]
        data_2=[78, 56, 65, 56, 42]                
    }
    if(api == "T18M403"){
        data_1=[23,36,18,47,34]
        data_2=[36, 42, 65, 23, 42]                
    }
    
        $('#grafico_111').html("");
        if ($('#grafico_111').length == 0) {
            return;
        }

        Morris.Donut({
            element: 'grafico_111',
            data: [{
                    label: "Falla equipo A",
                    value: data_1[0]
                },
                {
                    label: "Falla equipo B",
                    value: data_1[1]
                },
                {
                    label: "Mantenimiento deficiente",
                    value: data_1[2]
                },
                {
                    label: "Atraso en la llegada de los suministros",
                    value: data_1[3]
                },
                {
                    label: "Fugas, sobrecalentamientos",
                    value: data_1[4]
                }
            ],
            colors: [
                KTApp.getStateColor('success'),
                KTApp.getStateColor('danger'),
                KTApp.getStateColor('warning'),
                KTApp.getStateColor('brand'),
                KTApp.getStateColor('info'),
            ],
        });    
    
        if ($('#grafico_222').length == 0) {
            return;
        }

        Morris.Donut({
            element: 'grafico_222',
            data: [{
                    label: "Deficiente Análisis y modelación",
                    value: data_2[0]
                },
                {
                    label: "Subestimación de los plazos de licitación",
                    value: data_2[1]
                },
                {
                    label: "Plan de ejecución deficiente",
                    value: data_2[2]
                },
                {
                    label: "Falla redes eléctricas",
                    value: data_2[3]
                },
                {
                    label: "Falla correa",
                    value: data_2[4]
                }
            ],
            colors: [
                KTApp.getStateColor('success'),
                KTApp.getStateColor('danger'),
                KTApp.getStateColor('warning'),
                KTApp.getStateColor('brand'),
                KTApp.getStateColor('info'),
            ],
        });    




}

$("#span_detalle").click(function(){
    setTimeout(() => {
        graficosDetalle_5("T18M400");
    }, 8500);
    //graficosDetalle.init();
});