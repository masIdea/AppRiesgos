from django.shortcuts import render
from core.clases.core.identificadores import GetId
from core.clases.core.traeDatosJerarquicos import DatosDirecciones
from core.models import Riesgo, Direcciones, RiesgoCausas, RiesgoConsecuencias, RiesgoNCausariesgo, RiesgoNRiesgoconsecuencia, Gerencias, RiesgoEvaluacioncualitativainherente, RiesgoListas
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .queries import QueryRiesgoSimilar, QueryFamilia, QuerySubproceso
from datetime import date, datetime
from appCarga.clases.appCarga.Auditoria import Auditoria
from core.utils import id_generator


# Create your views here.
def inicio(request):
    listado_causas = list(RiesgoCausas.objects.all().values())
    lsitado_consecuencias = list(RiesgoConsecuencias.objects.all().values())    
    gerencias = list(Gerencias.objects.all().values())
    proyectos = RiesgoListas.objects.filter(tipo="Proyectos", estado="ACTIVO").values("glosa")
    clasificaciones = RiesgoListas.objects.filter(tipo="Clasificaciones", estado="ACTIVO").values("glosa")
    fases = RiesgoListas.objects.filter(tipo="Fases", estado="ACTIVO").values("glosa")
    duenos = RiesgoListas.objects.filter(tipo="Duenos", estado="ACTIVO").values("glosa")
    cargos = RiesgoListas.objects.filter(tipo="Cargos", estado="ACTIVO").values("glosa")
    estados = RiesgoListas.objects.filter(tipo="Estados", estado="ACTIVO").values("glosa")    
    familias = list(QueryFamilia())

    data = {'causas':listado_causas, 
            'consecuencias':lsitado_consecuencias, 
            'familias':familias,
            'gerencias':gerencias,
            'proyectos':proyectos,
            'clasificaciones':clasificaciones,
            'fases':fases,
            'duenos':duenos,
            'cargos':cargos,
            'estados':estados,
            }
    return render(request, "crearRiesgo/index.html", data)

def traeDirecciones(request):
    if request.method == "GET":
        id_gerencia = request.GET['id_gerencia']
        direcciones = DatosDirecciones(id_gerencia=id_gerencia).getDireccionesPorGerencia()        
        data = {'direcciones':direcciones}
        return JsonResponse(data, safe=False)

def saveRiesgo(request):
    if request.method == "POST":
                
        #id_riesgo = GetId('Riesgo', 'RR', 'idriesgo').get_id()
        #cod_riesgo = GetId('Riesgo', 'CR', 'codigoriesgo').get_id()
        id_riesgo = id_generator()
        cod_riesgo = id_generator()
        fecha = None
        if request.POST.get("riesgos_fechas") != "" and request.POST.get("riesgos_fechas") != None and request.POST.get("riesgos_fechas") != " " :
            fecha = request.POST.get("riesgos_fechas").split("/")
            fecha = fecha[2] + '-' + fecha[0] + '-' + fecha[1]


        gerencia = request.POST.get("riesgos_gerencias")
        direccion = request.POST.get("riesgos_direcciones")
        proyecto = request.POST.get("riesgos_proyectos")
        codigo_proyecto = request.POST.get("riesgos_codigos_proyectos")
        fase = request.POST.get("riesgos_fases")
        cargos = request.POST.get("riesgos_cargos")
        estado = request.POST.get("riesgos_estados")
        riesgo_descripcion = request.POST.get("riesgos_descripciones_riesgos")
        clasificacion = request.POST.get("riesgos_clasificaciones")    



        dueno = request.POST.get("riesgos_duenos")
        idrbs = request.POST.get("riesgos_subprocesos")
        descripcion_riesgo = request.POST.get("riesgo_descripcion_riesgo")
        
        maxPerdidaMus = request.POST.get("maxima-perdida-mus")
        maxPerdidaMeses = request.POST.get("maxima-perdida-meses")
        
        riesgo = Riesgo(
            idriesgo = id_riesgo,
            codigoriesgo = cod_riesgo,
            gerencia = gerencia,
            direccion = direccion,
            proyecto = proyecto,
            codigoproyecto = codigo_proyecto,
            fasedelriesgo = fase,
            dueño = dueno,
            cargodeldueño = cargos,
            idrbs = idrbs,
            riesgo = riesgo_descripcion,
            estado = estado,
            fechacreacion = fecha,
            usrdigita = 'jorel033',
            fechadigita = fecha,
            estadovalidacion = 'Abierto',
            estadoregistro = 'Activo',
            modificado = fecha,
            creado = fecha,
            creadopor = 'jorel033',
            modificadopor = 'jorel033',
            clasificacion= clasificacion,
            maximaperdidamus = maxPerdidaMus,
            maximaperdidameses = maxPerdidaMeses,
            descripcionriesgo = descripcion_riesgo,
        )

        
        riesgo.save()        
        if riesgo.pk is not None:
            Auditoria("jorel", "Crea Riesgo "+str(riesgo_descripcion), "CreaRiesgo", riesgo.pk).saveAudit()            
            data = {'valida':True, 'identificador':riesgo.pk}

        
        return JsonResponse(data, safe=False)

def traeRiesgoSimilar(request):
    if request.method == "GET":

        descripcion_riesgo = request.GET['desc_riesgo']
        riesgos_simialres = list(QueryRiesgoSimilar(descripcion_riesgo))

        data = {'riesgos_simialres':riesgos_simialres}

        return JsonResponse(data, safe=False)

#registra-causa-consecuencia
def registraCausaConsecuencia(request):
    valor = request.GET['valor'].split("&")
    identificador_riesgo = request.GET['identificador_riesgo_creado']

    tipo_valor = valor[0]

    if tipo_valor == "CAUSA":        
        registra_riesgo_causa = RiesgoNCausariesgo(
            idcausa = valor[1],
            idriesgo = identificador_riesgo,
            estadoregistro = "ACTIVO",
            modificado = datetime.now(),
            creado = datetime.now(),
            creadopor = 'jorel',
            modificadopor = 'jorel',
        )
        registra_riesgo_causa.save()
        valor_registro = registra_riesgo_causa.pk
        Auditoria("jorel", "Registra Causa Al Riesgo "+str(identificador_riesgo), "CreaCausa", valor_registro).saveAudit()

    if  tipo_valor == "CONSECUENCIA":        
        registra_riesgo_consecuencia = RiesgoNRiesgoconsecuencia(
            idriesgo = identificador_riesgo,
            idconsecuencia = valor[1],
            modificado = datetime.now(),
            estadoregistro = "ACTIVO",
            creado = datetime.now(),
            creadopor = 'jorel',
            modificadopor = 'jorel',
        )
        registra_riesgo_consecuencia.save()
        valor_registro = registra_riesgo_consecuencia.pk
        Auditoria("jorel", "Registra Consecuencia Al Riesgo "+str(identificador_riesgo), "CreaConsecuencia", valor_registro).saveAudit()
    
    valida = False
    if valor_registro is not None:
        valida = True
    
    data = {'valida':valida}
    return JsonResponse(data, safe=False)


def eliminaCausaConsecuencia(request):
    valor = request.GET['valor'].split("&")
    identificador_riesgo = request.GET['identificador_riesgo_creado']

    tipo_valor = valor[0]
    
    try:        
        if tipo_valor == "CAUSA":
            RiesgoNCausariesgo.objects.filter(idcausa = valor[1], idriesgo = identificador_riesgo).delete()
            Auditoria("jorel", "Elimina Causa del Riesgo "+str(identificador_riesgo), "EliminaCausaRiesgo", valor[1]).saveAudit()
        if  tipo_valor == "CONSECUENCIA":        
            RiesgoNRiesgoconsecuencia.objects.filter(idconsecuencia = valor[1], idriesgo = identificador_riesgo).delete()
            Auditoria("jorel", "Elimina Consecuencia del Riesgo "+str(identificador_riesgo), "EliminaConsecuenciaRiesgo", valor[1]).saveAudit()
        valida = True
    except Exception as e:   
        valida = False

    
    data = {'valida':valida}
    return JsonResponse(data, safe=False)

def traeCausas(request):
    if request.method=="GET":
        id_riesgo = request.GET['id_riesgo']
        registros = list(RiesgoNCausariesgo.objects.filter(idriesgo=id_riesgo).values_list('idcausa', flat=True))

        causas = list(RiesgoCausas.objects.filter(idcausa__in=registros).values())

        print(causas)
        data = {'causas':causas}
        return JsonResponse(data, safe=False)

def traeConsecuencias(request):
    if request.method=="GET":
        id_riesgo = request.GET['id_riesgo']
        registros = list(RiesgoNRiesgoconsecuencia.objects.filter(idriesgo=id_riesgo).values_list('idconsecuencia', flat=True))

        consecuencias = list(RiesgoConsecuencias.objects.filter(idconsecuencia__in=registros).values())        
        data = {'consecuencias':consecuencias}
        return JsonResponse(data, safe=False)

def traeSubprocesos(request):
    print("trae")
    glosa_familia = request.GET['glosa_familia']
    subprocesos = list(QuerySubproceso(glosa_familia))
    data = {'subprocesos':subprocesos}
    return JsonResponse(data, safe=False)


def saveRiesgoInherente(request):
    if request.method == "POST":                        
        #id_riesgo_ci = GetId('RiesgoEvaluacioncualitativainherente', 'RINHECI', 'ideci').get_id()
        #id_riesgo = request.POST.get("identificador-riesgo-creado-inherente")
        id_riesgo_ci = id_generator()
        id_riesgo = id_generator()

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
                
        save_riesgo_inherente = RiesgoEvaluacioncualitativainherente(
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
            creadopor = "jorel",
            modificadopor = "jorel"
        )


        save_riesgo_inherente.save()
        if save_riesgo_inherente.pk is not None:
            Auditoria("jorel", "Registra Matriz Inherente del Riesgo "+str(id_riesgo), "MatrizInherente", save_riesgo_inherente.pk).saveAudit()            
            data = {'valida':True, 'identificador':save_riesgo_inherente.pk}

        
        return JsonResponse(data, safe=False)


    


        

