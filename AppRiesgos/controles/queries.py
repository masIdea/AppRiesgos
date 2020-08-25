from django.db import connection

def QueryRiesgoCausas(id_riesgo = None):        
    arreglo=[]
    cursor = connection.cursor()
    try:
        cursor.execute("CALL sp_riesgos_causa_riesgo ('"+str(id_riesgo)+"');")
        result_set = cursor.fetchall()
        for data in result_set:            
            arreglo.append({
                            'CAUSA':str(data[0]),                            
                            'IdCausa':str(data[1]),   
                            })
            
    finally:
        cursor.close()  
    return arreglo

def QueryRiesgoConsecuencias(id_riesgo = None):        
    arreglo=[]
    cursor = connection.cursor()
    try:
        cursor.execute("CALL sp_riesgos_consecuencias_riesgo ('"+str(id_riesgo)+"');")
        result_set = cursor.fetchall()
        for data in result_set:            
            arreglo.append({
                            'CONSECUENCIA':str(data[0]),       
                            'IdConsecuencia':str(data[1]),                            
                            })
            
    finally:
        cursor.close()  
    return arreglo

def QueryRiesgosControlesCreados(riesgo = None):      
    print("EXEC [dbo].[sp_riesgos_controles_creados] '"+str(riesgo)+"'")
    arreglo=[]
    cursor = connection.cursor()
    try:
        cursor.execute("CALL sp_riesgos_controles_creados ('"+str(riesgo)+"');")
        result_set = cursor.fetchall()
        for data in result_set:            
            arreglo.append({
                            'IDCONTROL':str(data[0]),
                            'IDRIESGO':str(data[1]),
                            'NOMBRECONTROL':str(data[2]),
                            'DESCRIPCIONCONTROL':str(data[3]),
                            'TIPOCONTROL':str(data[4]),
                            'DUENOCONTROL':str(data[5]),
                            'FRECUENCIACONTROL':str(data[6]),
                            'ESTADOREGISTRO':str(data[7]),
                            })
            
    finally:
        cursor.close()  
    return arreglo


def QueryRiesgosControlesAsociados(id_riesgo = None):        
    arreglo=[]
    cursor = connection.cursor()
    try:
        cursor.execute("CALL sp_riesgos_controles_asociados ('"+str(id_riesgo)+"');")
        result_set = cursor.fetchall()
        for data in result_set:            
            arreglo.append({
                            'IDCONTROL':str(data[0]),
                            'IDRIESGO':str(data[1]),
                            'NOMBRECONTROL':str(data[2]),
                            'DESCRIPCIONCONTROL':str(data[3]),
                            'TIPOCONTROL':str(data[4]),
                            'DUENOCONTROL':str(data[5]),
                            'FRECUENCIACONTROL':str(data[6]),
                            'ESTADOREGISTRO':str(data[7]),
                            })
            
    finally:
        cursor.close()  
    return arreglo

def QueryDatosControl(id_control = None):        
    arreglo=[]
    cursor = connection.cursor()
    try:
        cursor.execute("CALL sp_riesgos_datos_control ('"+str(id_control)+"');")
        result_set = cursor.fetchall()
        for data in result_set:            
            arreglo.append({
                            'IdControl':str(data[0]),
                            'IdRiesgo':str(data[1]),
                            'NombreControl':str(data[2]),
                            'DescripcionControl':str(data[3]),
                            'TipoControl':str(data[4]),
                            'DuenoControl':str(data[5]),
                            'FrecuenciaControl':str(data[6]),
                            'EstadoRegistro':str(data[7]),
                            })
            
    finally:
        cursor.close()  
    return arreglo


def QueryCausasControl(id_control = None):        
    arreglo=[]
    cursor = connection.cursor()
    try:
        cursor.execute("CALL sp_riesgos_causas_control ('"+str(id_control)+"');")
        result_set = cursor.fetchall()
        for data in result_set:            
            arreglo.append({
                            'IdCausa':str(data[0]),
                            'Causa':str(data[1]),                        
                            })
            
    finally:
        cursor.close()  
    return arreglo

def QueryConsecuenciasControl(id_control = None):        
    arreglo=[]
    cursor = connection.cursor()
    try:
        cursor.execute("CALL sp_riesgos_consecuencias_control ('"+str(id_control)+"');")
        result_set = cursor.fetchall()
        for data in result_set:            
            arreglo.append({
                            'IdConsecuencia':str(data[0]),
                            'Consecuencia':str(data[1]),                        
                            })
            
    finally:
        cursor.close()  
    return arreglo


def QueryAutoevaluacionControl(id_control = None):        
    arreglo=[]
    cursor = connection.cursor()
    try:
        cursor.execute("CALL sp_riesgos_autoevaulacion_control ('"+str(id_control)+"');")
        result_set = cursor.fetchall()
        for data in result_set:            
            arreglo.append({
                            'eficacia':str(data[2]),
                            'eficiencia':str(data[3]),                        
                            'efectividad':str(data[4]),
                            })
            
    finally:
        cursor.close()  
    return arreglo


def QueryMonitoreoControl(id_control = None):        
    arreglo=[]
    cursor = connection.cursor()
    try:
        cursor.execute("CALL sp_riesgos_monitoreo_control ('"+str(id_control)+"');")
        result_set = cursor.fetchall()
        for data in result_set:            
            arreglo.append({
                            'frecuencia':str(data[2]),
                            'inicio':str(data[3]),                        
                            'fin':str(data[4]),
                            })
            
    finally:
        cursor.close()  
    return arreglo
    

def QueryEvidenciaControl(id_control = None):        
    arreglo=[]
    cursor = connection.cursor()
    try:
        cursor.execute("CALL sp_riesgos_evidencia_control ('"+str(id_control)+"');")
        result_set = cursor.fetchall()
        for data in result_set:            
            arreglo.append({
                            'tipo_contenido':str(data[0]),
                            'archivo':str(data[1]),                                                    
                            })
            
    finally:
        cursor.close()  
    return arreglo
    
