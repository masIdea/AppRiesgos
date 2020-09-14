var nivel5 = function(direccion){    
    setTimeout(() => {  
        $('#grafico_111').html("");
        $('#grafico_222').html("");
        graficosDetalle_5(direccion);
    }, 1000);   
    datos = datos_direccion(direccion)
    console.log(datos);
    for(var i in datos){
        console.log(i);
        console.log(datos[i]);
    }
    $("#id-span-dato-nivel-5-seleccionado").html(direccion);
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
        tbody+='<a href="javascript:;" onclick="graficosDetalle_5(\''+i+'\')" class="btn btn-sm btn-clean btn-icon btn-icon-md" title="Ver"><i class="la la-filter"></i></a>';        
        tbody+="</td>";
        tbody+="<td>"+datos[i].kpi+"</td>";
        contador+=1;
        
    }
    $("#id-cuerpo-nivel-5").html(tbody);
    createDatatable("id-tb-nivel-5");
    $("#modal_nivel_5").modal("show");

    $("#id-graf-dir-1").css("display", "none");
    $("#id-graf-dir-2").css("display", "none");

}


var datos_direccion = function(direccion){
    objeto = new Object();
    if(direccion == "DCR"){        
        objeto['T18M400'] = {
            'monto':100,
            'porc_monto':10,
            'cantidad':5,
            'porc_cantidad':5,
            "kpi":'<span class="dot" style="height: 15px;width: 15px;background-color: #f34747;border-radius: 50%;display: inline-block;"></span>'
        }
        objeto['T18M401'] = {
            'monto':100,
            'porc_monto':10,
            'cantidad':5,
            'porc_cantidad':5,
            "kpi":'<span class="dot" style="height: 15px;width: 15px;background-color: #f34747;border-radius: 50%;display: inline-block;"></span>'
        }
        objeto['T18M402'] = {
            'monto':100,
            'porc_monto':10,
            'cantidad':5,
            'porc_cantidad':5,
            "kpi":'<span class="dot" style="height: 15px;width: 15px;background-color: #f34747;border-radius: 50%;display: inline-block;"></span>'
        }
        objeto['T18M403'] = {
            'monto':100,
            'porc_monto':10,
            'cantidad':5,
            'porc_cantidad':5,
            "kpi":'<span class="dot" style="height: 15px;width: 15px;background-color: #f34747;border-radius: 50%;display: inline-block;"></span>'
        }
    }

    return objeto
}


