from django.shortcuts import render
from kpiDashboard.models import RiesgoKpi
from core.clases.core.identificadores import GetId
from appCarga.clases.appCarga.Auditoria import Auditoria
from datetime import datetime
from core.models import RiesgoColorindicadores
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def inicio(request):
    registros_kpi = list(RiesgoKpi.objects.all().values())
    valores_kus = []
    valores_tmf = []
    if RiesgoKpi.objects.filter(tipo='KUSNETO').exists():
        valores_kus = list(RiesgoKpi.objects.filter(tipo='KUSNETO').values())
    if RiesgoKpi.objects.filter(tipo='TMFSIN').exists():
        valores_tmf = list(RiesgoKpi.objects.filter(tipo='TMFSIN').values())
    

    data = {'registros_kpi': registros_kpi, 'valores_kus':valores_kus, 'valores_tmf':valores_tmf}
    return render(request, "kpiDashboard/inicio.html", data)

def saveKpi(request):
    if request.method == "POST":
        id_kpi = GetId('RiesgoKpi', 'RIKPI', 'idriesgokpi').get_id()        
        tipo = request.POST.get("tipo")
        valor = request.POST.get("valor")
        porcavance = request.POST.get("porcavance")        

        save_kpi = RiesgoKpi(
            idriesgokpi = id_kpi,
            tipo = tipo,
            valor = valor,
            porcavance = porcavance,
            mes = datetime.now().month,
            ano = datetime.now().year,
            fecreg = datetime.now(),
            fecmod = datetime.now(),
        )
        save_kpi.save()
        if save_kpi.pk is not None:
            return HttpResponseRedirect(reverse("inicio_kpis"))

def saveColores(request):
    if request.method =="POST":
        riesgoAtraso = request.POST.get("name-select-riesgo-atraso")
        vulnAtraso = request.POST.get("name-select-vulnerabilidad-atraso")
        RiesgoColorindicadores.objects.filter(tipoindicador='atraso').update(vulnerabilidad=vulnAtraso, riesgo=riesgoAtraso)

        riesgoProbidad = request.POST.get("name-select-riesgo-probidad")
        vulnProbidad = request.POST.get("name-select-vulnerabilidad-probidad")
        RiesgoColorindicadores.objects.filter(tipoindicador='probidad').update(vulnerabilidad=vulnProbidad, riesgo=riesgoProbidad)

        riesgoAgua = request.POST.get("name-select-riesgo-agua")
        vulnAgua = request.POST.get("name-select-vulnerabilidad-agua")
        RiesgoColorindicadores.objects.filter(tipoindicador='agua').update(vulnerabilidad=vulnAgua, riesgo=riesgoAgua)

        riesgoEquipo = request.POST.get("name-select-riesgo-equipo")
        vulnEquipo = request.POST.get("name-select-vulnerabilidad-equipo")
        RiesgoColorindicadores.objects.filter(tipoindicador='equipo').update(vulnerabilidad=vulnEquipo, riesgo=riesgoEquipo)

        riesgoIncendio = request.POST.get("name-select-riesgo-incendio")
        vulnIncendio = request.POST.get("name-select-vulnerabilidad-incendio")
        RiesgoColorindicadores.objects.filter(tipoindicador='incendio').update(vulnerabilidad=vulnIncendio, riesgo=riesgoIncendio)

        riesgoPandemia = request.POST.get("name-select-riesgo-pandemia")
        vulnPandemia = request.POST.get("name-select-vulnerabilidad-pandemia")
        RiesgoColorindicadores.objects.filter(tipoindicador='pandemia').update(vulnerabilidad=vulnPandemia, riesgo=riesgoPandemia)

        riesgoMineral = request.POST.get("name-select-riesgo-mineral")
        vulnMineral = request.POST.get("name-select-vulnerabilidad-mineral")
        RiesgoColorindicadores.objects.filter(tipoindicador='mineral').update(vulnerabilidad=vulnMineral, riesgo=riesgoMineral)

        riesgoCultural = request.POST.get("name-select-riesgo-cultural")
        vulnCultural = request.POST.get("name-select-vulnerabilidad-cultural")
        RiesgoColorindicadores.objects.filter(tipoindicador='cultural').update(vulnerabilidad=vulnCultural, riesgo=riesgoCultural)

        riesgoOtros = request.POST.get("name-select-riesgo-otros")
        vulnOtros = request.POST.get("name-select-vulnerabilidad-otros")
        RiesgoColorindicadores.objects.filter(tipoindicador='otros').update(vulnerabilidad=vulnOtros, riesgo=riesgoOtros)


        return HttpResponseRedirect(reverse("inicio_kpis"))

def saveKusNeto(request):
    if request.method == "POST":
        id_kpi = GetId('RiesgoKpi', 'RIKPI', 'idriesgokpi').get_id()        
        tipo = "KUSNETO"
        valor = request.POST.get("name-kus-neto")
        porcavance = "0"      

        save_kpi = RiesgoKpi(
            idriesgokpi = id_kpi,
            tipo = tipo,
            valor = valor,
            porcavance = porcavance,
            mes = datetime.now().month,
            ano = datetime.now().year,
            fecreg = datetime.now(),
            fecmod = datetime.now(),
        )
        save_kpi.save()
        if save_kpi.pk is not None:
            return HttpResponseRedirect(reverse("inicio_kpis"))

def saveTmfSinMitigar(request):
    if request.method == "POST":
        id_kpi = GetId('RiesgoKpi', 'RIKPI', 'idriesgokpi').get_id()        
        tipo = "TMFSIN"
        valor = request.POST.get("name-tmf-sin")
        porcavance = "0"      

        save_kpi = RiesgoKpi(
            idriesgokpi = id_kpi,
            tipo = tipo,
            valor = valor,
            porcavance = porcavance,
            mes = datetime.now().month,
            ano = datetime.now().year,
            fecreg = datetime.now(),
            fecmod = datetime.now(),
        )
        save_kpi.save()
        if save_kpi.pk is not None:
            return HttpResponseRedirect(reverse("inicio_kpis"))

        