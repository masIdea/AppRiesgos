from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio_causas"),
    path("save-causa/", views.saveCausa, name="save_causa"),
    
]