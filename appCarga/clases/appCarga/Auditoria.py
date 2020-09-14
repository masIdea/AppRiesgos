from core.models import RiesgoAuditoria
from datetime import datetime
from core.clases.core.identificadores import GetId

class Auditoria():
    def __init__(self, usuario="", accion="", app="", id_registro=""):
        self.usuario = usuario
        self.accion = accion
        self.app = app
        self.id_registro = id_registro
    
    
    def saveAudit(self):
        id_auditoria = GetId('RiesgoAuditoria', 'IDAUDIT', 'idauditoria').get_id()    
        registro_auditoria = RiesgoAuditoria(
            idauditoria = id_auditoria,
            #usuario=request.user,
            usuario = str(self.usuario),
            accion = self.accion,
            app = self.app,
            idregistro = self.id_registro,
            fecharegistro = datetime.now(),
            fechaedicion = datetime.now()
        )
        registro_auditoria.save()
