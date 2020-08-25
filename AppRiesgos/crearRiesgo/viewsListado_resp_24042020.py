from django.shortcuts import render
from core.clases.core.identificadores import GetId
from core.models import Riesgo, Direcciones, RiesgoCausas, RiesgoConsecuencias, RiesgoNCausariesgo, RiesgoNRiesgoconsecuencia, Gerencias, RiesgoEvaluacioncualitativainherente, RiesgoListas, RiesgoRbsfamilia
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .queries import QueryRiesgoSimilar, QueryTraeRiesgos, QueryFamilia
from datetime import date, datetime


def inicio(request):
    listado_causas = list(RiesgoCausas.objects.all().values())
    lsitado_consecuencias = list(RiesgoConsecuencias.objects.all().values())    
    gerencias = list(Gerencias.objects.all().values())
    direcciones = list(Direcciones.objects.all().values())
    proyectos = RiesgoListas.objects.filter(tipo="Proyectos", estado="ACTIVO").values("glosa")
    clasificaciones = RiesgoListas.objects.filter(tipo="Clasificaciones", estado="ACTIVO").values("glosa")
    fases = RiesgoListas.objects.filter(tipo="Fases", estado="ACTIVO").values("glosa")
    duenos = RiesgoListas.objects.filter(tipo="Duenos", estado="ACTIVO").values("glosa")
    cargos = RiesgoListas.objects.filter(tipo="Cargos", estado="ACTIVO").values("glosa")
    estados = RiesgoListas.objects.filter(tipo="Estados", estado="ACTIVO").values("glosa")    
    familias = list(QueryFamilia())
    subprocesos = list(RiesgoRbsfamilia.objects.values())
    riesgos = QueryTraeRiesgos()

    data = {'causas':listado_causas, 
            'consecuencias':lsitado_consecuencias, 
            'familias':familias,
            'gerencias':gerencias,
            'proyectos':proyectos,
            'direcciones':direcciones,
            'clasificaciones':clasificaciones,
            'fases':fases,
            'duenos':duenos,
            'cargos':cargos,
            'estados':estados,
            'riesgos':riesgos,
            'subprocesos':subprocesos,
            }        
    return render(request, "crearRiesgo/listado.html", data)

def editarRiesgo(request):
    if request.method == "POST":
        id_riesgo = request.POST.get("id-riesgo")
        gerencia = request.POST.get("riesgos_gerencias")
        direccion = request.POST.get("riesgos_direcciones")
        proyecto = request.POST.get("riesgos_proyectos")
        codigo_proyecto = request.POST.get("riesgos_codigos_proyectos")
        fase = request.POST.get("riesgos_fases")
        cargos = request.POST.get("riesgos_cargos")        
        clasificacion = request.POST.get("riesgos_clasificaciones")        
        fecha = request.POST.get("riesgos_fechas").split("/")
        fecha = fecha[2] + '-' + fecha[0] + '-' + fecha[1]
        dueno = request.POST.get("riesgos_duenos")
        idrbs = request.POST.get("riesgos_subprocesos")
        descripcion_riesgo = request.POST.get("riesgo_descripcion_riesgo")
        print(descripcion_riesgo)
        maxima_perdida_mus = request.POST.get("maxima-perdida-mus")
        maxima_perdida_meses = request.POST.get("maxima-perdida-meses")
        Riesgo.objects.filter(idriesgo=id_riesgo).update(            
            gerencia = gerencia,
            direccion = direccion,
            proyecto = proyecto,
            codigoproyecto = codigo_proyecto,
            fasedelriesgo = fase,
            dueño = dueno,
            cargodeldueño = cargos,
            idrbs = idrbs,                                                                                    
            modificado = datetime.now(),                        
            modificadopor = "jorel",
            clasificacion = clasificacion,
            maximaperdidamus = maxima_perdida_mus,
            maximaperdidameses = maxima_perdida_meses,
            descripcionriesgo = descripcion_riesgo
        )
        return HttpResponseRedirect(reverse("trae_riesgos"))

def datosEditaRiesgo(request):
    if request.method == "GET":
        familia= ''
        id_causas_riesgo = ''
        id_consecuencias_riesgo = ''
        inherente = ''
        causas_asociadas = ''
        consecuencias_asociadas = ''
        id_riesgo = request.GET['id_riesgo']
        datos_riesgo = list(Riesgo.objects.filter(idriesgo=id_riesgo).values())        
        id_rbs = datos_riesgo[0]['idrbs']
        if RiesgoRbsfamilia.objects.filter(idrbs=id_rbs).exists():
            registro_rbs = list(RiesgoRbsfamilia.objects.filter(idrbs=id_rbs).values())
            familia = registro_rbs[0]['familia']
        
        if RiesgoNCausariesgo.objects.filter(idriesgo=id_riesgo).exists():
            id_causas_riesgo = list(RiesgoNCausariesgo.objects.filter(idriesgo=id_riesgo).values_list("idcausa", flat=True))
        
        if RiesgoNRiesgoconsecuencia.objects.filter(idriesgo=id_riesgo).exists():
            id_consecuencias_riesgo = list(RiesgoNRiesgoconsecuencia.objects.filter(idriesgo=id_riesgo).values_list("idconsecuencia", flat=True))
        
        if RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=id_riesgo).exists():
            inherente = list(RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=id_riesgo).values())

        if RiesgoCausas.objects.filter(idcausa__in=id_causas_riesgo).exists():
            causas_asociadas = list(RiesgoCausas.objects.filter(idcausa__in=id_causas_riesgo).values())
        
        if RiesgoConsecuencias.objects.filter(idconsecuencia__in=id_consecuencias_riesgo).exists():
            consecuencias_asociadas = list(RiesgoConsecuencias.objects.filter(idconsecuencia__in=id_consecuencias_riesgo).values())



        data = {'inherente':inherente, 'datos_riesgo':datos_riesgo, 'familia':familia, 'subproceso':id_rbs, 'causas_asociadas':causas_asociadas, 'consecuencias_asociadas':consecuencias_asociadas}        
        return JsonResponse(data, safe=False)

def editaRiesgoInherente(request):
    if request.method == "POST":
        id_riesgo = request.POST.get("identificador-riesgo-creado")
        probabilidad = request.POST.get("inhe_probabilidad")
        impacto = request.POST.get("inhe_impacto")
        impactocapex = request.POST.get("inhe_capex")
        impactoplazo = request.POST.get("inhe_plazo")
        impactoeconomico = request.POST.get("inhe_economico")
        impactosso = request.POST.get("inhe_sso")
        impactomedioambiente = request.POST.get("inhe_medioambiente")
        impactocomunitario = request.POST.get("inhe_comunitario")
        impactoreputacional = request.POST.get("inhe_reputacional")
        impactolegal = request.POST.get("inhe_legal")
        ambitodominante = 0
        magnitudriesgo = request.POST.get("inhe_magnitud")
        nivelriesgo = request.POST.get("inhe_nivel")
        modificado = datetime.now()
        modificadopor = 'jorel'

        RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=id_riesgo).update(
            probabilidad = probabilidad,
            impacto = impacto,
            impactocapex = impactocapex,
            impactoplazo = impactoplazo,
            impactoeconomico = impactoeconomico,
            impactosso = impactosso,
            impactomedioambiente = impactomedioambiente,
            impactocomunitario = impactocomunitario,
            impactoreputacional = impactoreputacional,
            impactolegal = impactolegal,
            ambitodominante = ambitodominante,
            magnitudriesgo = magnitudriesgo,
            nivelriesgo = nivelriesgo,
            modificado = modificado,
            modificadopor = modificadopor,
        )

        return JsonResponse(True, safe=False)