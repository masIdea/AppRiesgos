from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio_dashboard"),
    path("report-dashboard/", views.inicio2, name="inicio_dashboard2"),
    path("mobile/", views.inicioResponsive, name="inicio_responsive"),
        
    path("trae-riesgos-criticos/", views.getRiesgosCriticosPorGerencia, name="trae_riesgos_criticos"),
    path("trae-detalle-criticos/", views.getDetalleRiesgosCriticos, name="trae_detalle_criticos"),
    path("trae-causas-riesgos-criticos/", views.getCausasRiesgosCriticos, name="trae_causas_riesgos_criticos"),
    path("trae-riesgos-por-direccion/", views.getRiesgosPorDireccion, name="trae_riesgos_por_direccion"),
    path("trae-matrices/", views.getMatrices, name="trae_matrices"),
    path("trae-riesgos-por-direccion-valorizados/", views.getRiesgosPorDireccionValorizados, name="trae_riesgos_por_direccion_valorizados"),

    path("datos-dashboard-tipo-riesgo/", views.getDatosDashboardTipoRiesgo, name="datos_dashboard_tipo_riesgo"),

    path("detalle-coordenada-matriz/", views.detalleCoordenadaMatriz, name="detalle_coordenada_matriz"),

    path("datos-clasificacion-eventos/", views.datosClasificacionEventos, name="datos_clasificacion_eventos"),
    path("datos-campos/", views.getDatosCampo, name="datos_campos"),
    path("clasificacion-tipo-evento/", views.listadoClasificacionTipoEvento, name="clasificacion_tipo_evento"),
    path("clasificacion-gerencia/", views.listadoClasificacionGerencia, name="clasificacion_gerencia"),

    path("get-color-indicadores/", views.getColorIndicadores, name="get_color_indicadores"),

                    
]
