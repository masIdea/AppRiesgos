from django.shortcuts import render
from core.models import RiesgoConsecuencias
from core.clases.core.identificadores import GetId, GetIdCons
from datetime import date, datetime
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicio(request):
    listado_consecuencias = list(RiesgoConsecuencias.objects.all().values())
    print(listado_consecuencias)
    data = {'consecuencias':listado_consecuencias}
    return render(request, "consecuencias/index.html", data)

def saveConsecuencia(request):
    if request.method == "POST":
        print(request.POST)
        id_consecuencia = GetIdCons('RiesgoConsecuencias', 'CO', 'idconsecuencia').get_id()
        consecuencia = request.POST.get("consecuencias_descripciones")

        save_consecuencia = RiesgoConsecuencias(
            idconsecuencia = id_consecuencia,
            consecuencia = consecuencia,
            estadoregistro = 'ACTIVO',
            modificado = datetime.now(),
            creado = datetime.now(),
            creado_por = request.user,
            modificado_por = request.user
        )

        save_consecuencia.save()

        return HttpResponseRedirect(reverse("inicio_consecuencias"))
