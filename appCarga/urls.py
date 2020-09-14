from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio_carga_datos"),
    path("genera-archivo/", views.generaArchivo, name="genera_archivo"),
    path("carga-datos/", views.cargaDatos, name="carga_datos"),
    path("datos-cio/", views.datosCIO, name="datos_cio"),
    path("datos-n1/", views.datosN1, name="datos_n1"),
    path("get-datos-cio/", views.getDatosCIO, name="get_datos_cio"),    
    path("datos-id-cio/", views.getDatosCIOId, name="get_datos_cio_id"),
    path("editar-cio/", views.editarCIO, name="editar_cio"),
    path("get-datos-n1/", views.getDatosN1, name="get_datos_n1"),
    path("datos-id-n1/", views.getDatosN1Id, name="get_datos_n1_id"),
    path("editar-n1/", views.editarN1, name="editar_n1"),

    path("get-datos-dashboard/", views.datosDashboard, name="get_datos_dashboard"),
    path("datos-dashboard/", views.Dashboard, name="datos_dashboard"),
    path("datos-id-dashboard/", views.DashboardIdDashboard, name="datos_id_dashboard"),
    path("editar-datos-dashboard/", views.editarDatosDashboard, name="editar_datos_dashboard"),
    
    

    

    

    

    
    

    
]

