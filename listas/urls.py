from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio_listas"),
    path("save-lista/", views.saveLista, name="save_lista"),
    path("registros-listas/", views.registrosListas, name="registros_listas"),
    
]