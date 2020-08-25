from django.urls import path
from . import views, view_pdf

urlpatterns=[
    path("riesgos-criticos/", views.riesgosCriticos, name="riesgos_criticos"),
    path("trae-riesgos-criticos/", views.traeRiesgosCriticos, name="trae_riesgos_criticos"),

    path("matrices-riesgos/", views.getMatrices, name="matrices_riesgos"),

    path("tendencia-matrices/", views.tendenciaMatrices, name="tendencia_matrices"),

    path("riesgos-gerencia/", views.riesgosGerencia, name="riesgos_gerencia"),
    path('view_pdf/<slug:url>', view_pdf.home, name='view_pdf'),
    path('view_png/<slug:url>', view_pdf.viewPng, name='view_png'),    

    path('reporte-dashboard/', views.getReporteDashboard, name='reporte_dashboard'),
    path('inicio-reporte-dashboard/', views.inicioReporteDashboard, name='inicio_reporte_dashboard'),
    path('bowtie/', views.bowtie, name='bowtie'),
    path('riesgos-bowtie/', views.riesgosBowTie, name='riesgos_bowtie'),
    path('ficha-control/', views.fichaControl, name='ficha_control'),
    path('riesgos-ficha-control/', views.riesgosFichaControl, name='riesgos_ficha_control'),
    path('ficha-plan-accion/', views.fichaPlanAccion, name='ficha_plan_accion'),
    path('riesgos-ficha-plan-accion/', views.riesgosFichaPlanAccion, name='riesgos_ficha_plan_accion'),

    path('seguimiento-plan-accion/', views.seguimientoPlanAccion, name='seguimiento_plan_accion'),
    path('detalle-seguimiento-plan-accion/', views.detalleSeguimientoPlanAccion, name='detalle_seguimiento_plan_accion'),
    
    

    
    
    

    

    

    

    

    
]

