from django.shortcuts import render
from core.models import Gerencias
from datetime import datetime
from core.clases.core.identificadores import GetId
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicio(request):
    gerencias = list(Gerencias.objects.filter(estado="ACTIVO").values())
    data = {'gerencias':gerencias}
    return render(request, "gerencias/inicio.html", data)

def save_gerencia(request):
    if request.method == "POST":
        descripcion = request.POST.get("gerencia_descripciones")
        sigla = request.POST.get("gerencia_siglas")
        id_gerencia = GetId('Gerencias', 'GER', 'idgerencia').get_id()

        gerencia_save = Gerencias(
            idgerencia = id_gerencia,
            sigla = sigla,
            gerencia = descripcion,
            modificado = datetime.now(),
            creado = datetime.now(),
            creadopor = request.user,
            modificadopor = request.user,
            estado = "ACTIVO",
        )
        gerencia_save.save()

        if gerencia_save.pk is not None:
            return HttpResponseRedirect(reverse("inicio_gerencia"))
