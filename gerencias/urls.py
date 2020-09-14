from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio_gerencia"),
    path("save-gerencia/", views.save_gerencia, name="save_gerencia"),
]