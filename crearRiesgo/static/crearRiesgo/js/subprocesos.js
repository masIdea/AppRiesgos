$("#riesgo_familia").change(function(){    
    $.ajax({
        url:"trae-subprocesos",
        type:"GET",
        dataType:"json",
        data:{'glosa_familia':this.value},
        success:function(data){
            console.log(data);
            var options = "";
            for(var i =0; i<data.subprocesos.length; i++){
                options+= "<option value='"+data.subprocesos[i].ID+"'>"+data.subprocesos[i].SUBPROCESO+"</option>";
            }
            $("#riesgo_subproceso").html(options);
        }, error:function(err){
            console.error(err);
        }
    })
})