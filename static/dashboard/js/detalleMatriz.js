$(".r-circle").click(function(){
    var directic = 0
    if($('#id-chk-directic').prop("checked") == true){
        directic = 1
    }
    coordenadas = this.id.split("_")
    x = coordenadas[3];
    y = coordenadas[2];
    tipo_matriz = coordenadas[0];
    gerencia = $("#id-txt-gerencia-matriz").val();
    $("#id-cuerpo-detalle-riesgos-matriz").html("");
    $.ajax({
        url:'detalle-coordenada-matriz',
        type:"GET",
        dataType:"json",
        data:{'X':x, "Y":y, "tipo_matriz":tipo_matriz, "gerencia":gerencia, "directic":directic},
        success:function(data){
            $("#id-tb-matriz-detalle").DataTable().destroy();
            $("#id-cuerpo-detalle-riesgos-matriz").html("");
            var tbody = ""
            for(var i = 0; i<data.length; i++){
                tbody+="<tr>";
                tbody+="<td>"+data[i].riesgo+"</td>";
                tbody+="<td>"+data[i].gerencia+"</td>";
                tbody+="<td>"+data[i].direccion+"</td>";
                tbody+="<td>"+data[i].dueño+"</td>";
                tbody+="</tr>";
            }
            
            $("#id-cuerpo-detalle-riesgos-matriz").html(tbody);
            
            if(tipo_matriz=="res"){
                tipo_matriz = "Residual";
            }else if(tipo_matriz=="inhe"){
                tipo_matriz = "Inherente";
            }else if(tipo_matriz=="obj"){
                tipo_matriz = "Objetivo";
            }
            $("#id-titulo-detalle-matriz").html("Detalle Matriz "+tipo_matriz+" Impacto <b>"+y+"</b> Probabilidad <b>"+x+"</b>"); 
            
            $("#id-modal-detalle-matriz").css("background-color", "#0000004d");
            $("#id-modal-detalle-matriz").modal("show");
            createDatatable("id-tb-matriz-detalle", 5);

        }, error:function(err){
            console.error(err);
        }
    })

    
    //$("#id-cuerpo-detalle-riesgos-matriz").html("");

})
