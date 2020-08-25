from django.shortcuts import render
from core.models import Gerencias, Direcciones
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from core.clases.core.identificadores import GetId
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def inicio(request):
    gerencias = list(Gerencias.objects.all().values())
    direcciones = list(Direcciones.objects.all().values())
    print(direcciones)
    data = {'gerencias':gerencias, 'direcciones':direcciones}
    return render(request, "direccionesSup/inicio.html", data)

def saveDireccion(request):
    if request.method=="POST":
        print(request.POST)
        sigla = request.POST.get("direccion_siglas")
        id_direccion = GetId('Direcciones', 'DIR', 'iddireccion').get_id()
        direccion = request.POST.get("direccion_descripciones")
        gerencia = request.POST.get("gerencias")

        save_direccion = Direcciones(
            iddireccion = id_direccion,
            gerencia = gerencia,
            sigla = sigla,
            direccion = direccion,
            tipodireccion = '1',
            modificado = datetime.now(),
            creado = datetime.now(),
            creadopor = request.user,
            modificadopor = request.user
        )
        save_direccion.save()
        if save_direccion.pk is not None:
            return HttpResponseRedirect(reverse("inicio_direcciones_sup"))


        
    
