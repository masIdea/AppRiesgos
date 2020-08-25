var reporteDashboard = function(nivel){
    $("#id-div-links").html("");
    $.ajax({
        url:'../reporte-dashboard',
        data:{'nivel':nivel},
        type:"GET",
        dataType:"json",
        beforeSend: function() {
            $("#id-div-links").html('<div style="float: left;" id="loading-right-direcciones" class="kt-spinner kt-spinner--sm kt-spinner--success"></div>');
            $("#id-div-links").append('<br />');
            $("#id-div-links").append('<span>Por favor espere un momento, los reportes están siendo generados.</span>');
        },  
        success:function(data){
            console.log(data);
            if(data){
                $("#id-div-links").html(
                    "<a href='../view_png/"+data[0]+"' target='_blank'>Reporte En .PNG</a><br /><a target='_blank' href='../view_pdf/"+data[1]+"'>Reporte En .PDF</a>"
                );
            }else{
                $("#id-div-links").html("<span style='color:red'>Ha ocurrido un error al generar el reporte seleccionado, por favor reintente.</span>")
            }
            
        }, error(err){
            console.error(err);
        }
    })
}
