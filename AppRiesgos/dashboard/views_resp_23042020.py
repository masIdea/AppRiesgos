from django.shortcuts import render
from kpiDashboard.models import RiesgoKpi
from core.models import Riesgo, RiesgoListas, RiesgoCargasistemacio, RiesgoCargasisteman1, Gerencias, RiesgoEvaluacioncualitativainherente, RiesgoEvaluacioncualitativaresidual, RiesgoEvaluacioncualitativaobjetivo, RiesgoProbImp, RiesgoNCausariesgo, RiesgoCausas, RiesgoUnifica
from datetime import datetime
from django.http import JsonResponse
from collections import OrderedDict
import operator
from django.db.models import Sum
from dashboard.clases.RiesgosCriticos import RiesgosCriticos

# Create your views here.
def inicio(request):
    mes = datetime.now().month
    ano = datetime.now().year                
    kpi_costo_presupuesto = list(RiesgoKpi.objects.filter(ano=ano, mes=mes, tipo="Costo Presupuesto").order_by('-fecreg').values())
    kpi_produccion = list(RiesgoKpi.objects.filter(ano=ano, mes=mes, tipo="Producción").order_by('-fecreg').values())
    kpi_seguridad = list(RiesgoKpi.objects.filter(ano=ano, mes=mes, tipo="Seguridad").order_by('-fecreg').values())
    kpi_ambiental = list(RiesgoKpi.objects.filter(ano=ano, mes=mes, tipo="Ambiental").order_by('-fecreg').values())

    atraso_proyecto = kpiAtrasoProyecto()
    probidad_transparencia = kpiProbidadTransparencia()
    falta_agua = kpiFaltaAgua()
    falla_equipo_critico = kpiFallaEquipoCritico()
    incendio = kpiIncendio()
    #riesgos_totales = riesgosGerencias()
    #clasificaciones_riesgos = getRiesgoClasificaciones()


    cantidad_riesgos_acumulados = len(list(RiesgoUnifica.objects.all().values()))
    cantidad_riesgos_mes = len(list(RiesgoUnifica.objects.filter(fecha__year=datetime.now().year, fecha__month=datetime.now().month).values()))

    #cantidad_riesgos_acumulados = len(list(Riesgo.objects.all().values()))
    #cantidad_riesgos_mes = len(list(Riesgo.objects.filter(fechadigita__year=datetime.now().year, fechadigita__month=datetime.now().month).values()))

    eventos_materializados = impactoFinancieroEventosMaterializados()    


    data = {
        'kpi_costo_presupuesto':kpi_costo_presupuesto,
        'kpi_produccion':kpi_produccion,
        'kpi_seguridad':kpi_seguridad,
        'kpi_ambiental':kpi_ambiental,

        'atraso_proyecto':atraso_proyecto,
        'probidad_transparencia':probidad_transparencia,
        'falta_agua':falta_agua,
        'falla_equipo_critico':falla_equipo_critico,
        'incendio':incendio,
        'cantidad_riesgos_acumulados':cantidad_riesgos_acumulados,
        'cantidad_riesgos_mes':cantidad_riesgos_mes,
        'eventos_materializados':eventos_materializados,
    }
    

    return render(request, "dashboard/index.html", data)

def kpiAtrasoProyecto():
    riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion="Atraso Proyecto").values())
    num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
    suma = 0
    for atraso in riesgos_atraso_proyecto_acum:
        suma += atraso['maximaperdidamus']
    suma = suma * 100

    riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Atraso Proyecto", fechadigita__year=datetime.now().year, fechadigita__month=datetime.now().month).values())
    num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
    suma_mes = 0
    for atraso_mes in riesgos_atraso_proyecto:
        suma_mes += atraso_mes['maximaperdidamus']
    suma_mes = suma_mes * 100

    data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':suma, 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':suma_mes}
    return data


def kpiProbidadTransparencia():
    riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion="Providad y Transparencia").values())
    num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
    suma = 0
    for atraso in riesgos_atraso_proyecto_acum:
        suma += atraso['maximaperdidamus']
    suma = suma * 100

    riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Providad y Transparencia", fechadigita__year=datetime.now().year, fechadigita__month=datetime.now().month).values())
    num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
    suma_mes = 0
    for atraso_mes in riesgos_atraso_proyecto:
        suma_mes += atraso_mes['maximaperdidamus']
    suma_mes = suma_mes * 100

    data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':suma, 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':suma_mes}
    return data


def kpiFaltaAgua():
    riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion="Falta Agua").values())
    num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
    suma = 0
    for atraso in riesgos_atraso_proyecto_acum:
        suma += atraso['maximaperdidamus']
    suma = suma * 1000

    riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Falta Agua", fechadigita__year=datetime.now().year, fechadigita__month=datetime.now().month).values())
    num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
    suma_mes = 0
    for atraso_mes in riesgos_atraso_proyecto:
        suma_mes += atraso_mes['maximaperdidamus']
    suma_mes = suma_mes * 1000

    data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':suma, 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':suma_mes}
    return data


def kpiFallaEquipoCritico():
    riesgos_atraso_proyecto_acum = list(RiesgoUnifica.objects.filter(clasificacion="Falla Equipo Crítico").values())    
    num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)

    suma = 0
    for materializado in riesgos_atraso_proyecto_acum:
        suma += float(materializado['montoperdidakusd'])


    riesgos_atraso_proyecto_mes = list(RiesgoUnifica.objects.filter(clasificacion="Falla Equipo Crítico", fecha__year=datetime.now().year, fecha__month=datetime.now().month).values())    
    num_riesgos_atraso_proyecto_mes = len(riesgos_atraso_proyecto_mes)
     
    suma_mes = 0
    for materializado_mes in riesgos_atraso_proyecto_mes:
        suma_mes += float(materializado_mes['montoperdidakusd'])


    data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto_mes, 'suma_mes':int(suma_mes)}
    return data

def kpiIncendio():
    riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion="Incendio").values())
    num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
    suma = 0
    for atraso in riesgos_atraso_proyecto_acum:
        suma += atraso['maximaperdidamus']
    suma = suma * 1000

    riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Incendio", fechadigita__year=datetime.now().year, fechadigita__month=datetime.now().month).values())
    num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
    suma_mes = 0
    for atraso_mes in riesgos_atraso_proyecto:
        suma_mes += atraso_mes['maximaperdidamus']
    suma_mes = suma_mes * 1000

    data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':suma, 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':suma_mes}
    return data

def impactoFinancieroEventosMaterializados():
    listas_clasificaciones = list(RiesgoListas.objects.filter(tipo="Clasificaciones").values_list("glosa", flat=True))
    total = 0
    diccionario = dict()
    i = 0
    arreglo_colores = ['success', 'danger', 'warning', 'brand', 'info', 'red']
    for clasificacion in listas_clasificaciones:
        valores_cio = list(RiesgoCargasistemacio.objects.filter(clasificacion=clasificacion).values_list("montodeperdida", flat=True))
        valoreS_n1 = list(RiesgoCargasisteman1.objects.filter(clasificacion=clasificacion).values_list("montodeperdida", flat=True))        
        ciolist = [float(x) for x in valores_cio]
        n1list = [float(x) for x in valoreS_n1]
        diccionario[clasificacion] = {
            'valor':sum(ciolist) + sum(n1list),
            'color': arreglo_colores[i]
            }
       
        total += sum(ciolist) + sum(n1list)
        i += 1    
    
    data = {'valores_por_clasificacion':diccionario, 'total':total, 'arreglo_colores':arreglo_colores}
    
    return data


def riesgosGerencias():
    gerencias = list(Gerencias.objects.all().values())
    diccionario_riesgos_gerencias = dict()
    total = 0
    for gerencia in gerencias:
        total_riesgos_gerencia = len(list(Riesgo.objects.filter(gerencia=gerencia['sigla']).values()))
        diccionario_riesgos_gerencias[gerencia['gerencia']] = total_riesgos_gerencia
        total += total_riesgos_gerencia
    print(diccionario_riesgos_gerencias)
    return diccionario_riesgos_gerencias

def getRiesgoClasificaciones():
    clasificaciones = list(Riesgo.objects.values("clasificacion").distinct())
    dict_riesgos_cantidad_clasificacion = dict()    
    for clasificacion in clasificaciones:
        cantidad_riesgos_acumulado = len(list(Riesgo.objects.filter(clasificacion=clasificacion['clasificacion']).values()))
        valores_riesgos_acumulado = list(Riesgo.objects.filter(clasificacion=clasificacion['clasificacion']).values_list("maximaperdidamus", flat=True))
        arreglo_valores_acumulado = [float(x) for x in valores_riesgos_acumulado]
        suma_valores_acumulados = sum(arreglo_valores_acumulado)

        cantidad_riesgos_mes = len(list(Riesgo.objects.filter(clasificacion=clasificacion['clasificacion'], fechadigita__month=datetime.now().month, fechadigita__year=datetime.now().year).values()))
        valores_riesgos_mes = list(Riesgo.objects.filter(clasificacion=clasificacion['clasificacion'], fechadigita__month=datetime.now().month, fechadigita__year=datetime.now().year).values_list("maximaperdidamus", flat=True))
        arreglo_valores_mes = [float(x) for x in valores_riesgos_mes]
        suma_valores_mes = sum(arreglo_valores_mes)
                
        dict_riesgos_cantidad_clasificacion[clasificacion['clasificacion']] = {
            'cantidad_riesgos_mes':cantidad_riesgos_mes,
            'suma_valores_mes':suma_valores_mes,
            'cantidad_riesgos_acumulado':cantidad_riesgos_acumulado,
            'suma_valores_acumulados':suma_valores_acumulados
        }
    cantidad_acumulada = 0     
    arreglo_llaves = []
    i = 0
    llave = ''
    for key, value in dict_riesgos_cantidad_clasificacion.items():
        
        i+=1
        if key not in arreglo_llaves:
            if float(value['cantidad_riesgos_acumulado']) > cantidad_acumulada:
                cantidad_acumulada = value['cantidad_riesgos_acumulado']
                llave = key
            if i == len(dict_riesgos_cantidad_clasificacion):
                arreglo_llaves.append(llave)
    

    return clasificaciones

def getRiesgosCriticosPorGerencia(request):
    if request.method == "GET":
        gerencias = list(Gerencias.objects.all().values())
        dict_criticos = {}        
        for gerencia in gerencias:
            rojos = 0
            riesgos_gerencia = list(Riesgo.objects.filter(gerencia=gerencia['sigla']).values())            
                        
            for riesgo in riesgos_gerencia:
                nombre_color = ''                
                resultado_inherente_riesgo = list(RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=riesgo['idriesgo']).values('probabilidad', 'impacto'))
                probabilidad = resultado_inherente_riesgo[0]['probabilidad']
                impacto = resultado_inherente_riesgo[0]['impacto']
                color = list(RiesgoProbImp.objects.filter(probabilidad=probabilidad, impacto=impacto).values('color_hex', 'color'))                
                if len(color) > 0:
                    nombre_color = color[0]['color']                    
                if nombre_color == 'rojo':
                    rojos+=1            
            dict_criticos[gerencia['gerencia']] = rojos

        gerencias_ordenadas = sorted(dict_criticos.items(), key=operator.itemgetter(1), reverse=True)
        cinco_primeras = 0
        total_cinco_criticos = 0
        dict_cinco_gerencias = OrderedDict()
        for gerencias in gerencias_ordenadas:
            cinco_primeras+=1
            if cinco_primeras < 5:                
                dict_cinco_gerencias[gerencias[0]] = {'cantidad':gerencias[1]}
                total_cinco_criticos+=gerencias[1]
        
        i_color = 0
        arreglo_colores = ['success', 'danger', 'warning', 'brand', 'info', 'red']
        for key in dict_cinco_gerencias.keys():      
            porcentaje = round(float(((int(dict_cinco_gerencias[key]['cantidad']) / total_cinco_criticos) * 100)), 0)
            dict_cinco_gerencias[key] = {'cantidad':dict_cinco_gerencias[key]['cantidad'], 'porcentaje':porcentaje, 'color':arreglo_colores[i_color]}
            i_color+=1
        
        return JsonResponse(dict_cinco_gerencias, safe=False)

def getDetalleRiesgosCriticos(request):
    if request.method == "GET":
        datos = RiesgosCriticos().getRiesgosCriticosTabla()
        return JsonResponse(datos, safe=False)


def getCausasRiesgosCriticos(request):
    if request.method == "GET":
        tipo_datos = request.GET['tipo_datos']
        tipo = request.GET['tipo']
        nivel = request.GET['nivel']
        datos_riesgos = RiesgosCriticos(tipo_datos, nivel, tipo, "").getCausasRiesgos()
        return JsonResponse(datos_riesgos, safe=False)

def getRiesgosPorDireccion(request):
    if request.method == "GET":
        tipo_datos = request.GET['tipo_datos']
        tipo = request.GET['tipo']
        nivel = request.GET['nivel']
        datos_riesgos = RiesgosCriticos(tipo_datos, nivel, tipo, "").getRiesgosPorDirSup()                      
        return JsonResponse(datos_riesgos, safe=False)


def getMatrices(request):
    if request.method == "GET":
        tipo = request.GET['tipo']
        matriz_inherente = getMatrizInherente(tipo)
        matriz_residual = getMatrizResidual(tipo)
        matriz_objetivo = getMatrizObjetivo(tipo)
        data = {'matriz_inherente':matriz_inherente, 'matriz_residual':matriz_residual, 'matriz_objetivo':matriz_objetivo}
        return JsonResponse(data, safe=False)

def getMatrizInherente(tipo):
    if tipo == "DET":
        gerencias = list(Gerencias.objects.all().values())
    else:
        gerencias = list(Gerencias.objects.filter(sigla=tipo).values())
    
    nombre_color = ""
    dict_inherentes = {}
    probabilidad_inherente = ""
    impacto_inherente = ""
    for gerencia in gerencias:
        id_riesgos = list(Riesgo.objects.filter(gerencia=gerencia['sigla']).values_list('idriesgo', flat=True))                        
        for id_riesgo in id_riesgos:
            if RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=id_riesgo).exists():
                if list(RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=id_riesgo).values("probabilidad"))[0]["probabilidad"] is not None:
                    probabilidad_inherente = int(list(RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=id_riesgo).values("probabilidad"))[0]["probabilidad"])
            if RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=id_riesgo).exists():
                if list(RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=id_riesgo).values("impacto"))[0]["impacto"] is not None:
                    impacto_inherente = int(list(RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=id_riesgo).values("impacto"))[0]["impacto"])

            if probabilidad_inherente and impacto_inherente:
                color = list(RiesgoProbImp.objects.filter(probabilidad=probabilidad_inherente, impacto=impacto_inherente).values('color_hex', 'color'))                            
                if len(color) > 0:
                    nombre_color = color[0]['color']                
                if nombre_color == 'rojo':                                                
                    label_coords = str(impacto_inherente)+'_'+str(probabilidad_inherente)                
                    if label_coords in dict_inherentes:
                        dict_inherentes[label_coords] += 1
                    else:
                        dict_inherentes[label_coords] = 1                
    return dict_inherentes


def getMatrizResidual(tipo):
    if tipo == "DET":
        gerencias = list(Gerencias.objects.all().values())
    else:
        gerencias = list(Gerencias.objects.filter(sigla=tipo).values())
    
    nombre_color = ""
    dict_residual = {}
    probabilidad_residual = ""
    impacto_residual = ""
    for gerencia in gerencias:
        id_riesgos = list(Riesgo.objects.filter(gerencia=gerencia['sigla']).values_list('idriesgo', flat=True))                        
        for id_riesgo in id_riesgos:
            if RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=id_riesgo).exists():
                if list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=id_riesgo).values("probabilidadresidual"))[0]["probabilidadresidual"] is not None:
                    probabilidad_residual = int(list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=id_riesgo).values("probabilidadresidual"))[0]["probabilidadresidual"])
            if RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=id_riesgo).exists():
                if list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=id_riesgo).values("impactoresidual"))[0]["impactoresidual"] is not None:
                    impacto_residual = int(list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=id_riesgo).values("impactoresidual"))[0]["impactoresidual"])

            if probabilidad_residual and impacto_residual:
                color = list(RiesgoProbImp.objects.filter(probabilidad=probabilidad_residual, impacto=impacto_residual).values('color_hex', 'color'))                            
                if len(color) > 0:
                    nombre_color = color[0]['color']                
                if nombre_color == 'rojo':                                                
                    label_coords = str(impacto_residual)+'_'+str(probabilidad_residual)                
                    if label_coords in dict_residual:
                        dict_residual[label_coords] += 1
                    else:
                        dict_residual[label_coords] = 1
                
    return dict_residual

def getMatrizObjetivo(tipo):
    if tipo == "DET":
        gerencias = list(Gerencias.objects.all().values())
    else:
        gerencias = list(Gerencias.objects.filter(sigla=tipo).values())
    
    nombre_color = ""
    dict_objetivo = {}
    probabilidad_objetivo = ""
    impacto_objetivo = ""
    for gerencia in gerencias:
        id_riesgos = list(Riesgo.objects.filter(gerencia=gerencia['sigla']).values_list('idriesgo', flat=True))                        
        for id_riesgo in id_riesgos:
            if RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=id_riesgo).exists():
                if list(RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=id_riesgo).values("probabilidadcontrol"))[0]["probabilidadcontrol"] is not None:
                    probabilidad_objetivo = int(list(RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=id_riesgo).values("probabilidadcontrol"))[0]["probabilidadcontrol"])
            if RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=id_riesgo).exists():
                if list(RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=id_riesgo).values("impactocontrol"))[0]["impactocontrol"] is not None:
                    impacto_objetivo = int(list(RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=id_riesgo).values("impactocontrol"))[0]["impactocontrol"])

            if probabilidad_objetivo and impacto_objetivo:
                color = list(RiesgoProbImp.objects.filter(probabilidad=probabilidad_objetivo, impacto=impacto_objetivo).values('color_hex', 'color'))                            
                if len(color) > 0:
                    nombre_color = color[0]['color']                
                if nombre_color == 'rojo':                                                
                    label_coords = str(impacto_objetivo)+'_'+str(probabilidad_objetivo)                
                    if label_coords in dict_objetivo:
                        dict_objetivo[label_coords] += 1
                    else:
                        dict_objetivo[label_coords] = 1                
    return dict_objetivo


def getRiesgosPorDireccionValorizados(request):
    if request.method == "GET":
        tipo_datos = request.GET['tipo_datos']
        tipo = request.GET['tipo']
        nivel = request.GET['nivel']
        datos_riesgos = RiesgosCriticos(tipo_datos, nivel, tipo, "").getRiesgosValorizadosDirSup()
        return JsonResponse(datos_riesgos, safe=False)




