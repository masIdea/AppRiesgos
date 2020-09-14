var nivel4 = function(gerencia){
    setTimeout(() => {
        $('#grafico_11').html("");
        $('#grafico_22').html("");
        $('#grafico_33').html("");
        $('#grafico_44').html("");
        graficosDetalle_4(gerencia);
    }, 1000);
    datos = datos_gerencia(gerencia)
    console.log(datos);
    for(var i in datos){
        console.log(i);
        console.log(datos[i]);
    }
    $("#id-span-dato-nivel-seleccionado").html(gerencia);
    var tbody = ""
    var contador = 1;
    for(var i in datos){
        console.log(i);
        console.log(datos[i]);
        tbody+="<tr>";
        tbody+="<td>"+contador+"</td>";
        tbody+="<td>"+i+"</td>";
        tbody+="<td>"+datos[i].monto+"</td>";
        tbody+="<td>"+datos[i].porc_monto+"</td>";
        tbody+="<td>"+datos[i].cantidad+"</td>";
        tbody+="<td>"+datos[i].porc_cantidad+"</td>";
        tbody+="<td>"
        tbody+='<a href="javascript:;" onclick="verMatrizDetalle(\''+i+'\')" class="btn btn-sm btn-clean btn-icon btn-icon-md" title="Ver"><i class="la la-eye"></i></a>';
        tbody+='<a href="javascript:;" onclick="nivel5(\''+i+'\')" class="btn btn-sm btn-clean btn-icon btn-icon-md filtro-eye" title="Siguiente Nivel"><i class="la la-info"></i></a>';
        tbody+='<a href="javascript:;" onclick="graficosDetalle_4(\''+i+'\')" class="btn btn-sm btn-clean btn-icon btn-icon-md filtro-eye" title="Aplicar Filtro"><i class="la la-filter"></i></a>';
        tbody+="</td>";
        tbody+="<td>"+datos[i].kpi+"</td>";
        contador+=1;
    }
    //$("#id-cuerpo-nivel").html(tbody);
    
    $("#modal_nivel").modal("show");
}


var datos_gerencia = function(gerencia){
    objeto = new Object();
    if(gerencia == "GPRO"){        
        objeto['DCR'] = {
            'monto':100,
            'porc_monto':10,
            'cantidad':5,
            'porc_cantidad':5,
            "kpi":'<span class="dot" style="height: 15px;width: 15px;background-color: #f34747;border-radius: 50%;display: inline-block;"></span>'
        }
        objeto['DIP'] = {
            'monto':100,
            'porc_monto':10,
            'cantidad':5,
            'porc_cantidad':5,
            "kpi":'<span class="dot" style="height: 15px;width: 15px;background-color: #f34747;border-radius: 50%;display: inline-block;"></span>'
        }
        objeto['DGS'] = {
            'monto':100,
            'porc_monto':10,
            'cantidad':5,
            'porc_cantidad':5,
            "kpi":'<span class="dot" style="height: 15px;width: 15px;background-color: #f34747;border-radius: 50%;display: inline-block;"></span>'
        }
        objeto['DSP'] = {
            'monto':100,
            'porc_monto':10,
            'cantidad':5,
            'porc_cantidad':5,
            "kpi":'<span class="dot" style="height: 15px;width: 15px;background-color: #f34747;border-radius: 50%;display: inline-block;"></span>'
        }
    }

    return objeto
}
