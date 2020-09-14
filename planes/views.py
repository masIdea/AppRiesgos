from django.shortcuts import render
from controles.queries import QueryRiesgoCausas, QueryRiesgoConsecuencias, QueryRiesgosControlesCreados, QueryRiesgosControlesAsociados, QueryCausasControl, QueryConsecuenciasControl, QueryMonitoreoControl, QueryAutoevaluacionControl, QueryEvidenciaControl, QueryDatosControl
from core.models import *
from crearRiesgo.queries import QueryTraeRiesgos
from django.http import JsonResponse, HttpResponseRedirect
from core.clases.core.identificadores import GetId
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from core.utils import id_generator

# Create your views here.
@login_required
def inicio(request):
    riesgos = QueryTraeRiesgos()
    causas = list(RiesgoCausas.objects.all().values())
    consecuencias = list(RiesgoConsecuencias.objects.all().values())        
    data = {'riesgos':riesgos, 'causas':causas, 'consecuencias':consecuencias}
    return render(request, "planes/inicio.html", data)

def traeDetalleriesgo(request):
    if request.method == "GET":        
        id_riesgo = request.GET['id_riesgo']
        detalle_riesgo = list(Riesgo.objects.filter(idriesgo=id_riesgo).values())
        causas = QueryRiesgoCausas(id_riesgo)
        consecuencias = QueryRiesgoConsecuencias(id_riesgo)
        print(causas)
        print(consecuencias)

        data = {'detalle_riesgo':detalle_riesgo, 'causas':causas, 'consecuencias':consecuencias}
        return JsonResponse(data, safe=False)

def savePlanRespuesta(request):
    if request.method == "POST":
        id_plan_respuesta = GetId('RiesgoPlanderespuesta', 'PLRES', 'idplanrespuesta').get_id()
        id_riesgo = request.POST.get("riesgo-plan")
        estrategia = request.POST.get("estrategia-plan")
        trigger = request.POST.get("trigger-plan")
        descripcion = request.POST.get("descripcion-plan")
        dueno = request.POST.get("dueno-plan")
        cargo_dueno = request.POST.get("cargo-dueno-plan")
        edit = request.POST.get("edit-plan")
        print("EL EDIT ES ", edit)
        if edit == str(1):
            return_edit = editarPlan(request)
            data = {'valida':return_edit}            
            return JsonResponse(data, safe=False)
        else:                
            save_plan = RiesgoPlanderespuesta(
                idplanrespuesta = id_plan_respuesta,
                idriesgo = id_riesgo,
                estrategia = estrategia,
                trigger= trigger,
                descripcion = descripcion,
                dueñoplanderespuesta = dueno,
                cargodueñoplan = cargo_dueno,
                costo = None,
                fechainicio = None,
                fechatermino = None,
                avancereal = None,
                avanceplanificado = None,
                estadoplanderespuesta = "ACTIVO",
                fecha = None,
                estadoregistro = "Vigente",
                modificado = datetime.now(),
                creado = datetime.now(),
                creado_por = str(request.user),
                modificado_por = str(request.user)
            )
            save_plan.save()
            
            if save_plan.pk is not None:
                data = {'valida':True}
            else:
                data = {'valida':False}
            
            return JsonResponse(data, safe=False)

def editarPlan(request):
    if request.method == "POST":
        print("A editar")
        estrategia = request.POST.get("estrategia-plan")
        trigger = request.POST.get("trigger-plan")
        descripcion = request.POST.get("descripcion-plan")
        dueno = request.POST.get("dueno-plan")
        cargo_dueno = request.POST.get("cargo-dueno-plan")
        id_plan = request.POST.get("name-plan-id")
        RiesgoPlanderespuesta.objects.filter(idplanrespuesta=id_plan).update(            
            estrategia = estrategia,
            trigger = trigger,
            descripcion = descripcion,
            dueñoplanderespuesta = dueno,
            cargodueñoplan = cargo_dueno,
            modificado  = datetime.now(),          
            modificado_por = str(request.user),
        )
        
        return True

def eliminarPlan(request):
    if request.method == "GET":
        id_plan = request.GET['id_plan']
        RiesgoPlanderespuesta.objects.filter(idplanrespuesta=id_plan).update(            
            estadoregistro="ELIMINADO",
        )        
        return JsonResponse(True, safe=False)        

def saveDetallePlanRespuesta(request):
    if request.method == "POST":
        pass

def traeDetallePlanesRiesgo(request):
    if request.method == "GET":
        print("detalle plan")
        id_riesgo = request.GET['id_riesgo']
        print(id_riesgo)
        detalle_plan_riesgo = list(RiesgoPlanderespuesta.objects.filter(idriesgo=id_riesgo, estadoregistro="Vigente").values())
        print("EL DETALLE DEL PLAN ES -- > ", detalle_plan_riesgo)
        data = {'detalle_plan_riesgo':detalle_plan_riesgo}
        return JsonResponse(data, safe=False)

def traeDetallePlanRespuesta(request):
    if request.method == "GET":        
        id_plan_respuesta = request.GET['id_plan']
        print(id_plan_respuesta)
        detalle_plan_respuesta = list(RiesgoPlanderespuesta.objects.filter(idplanrespuesta=id_plan_respuesta).values())
        actividades_plan_respuesta = list(RiesgoPlanderespuestaActividad.objects.filter(idplanderespuesta=id_plan_respuesta, estadoregistro="Vigente").values())        
        print(actividades_plan_respuesta)
        programado = porcentajeAvanceProgramadoFecha(actividades_plan_respuesta)
        inicio_termino = fecIniFecTermActividad(actividades_plan_respuesta)
        
        data = {'detalle_plan_respuesta':detalle_plan_respuesta, 'actividades_plan_respuesta':actividades_plan_respuesta, 'programado':programado, 'inicio_termino':inicio_termino}
        return JsonResponse(data, safe=False)

def porcentajeAvanceProgramadoFecha(actividadObjeto):
    porcentaje_dia_actual = 0
    for actividad in actividadObjeto:
        if actividad['inicio'] and actividad['termino']:
            mes_inicio = actividad['inicio'].month
            mes_termino = actividad['termino'].month
            ano_inicio = actividad['inicio'].year
            ano_termino = actividad['termino'].year
        else:
            mes_inicio = -1
            mes_termino = 0
            ano_inicio = 0
            ano_termino = 0

        if ano_inicio == ano_termino and mes_inicio == mes_termino:
            porcentaje_dia_actual += float(traeAnoIniEAnoTermEMesIniEMesTerm(actividad))

    return porcentaje_dia_actual

def traeAnoIniEAnoTermEMesIniEMesTerm(actividad):    
    contador = 1    
    diccionario_porcentajes = {}
    dias = 0
    dias = actividad['termino'].day - actividad['inicio'].day
    #print(dias)
    for i in range(actividad['inicio'].day, (actividad['termino'].day + 1 )):        
        porcentaje_dia = contador/dias
        #print("EL CONTADOR Y EL DIA RESPECTIVAMENTE SON ", contador, dias)
        diccionario_porcentajes[i] = porcentaje_dia
        if contador != dias:
            contador +=1


    if int(datetime.now().day) <= int(actividad['termino'].day):
        porcentaje_actividad = diccionario_porcentajes[datetime.now().day] * actividad['pesoespecifico']
    else:
        porcentaje_actividad = (100 * actividad['pesoespecifico']) / 100
    
    
    return porcentaje_actividad

def fecIniFecTermActividad(actividades):
    inicio = None
    termino = None
    inicio_termino = {}
    for actividad in actividades:
        if actividad['inicio']:
            if inicio is None:
                inicio = actividad['inicio']
            if termino is None:
                termino = actividad['termino']

            if actividad['inicio'] < inicio:
                inicio = actividad['inicio']
            
            if actividad['termino'] > termino:
                termino = actividad['termino']
        else:
            inicio_termino={'inicio':'','termino':''}

    inicio_termino['inicio'] = inicio
    inicio_termino['termino'] = termino

    return inicio_termino


def saveActividadPlan(request):
    if request.method == "POST":
        print("QWETRTYU")
        edita = request.POST.get("txt-edit-actividad")
        if edita == str(1):
            return_edita_actividad = editaActividad(request)
            return JsonResponse(return_edita_actividad, safe=False)
        valida = False        

        myfile = request.FILES['evidencia']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        id_plan_respuesta = request.POST.get("txt-id-plan")
        id_actividad = id_generator()
        nombre_actividad = request.POST.get("actividad-nombre")
        nombre_responsable = request.POST.get("actividad-responsable")
        estrategia = request.POST.get("actividad-estrategia")
        costo = request.POST.get("actividad-costo")
        estado = request.POST.get("actividad-estado")
        fec_ini = request.POST.get("actividad-fecha-inicio").split("/")
        fec_termino = request.POST.get("actividad-fecha-termino").split("/")
        detalle = request.POST.get("actividad-detalle-actividad")
        peso = request.POST.get("actividad-peso-especifico")
        avance_real = request.POST.get("actividad-avance-real")


        #falta agregar el campo nuevo
        save_plan_respuesta_actividad = RiesgoPlanderespuestaActividad(
            idplanderespuesta = id_plan_respuesta,
            idactividad = id_actividad,
            nombreactividad = nombre_actividad,
            responsable = nombre_responsable,
            estrategia = estrategia,
            costo = costo,
            estadoactividad = estado,
            inicio = fec_ini[2]+"-"+fec_ini[0]+"-"+fec_ini[1],
            termino = fec_termino[2]+"-"+fec_termino[0]+"-"+fec_termino[1],
            detalleactividad = detalle,
            pesoespecifico = peso,
            estadoregistro = "Vigente",
            modificado = datetime.now(),
            creado = datetime.now(),
            creadopor = str(request.user),
            modificadopor = str(request.user),
            avancereal = avance_real,
        )
        save_plan_respuesta_actividad.save()

        if save_plan_respuesta_actividad.pk is not None:
            id_control = GetId('RiesgoPlanderespuestaEvidencia', 'CTRLEVIDACT', 'idcontrol').get_id()
            save_evidencia = RiesgoPlanderespuestaEvidencia(
                idcontrol = id_control,
                tipo_de_contenido = "file",
                archivo = uploaded_file_url,
                estadoregistro = "Vigente",
                modificado = datetime.now(),
                creado = datetime.now(),
                creadopor = str(request.user),
                modificadopor = str(request.user),
                idactividad = save_plan_respuesta_actividad.pk
            )
            save_evidencia.save()

            if save_evidencia.pk is not None:
                valida = True        
        data = {'valida':valida}
        return JsonResponse(data, safe=False)

def detalleActividad(request):
    if request.method == "GET":
        id_actividad = request.GET['id_actividad']
        actividad = list(RiesgoPlanderespuestaActividad.objects.filter(idactividad=id_actividad, estadoregistro="Vigente").values())        
        archivo = ""
        if len(RiesgoPlanderespuestaEvidencia.objects.filter(idactividad=id_actividad).values()) > 0:
            archivo = RiesgoPlanderespuestaEvidencia.objects.filter(idactividad=id_actividad).values("archivo")[0]["archivo"]
        
        data = {'actividad':actividad, "archivo":archivo}
        return JsonResponse(data, safe=False)

def editaActividad(request):
    if request.method == "POST":
        id_actividad = request.POST.get("txt-id-actividad")
        avance_real_modificado = float(request.POST.get("actividad-avance-real"))
        id_plan = request.POST.get("txt-id-plan")

        avances_reales_plan = list(RiesgoPlanderespuestaActividad.objects.filter(idplanderespuesta=id_plan, estadoregistro = "Vigente").exclude(idactividad=id_actividad).values_list("avancereal", flat=True))
        real_actividad_actual = float(RiesgoPlanderespuestaActividad.objects.filter(idactividad=id_actividad, estadoregistro = "Vigente").values("avancereal")[0]['avancereal'])
        sumatoria_reales_plan_seleccionado = 0 
        for real in avances_reales_plan:
            sumatoria_reales_plan_seleccionado += float(real)        
        resultado_suma_total = avance_real_modificado + sumatoria_reales_plan_seleccionado

        print(resultado_suma_total)
        print(avance_real_modificado)
        print(sumatoria_reales_plan_seleccionado)
        if resultado_suma_total > 100:
            data = {"valida":False, "mensaje":"El valor ingresado no debe superar al 100% de la sumatoria de todas las actividades asociadas al plan."}
        elif real_actividad_actual >= avance_real_modificado:
            data = {"valida":False, "mensaje":"El valor de avance real ingresado debe ser mayor al valor existente en la actividad."}
        else:
            RiesgoPlanderespuestaActividad.objects.filter(idactividad=id_actividad).update(avancereal=avance_real_modificado)
            data = {"valida":True, "mensaje":"Registro Editado."}
        return data

def eliminarActividad(request):
    if request.method == "GET":
        id_actividad = request.GET['id_actividad']
        RiesgoPlanderespuestaActividad.objects.filter(idactividad=id_actividad).update(estadoregistro="ELIMINADO")
        data = {"info":"Registro Eliminado."}
        return JsonResponse(data, safe=False)

def saveMatrizObjetivo(request):
    if request.method == "POST":
        if RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=request.POST.get("riesgo-control-objetivo")).exists():
            #RespaldoUpdate("RiesgoEvaluacioncualitativaresidual", "RiesgoEvaluacioncualitativaresidualupdate", request.POST.get("riesgo-control-residual")).respaldoUpdate()
            RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=request.POST.get("riesgo-control-objetivo")).update(
                probabilidadcontrol = request.POST.get("obj_probabilidad"),
                impactocontrol = request.POST.get("obj_impacto"),
                impactocapexcontrol = request.POST.get("obj_capex"),
                impactoplazocontrol = request.POST.get("obj_plazo"),
                impactoeconomicocontrol = request.POST.get("obj_economico"),
                impactossocontrol = request.POST.get("obj_sso"),
                impactomedioambientecontrol = request.POST.get("obj_medioambiente"),
                impactocomunitariocontrol = request.POST.get("obj_comunitario"),
                impactoreputacionalcontrol = request.POST.get("obj_reputacional"),
                impactolegalcontrol = request.POST.get("obj_legal"),
                ambitodominantecontrol = 0,
                magnitudriesgocontrol = request.POST.get("obj_magnitud"),
                nivelriesgocontrol = request.POST.get("obj_nivel"),
                fecha = datetime.now(),
                estado = "Vigente",
                modificado= datetime.now(),
                creado = datetime.now(),
                creadopor = str(request.user),
                modificadopor = str(request.user),
            )
            valor = True
        else:
            save_matriz_objetivo = RiesgoEvaluacioncualitativaobjetivo(
                idriesgo = request.POST.get("riesgo-control-objetivo"),
                ideco = request.POST.get("riesgo-control-objetivo"),
                probabilidadcontrol = request.POST.get("obj_probabilidad"),
                impactocontrol = request.POST.get("obj_impacto"),
                impactocapexcontrol = request.POST.get("obj_capex"),
                impactoplazocontrol = request.POST.get("obj_plazo"),
                impactoeconomicocontrol = request.POST.get("obj_economico"),
                impactossocontrol = request.POST.get("obj_sso"),
                impactomedioambientecontrol = request.POST.get("obj_medioambiente"),
                impactocomunitariocontrol = request.POST.get("obj_comunitario"),
                impactoreputacionalcontrol = request.POST.get("obj_reputacional"),
                impactolegalcontrol = request.POST.get("obj_legal"),
                ambitodominantecontrol = 0,
                magnitudriesgocontrol = request.POST.get("obj_magnitud"),
                nivelriesgocontrol = request.POST.get("obj_nivel"),
                fecha = datetime.now(),
                estado = "Vigente",
                modificado= datetime.now(),
                creado = datetime.now(),
                creadopor = str(request.user),
                modificadopor = str(request.user),
            )
            save_matriz_objetivo.save()
            if save_matriz_objetivo.pk is not None:
                valor = True
            else:
                valor = False
        return JsonResponse(valor, safe=False)


