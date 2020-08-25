var datos_cio = function(){
    $.ajax({
        url:"../get-datos-cio",
        type:"GET",
        dataType:"json",
        data:{},
        success:function(data){
            console.log(data);
            var tbody = ""
            for(var i=0; i<data.datos.length;i++){
                tbody+="<tr>";
                tbody+="<td>"+data.datos[i].idcosto+"</td>";
                tbody+="<td>"+data.datos[i].fecha+"</td>";
                tbody+="<td>"+data.datos[i].gerencia+"</td>";
                tbody+="<td>"+data.datos[i].superintendencia+"</td>";
                tbody+="<td>"+data.datos[i].unidadoperacional+"</td>";
                tbody+="<td>"+data.datos[i].tipoobjeto+"</td>";
                tbody+="<td>"+data.datos[i].evento+"</td>";
                tbody+="<td>"+data.datos[i].nivelimpacto+"</td>";
                tbody+="<td>"+data.datos[i].comentarios+"</td>";
                tbody+="<td>"+data.datos[i].cantidaddiasdetencion+"</td>";
                tbody+="<td>"+data.datos[i].cantidadtmfperdidas+"</td>";
                tbody+="<td>"+data.datos[i].areadeevento+"</td>";
                tbody+="<td>"+data.datos[i].superintendenciaevento+"</td>";
                tbody+="<td>"+data.datos[i].proyecto+"</td>";
                tbody+="<td>"+data.datos[i].familia+"</td>";
                tbody+="<td>"+data.datos[i].subproceso+"</td>";
                tbody+="<td>"+data.datos[i].clasificacion+"</td>";
                tbody+="<td>"+data.datos[i].controlesquenofuncionaron+"</td>";
                tbody+="<td>"+data.datos[i].tipofalla+"</td>";
                tbody+="<td>"+data.datos[i].montodeperdida+"</td>";
                tbody+="<td>"+data.datos[i].repeticiondelevento+"</td>";
                tbody+="<td>"+data.datos[i].estadistica+"</td>";
                tbody+='<td><center><i style="cursor:pointer;" onclick="editarCio(\''+data.datos[i].idcio+'\')" class="flaticon2-pen"></i></td>';
                tbody+="</tr>";
            }
            $("#id-cuerpo-datos-cio").html(tbody);
            createDatatable("id-tb-datos-cio");
        }, error:function(err){
            console.error(err);
        }
    });    
}

var editarCio = function(id_registro){
    $("#id-txt-cio").val(id_registro);
    $("#id-form-datos-cio").fadeIn("slow");
    $.ajax({
        url:'../datos-id-cio',
        type:"GET",
        dataType:"json",
        data:{'id':id_registro},
        success:function(data){
            console.log(data);
            $("#id-txt-IdCosto").val(data.datos[0].idcosto)
            $("#id-txt-Fecha").val(data.datos[0].fecha)
            $("#id-txt-Gerencia").val(data.datos[0].gerencia)
            $("#id-txt-SuperIntendencia").val(data.datos[0].superintendencia)
            $("#id-txt-UnidadOperacional").val(data.datos[0].unidadoperacional)
            $("#id-txt-TipoObjeto").val(data.datos[0].tipoobjeto)
            $("#id-txt-Evento").val(data.datos[0].evento)
            $("#id-txt-NivelImpacto").val(data.datos[0].nivelimpacto)
            $("#id-txt-Comentarios").val(data.datos[0].comentarios)
            $("#id-txt-CantidadDiasDetencion").val(data.datos[0].cantidaddiasdetencion)
            $("#id-txt-CantidadTMFPerdidas").val(data.datos[0].cantidadtmfperdidas)
            $("#id-txt-MontoDePerdida").val(data.datos[0].montodeperdida)
            $("#id-txt-RepeticionDelEvento").val(data.datos[0].repeticiondelevento)
            $("#id-txt-Estadistica").val(data.datos[0].estadistica)
            $("#id-txt-AreaDeEvento").val(data.datos[0].areadeevento)
            $("#id-txt-SuperIntendenciaEvento").val(data.datos[0].superintendenciaevento)
            $("#id-txt-Proyecto").val(data.datos[0].proyecto)
            //$("#id-txt-RiesgoAsociadoAlEvento").val(data.datos[0].)
            $("#id-txt-Familia").val(data.datos[0].familia)
            $("#id-txt-SubProceso").val(data.datos[0].subproceso)
            $("#id-txt-Clasificacion").val(data.datos[0].clasificacion)
            $("#id-txt-ControlesQueNoFuncionaron").val(data.datos[0].controlesquenofuncionaron)
            $("#id-txt-TipoFalla").val(data.datos[0].tipofalla)
        }, error:function(err){
            console.error(err);
        }
    })
}
