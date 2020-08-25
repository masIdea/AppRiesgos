from django.shortcuts import render
from core.models import Gerencias, RiesgoEvaluacioncualitativaresidual, RiesgoEvaluacioncualitativaobjetivo, RiesgoEvaluacioncualitativainherente, Riesgo, RiesgoCausas, RiesgoConsecuencias, RiesgoNCausariesgo, RiesgoNRiesgoconsecuencia, RiesgoControl, RiesgoControlCausa, RiesgoControlConsecuencia, RiesgoPlanderespuestaActividad, RiesgoPlanderespuesta
from django.http import JsonResponse
from .clases.Matrices import Html 
from .clases.Reports import ReportePDF
from datetime import datetime
from informes.clases.Selenium import Sel
from .clases.ReporteFichaControl import Html as HtmlControl
from .clases.ReporteFichaPlanAccion import Html as HtmlPlan
from .clases.ReporteSeguimientoPlanAccion import Html as HtmlSeguimientoPlan
from core.utils import id_generator

# Create your views here.
def riesgosCriticos(request):
    gerencias = list(Gerencias.objects.all().values())    
    data = {'gerencias':gerencias}
    return render(request, 'informes/riesgosCriticos.html', data)

def tendenciaMatrices(request):
    gerencias = list(Gerencias.objects.all().values())
    data = {'gerencias':gerencias}
    return render(request, 'informes/tendenciaMatrices.html', data)

def bowtie(request):
    gerencias = list(Gerencias.objects.all().values())
    data = {'gerencias':gerencias}
    return render(request, 'informes/bowtie.html', data)

def fichaControl(request):
    gerencias = list(Gerencias.objects.all().values())
    data = {'gerencias':gerencias}
    return render(request, "informes/fichaControl.html", data)

def seguimientoPlanAccion(request):
    gerencias = list(Gerencias.objects.all().values())
    data = {'gerencias':gerencias}
    return render(request, "informes/seguimientoPlanAccion.html", data)

def detalleSeguimientoPlanAccion(request):
    if request.method == "GET":
        id_gerencia = request.GET['id_gerencia']
        html = HtmlSeguimientoPlan("Ficha Seguimiento Plan de Acción", "Seguimiento "+str(id_gerencia)+"", None, id_gerencia, None).joinHtml()
        nombre_archivo = "ficha_control"+ id_generator()
        archivo_generado = ReportePDF(html, nombre_archivo).generaPDF()        

        return JsonResponse(archivo_generado, safe=False)


def fichaPlanAccion(request):
    gerencias = list(Gerencias.objects.all().values())
    data = {'gerencias':gerencias}
    return render(request, "informes/fichaPlanDeAccion.html", data)

def riesgosFichaPlanAccion(request):
    if request.method == "GET":
        id_riesgo = request.GET['id_riesgo'].split("&")[0]
        riesgo = list(Riesgo.objects.filter(idriesgo=id_riesgo).values())

        direccion = riesgo[0]['direccion']
        gerencia = riesgo[0]['gerencia']
        codigoproyecto = riesgo[0]['codigoproyecto']
        codigodireccion = riesgo[0]['direccion']
        codigoarea = riesgo[0]['codigoproyecto']
        fechacreacion = riesgo[0]['fechacreacion']        
        descripcionriesgo = riesgo[0]['descripcionriesgo']
        dueno = riesgo[0]['dueño']
        
        
        consecuencias_riesgo = []
        causas_riesgo = []
        probabilidad = ""
        impacto = ""
        nivel_objetivo = ""
        probabilidad_residual = ""
        impacto_residual = ""
        nivel_residual = ""        
        for dato_riesgo in riesgo:
            if RiesgoNRiesgoconsecuencia.objects.filter(idriesgo=dato_riesgo['idriesgo']).exists():
                ids_consecuencias = RiesgoNRiesgoconsecuencia.objects.filter(idriesgo=dato_riesgo['idriesgo']).values_list("idconsecuencia", flat=True)
                for id_cons in ids_consecuencias:
                    consecuencias_riesgo.append(list(RiesgoConsecuencias.objects.filter(idconsecuencia=id_cons).values("consecuencia"))[0]['consecuencia'])
            if RiesgoNCausariesgo.objects.filter(idriesgo=dato_riesgo['idriesgo']).exists():
                ids_causas = RiesgoNCausariesgo.objects.filter(idriesgo=dato_riesgo['idriesgo']).values_list("idcausa", flat=True)
                for id_caus in ids_causas:
                    causas_riesgo.append(list(RiesgoCausas.objects.filter(idcausa=id_caus).values("causa"))[0]['causa'])

            if RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=dato_riesgo['idriesgo']).exists():
                probabilidad = list(RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=dato_riesgo['idriesgo']).values("probabilidadcontrol"))[0]['probabilidadcontrol']
                impacto = list(RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=dato_riesgo['idriesgo']).values("impactocontrol"))[0]['impactocontrol']
                nivel_objetivo = list(RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=dato_riesgo['idriesgo']).values("nivelriesgocontrol"))[0]['nivelriesgocontrol']
            if RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=dato_riesgo['idriesgo']).exists():
                probabilidad_residual = list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=dato_riesgo['idriesgo']).values("probabilidadresidual"))[0]['probabilidadresidual']
                impacto_residual = list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=dato_riesgo['idriesgo']).values("impactoresidual"))[0]['impactoresidual']
                nivel_residual = list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=dato_riesgo['idriesgo']).values("nivelriesgoresidual"))[0]['nivelriesgoresidual']        
        

        data_riesgo = {"datos_riesgo":riesgo, "causas":causas_riesgo, "consecuencias":consecuencias_riesgo, "probabilidad":probabilidad, "impacto":impacto, "nivel_objetivo":nivel_objetivo, "probabilidad_residual":probabilidad_residual, "impacto_residual":impacto_residual, "nivel_residual":nivel_residual, "direccion":direccion, "gerencia":gerencia, "codigoproyecto":codigoproyecto, "codigodireccion":codigodireccion, "codigoarea":codigoarea, "fechacreacion":fechacreacion, "descripcionriesgo":descripcionriesgo, "dueno":dueno, "id_riesgo":id_riesgo, "trigger":"", "dueno_plan":""}

        subtitulo = "CORPORACIÓN NACIONAL DEL COBRE DE CHILE"
        subtitulo += "<br>DIVISIÓN EL TENIENTE"
        subtitulo += "<br>GERENCIA "+str(gerencia)+""
        html = HtmlPlan("Ficha Plan de Acción", subtitulo, None, id_riesgo, data_riesgo).joinHtml()
        nombre_archivo = "ficha_control"+ id_generator()
        archivo_generado = ReportePDF(html, nombre_archivo).generaPDF()        

        return JsonResponse(archivo_generado, safe=False)

def riesgosFichaControl(request):
    if request.method == "GET":
        id_riesgo = request.GET['id_riesgo'].split("&")[0]
        riesgo = list(Riesgo.objects.filter(idriesgo=id_riesgo).values())

        direccion = riesgo[0]['direccion']
        gerencia = riesgo[0]['gerencia']
        codigoproyecto = riesgo[0]['codigoproyecto']
        codigodireccion = riesgo[0]['direccion']
        codigoarea = riesgo[0]['codigoproyecto']
        fechacreacion = riesgo[0]['fechacreacion']        
        descripcionriesgo = riesgo[0]['descripcionriesgo']
        dueno = riesgo[0]['dueño']
        
        
        consecuencias_riesgo = []
        causas_riesgo = []
        probabilidad = ""
        impacto = ""
        nivel_inherente = ""
        probabilidad_residual = ""
        impacto_residual = ""
        nivel_residual = ""        
        for dato_riesgo in riesgo:
            if RiesgoNRiesgoconsecuencia.objects.filter(idriesgo=dato_riesgo['idriesgo']).exists():
                ids_consecuencias = RiesgoNRiesgoconsecuencia.objects.filter(idriesgo=dato_riesgo['idriesgo']).values_list("idconsecuencia", flat=True)
                for id_cons in ids_consecuencias:
                    consecuencias_riesgo.append(list(RiesgoConsecuencias.objects.filter(idconsecuencia=id_cons).values("consecuencia"))[0]['consecuencia'])
            if RiesgoNCausariesgo.objects.filter(idriesgo=dato_riesgo['idriesgo']).exists():
                ids_causas = RiesgoNCausariesgo.objects.filter(idriesgo=dato_riesgo['idriesgo']).values_list("idcausa", flat=True)
                for id_caus in ids_causas:
                    causas_riesgo.append(list(RiesgoCausas.objects.filter(idcausa=id_caus).values("causa"))[0]['causa'])

            if RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=dato_riesgo['idriesgo']).exists():
                probabilidad = list(RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=dato_riesgo['idriesgo']).values("probabilidad"))[0]['probabilidad']
                impacto = list(RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=dato_riesgo['idriesgo']).values("impacto"))[0]['impacto']
                nivel_inherente = list(RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=dato_riesgo['idriesgo']).values("nivelriesgo"))[0]['nivelriesgo']
            if RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=dato_riesgo['idriesgo']).exists():
                probabilidad_residual = list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=dato_riesgo['idriesgo']).values("probabilidadresidual"))[0]['probabilidadresidual']
                impacto_residual = list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=dato_riesgo['idriesgo']).values("impactoresidual"))[0]['impactoresidual']
                nivel_residual = list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=dato_riesgo['idriesgo']).values("nivelriesgoresidual"))[0]['nivelriesgoresidual']

        data_riesgo = {"datos_riesgo":riesgo, "causas":causas_riesgo, "consecuencias":consecuencias_riesgo, "probabilidad":int(probabilidad), "impacto":int(impacto), "nivel_inherente":nivel_inherente, "probabilidad_residual":int(probabilidad_residual), "impacto_residual":int(impacto_residual), "nivel_residual":nivel_residual, "direccion":direccion, "gerencia":gerencia, "codigoproyecto":codigoproyecto, "codigodireccion":codigodireccion, "codigoarea":codigoarea, "fechacreacion":fechacreacion, "descripcionriesgo":descripcionriesgo, "dueno":dueno, "id_riesgo":id_riesgo}

        subtitulo = "CORPORACIÓN NACIONAL DEL COBRE DE CHILE"
        subtitulo += "<br>DIVISIÓN EL TENIENTE"
        subtitulo += "<br>GERENCIA "+str(gerencia)+""
        html = HtmlControl("Ficha Control", subtitulo, None, id_riesgo, data_riesgo).joinHtml()
        nombre_archivo = "ficha_control"+ id_generator()
        archivo_generado = ReportePDF(html, nombre_archivo).generaPDF()        

        return JsonResponse(archivo_generado, safe=False)

def riesgosBowTie(request):
    if request.method == "GET":
        riesgo = request.GET['id_riesgo'].split("&")[1]
        id_riesgo = request.GET['id_riesgo'].split("&")[0]

        controles = list(RiesgoControl.objects.filter(idriesgo=id_riesgo).values())        
        arr_predictivos = []
        diccionario_predictivos = {}
        diccionario_correctivo = {}
        for control in controles:            
            if control['tipocontrol'] == "Preventivo/Detectivo":
                causas_control = []
                if RiesgoControlCausa.objects.filter(idcontrol=control['idcontrol']).exists():
                    causas = list(RiesgoControlCausa.objects.filter(idcontrol=control['idcontrol']).values_list("idcausa", flat=True))
                    for causa in causas:
                        causas_control = list(RiesgoCausas.objects.filter(idcausa=causa).values_list("causa", flat=True))
                diccionario_predictivos[control['nombrecontrol']]={
                    'causas':causas_control
                }
            
            if control['tipocontrol'] == "Mitigadores/Correctivos":
                consecuencias_control = []
                if RiesgoControlCausa.objects.filter(idcontrol=control['idcontrol']).exists():
                    consecuencias = list(RiesgoControlConsecuencia.objects.filter(idcontrol=control['idcontrol']).values_list("idconsecuencia", flat=True))
                    for consecuencia in consecuencias:
                        consecuencias_control = list(RiesgoConsecuencias.objects.filter(idconsecuencia=consecuencia).values_list("consecuencia", flat=True))
                diccionario_correctivo[control['nombrecontrol']]={
                    'consecuencias':consecuencias_control
                }

        #print(diccionario_predictivos)
        #print(diccionario_correctivo)

        data = {'predictivo':diccionario_predictivos, 'correctivo':diccionario_correctivo, 'riesgo':riesgo}
        print(data)                   
        return JsonResponse(data, safe=False)

def riesgosGerencia(request):
    if request.method == "GET":
        sigla_gerencia = request.GET['sigla_gerencia']
        riesgos = list(Riesgo.objects.filter(gerencia=sigla_gerencia).order_by('riesgo').values())
        data = {'riesgos':riesgos}
        print(data)
        return JsonResponse(data, safe=False)

def traeRiesgosCriticos(request):
    if request.method == "GET":
        gerencia = request.GET['gerencia']
        nivel_inherente = "-"
        nivel_residual = "-"
        nivel_objetivo = "-"
        id_riesgos_criticos = list(RiesgoEvaluacioncualitativaresidual.objects.filter(nivelriesgoresidual="Alto").values_list("idriesgo", flat=True))
        if gerencia != "0":
            riesgos_criticos = list(Riesgo.objects.filter(idriesgo__in=id_riesgos_criticos, gerencia=gerencia).values())
        else:
            riesgos_criticos = list(Riesgo.objects.filter(idriesgo__in=id_riesgos_criticos).values())

        dict_criticos = {}        
        for riesgo in riesgos_criticos:
            causas = list(RiesgoNCausariesgo.objects.filter(idriesgo=riesgo['idriesgo']).values_list("idcausa", flat=True))
            str_causas = ""
            for causa in causas:
                str_causas+=", " + str(list(RiesgoCausas.objects.filter(idcausa=causa).values("causa"))[0]['causa'])
            consecuencias = list(RiesgoNRiesgoconsecuencia.objects.filter(idriesgo=riesgo['idriesgo']).values_list("idconsecuencia", flat=True))
            str_consecuencias = ""
            for consecuencia in consecuencias:
                str_consecuencias+=", "+str(list(RiesgoConsecuencias.objects.filter(idconsecuencia=consecuencia).values("consecuencia"))[0]['consecuencia'])
            if RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=riesgo['idriesgo']).exists():
                nivel_inherente = list(RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=riesgo['idriesgo']).values("nivelriesgo"))[0]['nivelriesgo']
            if RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).exists():
                nivel_residual = list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).values("nivelriesgoresidual"))[0]['nivelriesgoresidual']
            if RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=riesgo['idriesgo']).exists():
                nivel_objetivo = list(RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=riesgo['idriesgo']).values("nivelriesgocontrol"))[0]['nivelriesgocontrol']


            dict_criticos[riesgo['idriesgo']]={
                'causas':str_causas,
                'descripcion':riesgo['riesgo'],
                'consecuencias':str_consecuencias,
                'dueno':riesgo['dueño'],
                'inherente':nivel_inherente,
                'residual':nivel_residual,
                'objetivo':nivel_objetivo,
                'otros':""
            }
        return JsonResponse(dict_criticos, safe=False)

def getMatrices(request):
    if request.method == "GET":
        gerencia = request.GET['gerencia']
        riesgo = request.GET['riesgo'].split("&")
        fecha_inicio = request.GET['fecha_inicio'].split("/")
        fecha_inicio = fecha_inicio[2]+"-"+fecha_inicio[0]+"-"+fecha_inicio[1]
        fecha_termino = request.GET['fecha_termino'].split("/")
        fecha_termino = fecha_termino[2]+"-"+fecha_termino[0]+"-"+fecha_termino[1]
        subtitulo = "<b>" + gerencia + "</b>" + " - " + riesgo[1]

        html = Html("Reporte Tendencia Matrices de Riesgo", subtitulo, riesgo[0], gerencia, fecha_inicio, fecha_termino).joinHtml()
        nombre_reporte = '_'+str(datetime.now().day)+'_'+str(datetime.now().month)+'_'+str(datetime.now().year)
        archivo_generado = ReportePDF(html, nombre_reporte).generaPDF()
        print(archivo_generado)
        return JsonResponse(archivo_generado, safe=False)

def inicioReporteDashboard(request):    
    return render(request, "informes/reporteDashboard.html")

def getReporteDashboard(request):
    if request.method == "GET":
        nivel = int(request.GET['nivel'])
        reporte = []
        if nivel == 2:
            reporte = Sel().dashboard_nivel_2()
        
        if nivel == 3:
            reporte = Sel().dashboard_nivel_3()
        return JsonResponse(list(reporte), safe=False)






