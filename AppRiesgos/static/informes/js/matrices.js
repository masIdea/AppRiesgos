var matrices = function(){
    $.ajax({
        url:"../matrices-riesgos",
        type:"get",
        dataType:"json",
        data:{
                "gerencia":$("#id-gerencias-riesgos-criticos").val(), 
                "riesgo":$("#id-riesgos-gerencia").val(),
                "fecha_inicio":$("#id-fecha-inicio").val(),
                "fecha_termino":$("#id-fecha-termino").val(),
            },
        success:function(data){            
            window.open("../view_pdf/"+data);
        }, error:function(err){ 
            console.error(err);
        }
    })
}

$("#id-gerencias-riesgos-criticos").change(function(){
    $("#id-riesgos-gerencia").html("<option value='' selected disabled>Seleccione</option>");
    $.ajax({
        url:'../riesgos-gerencia',
        type:"get",
        dataType:'json',
        data:{'sigla_gerencia':this.value},
        success:function(data){
            var option_riesgos = ""
            for(var i = 0; i<data.riesgos.length; i++){
                option_riesgos+="<option value='"+data.riesgos[i].idriesgo+"&"+data.riesgos[i].riesgo+"'>"+data.riesgos[i].riesgo+"</option>"
            }
            $("#id-riesgos-gerencia").append(option_riesgos);
            console.log(data);
        }, error:function(err){
            console.error(err);
        }
    })
})
