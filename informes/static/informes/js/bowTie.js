var bowTie = function(){
    id_riesgo = $("#id-riesgos-gerencia").val();
    $.ajax({
        url:'/informes/riesgos-bowtie',
        data:{'id_riesgo':id_riesgo},
        type:"GET",
        dataType:"json",
        success:function(data){
            $("#id-tb-bowtie").DataTable().destroy();
            var riesgo = data.riesgo;
            var predictivos = ""
            var causas_predictivos = ""
            var correctivos = ""
            var consecuencias_correctivo = ""
            console.log(data.predictivo);
            for(p in data.predictivo){
                predictivos+=p+"<br>";
                console.log(data.predictivo[p].causas);
                for(var i=0;i<data.predictivo[p].causas.length;i++){
                    console.log(data.predictivo[p].causas[i]);
                    causas_predictivos+=data.predictivo[p].causas[i]+"<br>";
                }
            }
            for(c in data.correctivo){
                correctivos+=c+"<br>";
                console.log(data.correctivo[c].consecuencias);
                for(var j=0;j<data.correctivo[c].consecuencias.length;j++){
                    console.log(data.correctivo[c].consecuencias[j]);
                    consecuencias_correctivo+=data.correctivo[c].consecuencias[j]+"<br>";
                }
            }
            tbody="<tr>"
            tbody+="<td>"+predictivos+"</td>"
            tbody+="<td>"+causas_predictivos+"</td>"
            tbody+="<td style='background-color: #ffff002e;'>"+riesgo+"</td>"
            tbody+="<td>"+correctivos+"</td>"
            tbody+="<td>"+consecuencias_correctivo+"</td>"
            tbody+="</tr>"            
            $("#id-cuerpo-bowtie").html(tbody);
            createDatatable("id-tb-bowtie", 5);
            



            
        }, error:function(err){
            console.error(err);
        }
    })
}

