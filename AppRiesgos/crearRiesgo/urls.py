from django.urls import path
from . import views, viewsListado

urlpatterns = [
    path("", views.inicio, name="inicio_creacion_riesgo"),
    path("save-riesgo/", views.saveRiesgo, name="save_riesgo"),
    path("trae-riesgos-similares/", views.traeRiesgoSimilar, name="trae_riesgos_similares"),
    path("registra-causa-consecuencia/", views.registraCausaConsecuencia, name="registra_causa_consecuencia"),
    path("elimina-causa-consecuencia/", views.eliminaCausaConsecuencia, name="elimina_causa_consecuencia"),

    path("trae-causas/", views.traeCausas, name="trae_causas"),
    path("trae-consecuencias/", views.traeConsecuencias, name="trae_consecuencias"),   
    path("trae-subprocesos/", views.traeSubprocesos, name="trae_subprocesos"),   

    path("trae-riesgos/", viewsListado.inicio, name="trae_riesgos"),   
    path("direcciones-gerencia/", views.traeDirecciones, name="direcciones_gerencia"),

    path("save-riesgo-inherente/", views.saveRiesgoInherente, name="save_riesgo_inherente"),
    path("datos-edita-riesgo/", viewsListado.datosEditaRiesgo, name="datos_edita_riesgo"),

    path("edita-riesgo-inherente/", viewsListado.editaRiesgoInherente, name="edita_riesgo_inherente"),

    path("editar-riesgo/", viewsListado.editarRiesgo, name="editar_riesgo"),

    

    

    

    #trae-riesgos-similares
    
]
