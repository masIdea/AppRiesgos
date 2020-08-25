from core.models import *

class DatosDirecciones():
    def __init__(self, id_gerencia=None, id_direccion=None):
        self.id_gerencia = id_gerencia
        self.id_direccion = id_direccion

    
    def getDireccionesPorGerencia(self):
        direcciones = list(Direcciones.objects.filter(gerencia=self.id_gerencia).values())
        return direcciones

    def getGerenciasPorDireccion(self):
        gerencia_direccion = Direcciones.objects.filter(iddireccion=self.id_direccion).values_list("gerencia", flat=False)
        gerencias = list(Gerencias.objects.filter(idgerencia__in=gerencia_direccion).values())
        return gerencias

class DatosGerencias():
    pass