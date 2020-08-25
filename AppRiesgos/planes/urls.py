from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio_planes"),
    path("trae-detalle-riesgo/", views.traeDetalleriesgo, name="detalle_riesgo_planes"),
    path("save-plan-respuesta/", views.savePlanRespuesta, name="save_plan_respuesta"),
    path("save-detalle-plan-respuesta/", views.saveDetallePlanRespuesta, name="save_detalle_plan"),
    path("detalle-planes-riesgo/", views.traeDetallePlanesRiesgo, name="detalle-planes-riesgo"),
    path("detalle-plan-respuesta/", views.traeDetallePlanRespuesta, name="detalle-plan-respuesta"),
    path("save-actividad-plan/", views.saveActividadPlan, name="save_actividad_plan"),
    path("eliminar-plan/", views.eliminarPlan, name="eliminar_plan"),
    path("detalle-actividad/", views.detalleActividad, name="detalle_actividad"),
    path("eliminar-actividad/", views.eliminarActividad, name="eliminar_actividad"),
    path("save-matriz-objetivo/", views.saveMatrizObjetivo, name="save_matriz_objetivo"),
            
    
]
