$(".btnTipoClasificacionGerencia").click(function(){    
    var mesGlosa = this.value;
    var meses = {   'Enero':1,
                'Febrero':2,
                'Marzo':3,
                'Abril':4,
                'Mayo':5,
                'Junio':6,
                'Julio':7,
                'Agosto':8,
                'Septiembre':9,
                'Octubre':10,
                'Noviembre':11,
                'Diciembre':12,
            }    
    
    var mesNumero = {'1':"Enero",'2':"Febrero",'3':"Marzo",'4':"Abril",'5':"Mayo",'6':"Junio",'7':"Julio",'8':"Agosto",'9':"Septiembre",'10':"Octubre",'11':"Noviembre",'12':"Diciembre",};
    var arregloMeses = []
    if ($(this).hasClass("btnClassTipEvenSeleccionadoGerencia")) {
        $(this).removeClass('btnClassTipEvenSeleccionadoGerencia');
        
    }else{
        $(this).addClass('btnClassTipEvenSeleccionadoGerencia');        
    }
    
    $('.btnClassTipEvenSeleccionadoGerencia').each(function(i) {        
        arregloMeses.push(meses[this.value])
    });

    
    var gerencia = $("#id-select-listado-gerencia").val();
    $.ajax({
        url:'/dashboard/clasificacion-gerencia',
        data:{'meses[]':arregloMeses, 'gerencia':gerencia},
        type:"GET",
        dataType:"json",
        success:function(data){
            console.log(data);
            var tbody = ''
            var clasificacion = null;
            $("#id-tb-clasificacion-gerencia").DataTable().destroy();
            var total = 0
            var totalQ = 0
            for(var i=0; i<data.length; i++){
                for(k in data[i]){        
                    console.log(data[i][k])   
                    tbody+="<tr>"
                    tbody+="<td>"+mesNumero[data[i][k].mes]+"</td>"
                    tbody+="<td>"+gerencia+"</td>"
                    
                    tbody+="<td>"+k+"</td>"
                    tbody+="<td>"+numberWithCommas(parseInt(data[i][k].valor))+"</td>"
                    tbody+="<td>"+data[i][k].q+"</td>"
                    tbody+="</tr>"
                    clasificacion=k;   
                    total+=parseInt(data[i][k].valor);
                    totalQ+=parseInt(data[i][k].q);                                      
                }
            }
            var tfoot = '<tr>';
            tfoot += '<td colspan="3"><strong>Total:</strong></td>';
            tfoot += '<td><strong>'+numberWithCommas(total)+'</strong></td>';
            tfoot += '<td><strong>'+numberWithCommas(totalQ)+'</strong></td>';
            tfoot += '</tr>';
            $("#id-tfoot-clasificacion-gerencia").html(tfoot);                                    
            $("#id-tbody-clasificacion-gerencia").html(tbody);
            
            $('#id-tb-clasificacion-gerencia').DataTable({
                searching: false, info: false,
                "pageLength": 8, 
                "order": [[ 3, "desc" ]],
                        "language": {
                            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
                        }
                });
        }, error:function(err){
            console.error(err);
        }
    })
})