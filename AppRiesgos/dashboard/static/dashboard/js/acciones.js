    $(document).ready(function(){
        $.ajax({
            url:'/dashboard/get-color-indicadores',
            data:{},
            type:"GET",
            dataType:"json",
            success:function(data){                
                for(var i=0; i<data.length;i++){
                    $("#id-spn-kpi-riesgo-"+data[i].tipoindicador).css("background-color", data[i].riesgo);
                    $("#id-spn-kpi-vuln-"+data[i].tipoindicador).css("background-color", data[i].vulnerabilidad);
                }
            }, error:function(err){
                console.error(err);
            }
        });





        Highcharts.chart('container', {

            chart: {
                type: 'bubble',
                plotBorderWidth: 1,
                zoomType: 'xy',
                backgroundColor: 'rgba(0,0,0,0)',
                plotBackgroundImage: '/static/core/highcharts/imgs/degrade_.jpg',
                renderTo: 'chartcontainer'
            },

            credits:false,
            exporting:false,

            legend: {
                enabled: false
            },

            title: {
                text: ''
            },

            subtitle: {
                text: ''
            },

            xAxis: {
                gridLineWidth: 0,
                title: {
                    text: 'Q Eventos'
                },
                labels: {
                    format: '{value}'
                },

            },

            yAxis: {
                gridLineWidth: 0,
                startOnTick: false,
                endOnTick: false,
                title: {
                    text: 'KUS$'
                },
                labels: {
                    format: '{value}'
                },
                maxPadding: 0.2,

            },

            tooltip: {
                useHTML: true,
                headerFormat: '<table>',
                pointFormat: '<tr><th colspan="2"><h3>{point.country}</h3></th></tr>' +
                    '<tr><th>Eventos:</th><td>{point.x}</td></tr>' +
                    '<tr><th>KUS$:</th><td>{point.y}</td></tr>',

                footerFormat: '</table>',
                followPointer: true
            },

            plotOptions: {
                series: {
                    dataLabels: {
                        enabled: true,
                        format: '{point.name}'
                    }
                }
            },

            series: [{
                data: [
                      { x: 438, y: 141497, z:45, name: 'GPTA', country: 'GPTA' },
                    { x: 145, y: 103100, z:41, name: 'GMIN', country: 'GMIN' },
                    { x: 227, y: 83405, z:38, name: 'GRSW', country: 'GRSW' },
                ]
            }]

        });
    });

