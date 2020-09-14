var trae_riesgos_criticos_x_gerencia = function(){
    $('#div_riesgos_criticos_gerencia').html("");
    $("#id-contenedor-riesgos-criticos-gerencia").html("");
    $.ajax({
        url:'/dashboard/trae-riesgos-criticos',
        type:"GET",
        dataType:"json",
        data:{},
        beforeSend:function(){
            $("#loading-riesgos-criticos").css("display", "block");
        },
        success:function(data){            
            objeto = Object();
            arreglo = [];
            arreglo_colores = []
            cuerpo_contenedor_gerencias = ""
            for(key in data){
                arreglo.push(
                    objeto={
                        label:key,
                        value:data[key]['cantidad']
                    }
                )
                arreglo_colores.push(
                    KTApp.getStateColor(data[key]['color'])
                )
                cuerpo_contenedor_gerencias += '<div class="kt-widget14__legend">'
                cuerpo_contenedor_gerencias +=    '<span class="kt-widget14__bullet kt-bg-'+data[key]['color']+'"></span>'
                cuerpo_contenedor_gerencias +=    '<span class="kt-widget14__stats">'+data[key]['porcentaje']+'% '+key+'</span>'
                cuerpo_contenedor_gerencias += '</div>'
            }
            $("#id-contenedor-riesgos-criticos-gerencia").html(cuerpo_contenedor_gerencias);
            grafico_riesgos_criticos_gerencia(arreglo, arreglo_colores);
            $("#loading-riesgos-criticos").css("display", "none");
        }, error:function(err){
            console.error(err);
        }
    });
}

var trae_detalle_riesgos_criticos_x_gerencia = function(){
    $("#id-cuerpo-tb-gerencias-riesgos-criticos").html("");
    $("#id-tipo-nivel").val("GERENCIA");
    $.ajax({
        url:'/dashboard/trae-detalle-criticos',
        type:"GET",
        dataType:"json",
        data:{},
        beforeSend:function(){
            $("#cargando-datos-tabla").css("display", "block");
        },
        success:function(data){                        
            var cuerpo_tabla = ""
            contador = 1;
            for(key in data){
                cuerpo_tabla+="<tr>"
                cuerpo_tabla+="<td>"+contador+"</td>"
                cuerpo_tabla+="<td>"+key+"</td>"
                if(data[key]['monto_perdida_critica'] == null){
                    cuerpo_tabla+="<td>0</td>"
                }else{
                    cuerpo_tabla+="<td>"+data[key]['monto_perdida_critica']+"</td>"
                }                
                cuerpo_tabla+="<td>"+data[key]['porcentaje_mus_perdida']+"</td>"
                cuerpo_tabla+="<td>"+data[key]['cantidad_riesgos_gerencia']+"</td>"
                cuerpo_tabla+="<td>"+data[key]['porc_riesgos_criticos']+"</td>"                
                cuerpo_tabla+='<td><a href="javascript:;" onclick="verMatriz(\''+key+'\')" class="btn btn-sm btn-clean btn-icon btn-icon-md" title="Ver"><i class="la la-eye"></i></a>'
                cuerpo_tabla+='<a href="javascript:;" onclick="cambia_gerencia(\''+key+'\')" class="btn btn-sm btn-clean btn-icon btn-icon-md filtro-eye-graf" title="Aplicar Filtro"><i class="la la-filter"></i></a>'
                cuerpo_tabla+='<a href="javascript:;" onclick="nivel4(\''+key+'\')" class="btn btn-sm btn-clean btn-icon btn-icon-md filtro-info" title="Siguiente Nivel"><i class="la la-info"></i></a></td>'
                if(data[key]['cantidad_riesgos_criticos']>0){
                    cuerpo_tabla+='<td><span style="overflow: visible; position: relative; width: 110px;"><span class="dot" style="height: 15px;width: 15px;background-color: #f34747;border-radius: 50%;display: inline-block;"></span></span>&nbsp; '+data[key]['cantidad_riesgos_criticos']+'</td>'
                }else{
                    cuerpo_tabla+="<td></td>"
                }
                cuerpo_tabla+="</tr>";
                contador+=1;                
            }
            $("#id-cuerpo-tb-gerencias-riesgos-criticos").html(cuerpo_tabla);
            createDatatable("id-tb-gerencias-riesgos-criticos", 5);
            $("#cargando-datos-tabla").css("display", "none");
        }, error:function(err){
            console.error(err);
        }
    });
}

var trae_causas_riesgos_criticos = function(tipo){
    $('#grafico_1').html("");
    $('#grafico_2').html("");
    $("#cuerpo-contenedor-causas").html("");
    $("#cuerpo-contenedor-causas-valorizadas").html("");
    var tipo_datos = $("#id-txt-tipo").val();
    $.ajax({
        url:'/dashboard/trae-causas-riesgos-criticos',
        type:"GET",
        dataType:"json",
        data:{'tipo':tipo, 'tipo_datos':tipo_datos, 'nivel': 1},
        beforeSend:function(){
            $("#loading-causas-riesgos-criticos").css("display", "block");
            $("#loading-causas-riesgos-criticos-valorizados").css("display", "block");
            
        },
        success:function(data){            
            objeto = Object();
            arreglo_objeto = [];
            arreglo_valorizados = [];
            arreglo_colores = [];
            cuerpo_contenedor_causas= "";
            for(key in data){
                arreglo_objeto.push(
                    objeto={
                        label:key,
                        value:data[key]['cantidad']
                    }
                )
                arreglo_valorizados.push(
                    objeto={
                        label:key,
                        value:data[key]['valor']
                    }
                )
                arreglo_colores.push(
                    data[key]['color']
                )

                cuerpo_contenedor_causas += '<div class="kt-widget14__legend">'
                cuerpo_contenedor_causas +=    '<span class="kt-widget14__bullet" style="background-color:'+data[key]['color']+'"></span>'
                cuerpo_contenedor_causas +=    '<span class="kt-widget14__stats">'+key+'</span>'
                cuerpo_contenedor_causas += '</div>'
            };
            

            
            setTimeout(() => {
                grafico_num_causas_riesgos_criticos(arreglo_objeto, arreglo_colores);
                grafico_num_causas_valorizadas_riesgos_criticos(arreglo_valorizados, arreglo_colores);
                $("#cuerpo-contenedor-causas").html(cuerpo_contenedor_causas);
                $("#cuerpo-contenedor-causas-valorizadas").html(cuerpo_contenedor_causas);
                $("#loading-causas-riesgos-criticos").css("display", "none");
                $("#loading-causas-riesgos-criticos-valorizados").css("display", "none");
            }, 1000);
            
        }, error:function(err){
            console.error(err);
        }
    });
}

var trae_riesgos_por_gerencia = function(tipo){
    $('#grafico_3').html("");
    $("#id-contenedor-riesgos-direcciones").html("");
    var tipo_datos = $("#id-txt-tipo").val();
    $.ajax({
        url:'/dashboard/trae-riesgos-por-direccion',
        type:"GET",
        dataType:"json",
        data:{'tipo':tipo, 'tipo_datos':tipo_datos, 'nivel':1},
        beforeSend:function(){
            $("#loading-causas-riesgos-direcciones").css("display", "block");
        },
        success:function(data){
            objeto = Object();
            arreglo_objeto_direcciones = [];
            arreglo_valorizados = [];
            arreglo_colores = [];
            cuerpo_contenedor_riesgos_direcciones= "";
            for(key in data){
                arreglo_objeto_direcciones.push(
                    objeto={
                        label:key,
                        value:data[key]['cantidad']
                    }
                )
                arreglo_colores.push(
                    data[key]['color']
                )

                cuerpo_contenedor_riesgos_direcciones += '<div class="kt-widget14__legend">'
                cuerpo_contenedor_riesgos_direcciones +=    '<span class="kt-widget14__bullet" style="background-color:'+data[key]['color']+'"></span>'
                cuerpo_contenedor_riesgos_direcciones +=    '<span class="kt-widget14__stats">'+key+'</span>'
                cuerpo_contenedor_riesgos_direcciones += '</div>'
            };            
            setTimeout(() => {                
                grafico_num_riesgos_direccion(arreglo_objeto_direcciones, arreglo_colores);
                $("#id-contenedor-riesgos-direcciones").html(cuerpo_contenedor_riesgos_direcciones);
                $("#loading-causas-riesgos-direcciones").css("display", "none");
            }, 1000);

        }, error:function(err){
            console.error(err);
        }
    });
}

var trae_riesgos_por_direccion_valorizados = function(tipo){
    $('#grafico_4').html("");
    $("#id-contenedor-riesgos-direcciones-valorizados").html("");
    var tipo_datos = $("#id-txt-tipo").val();
    $.ajax({
        url:'/dashboard/trae-riesgos-por-direccion-valorizados',
        type:"GET",
        dataType:"json",
        data:{'tipo':tipo, 'tipo_datos':tipo_datos, 'nivel':1},
        beforeSend:function(){
            $("#loading-causas-riesgos-direcciones-valorizadas").css("display", "block");
        },
        success:function(data){
            objeto = Object();
            arreglo_objeto_direcciones_valorizados = [];            
            arreglo_colores = [];
            cuerpo_contenedor_riesgos_direcciones_valorizados= "";
            for(key in data){
                arreglo_objeto_direcciones_valorizados.push(
                    objeto={
                        label:key,
                        value:Math.round(parseInt(data[key]['cantidad']), 2)
                    }
                )
                arreglo_colores.push(
                    data[key]['color']
                )

                cuerpo_contenedor_riesgos_direcciones_valorizados += '<div class="kt-widget14__legend">'
                cuerpo_contenedor_riesgos_direcciones_valorizados +=    '<span class="kt-widget14__bullet" style="background-color:'+data[key]['color']+'"></span>'
                cuerpo_contenedor_riesgos_direcciones_valorizados +=    '<span class="kt-widget14__stats">'+key+'</span>'
                cuerpo_contenedor_riesgos_direcciones_valorizados += '</div>'
            };
            console.log("COLORES ", arreglo_colores)
            setTimeout(() => {                
                grafico_num_riesgos_direccion_valorizados(arreglo_objeto_direcciones_valorizados, arreglo_colores);
                $("#id-contenedor-riesgos-direcciones-valorizados").html(cuerpo_contenedor_riesgos_direcciones_valorizados);
                $("#loading-causas-riesgos-direcciones-valorizadas").css("display", "none");
            }, 1000);

        }, error:function(err){
            console.error(err);
        }
    });
}


var grafico_riesgos_criticos_gerencia = function(datos, arreglo_colores) {
    if ($('#div_riesgos_criticos_gerencia').length == 0) {
        return;
    }
    Morris.Donut({
        element: 'div_riesgos_criticos_gerencia',
        data: datos,
        colors:arreglo_colores,        
    });
}

var grafico_num_causas_riesgos_criticos = function(datos, arreglo_colores){
    $('#grafico_1').html("");
        if ($('#grafico_1').length == 0) {
            return;
        }
        Morris.Donut({
            element: 'grafico_1',
            data: datos,
            colors: arreglo_colores,
        });
}

var grafico_num_causas_valorizadas_riesgos_criticos = function(datos, arreglo_colores){
    $('#grafico_2').html("");
        if ($('#grafico_2').length == 0) {
            return;
        }
        Morris.Donut({
            element: 'grafico_2',
            data: datos,
            colors: arreglo_colores,
        });
}

var grafico_num_riesgos_direccion = function(datos, arreglo_colores){
    $('#grafico_3').html("");
        if ($('#grafico_3').length == 0) {
            return;
        }
        Morris.Donut({
            element: 'grafico_3',
            data: datos,
            colors: arreglo_colores,
        });
}

var grafico_num_riesgos_direccion_valorizados = function(datos, arreglo_colores){
    $('#grafico_4').html("");
        if ($('#grafico_4').length == 0) {
            return;
        }
        Morris.Donut({
            element: 'grafico_4',
            data: datos,
            colors: arreglo_colores,
        });
}
