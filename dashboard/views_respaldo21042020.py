from django.shortcuts import render
from kpiDashboard.models import RiesgoKpi
from core.models import Riesgo, RiesgoListas, RiesgoCargasistemacio, RiesgoCargasisteman1, Gerencias, RiesgoEvaluacioncualitativainherente, RiesgoEvaluacioncualitativaresidual, RiesgoEvaluacioncualitativaobjetivo, RiesgoProbImp, RiesgoNCausariesgo, RiesgoCausas, RiesgoCargasistemacio, RiesgoCargasisteman1
from datetime import datetime
from django.http import JsonResponse
from collections import OrderedDict
import operator
from django.db.models import Sum

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


    cantidad_riesgos_acumulados = len(list(RiesgoCargasistemacio.objects.all().values())) + len(list(RiesgoCargasisteman1.objects.all().values()))
    cantidad_riesgos_mes = len(list(RiesgoCargasistemacio.objects.filter(fecharegistro__year=datetime.now().year, fecharegistro__month=datetime.now().month).values())) + len(list(RiesgoCargasisteman1.objects.filter(fecharegistro__year=datetime.now().year, fecharegistro__month=datetime.now().month).values()))

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
        suma += float(atraso['maximaperdidamus'])
    suma = suma * 100

    riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Atraso Proyecto", fechadigita__year=datetime.now().year, fechadigita__month=datetime.now().month).values())
    num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
    suma_mes = 0
    for atraso_mes in riesgos_atraso_proyecto:
        suma_mes += float(atraso_mes['maximaperdidamus'])
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
    suma = suma * 100

    riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Falta Agua", fechadigita__year=datetime.now().year, fechadigita__month=datetime.now().month).values())
    num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
    suma_mes = 0
    for atraso_mes in riesgos_atraso_proyecto:
        suma_mes += atraso_mes['maximaperdidamus']
    suma_mes = suma_mes * 100

    data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':suma, 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':suma_mes}
    return data


def kpiFallaEquipoCritico():
    riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion="Falta Equipo Critico").values())
    num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
    suma = 0
    for atraso in riesgos_atraso_proyecto_acum:
        suma += atraso['maximaperdidamus']
    suma = suma * 100

    riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Falta Equipo Critico", fechadigita__year=datetime.now().year, fechadigita__month=datetime.now().month).values())
    num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
    suma_mes = 0
    for atraso_mes in riesgos_atraso_proyecto:
        suma_mes += atraso_mes['maximaperdidamus']
    suma_mes = suma_mes * 100

    data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':suma, 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':suma_mes}
    return data

def kpiIncendio():
    riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion="Incendio").values())
    num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
    suma = 0
    for atraso in riesgos_atraso_proyecto_acum:
        suma += atraso['maximaperdidamus']
    suma = suma * 100

    riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Incendio", fechadigita__year=datetime.now().year, fechadigita__month=datetime.now().month).values())
    num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
    suma_mes = 0
    for atraso_mes in riesgos_atraso_proyecto:
        suma_mes += atraso_mes['maximaperdidamus']
    suma_mes = suma_mes * 100

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
        gerencias = list(Gerencias.objects.all().values())
        dict_criticos = {}
        dict_arreglo_ids_criticos = {}
        for gerencia in gerencias:
            rojos = 0
            riesgos_gerencia = list(Riesgo.objects.filter(gerencia=gerencia['sigla']).values())
            arreglo_ids_riesgos_criticos = []            
                        
            for riesgo in riesgos_gerencia:
                nombre_color = ''                
                resultado_inherente_riesgo = list(RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=riesgo['idriesgo']).values('probabilidad', 'impacto'))
                probabilidad = resultado_inherente_riesgo[0]['probabilidad']
                impacto = resultado_inherente_riesgo[0]['impacto']
                color = list(RiesgoProbImp.objects.filter(probabilidad=probabilidad, impacto=impacto).values('color_hex', 'color'))                
                if len(color) > 0:
                    nombre_color = color[0]['color']                    
                if nombre_color == 'rojo':
                    arreglo_ids_riesgos_criticos.append(riesgo['idriesgo'])
                    rojos+=1            
            dict_criticos[gerencia['gerencia']] = rojos            
            dict_arreglo_ids_criticos[gerencia['gerencia']] = arreglo_ids_riesgos_criticos

        gerencias_ordenadas = sorted(dict_criticos.items(), key=operator.itemgetter(1), reverse=True)
        diccionario_ordenado = OrderedDict()
        
        for key, value in gerencias_ordenadas:
            valor_perdida_total = Riesgo.objects.filter(gerencia=key).aggregate(Sum('maximaperdidamus'))
            monto_perdida_critica = Riesgo.objects.filter(idriesgo__in=dict_arreglo_ids_criticos[key]).aggregate(Sum('maximaperdidamus'))
            cantidad_riesgos_gerencia = len(list(Riesgo.objects.filter(gerencia=key).values()))
            porc_riesgos_criticos = 0
            if cantidad_riesgos_gerencia > 0:
                porc_riesgos_criticos = round(((value / cantidad_riesgos_gerencia)*100) ,1)
            porcentaje_mus_perdida = 0            
            if valor_perdida_total['maximaperdidamus__sum'] > 0:
                porcentaje_mus_perdida = round(((monto_perdida_critica['maximaperdidamus__sum']/valor_perdida_total['maximaperdidamus__sum'])*100), 1)
            diccionario_ordenado[key] = {
                'cantidad_riesgos_gerencia':cantidad_riesgos_gerencia,
                'cantidad_riesgos_criticos':value,
                'porc_riesgos_criticos':porc_riesgos_criticos,
                'monto_perdida_critica':monto_perdida_critica['maximaperdidamus__sum'],
                'porcentaje_mus_perdida':porcentaje_mus_perdida,
            }        
            
        return JsonResponse(diccionario_ordenado, safe=False)


def getCausasRiesgosCriticos(request):
    if request.method == "GET":
        tipo = request.GET['tipo']
        if tipo == "DET":
            gerencias = list(Gerencias.objects.all().values())
        else:
            gerencias = list(Gerencias.objects.filter(sigla=tipo).values())

        dict_criticos = {}
        arreglo_ids_riesgos_criticos = []
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
                    arreglo_ids_riesgos_criticos.append(riesgo['idriesgo'])
                    rojos+=1
            dict_criticos[gerencia['gerencia']] = rojos
        
        id_causas = list(RiesgoNCausariesgo.objects.filter(idriesgo__in=arreglo_ids_riesgos_criticos).values_list("idcausa", flat=True))
        
        dict_causas_riesgos_criticos = {}
        for causa in id_causas:            
            causa_descripcion = list(RiesgoCausas.objects.filter(idcausa=causa).values("causa"))
            causa_descripcion = causa_descripcion[0]["causa"] + '&&' + causa
            
            if causa_descripcion in dict_causas_riesgos_criticos:
                dict_causas_riesgos_criticos[causa_descripcion] += 1
            else:
                dict_causas_riesgos_criticos[causa_descripcion] = 1
        
        causas_ordenadas = sorted(dict_causas_riesgos_criticos.items(), key=operator.itemgetter(1), reverse=True)
        i_causas = 0
        arreglo_colores = ['#0abb87', '#fd397a', '#ffb822', '#5d78ff', '#36a3f7 ', 'red']
        diccionario_causas_ordenadas = OrderedDict()
        for causa in causas_ordenadas:
            if i_causas < 5:
                id_causa = causa[0].split("&&")[1]
                ids_riesgos = list(RiesgoNCausariesgo.objects.filter(idcausa=id_causa, idriesgo__in=arreglo_ids_riesgos_criticos).values_list('idriesgo', flat=True))
                valores = Riesgo.objects.filter(idriesgo__in=ids_riesgos).aggregate(Sum('maximaperdidamus'))
                
                diccionario_causas_ordenadas[causa[0].split("&&")[0]] = {
                    'cantidad': causa[1],
                    'valor':float(valores['maximaperdidamus__sum'])*100,
                    'color':arreglo_colores[i_causas]
                }
            i_causas += 1        
        return JsonResponse(diccionario_causas_ordenadas, safe=False)

def getRiesgosPorDireccion(request):
    if request.method == "GET":
        tipo = request.GET['tipo']                
        if tipo == "DET":
            gerencias = list(Gerencias.objects.all().values())
        else:
            gerencias = list(Gerencias.objects.filter(sigla=tipo).values())
                
        arreglo_ids_riesgos_criticos = []
        dict_direcciones_criticos = {}
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
                    arreglo_ids_riesgos_criticos.append(riesgo['idriesgo'])
                    if riesgo['direccion'] != '-' and riesgo['direccion'] is not None:                        
                        if riesgo['direccion'] in dict_direcciones_criticos:
                            dict_direcciones_criticos[riesgo['direccion']] += 1
                        else:
                            dict_direcciones_criticos[riesgo['direccion']] = 1
                    rojos+=1
        
        riesgos_direcciones_ordenados = sorted(dict_direcciones_criticos.items(), key=operator.itemgetter(1), reverse=True)
        riesgos_ordenados = OrderedDict()
        arreglo_colores = ['#0abb87', '#fd397a', '#ffb822', '#5d78ff', '#36a3f7 ', 'red']
        i_riesgos_direccion = 0
        for riesgo_direccion in riesgos_direcciones_ordenados:
            if i_riesgos_direccion <5:
                riesgos_ordenados[riesgo_direccion[0]] = {'cantidad': riesgo_direccion[1], 'color':arreglo_colores[i_riesgos_direccion]}
            i_riesgos_direccion += 1        


        return JsonResponse(riesgos_ordenados, safe=False)


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
        tipo = request.GET['tipo']                
        if tipo == "DET":
            gerencias = list(Gerencias.objects.all().values())
        else:
            gerencias = list(Gerencias.objects.filter(sigla=tipo).values())
                
        arreglo_ids_riesgos_criticos = []
        dict_direcciones_criticos = {}
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
                    arreglo_ids_riesgos_criticos.append(riesgo['idriesgo'])
                    if riesgo['direccion'] != '-' and riesgo['direccion'] is not None:                        
                        if riesgo['direccion'] in dict_direcciones_criticos:
                            dict_direcciones_criticos[riesgo['direccion']] += float(riesgo['maximaperdidamus'])*100
                        else:
                            dict_direcciones_criticos[riesgo['direccion']] = float(riesgo['maximaperdidamus'])*100
                    rojos+=1
        
        riesgos_direcciones_ordenados = sorted(dict_direcciones_criticos.items(), key=operator.itemgetter(1), reverse=True)
        riesgos_ordenados = OrderedDict()
        arreglo_colores = ['#0abb87', '#fd397a', '#ffb822', '#5d78ff', '#36a3f7 ', 'red']
        i_riesgos_direccion = 0
        for riesgo_direccion in riesgos_direcciones_ordenados:
            if i_riesgos_direccion <5:
                riesgos_ordenados[riesgo_direccion[0]] = {'cantidad': riesgo_direccion[1], 'color':arreglo_colores[i_riesgos_direccion]}
            i_riesgos_direccion += 1

        print("VALORIZADOS --> ", riesgos_ordenados)


        return JsonResponse(riesgos_ordenados, safe=False)



