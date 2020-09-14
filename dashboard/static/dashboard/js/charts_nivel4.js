var graficosDetalle_4 = function(direccion) {
    $('#grafico_11').html("");
    $('#grafico_22').html("");
    $('#grafico_33').html("");
    $('#grafico_44').html("");
    if(direccion == "DCR"){
        data_1=[42, 23, 21, 12, 10]
        data_2=[23, 24, 54, 12, 36]
        data_3=[42, 34, 21, 12, 78]
        data_4=[42, 56, 12, 15, 10]
    }
    if(direccion == "DIP"){
        data_1=[23, 34, 56, 54, 12]
        data_2=[36, 24, 54, 56, 36]
        data_3=[12, 56, 21, 42, 78]
        data_4=[42, 56, 12, 15, 42]
    }
    if(direccion == "DGS"){
        data_1=[34, 56,23,15, 12]
        data_2=[78, 56, 65, 56, 42]
        data_3=[42, 15, 56, 78, 15]
        data_4=[42, 56, 36, 15, 42]
    }
    if(direccion == "DSP"){
        data_1=[23,36,18,47,34]
        data_2=[36, 42, 65, 23, 42]
        data_3=[42, 45, 87, 78, 15]
        data_4=[76, 56, 36, 15, 42]
    }

        $('#grafico_11').html("");
        if ($('#grafico_11').length == 0) {
            return;
        }

        Morris.Donut({
            element: 'grafico_11',
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
    
        if ($('#grafico_22').length == 0) {
            return;
        }

        Morris.Donut({
            element: 'grafico_22',
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
    
        if ($('#grafico_33').length == 0) {
            return;
        }

        Morris.Donut({
            element: 'grafico_33',
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
    
        if ($('#grafico_44').length == 0) {
            return;
        }

        Morris.Donut({
            element: 'grafico_44',
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
        $('#grafico_11').html("");
        $('#grafico_22').html("");
        $('#grafico_33').html("");
        $('#grafico_44').html("");
        graficosDetalle_4("DCR");
    }, 7000);
    //graficosDetalle.init();
});