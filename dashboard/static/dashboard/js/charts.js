var graficosDetalle = function(gerencia="GPRO") {
    $('#grafico_1').html("");
    $('#grafico_2').html("");
    $('#grafico_3').html("");
    $('#grafico_4').html("");
    if(gerencia == "GPRO"){
        data_1=[42, 23, 21, 12, 10]
        data_2=[23, 24, 54, 12, 36]
        data_3=[42, 34, 21, 12, 78]
        data_4=[42, 56, 12, 15, 10]
    }
    if(gerencia == "GMIN"){
        data_1=[23, 34, 56, 54, 12]
        data_2=[36, 24, 54, 56, 36]
        data_3=[12, 56, 21, 42, 78]
        data_4=[42, 56, 12, 15, 42]
    }
    if(gerencia == "GSYS"){
        data_1=[34, 56,23,15, 12]
        data_2=[78, 56, 65, 56, 42]
        data_3=[42, 15, 56, 78, 15]
        data_4=[42, 56, 36, 15, 42]
    }
    if(gerencia == "GOBM"){
        data_1=[23,36,18,47,34]
        data_2=[36, 42, 65, 23, 42]
        data_3=[42, 45, 87, 78, 15]
        data_4=[76, 56, 36, 15, 42]
    }
    if(gerencia == "GDI"){
        data_1=[34,65,34,68,23]
        data_2=[34, 42, 78, 23, 42]
        data_3=[36, 45, 87, 78, 78]
        data_4=[45, 68, 23, 15, 42]
    }
    if(gerencia == "GPTA"){
        data_1=[12,45,67,43,76]
        data_2=[45, 42, 78, 23, 42]
        data_3=[36, 42, 78, 23, 78]
        data_4=[12, 76, 34, 15, 43]
    }
    if(gerencia == "GRHU"){
        data_1=[12,78,34,56,34]
        data_2=[45, 42, 23, 12, 42]
        data_3=[76, 54, 78, 23, 12]
        data_4=[42, 76, 23, 15, 43]
    }
    if(gerencia == "GRMD"){
        data_1=[23,54,46,78,45]
        data_2=[54, 42, 23, 12, 42]
        data_3=[76, 23, 46, 23, 12]
        data_4=[54, 46, 23, 15, 43]
    }
    if(gerencia == "GRSW"){
        data_1=[23,65,78,45,23]
        data_2=[12, 87, 23, 12, 42]
        data_3=[89, 45, 12, 23, 12]
        data_4=[23, 46, 23, 23, 65]
    }
    if(gerencia == "GSAE"){
        data_1=[12,45,87,34,23]
        data_2=[23, 87, 23, 12, 42]
        data_3=[23, 87, 34, 23, 12]
        data_4=[12, 45, 23, 87, 65]
    }
    if(gerencia == "GSSO"){
        data_1=[76,34,12,37,83]
        data_2=[23, 87, 23, 12, 42]
        data_3=[34, 87, 34, 23, 65]
        data_4=[76, 45, 23, 87, 65]
    }
    if(gerencia == "GFUN"){
        data_1=[12,89,34,69,12]
        data_2=[76, 12, 23, 12, 42]
        data_3=[34, 69, 42, 89, 65]
        data_4=[23, 87, 23, 87, 65]
    }
    if(gerencia == "GTRH"){
        data_1=[12,56,98,34,23]
        data_2=[76, 56, 23, 98, 42]
        data_3=[12, 23, 23, 89, 42]
        data_4=[23, 87, 34, 87, 69]
    }
        
        $('#grafico_1').html("");
        if ($('#grafico_1').length == 0) {
            return;
        }

        Morris.Donut({
            element: 'grafico_1',
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
    

        if ($('#grafico_2').length == 0) {
            return;
        }

        Morris.Donut({
            element: 'grafico_2',
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
    

        if ($('#grafico_3').length == 0) {
            return;
        }

        Morris.Donut({
            element: 'grafico_3',
            data: [{
                    label: "DPP",
                    value: data_3[0]
                },
                {
                    label: "SMN",
                    value: data_3[1]
                },
                {
                    label: "SIF",
                    value: data_3[2]
                },
                {
                    label: "SMF",
                    value: data_3[3]
                },
                {
                    label: "DPD",
                    value: data_3[4]
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
    

        if ($('#grafico_4').length == 0) {
            return;
        }

        Morris.Donut({
            element: 'grafico_4',
            data: [{
                    label: "Dirección Proyectos Recursos Norte",
                    value: data_4[0]
                },
                {
                    label: "Suptcia. Mina Central",
                    value: data_4[1]
                },
                {
                    label: "Suptcia. Mantenimiento Mina",
                    value: data_4[2]
                },
                {
                    label: "Suptcia. Planta de Flotación de Escoria",
                    value: data_4[3]
                },
                {
                    label: "Suptcia. Ingeniería Fundición",
                    value: data_4[4]
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
        $('#grafico_1').html("");
        $('#grafico_2').html("");
        $('#grafico_3').html("");
        $('#grafico_4').html("");
        graficosDetalle("GPRO");
    }, 1000);
    //graficosDetalle.init();
});