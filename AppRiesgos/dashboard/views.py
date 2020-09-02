from django.shortcuts import render
from kpiDashboard.models import RiesgoKpi
from core.models import Riesgo, RiesgoListas, RiesgoCargasistemacio, RiesgoCargasisteman1, Gerencias, RiesgoEvaluacioncualitativainherente, RiesgoEvaluacioncualitativaresidual, RiesgoEvaluacioncualitativaobjetivo, RiesgoProbImp, RiesgoNCausariesgo, RiesgoCausas, RiesgoUnifica, RiesgoColorindicadores
from datetime import datetime
from django.http import JsonResponse
from collections import OrderedDict
import operator
from django.db.models import Sum
from dashboard.clases.RiesgosCriticos import RiesgosCriticos
from core.utils import comprobeConvertedFloat
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    mes = datetime.now().month
    ano = datetime.now().year                
    kpi_costo_presupuesto = list(RiesgoKpi.objects.filter(ano=ano, mes=mes, tipo="Costo Presupuesto").order_by('-fecreg').values())
    kpi_produccion = list(RiesgoKpi.objects.filter(ano=ano, mes=mes, tipo="Producción").order_by('-fecreg').values())
    kpi_seguridad = list(RiesgoKpi.objects.filter(ano=ano, mes=mes, tipo="Seguridad").order_by('-fecreg').values())
    kpi_ambiental = list(RiesgoKpi.objects.filter(ano=ano, mes=mes, tipo="Ambiental").order_by('-fecreg').values())
    clasificaciones = RiesgoListas.objects.filter(tipo="Clasificaciones", estado="ACTIVO").values("glosa")

    atraso_proyecto = kpiAtrasoProyecto("directi")
    probidad_transparencia = kpiProbidadTransparencia("directi")
    falta_agua = kpiFaltaAgua("directi")
    falla_equipo_critico = kpiFallaEquipoCritico("directi")
    incendio = kpiIncendio("directi")
    pandemia = kpiUnifica("directi", "pandemia")
    #riesgos_totales = riesgosGerencias()
    #clasificaciones_riesgos = getRiesgoClasificaciones()

    cantidad_riesgos_acumulados_alto = list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
    cantidad_riesgos_mensuales_alto = list(RiesgoEvaluacioncualitativaresidual.objects.filter(modificado__year=datetime.now().year, modificado__month=datetime.now().month, nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
    cantidad_riesgos_acumulados = len(list(Riesgo.objects.filter(idriesgo__in=cantidad_riesgos_acumulados_alto, directic=1).values()))
    cantidad_riesgos_mes = len(list(Riesgo.objects.filter(idriesgo__in=cantidad_riesgos_mensuales_alto, directic=1).values()))    
    cantidad_total_registros = len(list(Riesgo.objects.filter(estadoregistro='Vigente', directic=1).values()))

    ano=datetime.now().year
    dicccionarioMesesSemestre1 = {}
    dicccionarioMesesSemestre2 = {}
    dicccionarioMesesSemestre1[1]={'mes':'Enero','valor':0,}
    dicccionarioMesesSemestre1[2]={'mes':'Febrero','valor':0,}
    dicccionarioMesesSemestre1[3]={'mes':'Marzo','valor':0,}
    dicccionarioMesesSemestre1[4]={'mes':'Abril','valor':0,}
    dicccionarioMesesSemestre1[5]={'mes':'Mayo','valor':0,}
    dicccionarioMesesSemestre1[6]={'mes':'Junio','valor':0,}

    dicccionarioMesesSemestre2[7]={'mes':'Julio','valor':0,}
    dicccionarioMesesSemestre2[8]={'mes':'Agosto','valor':0,}
    dicccionarioMesesSemestre2[9]={'mes':'Septiembre','valor':0,}
    dicccionarioMesesSemestre2[10]={'mes':'Octubre','valor':0,}
    dicccionarioMesesSemestre2[11]={'mes':'Noviembre','valor':0,}
    dicccionarioMesesSemestre2[12]={'mes':'Diciembre','valor':0,}

    eventosSemestres = list(RiesgoUnifica.objects.all().values())
    totalUnifica = 0
    totalTmf = 0
    qUnifica = 0
    for k, v in dicccionarioMesesSemestre1.items():
        valoresMes = RiesgoUnifica.objects.filter(fecha__year=ano, fecha__month=k).values()
        for valor in valoresMes:
            totalUnifica+=float(valor['montoperdidakusd'])
            totalTmf+=float(valor['qtmfperdida'])
            qUnifica+=1
            v['valor']+=float(valor['montoperdidakusd'])
    
    for k, v in dicccionarioMesesSemestre2.items():
        valoresMes = RiesgoUnifica.objects.filter(fecha__year=ano, fecha__month=k).values()
        for valor in valoresMes:
            totalUnifica+=float(valor['montoperdidakusd'])
            totalTmf+=float(valor['qtmfperdida'])
            qUnifica+=1
            v['valor']+=float(valor['montoperdidakusd'])
    
    print(dicccionarioMesesSemestre2)

    """riesgos_acumulados = list(RiesgoUnifica.objects.all().values())
    cantidad_riesgos_acumulados = 0
    for cantidad in riesgos_acumulados:
        if float(cantidad['montoperdidakusd']) > 0:
            cantidad_riesgos_acumulados+=1        
    
    riesgos_mes = list(RiesgoUnifica.objects.filter(fecha__year=datetime.now().year, fecha__month=datetime.now().month).values())
    cantidad_riesgos_mes = 0
    for cantidad_mes in riesgos_mes:
        if float(cantidad_mes['montoperdidakusd']) > 0:
            cantidad_riesgos_mes+=1"""

    #cantidad_riesgos_acumulados = len(list(Riesgo.objects.all().values()))
    #cantidad_riesgos_mes = len(list(Riesgo.objects.filter(fechadigita__year=datetime.now().year, fechadigita__month=datetime.now().month).values()))

    eventos_materializados = impactoFinancieroEventosMaterializados()
    kusNeto = 0
    tmfSin = 0
    if RiesgoKpi.objects.filter(tipo='KUSNETO').exists():
        kusNeto = RiesgoKpi.objects.filter(tipo='KUSNETO').order_by('-fecreg').first().valor
    if RiesgoKpi.objects.filter(tipo='TMFSIN').exists():
        tmfSin = RiesgoKpi.objects.filter(tipo='TMFSIN').order_by('-fecreg').first().valor
    
    gerencias = list(RiesgoUnifica.objects.all().values('gerencia').distinct())
    


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
        'clasificaciones':clasificaciones,
        'cantidad_total_registros':cantidad_total_registros,        
        'dicccionarioMesesSemestre1':dicccionarioMesesSemestre1,
        'dicccionarioMesesSemestre2':dicccionarioMesesSemestre2,
        'totalUnifica':totalUnifica,
        'qUnifica':qUnifica,
        'totalTmf':totalTmf,
        'kusNeto':kusNeto,
        'tmfSin':tmfSin,
        'gerencias':gerencias,
    }
    
    
    return render(request, "dashboard/index.html", data)

def inicioResponsive(request):
    mes = datetime.now().month
    ano = datetime.now().year                
    kpi_costo_presupuesto = list(RiesgoKpi.objects.filter(ano=ano, mes=mes, tipo="Costo Presupuesto").order_by('-fecreg').values())
    kpi_produccion = list(RiesgoKpi.objects.filter(ano=ano, mes=mes, tipo="Producción").order_by('-fecreg').values())
    kpi_seguridad = list(RiesgoKpi.objects.filter(ano=ano, mes=mes, tipo="Seguridad").order_by('-fecreg').values())
    kpi_ambiental = list(RiesgoKpi.objects.filter(ano=ano, mes=mes, tipo="Ambiental").order_by('-fecreg').values())
    clasificaciones = RiesgoListas.objects.filter(tipo="Clasificaciones", estado="ACTIVO").values("glosa")

    atraso_proyecto = kpiAtrasoProyecto("directi")
    probidad_transparencia = kpiProbidadTransparencia("directi")
    falta_agua = kpiFaltaAgua("directi")
    falla_equipo_critico = kpiFallaEquipoCritico("directi")
    incendio = kpiIncendio("directi")
    pandemia = kpiUnifica("directi", "pandemia")
    #riesgos_totales = riesgosGerencias()
    #clasificaciones_riesgos = getRiesgoClasificaciones()

    cantidad_riesgos_acumulados_alto = list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
    cantidad_riesgos_mensuales_alto = list(RiesgoEvaluacioncualitativaresidual.objects.filter(modificado__year=datetime.now().year, modificado__month=datetime.now().month, nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
    cantidad_riesgos_acumulados = len(list(Riesgo.objects.filter(idriesgo__in=cantidad_riesgos_acumulados_alto, directic=1).values()))
    cantidad_riesgos_mes = len(list(Riesgo.objects.filter(idriesgo__in=cantidad_riesgos_mensuales_alto, directic=1).values()))    
    cantidad_total_registros = len(list(Riesgo.objects.filter(estadoregistro='Vigente', directic=1).values()))

    ano=datetime.now().year
    dicccionarioMesesSemestre1 = {}
    dicccionarioMesesSemestre2 = {}
    dicccionarioMesesSemestre1[1]={'mes':'Enero','valor':0,}
    dicccionarioMesesSemestre1[2]={'mes':'Febrero','valor':0,}
    dicccionarioMesesSemestre1[3]={'mes':'Marzo','valor':0,}
    dicccionarioMesesSemestre1[4]={'mes':'Abril','valor':0,}
    dicccionarioMesesSemestre1[5]={'mes':'Mayo','valor':0,}
    dicccionarioMesesSemestre1[6]={'mes':'Junio','valor':0,}

    dicccionarioMesesSemestre2[7]={'mes':'Julio','valor':0,}
    dicccionarioMesesSemestre2[8]={'mes':'Agosto','valor':0,}
    dicccionarioMesesSemestre2[9]={'mes':'Septiembre','valor':0,}
    dicccionarioMesesSemestre2[10]={'mes':'Octubre','valor':0,}
    dicccionarioMesesSemestre2[11]={'mes':'Noviembre','valor':0,}
    dicccionarioMesesSemestre2[12]={'mes':'Diciembre','valor':0,}

    eventosSemestres = list(RiesgoUnifica.objects.all().values())
    totalUnifica = 0
    totalTmf = 0
    qUnifica = 0
    for k, v in dicccionarioMesesSemestre1.items():
        valoresMes = RiesgoUnifica.objects.filter(fecha__year=ano, fecha__month=k).values()
        for valor in valoresMes:
            totalUnifica+=float(valor['montoperdidakusd'])
            totalTmf+=float(valor['qtmfperdida'])
            qUnifica+=1
            v['valor']+=float(valor['montoperdidakusd'])
    
    for k, v in dicccionarioMesesSemestre2.items():
        valoresMes = RiesgoUnifica.objects.filter(fecha__year=ano, fecha__month=k).values()
        for valor in valoresMes:
            totalUnifica+=float(valor['montoperdidakusd'])
            totalTmf+=float(valor['qtmfperdida'])
            qUnifica+=1
            v['valor']+=float(valor['montoperdidakusd'])
    
    print(dicccionarioMesesSemestre2)

    """riesgos_acumulados = list(RiesgoUnifica.objects.all().values())
    cantidad_riesgos_acumulados = 0
    for cantidad in riesgos_acumulados:
        if float(cantidad['montoperdidakusd']) > 0:
            cantidad_riesgos_acumulados+=1        
    
    riesgos_mes = list(RiesgoUnifica.objects.filter(fecha__year=datetime.now().year, fecha__month=datetime.now().month).values())
    cantidad_riesgos_mes = 0
    for cantidad_mes in riesgos_mes:
        if float(cantidad_mes['montoperdidakusd']) > 0:
            cantidad_riesgos_mes+=1"""

    #cantidad_riesgos_acumulados = len(list(Riesgo.objects.all().values()))
    #cantidad_riesgos_mes = len(list(Riesgo.objects.filter(fechadigita__year=datetime.now().year, fechadigita__month=datetime.now().month).values()))

    eventos_materializados = impactoFinancieroEventosMaterializados()
    kusNeto = 0
    tmfSin = 0
    if RiesgoKpi.objects.filter(tipo='KUSNETO').exists():
        kusNeto = RiesgoKpi.objects.filter(tipo='KUSNETO').order_by('-fecreg').first().valor
    if RiesgoKpi.objects.filter(tipo='TMFSIN').exists():
        tmfSin = RiesgoKpi.objects.filter(tipo='TMFSIN').order_by('-fecreg').first().valor
    
    gerencias = list(RiesgoUnifica.objects.all().values('gerencia').distinct())
    


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
        'clasificaciones':clasificaciones,
        'cantidad_total_registros':cantidad_total_registros,        
        'dicccionarioMesesSemestre1':dicccionarioMesesSemestre1,
        'dicccionarioMesesSemestre2':dicccionarioMesesSemestre2,
        'totalUnifica':totalUnifica,
        'qUnifica':qUnifica,
        'totalTmf':totalTmf,
        'kusNeto':kusNeto,
        'tmfSin':tmfSin,
        'gerencias':gerencias,
    }
    
    
    return render(request, "dashboard/indexResponsive.html", data)

def inicio2(request):
    mes = datetime.now().month
    ano = datetime.now().year                
    kpi_costo_presupuesto = list(RiesgoKpi.objects.filter(ano=ano, mes=mes, tipo="Costo Presupuesto").order_by('-fecreg').values())
    kpi_produccion = list(RiesgoKpi.objects.filter(ano=ano, mes=mes, tipo="Producción").order_by('-fecreg').values())
    kpi_seguridad = list(RiesgoKpi.objects.filter(ano=ano, mes=mes, tipo="Seguridad").order_by('-fecreg').values())
    kpi_ambiental = list(RiesgoKpi.objects.filter(ano=ano, mes=mes, tipo="Ambiental").order_by('-fecreg').values())
    clasificaciones = RiesgoListas.objects.filter(tipo="Clasificaciones", estado="ACTIVO").values("glosa")

    atraso_proyecto = kpiAtrasoProyecto("directi")
    probidad_transparencia = kpiProbidadTransparencia("directi")
    falta_agua = kpiFaltaAgua("directi")
    falla_equipo_critico = kpiFallaEquipoCritico("directi")
    incendio = kpiIncendio("directi")

    cantidad_riesgos_acumulados_alto = list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
    cantidad_riesgos_mensuales_alto = list(RiesgoEvaluacioncualitativaresidual.objects.filter(modificado__year=datetime.now().year, modificado__month=datetime.now().month, nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
    cantidad_riesgos_acumulados = len(list(Riesgo.objects.filter(idriesgo__in=cantidad_riesgos_acumulados_alto, directic=1).values()))
    cantidad_riesgos_mes = len(list(Riesgo.objects.filter(idriesgo__in=cantidad_riesgos_mensuales_alto, directic=1).values()))

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
        'clasificaciones':clasificaciones,        
    }
        
    return render(request, "dashboard/index.html", data)

def kpiAtrasoProyecto(tipo):
    if tipo == "eventos":
        riesgos_atraso_proyecto_acum = list(RiesgoUnifica.objects.filter(clasificacion="Atraso Proyecto").values())
        num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
        suma = 0
        sumaTmfTotal = 0
        for atraso in riesgos_atraso_proyecto_acum:
            suma += float(atraso['montoperdidakusd'])
            sumaTmfTotal += float(atraso['qtmfperdida'])
        suma = suma

        riesgos_atraso_proyecto = list(RiesgoUnifica.objects.filter(clasificacion="Atraso Proyecto", fecha__year=datetime.now().year, fecha__month=datetime.now().month).values())
        num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
        suma_mes = 0
        sumaTmfMes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            suma_mes += float(atraso_mes['montoperdidakusd'])
            sumaTmfMes += float(atraso_mes['qtmfperdida'])
        suma_mes = suma_mes

        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes), 'suma_mes_tmf':int(sumaTmfMes), 'suma_tmf_total':int(sumaTmfTotal)}

    elif tipo == "riesgos":        
        riesgos_criticos = list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion="Atraso Proyecto", idriesgo__in=riesgos_criticos).values())
        num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
        suma = 0
        for atraso in riesgos_atraso_proyecto_acum:
            suma += float(atraso['maximaperdidamus'])
        suma = suma

        riesgos_criticos_mensuales = list(RiesgoEvaluacioncualitativaresidual.objects.filter(modificado__year=datetime.now().year, modificado__month=datetime.now().month, nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Atraso Proyecto", idriesgo__in=riesgos_criticos_mensuales).values())
        num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
        suma_mes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            suma_mes += float(atraso_mes['maximaperdidamus'])
        suma_mes = suma_mes

        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes)}

    elif tipo == "directi":
        riesgos_criticos = list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion="Atraso Proyecto", idriesgo__in=riesgos_criticos, directic=1).values())
        num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
        suma = 0
        for atraso in riesgos_atraso_proyecto_acum:
            suma += float(atraso['maximaperdidamus'])
        suma = suma

        riesgos_criticos_mensuales = list(RiesgoEvaluacioncualitativaresidual.objects.filter(modificado__year=datetime.now().year, modificado__month=datetime.now().month, nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Atraso Proyecto", idriesgo__in=riesgos_criticos_mensuales, directic=1).values())
        num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
        suma_mes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            suma_mes += float(atraso_mes['maximaperdidamus'])
        suma_mes = suma_mes

        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes)}

    return data


def kpiProbidadTransparencia(tipo):
    if tipo == "eventos":
        riesgos_atraso_proyecto_acum = list(RiesgoUnifica.objects.filter(clasificacion="Providad y Transparencia").values())
        num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
        suma = 0
        sumaTmfTotal = 0
        
        for atraso in riesgos_atraso_proyecto_acum:
            suma += float(atraso['montoperdidakusd'])
            sumaTmfTotal += float(atraso['qtmfperdida'])
        suma = suma

        riesgos_atraso_proyecto = list(RiesgoUnifica.objects.filter(clasificacion="Providad y Transparencia", fecha__year=datetime.now().year, fecha__month=datetime.now().month).values())
        num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
        suma_mes = 0
        sumaTmfMes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            suma_mes += float(atraso_mes['montoperdidakusd'])
            sumaTmfMes += float(atraso_mes['qtmfperdida'])
        suma_mes = suma_mes

        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes), 'suma_mes_tmf':int(sumaTmfMes), 'suma_tmf_total':int(sumaTmfTotal)}
        

    elif tipo == "riesgos":
        riesgos_criticos = list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion="Providad y Transparencia", idriesgo__in=riesgos_criticos).values())
        num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
        suma = 0
        for atraso in riesgos_atraso_proyecto_acum:
            suma += float(atraso['maximaperdidamus'])
        suma = suma

        riesgos_criticos_mensuales = list(RiesgoEvaluacioncualitativaresidual.objects.filter(modificado__year=datetime.now().year, modificado__month=datetime.now().month, nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Providad y Transparencia", idriesgo__in=riesgos_criticos_mensuales).values())
        num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
        suma_mes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            suma_mes += float(atraso_mes['maximaperdidamus'])
        suma_mes = suma_mes

        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes)}

    elif tipo == "directi":
        riesgos_criticos = list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion="Providad y Transparencia", idriesgo__in=riesgos_criticos, directic=1).values())
        num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
        suma = 0
        for atraso in riesgos_atraso_proyecto_acum:
            suma += float(atraso['maximaperdidamus'])
        suma = suma

        riesgos_criticos_mensuales = list(RiesgoEvaluacioncualitativaresidual.objects.filter(modificado__year=datetime.now().year, modificado__month=datetime.now().month, nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Providad y Transparencia", idriesgo__in=riesgos_criticos_mensuales, directic=1).values())
        num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
        suma_mes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            suma_mes += float(atraso_mes['maximaperdidamus'])
        suma_mes = suma_mes
        
        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes)}
    return data


def kpiFaltaAgua(tipo):
    if tipo == "eventos":
        riesgos_atraso_proyecto_acum = list(RiesgoUnifica.objects.filter(clasificacion="Falta Agua").values())
        num_riesgos_atraso_proyecto_acum = 0
        suma = 0
        sumaTmfTotal = 0
        for atraso in riesgos_atraso_proyecto_acum:
            sumaTmfTotal += float(atraso['qtmfperdida'])
            if atraso['montoperdidakusd'] != '-':                
                if float(atraso['montoperdidakusd']) > 0:
                    suma += float(atraso['montoperdidakusd'])
                    num_riesgos_atraso_proyecto_acum+=1        

        riesgos_atraso_proyecto = list(RiesgoUnifica.objects.filter(clasificacion="Falta Agua", fecha__year=datetime.now().year, fecha__month=datetime.now().month).values())
        num_riesgos_atraso_proyecto = 0
        suma_mes = 0
        sumaTmfMes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            sumaTmfMes += float(atraso_mes['qtmfperdida'])
            if atraso_mes['montoperdidakusd'] != '-':                
                if float(atraso_mes['montoperdidakusd']) > 0:
                    suma_mes += float(atraso_mes['montoperdidakusd'])
                    num_riesgos_atraso_proyecto+=1        

        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes), 'suma_mes_tmf':int(sumaTmfMes), 'suma_tmf_total':int(sumaTmfTotal)}
        

    elif tipo == "riesgos":
        riesgos_criticos = list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion="Falta Agua", idriesgo__in=riesgos_criticos).values())
        num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
        suma = 0
        for atraso in riesgos_atraso_proyecto_acum:
            suma += float(atraso['maximaperdidamus'])
        suma = suma

        riesgos_criticos_mensuales = list(RiesgoEvaluacioncualitativaresidual.objects.filter(modificado__year=datetime.now().year, modificado__month=datetime.now().month, nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Falta Agua", idriesgo__in=riesgos_criticos_mensuales).values())
        num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
        suma_mes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            suma_mes += float(atraso_mes['maximaperdidamus'])
        suma_mes = suma_mes

        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes)}

    elif tipo == "directi":
        riesgos_criticos = list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion="Falta Agua", idriesgo__in=riesgos_criticos, directic=1).values())
        num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
        suma = 0
        for atraso in riesgos_atraso_proyecto_acum:
            suma += float(atraso['maximaperdidamus'])
        suma = suma

        riesgos_criticos_mensuales = list(RiesgoEvaluacioncualitativaresidual.objects.filter(modificado__year=datetime.now().year, modificado__month=datetime.now().month, nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Falta Agua", idriesgo__in=riesgos_criticos_mensuales, directic=1).values())
        num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
        suma_mes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            suma_mes += float(atraso_mes['maximaperdidamus'])
        suma_mes = suma_mes

        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes)}
    return data



def kpiFallaEquipoCritico(tipo):
    if tipo == "eventos":
        riesgos_atraso_proyecto_acum = list(RiesgoUnifica.objects.filter(clasificacion="Falla Equipo Crítico").values())

        num_riesgos_atraso_proyecto_acum = 0
        suma = 0
        sumaTotal = 0
        sumaTmfTotal = 0 
        for atraso in riesgos_atraso_proyecto_acum:
            sumaTmfTotal += float(atraso['qtmfperdida'])
            if atraso['montoperdidakusd'] != "-":
                if float(atraso['montoperdidakusd']) > 0:
                    suma += float(atraso['montoperdidakusd'])
                    num_riesgos_atraso_proyecto_acum+=1
        suma = suma

        riesgos_atraso_proyecto = list(RiesgoUnifica.objects.filter(clasificacion="Falla Equipo Crítico", fecha__year=datetime.now().year, fecha__month=datetime.now().month).values())
        num_riesgos_atraso_proyecto = 0
        suma_mes = 0
        sumaTmfMes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            sumaTmfMes += float(atraso_mes['qtmfperdida'])
            if atraso_mes['montoperdidakusd'] != "-":
                if float(atraso_mes['montoperdidakusd']) > 0:            
                    suma_mes += float(atraso_mes['montoperdidakusd'])
                    num_riesgos_atraso_proyecto+=1
        suma_mes = suma_mes

        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes), 'suma_mes_tmf':int(sumaTmfMes), 'suma_tmf_total':int(sumaTmfTotal)}
        

    elif tipo == "riesgos":
        riesgos_criticos = list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion="Falla Equipo Crítico", idriesgo__in=riesgos_criticos).values())
        num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
        suma = 0
        for atraso in riesgos_atraso_proyecto_acum:
            suma += float(atraso['maximaperdidamus'])
        suma = suma

        riesgos_criticos_mensuales = list(RiesgoEvaluacioncualitativaresidual.objects.filter(modificado__year=datetime.now().year, modificado__month=datetime.now().month, nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Falla Equipo Crítico", idriesgo__in=riesgos_criticos_mensuales).values())
        num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
        suma_mes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            suma_mes += float(atraso_mes['maximaperdidamus'])
        suma_mes = suma_mes
        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes)}

    elif tipo == "directi":
        riesgos_criticos = list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion="Falla Equipo Crítico", idriesgo__in=riesgos_criticos, directic=1).values())
        num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
        suma = 0
        for atraso in riesgos_atraso_proyecto_acum:
            suma += float(atraso['maximaperdidamus'])
        suma = suma

        riesgos_criticos_mensuales = list(RiesgoEvaluacioncualitativaresidual.objects.filter(modificado__year=datetime.now().year, modificado__month=datetime.now().month, nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Falla Equipo Crítico", idriesgo__in=riesgos_criticos_mensuales, directic=1).values())
        num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
        suma_mes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            suma_mes += float(atraso_mes['maximaperdidamus'])
        suma_mes = suma_mes

        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes)}
    return data


def kpiIncendio(tipo):
    if tipo == "eventos":
        riesgos_atraso_proyecto_acum = list(RiesgoUnifica.objects.filter(clasificacion="Incendio").values())
        num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
        suma = 0
        sumaTmfTotal = 0
        for atraso in riesgos_atraso_proyecto_acum:
            sumaTmfTotal += float(atraso['qtmfperdida'])
            suma += float(atraso['montoperdidakusd'])
        suma = suma

        riesgos_atraso_proyecto = list(RiesgoUnifica.objects.filter(clasificacion="Incendio", fecha__year=datetime.now().year, fecha__month=datetime.now().month).values())
        num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
        suma_mes = 0
        sumaTmfMes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            sumaTmfMes += float(atraso_mes['qtmfperdida'])
            suma_mes += float(atraso_mes['montoperdidakusd'])
        suma_mes = suma_mes

        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes), 'suma_mes_tmf':int(sumaTmfMes), 'suma_tmf_total':int(sumaTmfTotal)}
        

    elif tipo == "riesgos":
        riesgos_criticos = list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion="Incendio", idriesgo__in=riesgos_criticos).values())
        num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
        suma = 0
        for atraso in riesgos_atraso_proyecto_acum:
            suma += float(atraso['maximaperdidamus'])
        suma = suma

        riesgos_criticos_mensuales = list(RiesgoEvaluacioncualitativaresidual.objects.filter(modificado__year=datetime.now().year, modificado__month=datetime.now().month, nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Incendio", idriesgo__in=riesgos_criticos_mensuales).values())
        num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
        suma_mes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            suma_mes += atraso_mes['maximaperdidamus']
        suma_mes = suma_mes
        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes)}

    elif tipo == "directi":
        riesgos_criticos = list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion="Incendio", idriesgo__in=riesgos_criticos, directic=1).values())
        num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
        suma = 0
        for atraso in riesgos_atraso_proyecto_acum:
            suma += float(atraso['maximaperdidamus'])
        suma = suma

        riesgos_criticos_mensuales = list(RiesgoEvaluacioncualitativaresidual.objects.filter(modificado__year=datetime.now().year, modificado__month=datetime.now().month, nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Incendio", idriesgo__in=riesgos_criticos_mensuales, directic=1).values())
        num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
        suma_mes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            suma_mes += float(atraso_mes['maximaperdidamus'])
        suma_mes = suma_mes

        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes)}
    return data


def kpiUnifica(tipo, clasificacion):
    if tipo == "eventos":
        riesgos_atraso_proyecto_acum = list(RiesgoUnifica.objects.filter(clasificacion=clasificacion).values())
        num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
        suma = 0
        sumaTmfTotal = 0
        for atraso in riesgos_atraso_proyecto_acum:
            suma += float(atraso['montoperdidakusd'])
            sumaTmfTotal += float(atraso['qtmfperdida'])
        suma = suma

        riesgos_atraso_proyecto = list(RiesgoUnifica.objects.filter(clasificacion=clasificacion, fecha__year=datetime.now().year, fecha__month=datetime.now().month).values())
        num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
        suma_mes = 0
        sumaTmfMes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            suma_mes += float(atraso_mes['montoperdidakusd'])
            sumaTmfMes += float(atraso_mes['qtmfperdida'])
        suma_mes = suma_mes

        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes), 'suma_mes_tmf':int(sumaTmfMes), 'suma_tmf_total':int(sumaTmfTotal)}
        

    elif tipo == "riesgos":
        riesgos_criticos = list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion=tipo, idriesgo__in=riesgos_criticos).values())
        num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
        suma = 0
        for atraso in riesgos_atraso_proyecto_acum:
            suma += float(atraso['maximaperdidamus'])
        suma = suma

        riesgos_criticos_mensuales = list(RiesgoEvaluacioncualitativaresidual.objects.filter(modificado__year=datetime.now().year, modificado__month=datetime.now().month, nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion=clasificacion, idriesgo__in=riesgos_criticos_mensuales).values())
        num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
        suma_mes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            suma_mes += atraso_mes['maximaperdidamus']
        suma_mes = suma_mes
        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes)}

    elif tipo == "directi":
        riesgos_criticos = list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto_acum = list(Riesgo.objects.filter(clasificacion=clasificacion, idriesgo__in=riesgos_criticos, directic=1).values())
        num_riesgos_atraso_proyecto_acum = len(riesgos_atraso_proyecto_acum)
        suma = 0
        for atraso in riesgos_atraso_proyecto_acum:
            suma += float(atraso['maximaperdidamus'])
        suma = suma

        riesgos_criticos_mensuales = list(RiesgoEvaluacioncualitativaresidual.objects.filter(modificado__year=datetime.now().year, modificado__month=datetime.now().month, nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        riesgos_atraso_proyecto = list(Riesgo.objects.filter(clasificacion="Incendio", idriesgo__in=riesgos_criticos_mensuales, directic=1).values())
        num_riesgos_atraso_proyecto = len(riesgos_atraso_proyecto)
        suma_mes = 0
        for atraso_mes in riesgos_atraso_proyecto:
            suma_mes += float(atraso_mes['maximaperdidamus'])
        suma_mes = suma_mes

        data = {'num_acumulado':num_riesgos_atraso_proyecto_acum, 'suma_acum':int(suma), 'num_mes':num_riesgos_atraso_proyecto, 'suma_mes':int(suma_mes)}
    return data


def impactoFinancieroEventosMaterializados():
    listas_clasificaciones = list(RiesgoListas.objects.filter(tipo="Clasificaciones").values_list("glosa", flat=True))
    total = 0
    diccionario = dict()
    i = 0
    arreglo_colores = ['success', 'danger', 'warning', 'brand', 'info', 'red']
    for clasificacion in listas_clasificaciones:
        valores = list(RiesgoUnifica.objects.filter(clasificacion=clasificacion).values_list("montoperdidakusd", flat=True))
        #valoreS_n1 = list(RiesgoCargasisteman1.objects.filter(clasificacion=clasificacion).values_list("montodeperdidakusd", flat=True))        
        valores_unifica = []
        for x in valores:
            if x == "-":                
                valor = 0
            else:                
                valor = float(x)
            valores_unifica.append(valor)
            #float(x or 0)
        #valores_unifica = [float(x or 0) for x in valores]
        #n1list = [float(x) for x in valoreS_n1]
        diccionario[clasificacion] = {
            'valor':sum(valores_unifica),
            'color': arreglo_colores[i]
            }
       
        total += sum(valores_unifica)
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
        arreglo_valores_acumulado = [float(x or 0) for x in valores_riesgos_acumulado]
        suma_valores_acumulados = sum(arreglo_valores_acumulado)

        cantidad_riesgos_mes = len(list(Riesgo.objects.filter(clasificacion=clasificacion['clasificacion'], fechadigita__month=datetime.now().month, fechadigita__year=datetime.now().year).values()))
        valores_riesgos_mes = list(Riesgo.objects.filter(clasificacion=clasificacion['clasificacion'], fechadigita__month=datetime.now().month, fechadigita__year=datetime.now().year).values_list("maximaperdidamus", flat=True))
        arreglo_valores_mes = [float(x or 0) for x in valores_riesgos_mes]
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
        probabilidad = ""
        impacto = ""
        color = ""
        for gerencia in gerencias:
            rojos = 0
            amarillos = 0
            nombre_color = ''
            riesgos_gerencia = list(Riesgo.objects.filter(gerencia=gerencia['sigla']).values())            
                        
            for riesgo in riesgos_gerencia:                
                if RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).exists():
                    resultado_inherente_riesgo = list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).values('probabilidadresidual', 'impactoresidual'))
                    probabilidad = resultado_inherente_riesgo[0]['probabilidadresidual']
                    impacto = resultado_inherente_riesgo[0]['impactoresidual']
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
        directic = int(request.GET['directic'])
        matriz_inherente = getMatrizInherente(tipo, directic)        
        matriz_residual = getMatrizResidual(tipo, directic)
        matriz_objetivo = getMatrizObjetivo(tipo, directic)                        
        suma_inherente = 0
        for k, v in matriz_inherente.items():
            if len(k.split("_"))>1:
                suma_inherente+=v
        suma_residual = 0
        for k, v in matriz_residual.items():            
            if len(k.split("_"))>1:
                suma_residual+=v
        suma_objetivo = 0
        for k, v in matriz_objetivo.items():            
            if len(k.split("_")[1])>1:
                suma_objetivo+=v


        data = {'matriz_inherente':matriz_inherente, 'matriz_residual':matriz_residual, 'matriz_objetivo':matriz_objetivo, "suma_inherente":suma_inherente, "suma_residual":suma_residual, "suma_objetivo":suma_objetivo}
        return JsonResponse(data, safe=False)

def getMatrizInherente(tipo, directic):
    if tipo == "DET":
        gerencias = list(Gerencias.objects.all().values())
    else:
        gerencias = list(Gerencias.objects.filter(sigla=tipo).values())
        
    dict_inherentes = {}
    for gerencia in gerencias:        
        id_riesgos = list(Riesgo.objects.filter(gerencia=gerencia['sigla']).values_list('idriesgo', flat=True))                        
        if directic == 1:
            id_riesgos = list(Riesgo.objects.filter(gerencia=gerencia['sigla'], directic=1).values_list('idriesgo', flat=True))

        for id_riesgo in id_riesgos:
            probabilidad_inherente = ""
            impacto_inherente = ""
            if RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=id_riesgo).exists():
                if list(RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=id_riesgo).values("probabilidad"))[0]["probabilidad"] is not None:
                    probabilidad_inherente = int(list(RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=id_riesgo).values("probabilidad"))[0]["probabilidad"])
            if RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=id_riesgo).exists():
                if list(RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=id_riesgo).values("impacto"))[0]["impacto"] is not None:
                    impacto_inherente = int(list(RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=id_riesgo).values("impacto"))[0]["impacto"])
            
            label_coords = str(impacto_inherente)+'_'+str(probabilidad_inherente)                
            if label_coords in dict_inherentes:
                dict_inherentes[label_coords] += 1
            else:
                dict_inherentes[label_coords] = 1

    return dict_inherentes


def getMatrizResidual(tipo, directic):
    if tipo == "DET":
        gerencias = list(Gerencias.objects.all().values())
    else:
        gerencias = list(Gerencias.objects.filter(sigla=tipo).values())
        
    dict_residual = {}
    for gerencia in gerencias:
        id_riesgos = list(Riesgo.objects.filter(gerencia=gerencia['sigla']).values_list('idriesgo', flat=True))                        
        if directic == 1:            
            id_riesgos = list(Riesgo.objects.filter(gerencia=gerencia['sigla'], directic=1).values_list('idriesgo', flat=True))
        for id_riesgo in id_riesgos:
            probabilidad_residual = ""
            impacto_residual = ""
            if RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=id_riesgo).exists():
                if list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=id_riesgo).values("probabilidadresidual"))[0]["probabilidadresidual"] is not None:
                    probabilidad_residual = int(list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=id_riesgo).values("probabilidadresidual"))[0]["probabilidadresidual"])
            if RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=id_riesgo).exists():
                if list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=id_riesgo).values("impactoresidual"))[0]["impactoresidual"] is not None:
                    impacto_residual = int(list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=id_riesgo).values("impactoresidual"))[0]["impactoresidual"])
                                               
            label_coords = str(impacto_residual)+'_'+str(probabilidad_residual)                
            if label_coords in dict_residual:
                dict_residual[label_coords] += 1
            else:
                dict_residual[label_coords] = 1    
    return dict_residual

def getMatrizObjetivo(tipo, directic):
    if tipo == "DET":
        gerencias = list(Gerencias.objects.all().values())
    else:
        gerencias = list(Gerencias.objects.filter(sigla=tipo).values())
        
    dict_objetivo = {}
    for gerencia in gerencias:
        id_riesgos = list(Riesgo.objects.filter(gerencia=gerencia['sigla']).values_list('idriesgo', flat=True))                        
        if directic == 1:
            id_riesgos = list(Riesgo.objects.filter(gerencia=gerencia['sigla'], directic=1).values_list('idriesgo', flat=True))
        for id_riesgo in id_riesgos:
            probabilidad_objetivo = ""
            impacto_objetivo = ""
            if RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=id_riesgo).exists():
                if list(RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=id_riesgo).values("probabilidadcontrol"))[0]["probabilidadcontrol"] is not None:
                    probabilidad_objetivo = int(list(RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=id_riesgo).values("probabilidadcontrol"))[0]["probabilidadcontrol"])
            if RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=id_riesgo).exists():
                if list(RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=id_riesgo).values("impactocontrol"))[0]["impactocontrol"] is not None:
                    impacto_objetivo = int(list(RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=id_riesgo).values("impactocontrol"))[0]["impactocontrol"])

                                         
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

def getDatosDashboardTipoRiesgo(request):
    if request.method == "GET":        
        tipo = request.GET['tipo']
        atraso_proyecto = kpiAtrasoProyecto(tipo)
        probidad_transparencia = kpiProbidadTransparencia(tipo)
        falta_agua = kpiFaltaAgua(tipo)
        falla_equipo_critico = kpiFallaEquipoCritico(tipo)
        incendio = kpiIncendio(tipo)
        pandemia = kpiUnifica("eventos", "pandemia")
        otro = kpiUnifica("eventos", "otro")

        
        if tipo == "eventos":
            glosa = "Eventos"
            riesgos_acumulados = list(RiesgoUnifica.objects.all().values())
            cantidad_total_registros = len(riesgos_acumulados)
            cantidad_riesgos_acumulados = 0
            for cantidad in riesgos_acumulados:
                if comprobeConvertedFloat(cantidad['montoperdidakusd']):
                    if cantidad['montoperdidakusd'] != "-":
                        if float(cantidad['montoperdidakusd']) > 0:
                            cantidad_riesgos_acumulados+=1
            
            riesgos_mes = list(RiesgoUnifica.objects.filter(fecha__year=datetime.now().year, fecha__month=datetime.now().month).values())
            cantidad_riesgos_mes = 0
            for cantidad_mes in riesgos_mes:
                if comprobeConvertedFloat(cantidad['montoperdidakusd']):
                    if cantidad_mes['montoperdidakusd'] != "-":
                        if float(cantidad_mes['montoperdidakusd']) > 0:
                            cantidad_riesgos_mes+=1
            #cantidad_riesgos_acumulados = len(list(RiesgoUnifica.objects.all().values()))
            #cantidad_riesgos_mes = len(list(RiesgoUnifica.objects.filter(fecha__year=datetime.now().year, fecha__month=datetime.now().month).values()))            
        elif tipo == "riesgos":
            glosa = "Riesgos"
            cantidad_total_registros = len(list(Riesgo.objects.filter(estadoregistro='Vigente').values()))
            cantidad_riesgos_acumulados = len(list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values()))
            cantidad_riesgos_mes = len(list(RiesgoEvaluacioncualitativaresidual.objects.filter(modificado__year=datetime.now().year, modificado__month=datetime.now().month, nivelriesgoresidual="Alto").values()))
        elif tipo == "directi":
            glosa = "Directi"
            cantidad_total_registros = len(list(Riesgo.objects.filter(estadoregistro='Vigente', directic=1).values()))
            cantidad_riesgos_acumulados_alto = list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
            cantidad_riesgos_mensuales_alto = list(RiesgoEvaluacioncualitativaresidual.objects.filter(modificado__year=datetime.now().year, modificado__month=datetime.now().month, nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
            cantidad_riesgos_acumulados = len(list(Riesgo.objects.filter(idriesgo__in=cantidad_riesgos_acumulados_alto, directic=1).values()))
            cantidad_riesgos_mes = len(list(Riesgo.objects.filter(idriesgo__in=cantidad_riesgos_mensuales_alto, directic=1).values()))
                  
        data = {'atraso_proyecto':atraso_proyecto, 'probidad_transparencia':probidad_transparencia, 'falta_agua':falta_agua, 'falla_equipo_critico':falla_equipo_critico, 'incendio':incendio, 'pandemia':pandemia, 'otro':otro, 'cantidad_riesgos_acumulados':cantidad_riesgos_acumulados, 'cantidad_riesgos_mes':cantidad_riesgos_mes, 'cantidad_total_registros':cantidad_total_registros, "glosa":glosa}

        return JsonResponse(data, safe=False)

def detalleCoordenadaMatriz(request):
    if request.method == "GET":
        X = request.GET['X']
        Y = request.GET['Y']
        tipo_matriz = request.GET['tipo_matriz']
        gerencia = request.GET['gerencia']
        directic = int(request.GET['directic'])        

        if tipo_matriz == "res":
            id_riesgo = list(RiesgoEvaluacioncualitativaresidual.objects.filter(probabilidadresidual=X, impactoresidual=Y).values_list("idriesgo", flat=True))
        if tipo_matriz == "inhe":
            id_riesgo = list(RiesgoEvaluacioncualitativainherente.objects.filter(probabilidad=X, impacto=Y).values_list("idriesgo", flat=True))
        if tipo_matriz == "obj":
            id_riesgo = list(RiesgoEvaluacioncualitativaobjetivo.objects.filter(probabilidadcontrol=X, impactocontrol=Y).values_list("idriesgo", flat=True))
        
        if gerencia == "DET":
            lista_riesgos = list(Riesgo.objects.filter(idriesgo__in=id_riesgo).values())
        else:
            lista_riesgos = list(Riesgo.objects.filter(idriesgo__in=id_riesgo, gerencia=gerencia).values())
        
        if directic == 1:
            if gerencia == "DET":
                lista_riesgos = list(Riesgo.objects.filter(idriesgo__in=id_riesgo, directic=1).values())
            else:
                lista_riesgos = list(Riesgo.objects.filter(idriesgo__in=id_riesgo, gerencia=gerencia, directic=1).values())                        
        return JsonResponse(lista_riesgos, safe=False)

def getDatosCampo(request):
    if request.method == "GET":
        campo = request.GET['campo']
        datos_campo = list(RiesgoUnifica.objects.values_list(campo, flat=True).distinct())
        diccionario_datos_contador = {}
        diccionario_datos_montos = {}
        tipo = request.GET['tipo']
        valor = request.GET['valor']                
        for campo_consulta in datos_campo:            
            query = 'list(RiesgoUnifica.objects.filter('+campo+'=\''+str(campo_consulta)+'\').values("evento", "montoperdidakusd"))'
            datos = eval(query)
            if valor == "DET":
                query = 'list(RiesgoUnifica.objects.filter('+campo+'=\''+str(campo_consulta)+'\').values("evento", "montoperdidakusd"))'
                datos = eval(query)
            else:
                if tipo == "GERENCIA":
                    query = 'list(RiesgoUnifica.objects.filter(gerencia=\''+str(valor)+'\','+campo+'=\''+str(campo_consulta)+'\').values("evento", "montoperdidakusd"))'                    
                    datos = eval(query)
                elif tipo == "SUPERINTENDENCIA":
                    query = 'list(RiesgoUnifica.objects.filter(superintendencia=\''+str(valor)+'\','+campo+'=\''+str(campo_consulta)+'\').values("evento", "montoperdidakusd"))'
                    datos = eval(query)

            for dato in datos:
                if campo_consulta in diccionario_datos_contador:
                    diccionario_datos_contador[campo_consulta]+=1
                else:
                    diccionario_datos_contador[campo_consulta]=1
                if campo_consulta in diccionario_datos_montos:
                    if dato['montoperdidakusd'] != "-":
                        diccionario_datos_montos[campo_consulta] += int(float(dato['montoperdidakusd']))
                else:
                    if dato['montoperdidakusd'] != "-":
                        diccionario_datos_montos[campo_consulta] = int(float(dato['montoperdidakusd']))
                
                        
        datos_ordenados_contador = sorted(diccionario_datos_contador.items(), key=operator.itemgetter(1), reverse=True)
        datos_ordenados_montos = sorted(diccionario_datos_montos.items(), key=operator.itemgetter(1), reverse=True)
        i_q = 0
        dict_cantidades = {}
        for cantidad_ordenada in datos_ordenados_contador:
            if i_q < 5:
                dict_cantidades[cantidad_ordenada[0]] = cantidad_ordenada[1]
            i_q += 1
        
        i_m = 0
        dict_montos = {}
        for cantidad_ordenada_montos in datos_ordenados_montos:
            if i_m < 5:
                dict_montos[cantidad_ordenada_montos[0]] = cantidad_ordenada_montos[1]
            i_m += 1
        data = {'cantidad':dict_cantidades, 'montokus':dict_montos, 'datos_campo':datos_campo}        

        return JsonResponse(data ,safe=False)


def datosClasificacionEventos(request):
    if request.method == "GET":
        tipo = request.GET['tipo']
        valor = request.GET['valor']
        glosa = request.GET['glosa']
        campo = request.GET['campo']
        diccionario_datos_contador = {}
        diccionario_datos_montos = {}        
        if valor == "DET":
            query = 'list(RiesgoUnifica.objects.filter('+campo+'=\''+str(glosa)+'\').values("evento", "montoperdidakusd"))'
            datos = eval(query)
        else:
            if tipo == "GERENCIA":
                query = 'list(RiesgoUnifica.objects.filter(gerencia=\''+str(valor)+'\','+campo+'=\''+str(glosa)+'\').values("evento", "montoperdidakusd"))'
                datos = eval(query)
            elif tipo == "SUPERINTENDENCIA":
                query = 'list(RiesgoUnifica.objects.filter(superintendencia=\''+str(valor)+'\','+campo+'=\''+str(glosa)+'\').values("evento", "montoperdidakusd"))'
                datos = eval(query)
        
        for dato in datos:
            if dato['evento'] in diccionario_datos_contador:
                diccionario_datos_contador[dato['evento']]+=1                
            else:
                diccionario_datos_contador[dato['evento']]=1
            
            if dato['evento'] in diccionario_datos_montos:
                diccionario_datos_montos[dato['evento']]+=int(float(dato['montoperdidakusd']))
            else:
                diccionario_datos_montos[dato['evento']]=int(float(dato['montoperdidakusd']))

        datos_ordenados_contador = sorted(diccionario_datos_contador.items(), key=operator.itemgetter(1), reverse=True)
        datos_ordenados_montos = sorted(diccionario_datos_montos.items(), key=operator.itemgetter(1), reverse=True)

        i_q = 0
        dict_cantidades = {}
        for cantidad_ordenada in datos_ordenados_contador:
            if i_q < 9:
                dict_cantidades[cantidad_ordenada[0]] = cantidad_ordenada[1]
            i_q += 1
        
        i_m = 0
        dict_montos = {}
        for cantidad_ordenada_montos in datos_ordenados_montos:
            if i_m < 9:
                dict_montos[cantidad_ordenada_montos[0]] = cantidad_ordenada_montos[1]
            i_m += 1

        data = {'cantidad':dict_cantidades, 'montokus':dict_montos}        
        return JsonResponse(data, safe=False)


def listadoClasificacionTipoEvento(request):
    if request.method == "GET":
        meses = request.GET.getlist('meses[]')
        print(meses)
        #datos = list(RiesgoUnifica.objects.filter(fecha__month__in=meses).values())
        #print(datos)
        datos = []
        for mes in meses:
            clasificaciones = list(RiesgoUnifica.objects.filter(fecha__month=mes).values('clasificacion').distinct())
            dictDatos = {}
            
            for clasificacion in clasificaciones:
                dictDatos[clasificacion['clasificacion']] = {}
                datosClasificacion = list(RiesgoUnifica.objects.filter(fecha__month=mes, clasificacion=clasificacion['clasificacion']).values())
                for datosClas in datosClasificacion:
                    if datosClas['evento'] in dictDatos[clasificacion['clasificacion']]:
                        dictDatos[clasificacion['clasificacion']][datosClas['evento']]['valor']+=round(float(datosClas['montoperdidakusd']), 1)
                        dictDatos[clasificacion['clasificacion']][datosClas['evento']]['q']+=1
                        dictDatos[clasificacion['clasificacion']][datosClas['evento']]['mes']=str(datosClas['fecha'].month)
                    else:
                        dictDatos[clasificacion['clasificacion']][datosClas['evento']]={
                            'valor':round(float(datosClas['montoperdidakusd']), 1),
                            'q':1,
                            'mes':str(datosClas['fecha'].month)
                        }
            datos.append(dictDatos)
        
        return JsonResponse(datos, safe=False)



def listadoClasificacionGerencia(request):
    if request.method == "GET":
        meses = request.GET.getlist('meses[]')
        gerencia = request.GET['gerencia']
        #datos = list(RiesgoUnifica.objects.filter(fecha__month__in=meses).values())
        print(meses)
        #gerencias = list(RiesgoUnifica.objects.filter(fecha__month__in=meses,).values('gerencia').distinct())
        dictDatos = {}
        datos = []
        for mes in meses:            
            datosClasificacion = list(RiesgoUnifica.objects.filter(fecha__month=mes, gerencia=gerencia).values())
            for datosClas in datosClasificacion:
                if datosClas['clasificacion'] in dictDatos:
                    dictDatos[datosClas['clasificacion']]['valor']+=round(float(datosClas['montoperdidakusd']), 1)
                    dictDatos[datosClas['clasificacion']]['q']+=1
                    dictDatos[datosClas['clasificacion']]['mes']=str(mes)
                else:
                    dictDatos[datosClas['clasificacion']]={
                        'valor':round(float(datosClas['montoperdidakusd']), 1),
                        'q':1,
                        'mes':str(mes)
                        }
            datos.append(dictDatos.copy())
                
        arregloMeses = []
        for mes in meses:
            print(mes)
            dictDatosGerencia = {}
            datosClasificacion = []
            if RiesgoUnifica.objects.filter(fecha__month=mes, gerencia=gerencia).exists():
                datosClasificacion = list(RiesgoUnifica.objects.filter(fecha__month=mes, gerencia=gerencia).values())
            for dato in datosClasificacion:
                if dato['clasificacion'] in dictDatosGerencia:
                    dictDatosGerencia[dato['clasificacion']]['valor']+=round(float(dato['montoperdidakusd']), 1)
                    dictDatosGerencia[dato['clasificacion']]['q']+=1
                    dictDatosGerencia[dato['clasificacion']]['mes']=str(dato['fecha'].month)
                else:
                    dictDatosGerencia[dato['clasificacion']]={
                        'valor':round(float(dato['montoperdidakusd']), 1),
                        'q':1,
                        'mes':str(dato['fecha'].month)
                    }
                
            arregloMeses.append(dictDatosGerencia.copy())
        print(arregloMeses)


        
        return JsonResponse(arregloMeses, safe=False)
        

def getColorIndicadores(request):
    if request.method == "GET":
        data = list(RiesgoColorindicadores.objects.all().values())

        return JsonResponse(data, safe=False)

