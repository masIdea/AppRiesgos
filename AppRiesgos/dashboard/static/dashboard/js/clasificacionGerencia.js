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

    
    
    $.ajax({
        url:'clasificacion-gerencia',
        data:{'meses':meses[mesGlosa]},
        type:"GET",
        dataType:"json",
        success:function(data){
            console.log(data);
            var tbody = ''
            var clasificacion = null
            for(k in data){
                for(kk in data[k]){
                    tbody+="<tr>"
                    tbody+="<td>"+mesGlosa+"</td>"
                    tbody+="<td>"+k+"</td>"
                    
                    tbody+="<td>"+kk+"</td>"
                    tbody+="<td>"+numberWithCommas(parseInt(data[k][kk].valor))+"</td>"
                    tbody+="<td>"+data[k][kk].q+"</td>"
                    tbody+="</tr>"
                    clasificacion=k;
                }                
            }
            console.log(tbody)
            $("#id-tbody-clasificacion-gerencia").html(tbody);
        }, error:function(err){
            console.error(err);
        }
    })
})