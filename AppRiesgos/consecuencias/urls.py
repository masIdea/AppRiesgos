from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio_consecuencias"),
    path("save-consecuencia/", views.saveConsecuencia, name="save_consecuencia"),
]