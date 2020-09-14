$(".btnTipoClasificacion").click(function(){    
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
    if ($(this).hasClass("btnClasTipEvenSeleccionado")) {
        $(this).removeClass('btnClasTipEvenSeleccionado');
        
    }else{
        $(this).addClass('btnClasTipEvenSeleccionado');        
    }
    
    $('.btnClasTipEvenSeleccionado').each(function(i) {        
        arregloMeses.push(meses[this.value])
    });
    
    
    $.ajax({
        url:'/dashboard/clasificacion-tipo-evento',
        data:{'meses[]':arregloMeses},
        type:"GET",
        dataType:"json",
        success:function(data){            
            var tbody = ''
            var clasificacion = null
            $("#id-tb-clasificacion-evento").DataTable().destroy();
            var total = 0
            var totalQ = 0
            for(var i=0; i<data.length; i++){                
                for(k in data[i]){                                        
                    for(kk in data[i][k]){
                        if(parseInt(data[i][k][kk].valor)>0){
                            tbody+="<tr>"
                            tbody+="<td>"+mesNumero[data[i][k][kk].mes]+"</td>"
                            tbody+="<td>"+k+"</td>"
                            
                            tbody+="<td>"+kk+"</td>"
                            tbody+="<td>"+numberWithCommas(parseInt(data[i][k][kk].valor))+"</td>"
                            tbody+="<td>"+data[i][k][kk].q+"</td>"
                            tbody+="</tr>"
                            clasificacion=k;
                            total+=data[i][k][kk].valor;
                            totalQ+=data[i][k][kk].q;
                        }
                        
                    }
                    
                }
            }

            var tfoot = '<tr>';
            tfoot += '<td colspan="3"><strong>Total:</strong></td>';
            tfoot += '<td><strong>'+numberWithCommas(parseInt(total))+'</strong></td>';
            tfoot += '<td><strong>'+numberWithCommas(parseInt(totalQ))+'</strong></td>';
            tfoot += '</tr>';
            $("#id-tfoot-clasificacion-evento").html(tfoot);
            
            $("#id-tbody-clasificacion-evento").html(tbody);            
            $('#id-tb-clasificacion-evento').DataTable({
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