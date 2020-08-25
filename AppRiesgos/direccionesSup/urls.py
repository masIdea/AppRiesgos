from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio_direcciones_sup"),
    path("save-direccion/", views.saveDireccion, name="save_direccion"),
]