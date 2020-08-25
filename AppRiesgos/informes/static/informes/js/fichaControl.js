var fichaControl = function(){
    id_riesgo = $("#id-riesgos-gerencia").val();
    $.ajax({
        url:'/informes/riesgos-ficha-control',
        data:{'id_riesgo':id_riesgo},
        type:"GET",
        dataType:"json",
        success:function(data){
            window.open("../view_pdf/"+data);
        }
    })
}
