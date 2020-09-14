from django.shortcuts import render
from core.models import RiesgoListas
from datetime import datetime
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicio(request):
    listas_definidas = RiesgoListas.objects.values("tipo").distinct()
    data = {'listas':listas_definidas}
    return render(request, "listas/inicio.html", data)

def saveLista(request):
    if request.method == "POST":
        data = {'estado':False}
        tipo = request.POST.get("tipo")
        nueva_lista = request.POST.get("nueva-lista")
        glosa = request.POST.get("glosa")
        orden = request.POST.get("orden")
        if nueva_lista:
            if not RiesgoListas.objects.filter(tipo=nueva_lista).exists():
                save_lista = RiesgoListas(
                    tipo = nueva_lista,
                    glosa = glosa,
                    orden = orden,
                    estado = "ACTIVO",
                    modificado = datetime.now(),
                    creado = datetime.now(),
                    creadopor = request.user,
                    modificadopor = request.user
                )
                save_lista.save()
                data = {'estado':True, "msg":"Lista Almacenada Exitosamente.-"}
            else:
                data = {'estado':False, "msg":"La lista ingresada ya existe, puede seleccionarla en la lista desplegable a continuación.-"}
        else:
            if not RiesgoListas.objects.filter(tipo=nueva_lista).exists():
                save_lista = RiesgoListas(
                    tipo = tipo,
                    glosa = glosa,
                    orden = orden,
                    estado = "ACTIVO",
                    modificado = datetime.now(),
                    creado = datetime.now(),
                    creadopor = request.user,
                    modificadopor = request.user
                )
                save_lista.save()
                data = {'estado':True, "msg":"Lista Almacenada Exitosamente.-"}
                            
        return JsonResponse(data, safe=False)

def registrosListas(request):
    if request.method == "GET":
        registros = list(RiesgoListas.objects.all().values())
        data = {'registros':registros}
        return JsonResponse(data, safe=False)

