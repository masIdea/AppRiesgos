var seguimientoPlanDeAccion = function(){
    id_gerencia = $("#id-gerencias").val();
    $.ajax({
        url:'/informes/detalle-seguimiento-plan-accion',
        data:{'id_gerencia':id_gerencia},
        type:"GET",
        dataType:"json",
        success:function(data){
            window.open("../view_pdf/"+data);
        }
    })
}
