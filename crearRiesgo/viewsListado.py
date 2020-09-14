from django.shortcuts import render
from core.clases.core.identificadores import GetId
from core.models import Riesgo, Direcciones, RiesgoCausas, RiesgoConsecuencias, RiesgoNCausariesgo, RiesgoNRiesgoconsecuencia, Gerencias, RiesgoEvaluacioncualitativainherente, RiesgoListas, RiesgoRbsfamilia
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .queries import QueryRiesgoSimilar, QueryTraeRiesgos, QueryFamilia
from datetime import date, datetime
from core.utils import id_generator
from django.contrib.auth.decorators import login_required
from controles.clases.AlmacenaRespaldoUpdateMatrices import RespaldoUpdate


@login_required
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
        fecha = None
        if request.POST.get("riesgos_fechas") != "" and request.POST.get("riesgos_fechas") != None:
            fecha = request.POST.get("riesgos_fechas").split("/")
            fecha = fecha[2] + '-' + fecha[0] + '-' + fecha[1]
        dueno = request.POST.get("riesgos_duenos")
        idrbs = request.POST.get("riesgos_subprocesos")
        descripcion_riesgo = request.POST.get("riesgo_descripcion_riesgo")        
        maxima_perdida_mus = request.POST.get("maxima-perdida-mus")
        maxima_perdida_meses = request.POST.get("maxima-perdida-meses")
        riesgo = request.POST.get("riesgos_descripciones_riesgos")
        directic = request.POST.get("chk-directic")
        if directic is not None:
            directic = 1
        else:
            directic = 0  
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
            modificadopor = str(request.user),
            clasificacion = clasificacion,
            maximaperdidamus = maxima_perdida_mus,
            maximaperdidameses = maxima_perdida_meses,
            descripcionriesgo = descripcion_riesgo,
            directic = directic,
            riesgo = riesgo,
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

        print("La wea ", inherente)
        print(id_riesgo)

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
        print("se modifico a lasxx ", modificado, ' ', id_riesgo)

        if RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=id_riesgo).exists():
            RespaldoUpdate("RiesgoEvaluacioncualitativainherente", "RiesgoEvaluacioncualitativainherenteupdate", id_riesgo).respaldoUpdate()
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
        else:
            inhe_probabilidad = float(request.POST.get("inhe_probabilidad"))
            inhe_capex = float(request.POST.get("inhe_capex"))
            inhe_plazo = float(request.POST.get("inhe_plazo"))
            inhe_economico = float(request.POST.get("inhe_economico"))
            inhe_sso = float(request.POST.get("inhe_sso"))
            inhe_medioambiente = float(request.POST.get("inhe_medioambiente"))
            inhe_comunitario = float(request.POST.get("inhe_comunitario"))
            inhe_reputacional = float(request.POST.get("inhe_reputacional"))
            inhe_legal = float(request.POST.get("inhe_legal"))
            inhe_impacto = float(request.POST.get("inhe_impacto"))
            inhe_magnitud = float(request.POST.get("inhe_magnitud"))
            inhe_nivel = request.POST.get("inhe_nivel")
            id_riesgo_ci = id_generator()
                    
            save_edita_inherente = RiesgoEvaluacioncualitativainherente(
                idriesgo = id_riesgo,
                ideci = id_riesgo_ci,
                probabilidad = inhe_probabilidad,
                impacto = inhe_impacto,
                impactocapex = inhe_capex,
                impactoplazo = inhe_plazo,
                impactoeconomico = inhe_economico,
                impactosso = inhe_sso,
                impactomedioambiente = inhe_medioambiente,
                impactocomunitario = inhe_comunitario,
                impactoreputacional = inhe_reputacional,
                impactolegal = inhe_legal,
                ambitodominante = 0,
                magnitudriesgo = inhe_magnitud,
                nivelriesgo = inhe_nivel,
                fecha = datetime.now(),
                estado = "ACTIVO",
                modificado = datetime.now(),
                creado = datetime.now(),
                creadopor = str(request.user),
                modificadopor = str(request.user)
            )

            save_edita_inherente.save()
            print("hola")
            print(save_edita_inherente.pk)
            

        return JsonResponse(True, safe=False)
