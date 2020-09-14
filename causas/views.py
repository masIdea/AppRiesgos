from django.shortcuts import render
from core.models import RiesgoCausas
from core.clases.core.identificadores import GetId, GetIdCons
from datetime import date, datetime
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicio(request):
    listado_causas = list(RiesgoCausas.objects.all().values())
    print(listado_causas)
    data = {'causas':listado_causas}
    return render(request, "causas/index.html", data)

def saveCausa(request):
    if request.method == "POST":
        print(request.POST)
        id_causa = GetIdCons('RiesgoCausas', 'CA', 'idcausa').get_id()
        causa = request.POST.get("causas_descripciones")

        save_causa = RiesgoCausas(
            idcausa = id_causa,
            causa = causa,
            estadoregistro = 'ACTIVO',
            modificado = datetime.now(),
            creado = datetime.now(),
            creado_por = request.user,
            modificado_por = request.user
        )

        save_causa.save()

        return HttpResponseRedirect(reverse("inicio_causas"))
            










