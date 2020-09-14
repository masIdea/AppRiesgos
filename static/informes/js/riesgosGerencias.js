$("#id-gerencias-riesgos-criticos").change(function(){
    $.ajax({
        url:'../trae-riesgos-criticos',
        data:{'gerencia':this.value},
        type:"GET",
        dataType:"json",
        success:function(data){
            $("#id-tb-riesgos-criticos").DataTable().destroy();
            var tbody = ""
            for(k in data){
                tbody+="<tr>"
                tbody+="<td>"+k+"</td>"
                tbody+="<td>"+data[k].causas+"</td>"
                tbody+="<td>"+data[k].descripcion+"</td>"
                tbody+="<td>"+data[k].consecuencias+"</td>"
                tbody+="<td>"+data[k].dueno+"</td>"
                tbody+="<td>"+data[k].inherente+"</td>"
                tbody+="<td>"+data[k].residual+"</td>"
                tbody+="<td>"+data[k].objetivo+"</td>"
                tbody+="<td>"+data[k].otros+"</td>"
                tbody+="</tr>"
            }
            $("#id-cuerpo-riesgos-criticos").html(tbody);
            createDatatable("id-tb-riesgos-criticos", 5);
        }, error:function(err){
            console.error(err);
        }
    })
})

