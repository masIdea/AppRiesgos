from core.models import RiesgoEvaluacioncualitativaresidual, RiesgoEvaluacioncualitativaresidualupdate, RiesgoEvaluacioncualitativainherente, RiesgoEvaluacioncualitativainherenteupdate

from datetime import datetime
from core.clases.core.bulk import BulkCreateManager

class RespaldoUpdate():
    def __init__(self, tb_matriz, tb_update, id_riesgo):
        self.tb_matriz = tb_matriz
        self.id_riesgo = id_riesgo
        self.tb_update = tb_update
    
    def respaldoUpdate(self):
        columnas = [field.name for field in eval(self.tb_matriz)._meta.get_fields()]
        if eval(self.tb_matriz).objects.filter(idriesgo=self.id_riesgo).exists():
            datos_actuales = list(eval(self.tb_matriz).objects.filter(idriesgo=self.id_riesgo).values())
            str_query = ""+self.tb_update+"("
            for columna in columnas:
                if columna == "modificado":
                    str_query+=columna+"=\'"+str(datetime.now())+"\',"
                elif columna == "creado":
                    str_query+=columna+"=\'"+str(datetime.now())+"\',"
                else:
                    if datos_actuales[0][columna] is None:
                        str_query+=columna+"=\'"+str(0)+"\',"        
                    else:
                        str_query+=columna+"=\'"+str(datos_actuales[0][columna])+"\',"
            str_query+=")"

            bulk_mgr = BulkCreateManager()
            bulk_mgr.add(
                eval(str_query)
            )
            bulk_mgr.done()            

        return columnas
