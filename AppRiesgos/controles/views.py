from django.shortcuts import render
from crearRiesgo.queries import QueryTraeRiesgos
from django.http import JsonResponse, HttpResponseRedirect
from core.models import *
from .queries import QueryRiesgoCausas, QueryRiesgoConsecuencias, QueryRiesgosControlesCreados, QueryRiesgosControlesAsociados, QueryCausasControl, QueryConsecuenciasControl, QueryMonitoreoControl, QueryAutoevaluacionControl, QueryEvidenciaControl, QueryDatosControl
from django.core.files.storage import FileSystemStorage
from core.clases.core.identificadores import GetId
from datetime import datetime
from controles.clases.AlmacenaRespaldoUpdateMatrices import RespaldoUpdate
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicio(request):
    riesgos = QueryTraeRiesgos()
    causas = list(RiesgoCausas.objects.all().values())
    consecuencias = list(RiesgoConsecuencias.objects.all().values())        
    data = {'riesgos':riesgos, 'causas':causas, 'consecuencias':consecuencias}
    return render(request, "controles/inicio.html", data)

def traeDetalleRiesgo(request):
    if request.method == "GET":
        id_riesgo = request.GET['id_riesgo']
        detalle_riesgo = list(Riesgo.objects.filter(idriesgo=id_riesgo).values())
        causas = QueryRiesgoCausas(id_riesgo)
        consecuencias = QueryRiesgoConsecuencias(id_riesgo)
        print(consecuencias)
        
        data = {'detalle_riesgo':detalle_riesgo, 'causas':causas, 'consecuencias':consecuencias}
        return JsonResponse(data, safe=False)


def saveControl(request):
    if request.method == "POST":
        id_control = GetId('RiesgoControl', 'CTRL', 'idcontrol').get_id()
        id_riesgo = request.POST.get("id_riesgo_control")
        nombre_control = request.POST.get("nombres_controles")
        descripcion_control = request.POST.get("descripcion_control")
        tipo_control = request.POST.get("tipos_controles")
        dueno_control = request.POST.get("dueno_control")
        frecuencia_control = request.POST.get("frecuencias_controles")
        eficacia = request.POST.get("eficacia_controles")
        eficiencia = request.POST.get("eficiencia_controles")
        efectividad = request.POST.get("efectividad_controles")
        causas_control = request.POST.getlist("causas_asociadas_al_control")
        consecuencias_control = request.POST.getlist("consecuencias_asociadas_al_control")
        frecuencia_monitoreo = request.POST.get("frecuencias_monitoreos")
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_termino = request.POST.get("fecha_termino")

        print("las causas son ", causas_control)
        print("las consecuencias son ", consecuencias_control)

        save_control = RiesgoControl(
            idcontrol = id_control,
            idriesgo = id_riesgo,
            nombrecontrol = nombre_control,
            descripcioncontrol = descripcion_control, 
            tipocontrol = tipo_control,
            dueñocontrol = dueno_control,
            frecuenciacontrol = frecuencia_control,
            estadoregistro = "ACTIVO",
            modificado = datetime.now(),
            creado = datetime.now(),
            creadopor = str(request.user),
            modificadopor = str(request.user)
        )
        save_control.save()
        if save_control.pk is not None:
            save_autoevaluacion = RiesgoControlAutoevaluacion(
                idcontrol = save_control.pk,
                idriesgo = id_riesgo,
                eficacia = eficacia,
                eficiencia = eficiencia,
                efectividad = efectividad,
                modificado = datetime.now(),
                creado = datetime.now(),
                creadopor = str(request.user),
                modificadopor = str(request.user)
            )
            save_autoevaluacion.save()
            for causa in causas_control:
                save_control_causa = RiesgoControlCausa(
                    idcontrol = save_control.pk ,
                    idriesgo = id_riesgo ,
                    idcausa = causa,
                    estadoregistro = "ACTIVO",
                    modificado = datetime.now(),
                    creado = datetime.now(),
                    creadopor = str(request.user),
                    modificadopor = str(request.user),
                )
                save_control_causa.save()

            for consecuencia in consecuencias_control:
                save_control_consecuencia = RiesgoControlConsecuencia(
                    idcontrol = save_control.pk ,
                    idriesgo = id_riesgo ,
                    idconsecuencia = consecuencia,
                    estadoregistro = "ACTIVO",
                    modificado = datetime.now(),
                    creado = datetime.now(),
                    creadopor = str(request.user),
                    modificadopor = str(request.user),
                )
                save_control_consecuencia.save()

            myfile = request.FILES['evidencia']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

            save_evidencia = RiesgoControlEvidencia(
                idcontrol = save_control.pk,
                tipo_de_contenido = uploaded_file_url,
                archivo = uploaded_file_url,
                estadoregistro = "ACTIVO",
                modificado = datetime.now(),
                creado = datetime.now(),
                creadopor = str(request.user),
                modificadopor = str(request.user),
            )
            save_evidencia.save()

            save_control_monitoreo = RiesgoControlMonitoreo(
                idcontrol = save_control.pk, 
                idriesgo = id_riesgo, 
                frecuenciamonitoreo = frecuencia_monitoreo, 
                inicio = fecha_inicio, 
                fin = fecha_termino, 
                evidencia = save_evidencia.pk, 
                estadoregistro = "ACTIVO", 
                gestionriesgocritico = "-", 
                modificado = datetime.now(), 
                creado = datetime.now(), 
                creado_por = str(request.user), 
                modificado_por = str(request.user), 
            )
            save_control_monitoreo.save()
    
    print("la evidencia ", uploaded_file_url)

    return JsonResponse('', safe=False)

def traeControlesRiesgo(request):
    if request.method == "GET":
        riesgo_descripcion = request.GET['descr_riesgo']
        id_riesgo = request.GET['id_riesgo']

        controles_asociados = QueryRiesgosControlesAsociados(id_riesgo)
        controles_creados = QueryRiesgosControlesCreados(riesgo_descripcion)

        data = {'controles_asociados':controles_asociados, 'controles_creados':controles_creados}
        return JsonResponse(data, safe=False)

def traeDatosControl(request):
    if request.method == "GET":
        id_control = request.GET['id_control']

        causas = QueryCausasControl(id_control)
        consecuencias = QueryConsecuenciasControl(id_control)
        
        autoevaluacion = QueryAutoevaluacionControl(id_control)
        monitoreo = QueryMonitoreoControl(id_control)
        evidencia = QueryEvidenciaControl(id_control)
        datos_control = QueryDatosControl(id_control)

        data = {'causas':causas, 'consecuencias':consecuencias, 'autoevaluacion':autoevaluacion, 'monitoreo':monitoreo, 'evidencia':evidencia, 'datos_control':datos_control}

        return JsonResponse(data, safe=False)

def eliminarControl(request):
    if request.method =="GET":
        id_control = request.GET['id_control']
        id_riesgo = request.GET['id_riesgo']

        RiesgoControl.objects.filter(idcontrol = id_control, idriesgo = id_riesgo).delete()
        RiesgoControlAutoevaluacion.objects.filter(idcontrol = id_control, idriesgo = id_riesgo).delete()
        RiesgoControlCausa.objects.filter(idcontrol = id_control, idriesgo = id_riesgo).delete()
        RiesgoControlConsecuencia.objects.filter(idcontrol = id_control, idriesgo = id_riesgo).delete()
        RiesgoControlEvidencia.objects.filter(idcontrol = id_control).delete()
        RiesgoControlMonitoreo.objects.filter(idcontrol = id_control, idriesgo = id_riesgo).delete()

        return JsonResponse(True, safe=False)

def getMatrizResidual(request):
    if request.method == "GET":
        id_riesgo = request.GET['id_riesgo']
        matriz = list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=id_riesgo).values())
        return JsonResponse(matriz, safe = False)

def editarMatrizResidual(request):
    if request.method == "POST":
        if RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=request.POST.get("riesgo-control-residual")).exists():
            RespaldoUpdate("RiesgoEvaluacioncualitativaresidual", "RiesgoEvaluacioncualitativaresidualupdate", request.POST.get("riesgo-control-residual")).respaldoUpdate()
            RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=request.POST.get("riesgo-control-residual")).update(
                probabilidadresidual = request.POST.get("res_probabilidad"),
                impactoresidual = request.POST.get("res_impacto"),
                impactocapexresidual = request.POST.get("res_capex"),
                impactoplazoresidual = request.POST.get("res_plazo"),
                impactoeconomicoresidual = request.POST.get("res_economico"),
                impactossoresidual = request.POST.get("res_sso"),
                impactomedioambienteresidual = request.POST.get("res_medioambiente"),
                impactocomunitarioresidual = request.POST.get("res_comunitario"),
                impactoreputacionalresidual = request.POST.get("res_reputacional"),
                impactolegalresidual = request.POST.get("res_legal"),
                ambitodominanteresidual = 0,
                magnitudriesgoresidual = request.POST.get("res_magnitud"),
                nivelriesgoresidual = request.POST.get("res_nivel"),
                modificado = datetime.now()
            )
            valor = True
        else:
            valor = saveMatrizResidual(request)
        return JsonResponse(valor, safe=False)
        

def saveMatrizResidual(request):
    if request.method == "POST":
        save_residual = RiesgoEvaluacioncualitativaresidual(
            idriesgo = request.POST.get("riesgo-control-residual"),
            idecr = request.POST.get("riesgo-control-residual"),
            probabilidadresidual = float(request.POST.get("res_probabilidad")),
            impactoresidual = float(request.POST.get("res_impacto")),
            impactocapexresidual = float(request.POST.get("res_capex")),
            impactoplazoresidual = float(request.POST.get("res_plazo")),
            impactoeconomicoresidual = float(request.POST.get("res_economico")),
            impactossoresidual = float(request.POST.get("res_sso")),
            impactomedioambienteresidual = float(request.POST.get("res_medioambiente")),
            impactocomunitarioresidual = float(request.POST.get("res_comunitario")),
            impactoreputacionalresidual = float(request.POST.get("res_reputacional")),
            impactolegalresidual = float(request.POST.get("res_legal")),
            ambitodominanteresidual = 0,
            magnitudriesgoresidual = float(request.POST.get("res_magnitud")),
            nivelriesgoresidual = request.POST.get("res_nivel"),
            fecha = datetime.now(),
            estado = "Vigente",
            modificado = datetime.now(),
            creado = datetime.now(),
            creadopor = str(request.user),
            modificadopor = str(request.user)
        )
        save_residual.save()

        if save_residual.pk is not None:
            return True
        else:
            return False

def getRiesgoMagnitudnivel(request):
    if request.method == "GET":
        probabilidad = request.GET['probabilidad']
        impacto = request.GET['impacto']
        print(probabilidad)
        print(impacto)
        magnitud = ""
        nivel = ""
        if RiesgoMagnitudnivel.objects.filter(probabilidad = probabilidad, impacto=impacto).exists():
            magnitud_nivel = list(RiesgoMagnitudnivel.objects.filter(probabilidad = probabilidad, impacto=impacto).values())
            magnitud = magnitud_nivel[0]['magnitud']
            nivel = magnitud_nivel[0]['nivel']
        data = {'magnitud':magnitud, 'nivel':nivel}
        return JsonResponse(data, safe=False)
