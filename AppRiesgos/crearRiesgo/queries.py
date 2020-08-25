from django.db import connection

def QueryRiesgoSimilar(descripcion_riesgo = None):        
    arreglo=[]
    cursor = connection.cursor()
    try:
        cursor.execute("CALL sp_riesgos_like_descripcion ('"+descripcion_riesgo+"');")
        result_set = cursor.fetchall()
        for data in result_set:            
            arreglo.append({
                            'RIESGO':str(data[0]),                            
                            })
            
    finally:
        cursor.close()  
    return arreglo

def QueryFamilia():        
    arreglo=[]
    cursor = connection.cursor()
    try:
        cursor.execute("CALL sp_riesgos_trae_familias;")
        result_set = cursor.fetchall()
        for data in result_set:            
            arreglo.append({
                            'FAMILIA':str(data[0]),                            
                            })
            
    finally:
        cursor.close()  
    return arreglo


def QuerySubproceso(familia = None):        
    arreglo=[]
    cursor = connection.cursor()
    try:
        cursor.execute("CALL sp_riesgos_trae_subproceso ('"+familia+"');")
        result_set = cursor.fetchall()
        for data in result_set:            
            arreglo.append({
                            'ID':str(data[0]), 
                            'SUBPROCESO':str(data[1]),                            
                            })
            
    finally:
        cursor.close()  
    return arreglo

def QueryTraeRiesgos(familia = None):        
    arreglo=[]
    cursor = connection.cursor()
    try:
        cursor.execute("CALL sp_riesgos_trae_riesgos;")
        result_set = cursor.fetchall()
        for data in result_set:            
            arreglo.append({
                            'Gerencia':str(data[0]), 
                            'Direccion':str(data[1]),                            
                            'Proyecto':str(data[2]),
                            'codigoProyecto':str(data[3]),
                            'FasedelRiesgo':str(data[4]),
                            'dueno':str(data[5]),
                            'CargoDelDueño':str(data[6]),
                            'estado':str(data[7]),
                            'estadoValidacion':str(data[8]),
                            'estadoRegistro':str(data[9]),
                            'Clasificacion':str(data[10]),
                            'SubProceso':str(data[11]),
                            'Familia':str(data[12]),
                            'Riesgo':str(data[13]),
                            'IdRiesgo':str(data[14]),
                            'Directic':str(data[15]),
                            })
            
    finally:
        cursor.close()  
    return arreglo


    
