from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio_kpis"),
    path("save-kpi/", views.saveKpi, name="save_kpi"),
    
]