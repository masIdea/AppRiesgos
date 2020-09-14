from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio_kpis"),
    path("save-kpi/", views.saveKpi, name="save_kpi"),
    path("save-colores/", views.saveColores, name="save_colores"),
    path("save-kus-neto/", views.saveKusNeto, name="save_kus_neto"),
    path("save-tmf-sin-mitigar/", views.saveTmfSinMitigar, name="save_tmf_sin_mitigar"),

    
]