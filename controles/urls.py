from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio_controles"),
    path("trae-detalle-riesgo/", views.traeDetalleRiesgo, name="detalle_riesgo"),
    path("save-control/", views.saveControl, name="save_control"),
    path("get-controles-riesgo/", views.traeControlesRiesgo, name="controles_riesgo"),

    path("get-datos-control/", views.traeDatosControl, name="get_datos_control"),
    path("eliminar-control/", views.eliminarControl, name="eliminar_control"),

    path("get-matriz-residual/", views.getMatrizResidual, name="eliminar_control"),

    path("editar-matriz-residual/", views.editarMatrizResidual, name="editar_matriz_residual"),
    path("save-matriz-residual/", views.saveMatrizResidual, name="save_matriz_residual"),

    path("magnitud-nivel/", views.getRiesgoMagnitudnivel, name="magnitud_nivel"),

    

    

    

    

    
    

    
]
