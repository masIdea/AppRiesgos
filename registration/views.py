from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django import forms
#from .models_users import DireccionM
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from datetime import date, datetime

#from .models_users import DireccionM, EmpresaM, PersonalM, DcrUserClasificacion
#from .queries import tipo_clasificacion


def inicio(request):        
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('inicio_dashboard'))
    else:
        form = AuthenticationForm(data=request.POST)        
        return render(request, 'registration/index.html' , {'form': form,})

def valida_session(request):    
    if request.method=="POST":        
        form = AuthenticationForm(data=request.POST)
        print(form)
        if form.is_valid():            
            username=form.cleaned_data['username']
            password=form.cleaned_data["password"]            
            bool_usuario = User.objects.filter(username=username).exists()
            print(bool_usuario)
            if bool_usuario:                           
                user=authenticate(username=username, password=password)
                if user:                    
                    if user.is_active:
                        login(request,user)
                        if request.user.groups.filter(name = "ver").exists():
                            request.session['read'] = True
                        if request.user.groups.filter(name = "ver_crear").exists():                            
                            request.session['readcreate'] = True
                            request.session['read'] = True                       
                        return HttpResponseRedirect(reverse('inicio_dashboard'))
                    else:                        
                        return HttpResponseRedirect(reverse('inicio_dashboard'))
        else:
            return render(request, 'registration/login.html' , {'form': form})


def register(request):        
    print('NO ESTA ??? ')
    #Selects con los datos adicionales del usuario
    direcciones = DireccionM.objects.all().values() 
    empresas = EmpresaM.objects.all().values()   
    contratos = ContratosM.objects.all().filter(estado='EN EJECUCIÓN').order_by('empresa')  

    registered = False
    if request.method == 'POST':
        print(request.POST)
        user_form = UsuarioForm(data=request.POST)        
        if user_form.is_valid():
            nombre_de_usuario = user_form.cleaned_data['username'].lower()
            user = user_form.save(commit=False)     
            user.username=(user_form.cleaned_data['username'].lower())
            user.set_password(user_form.cleaned_data['password1'])
            user.save()    

            print('PK 1 ---> ', user.pk)
            contratos = request.POST.getlist('contratos')
            chk_codelco = request.POST.get('codelco_chk')
            print('--------> EL CHK ES -------->')
            print(chk_codelco)

            print(request.POST.get('Rut'))
            print(request.POST.get('Direccion'))
            print(user_form.cleaned_data['username'].lower())
            print(request.POST.get('Empresa'))
            print(request.POST.get('fono'))
            print(contratos)
            
            if user.pk is not None:
                rut = request.POST.get('Rut')
                fono = request.POST.get('fono')
                print(request.POST.get('Rut'))
                print(request.POST.get('Direccion'))
                print(user_form.cleaned_data['username'].lower())
                print(request.POST.get('Empresa'))
                print(request.POST.get('fono'))
                contratos = request.POST.getlist('contratos')
                if chk_codelco != 'on':
                    for contrato in contratos:
                        id_definicion_usuairo = GetId('SpmDefinicionUsuario', 'DEFUSUSPM', 'id_def_usuario')
                        id_definicion_usuairo = id_definicion_usuairo.get_id()
                        carga_definicion = DefinicionUsuariosDetalle(id_definicion_usuairo, nombre_de_usuario, contrato, rut, fono)
                        carga_definicion.InsertarDefinicionUsuario()                                              
                else:
                    id_definicion_usuairo = GetId('SpmDefinicionUsuario', 'DEFUSUSPM', 'id_def_usuario')
                    id_definicion_usuairo = id_definicion_usuairo.get_id()
                    carga_definicion = DefinicionUsuariosDetalle(id_definicion_usuairo, nombre_de_usuario, 'CODELCO', rut, fono)
                    carga_definicion.InsertarDefinicionUsuario() 

                print('PK 2 ---> ', carga_definicion)

            if carga_definicion is not None:                                
                registered = True
        else:
            pass
    else:
        user_form = UsuarioForm()
        user_form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario Codelco'})
        user_form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder': 'Ingrese Email Codelco'})
        user_form.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder': 'Nombre'})
        user_form.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder': 'Apellidos'})
        user_form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        user_form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña Confirmación'})                

    return render(request,'registration/signup.html',
                          {'user_form':user_form,                           
                           'registered':registered,
                           'direcciones':direcciones,
                           'empresas':empresas,
                           'contratos':contratos
                           })
