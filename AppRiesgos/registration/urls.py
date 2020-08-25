from django.urls import path
from . import views

urlpatterns = [
        path('', views.inicio, name="inicio"),
        path('validate/', views.valida_session, name="validate"),
        path('register/', views.register, name="register"),  
]
