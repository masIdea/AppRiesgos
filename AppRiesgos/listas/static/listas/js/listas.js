var registros_listas = function(){
    $.ajax({
        url:'registros-listas',
        type:"GET",
        dataType:"json",
        data:{},
        success:function(data){
            console.log(data);
            var tbody = ""
            for(var i = 0; i<data.registros.length; i++){
                tbody+="<tr>"
                tbody+="<td>"+data.registros[i].tipo+"</td>"
                tbody+="<td>"+data.registros[i].glosa+"</td>"
                tbody+="<td>"+data.registros[i].orden+"</td>"
                tbody+="</tr>"
            }
            $("#cuerpo-registros-listas").html(tbody);

            createDatatable("id-tb-listas", 5);
            

        }, error:function(err){
            console.error(err);
        }
    })
}

