"""Riesgos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include("dashboard.urls")),
    path('informes/', include("informes.urls")),
    path('', include("registration.urls")), 
    path('crea-riesgo/', include("crearRiesgo.urls")),
    path('causas-riesgo/', include("causas.urls")),
    path('consecuencias-riesgo/', include("consecuencias.urls")),
    path('gerencias-riesgo/', include("gerencias.urls")),
    path('controles-riesgo/', include("controles.urls")),
    path('direcciones-sup-riesgo/', include("direccionesSup.urls")),
    path('estados-riesgo/', include("estados.urls")),
    path('planes-riesgo/', include("planes.urls")),
    path('carga-datos-riesgo/', include("appCarga.urls")),
    path('listas-riesgo/', include("listas.urls")),
    path('kpi-riesgo/', include("kpiDashboard.urls")),
    path('login_person/', include("registration.urls")),
    path('accounts/', include('registration.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #url(r'^capture/$',  include('screamshot.urls', namespace='screamshot', app_name='screamshot')),
    #path('login_person/', include("registration.urls")),
    #path('accounts/', include('django.contrib.auth.urls')),  
    #path('accounts/', include('registration.urls')),
]


admin.site.site_header = 'Administración RIESGOS'

#Comprueba si el debug está activado en el archivo settings.py
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)