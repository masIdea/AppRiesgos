from django.shortcuts import render
from kpiDashboard.models import RiesgoKpi
from core.clases.core.identificadores import GetId
from appCarga.clases.appCarga.Auditoria import Auditoria
from datetime import datetime
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def inicio(request):
    registros_kpi = list(RiesgoKpi.objects.all().values())
    data = {'registros_kpi': registros_kpi}
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
