var datos_dashboard = function(){
    $.ajax({
        url:"../get-datos-dashboard",
        type:"GET",
        dataType:"json",
        data:{},
        success:function(data){
            console.log(data);
            var tbody = ""
            for(var i=0; i<data.length;i++){
                tbody+="<tr>";
                tbody+="<td>"+data[i].fecha+"</td>";
                tbody+="<td>"+data[i].gerencia+"</td>";
                tbody+="<td>"+data[i].superintendencia+"</td>";
                tbody+="<td>"+data[i].unidadoperacional+"</td>";
                tbody+="<td>"+data[i].area+"</td>";
                tbody+="<td>"+data[i].sector+"</td>";
                tbody+="<td>"+data[i].lugar+"</td>";
                tbody+="<td>"+data[i].tipoobjeto+"</td>";
                tbody+="<td>"+data[i].evento+"</td>";
                tbody+="<td>"+data[i].nivelimpacto+"</td>";
                tbody+="<td>"+data[i].comentarios+"</td>";
                tbody+="<td>"+data[i].qhorasdetencion+"</td>";
                tbody+="<td>"+data[i].qdiasdetencion+"</td>";
                tbody+="<td>"+data[i].qktsperdida+"</td>";
                tbody+="<td>"+data[i].qtmfperdida+"</td>";
                tbody+="<td>"+data[i].qlibrasperdida+"</td>";
                tbody+="<td>"+data[i].montoperdidakusd+"</td>";
                tbody+="<td>"+data[i].idriesgoasociado+"</td>";
                tbody+="<td>"+data[i].familia+"</td>";
                tbody+="<td>"+data[i].subproceso+"</td>";
                tbody+="<td>"+data[i].clasificacion+"</td>";
                tbody+="<td>"+data[i].tipofalla+"</td>";
                tbody+='<td><center><i style="cursor:pointer;" onclick="editarDashboard(\''+data[i].idregistro+'\')" class="flaticon2-pen"></i></td>';
                tbody+="</tr>";
            }
            $("#id-cuerpo-datos-dashboard").html(tbody);
            createDatatable("id-tb-datos-dashboard");
        }, error:function(err){
            console.error(err);
        }
    });    
}

var editarDashboard = function(id_registro){
    $("#id-txt-dashboard").val(id_registro);
    $("#id-form-datos-dashboard").fadeIn("slow");
    $.ajax({
        url:'../datos-id-dashboard',
        type:"GET",
        dataType:"json",
        data:{'id':id_registro},
        success:function(data){
            console.log(data);            
            $("#id-txt-Fecha").val(data.datos[0].fecha)
            $("#id-txt-Gerencia").val(data.datos[0].gerencia)
            $("#id-txt-SuperIntendencia").val(data.datos[0].superintendencia)
            $("#id-txt-UnidadOperacional").val(data.datos[0].unidadoperacional)
            $("#id-txt-AreaDeEvento").val(data.datos[0].area)
            $("#id-txt-sector").val(data.datos[0].sector)
            $("#id-txt-lugar").val(data.datos[0].lugar)
            $("#id-txt-TipoObjeto").val(data.datos[0].tipoobjeto)
            $("#id-txt-Evento").val(data.datos[0].evento)
            $("#id-txt-NivelImpacto").val(data.datos[0].nivelimpacto)
            $("#id-txt-Comentarios").val(data.datos[0].comentarios)
            $("#id-txt-q-horas-detencion").val(data.datos[0].qhorasdetencion)
            $("#id-txt-q-dias-detencion").val(data.datos[0].qdiasdetencion)
            $("#id-txt-q-kts-perdida").val(data.datos[0].qktsperdida)
            $("#id-txt-q-tmf-perdida").val(data.datos[0].qtmfperdida)
            $("#id-txt-q-libras-perdida").val(data.datos[0].qlibrasperdida)
            $("#id-txt-monto-perdida-kusd").val(data.datos[0].montoperdidakusd)
            $("#id-txt-riesgo-asociado").val(data.datos[0].idriesgoasociado)
            $("#id-txt-Familia").val(data.datos[0].familia)
            $("#id-txt-SubProceso").val(data.datos[0].subproceso)
            $("#id-txt-Clasificacion").val(data.datos[0].clasificacion)
            $("#id-txt-TipoFalla").val(data.datos[0].tipofalla)
        }, error:function(err){
            console.error(err);
        }
    })
}

