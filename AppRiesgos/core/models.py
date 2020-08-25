from django.db import models

# Create your models here.

class Direcciones(models.Model):
    iddireccion = models.CharField(db_column='IDdireccion', max_length=255, primary_key=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sigla = models.CharField(db_column='Sigla', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipodireccion = models.CharField(db_column='TipoDireccion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', blank=True, null=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='CreadoPor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='ModificadoPor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DIRECCIONES'

class RiesgoEvaluacioncualitativainherenteupdate(models.Model):
    idriesgo = models.CharField(db_column='IdRiesgo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ideci = models.CharField(db_column='IdECI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    probabilidad = models.FloatField(db_column='Probabilidad', blank=True, null=True)  # Field name made lowercase.
    impacto = models.FloatField(db_column='Impacto', blank=True, null=True)  # Field name made lowercase.
    impactocapex = models.FloatField(db_column='ImpactoCAPEX', blank=True, null=True)  # Field name made lowercase.
    impactoplazo = models.FloatField(db_column='ImpactoPlazo', blank=True, null=True)  # Field name made lowercase.
    impactoeconomico = models.FloatField(db_column='ImpactoEconomico', blank=True, null=True)  # Field name made lowercase.
    impactosso = models.FloatField(db_column='ImpactoSSO', blank=True, null=True)  # Field name made lowercase.
    impactomedioambiente = models.FloatField(db_column='ImpactoMedioambiente', blank=True, null=True)  # Field name made lowercase.
    impactocomunitario = models.FloatField(db_column='ImpactoComunitario', blank=True, null=True)  # Field name made lowercase.
    impactoreputacional = models.FloatField(db_column='ImpactoReputacional', blank=True, null=True)  # Field name made lowercase.
    impactolegal = models.FloatField(db_column='ImpactoLegal', blank=True, null=True)  # Field name made lowercase.
    ambitodominante = models.CharField(db_column='AmbitoDominante', max_length=255, blank=True, null=True)  # Field name made lowercase.
    magnitudriesgo = models.CharField(db_column='MagnitudRiesgo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nivelriesgo = models.CharField(db_column='NivelRiesgo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', primary_key=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_EvaluacionCualitativaInherenteUpdate'


class Gerencias(models.Model):
    idgerencia = models.CharField(db_column='IDgerencia', max_length=255, primary_key=True)  # Field name made lowercase.
    sigla = models.CharField(db_column='Sigla', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', blank=True, null=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='CreadoPor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='ModificadoPor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GERENCIAS'


class Riesgo(models.Model):
    idriesgo = models.CharField(db_column='IdRiesgo', max_length=255, primary_key=True)  # Field name made lowercase.
    codigoriesgo = models.CharField(db_column='CodigoRiesgo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    proyecto = models.CharField(db_column='Proyecto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codigoproyecto = models.CharField(db_column='CodigoProyecto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fasedelriesgo = models.CharField(db_column='FaseDelRiesgo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dueño = models.CharField(db_column='Dueño', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cargodeldueño = models.CharField(db_column='CargoDelDueño', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idrbs = models.CharField(db_column='IdRBS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    riesgo = models.CharField(db_column='Riesgo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fechacreacion = models.DateField(db_column='FechaCreacion', blank=True, null=True)  # Field name made lowercase.
    usrdigita = models.CharField(db_column='UsrDigita', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fechadigita = models.DateField(db_column='FechaDigita', blank=True, null=True)  # Field name made lowercase.
    estadovalidacion = models.CharField(db_column='EstadoValidacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estadoregistro = models.CharField(db_column='EstadoRegistro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateField(db_column='Creado', blank=True, null=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='CreadoPor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='ModificadoPor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    maximaperdidameses = models.IntegerField(db_column='MaximaPerdidaMeses', blank=True, null=True)  # Field name made lowercase.
    maximaperdidamus = models.FloatField(db_column='MaximaPerdidaMUS', blank=True, null=True)  # Field name made lowercase.
    descripcionriesgo = models.CharField(db_column='DescripcionRiesgo', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    directic = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RIESGO'


class RiesgoAuditoria(models.Model):
    idauditoria = models.CharField(db_column='IdAuditoria', max_length=255, primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accion = models.CharField(db_column='Accion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    app = models.CharField(db_column='App', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idregistro = models.CharField(db_column='idRegistro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.DateTimeField(db_column='FechaRegistro', blank=True, null=True)  # Field name made lowercase.
    fechaedicion = models.DateTimeField(db_column='FechaEdicion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_Auditoria'


class RiesgoCargasistemacio(models.Model):
    idcargacio = models.CharField(db_column='IdCargaCIO', max_length=255, primary_key=True)  # Field name made lowercase.
    idcosto = models.CharField(db_column='IdCosto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fecha = models.CharField(db_column='Fecha', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    superintendencia = models.CharField(db_column='SuperIntendencia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unidadoperacional = models.CharField(db_column='UnidadOperacional', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipoobjeto = models.CharField(db_column='TipoObjeto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    evento = models.CharField(db_column='Evento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nivelimpacto = models.CharField(db_column='NivelImpacto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comentarios = models.CharField(db_column='Comentarios', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cantidaddiasdetencion = models.CharField(db_column='CantidadDiasDetencion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cantidadtmfperdidas = models.CharField(db_column='CantidadTMFPerdidas', max_length=255, blank=True, null=True)  # Field name made lowercase.
    montodeperdida = models.CharField(db_column='MontoDePerdida', max_length=255, blank=True, null=True)  # Field name made lowercase.
    repeticiondelevento = models.CharField(db_column='RepeticionDelEvento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estadistica = models.CharField(db_column='Estadistica', max_length=255, blank=True, null=True)  # Field name made lowercase.
    areadeevento = models.CharField(db_column='AreaDeEvento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    superintendenciaevento = models.CharField(db_column='SuperIntendenciaEvento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    proyecto = models.CharField(db_column='Proyecto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    familia = models.CharField(db_column='Familia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subproceso = models.CharField(db_column='SubProceso', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    controlesquenofuncionaron = models.CharField(db_column='ControlesQueNoFuncionaron', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipofalla = models.CharField(db_column='TipoFalla', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.DateTimeField(db_column='FechaRegistro', blank=True, null=True)  # Field name made lowercase.
    fechamodificacion = models.DateTimeField(db_column='Fechamodificacion', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idcio = models.CharField(db_column='idCIO', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_CargaSistemaCIO'


class RiesgoCargasisteman1(models.Model):
    idcargan1 = models.CharField(db_column='IdCargaN1', max_length=255, primary_key=True)  # Field name made lowercase.
    codigorsso = models.CharField(db_column='CodigoRSSO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tiporsso = models.CharField(db_column='TipoRSSO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True)  # Field name made lowercase.
    causal = models.CharField(db_column='Causal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nivelrsso = models.CharField(db_column='NivelRSSO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fechacreacion = models.CharField(db_column='FechaCreacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fechahallazgo = models.CharField(db_column='FechaHallazgo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    division = models.CharField(db_column='Division', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    superintendencia = models.CharField(db_column='Superintendencia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sapinformante = models.CharField(db_column='SAPInformante', max_length=255, blank=True, null=True)  # Field name made lowercase.
    informante = models.CharField(db_column='Informante', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sapresponsable = models.CharField(db_column='SAPResponsable', max_length=255, blank=True, null=True)  # Field name made lowercase.
    responsable = models.CharField(db_column='Responsable', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fechacierre = models.CharField(db_column='FechaCierre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descripcionincidente = models.CharField(db_column='DescripcionIncidente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accionrealizada = models.CharField(db_column='AccionRealizada', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estandar = models.CharField(db_column='Estandar', max_length=255, blank=True, null=True)  # Field name made lowercase.
    riesgocritico = models.CharField(db_column='RiesgoCritico', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idevento = models.CharField(db_column='IdEvento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cantidaddiasdetencion = models.CharField(db_column='CantidadDiasDetencion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cantidadtmfperdidas = models.CharField(db_column='CantidadTMFPerdidas', max_length=255, blank=True, null=True)  # Field name made lowercase.
    areadeevento = models.CharField(db_column='AreaDeEvento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    superintendenciaevento = models.CharField(db_column='SuperIntendenciaEvento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    proyecto = models.CharField(db_column='Proyecto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    familia = models.CharField(db_column='Familia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subproceso = models.CharField(db_column='SubProceso', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    controlesquenofuncionaron = models.CharField(db_column='ControlesQueNoFuncionaron', max_length=255, blank=True, null=True)  # Field name made lowercase.
    montodeperdida = models.CharField(db_column='MontoDePerdida', max_length=255, blank=True, null=True)  # Field name made lowercase.
    repeticiondelevento = models.CharField(db_column='RepeticionDelEvento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipofalla = models.CharField(db_column='TipoFalla', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estadistica = models.CharField(db_column='Estadistica', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.DateTimeField(db_column='FechaRegistro', blank=True, null=True)  # Field name made lowercase.
    fechamodificacion = models.DateTimeField(db_column='Fechamodificacion', blank=True, null=True)  # Field name made lowercase.
    estadoregistro = models.CharField(db_column='EstadoRegistro', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idn1 = models.CharField(db_column='idN1', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_CargaSistemaN1'


class RiesgoCausas(models.Model):
    idcausa = models.CharField(db_column='IdCausa', max_length=255, primary_key=True)  # Field name made lowercase.
    causa = models.CharField(db_column='Causa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estadoregistro = models.CharField(db_column='EstadoRegistro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', blank=True, null=True)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado por', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    modificado_por = models.CharField(db_column='Modificado por', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'RIESGO_Causas'


class RiesgoConsecuencias(models.Model):
    idconsecuencia = models.CharField(db_column='IdConsecuencia', max_length=255, primary_key=True)  # Field name made lowercase.
    consecuencia = models.CharField(db_column='Consecuencia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estadoregistro = models.CharField(db_column='EstadoRegistro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', blank=True, null=True)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado por', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    modificado_por = models.CharField(db_column='Modificado por', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'RIESGO_Consecuencias'


class RiesgoControl(models.Model):
    idcontrol = models.CharField(db_column='IdControl', max_length=255, primary_key=True)  # Field name made lowercase.
    idriesgo = models.CharField(db_column='IdRiesgo', max_length=255)  # Field name made lowercase.
    nombrecontrol = models.CharField(db_column='NombreControl', max_length=500, blank=True, null=True)  # Field name made lowercase.
    descripcioncontrol = models.TextField(db_column='DescripcionControl', blank=True, null=True)  # Field name made lowercase.
    tipocontrol = models.CharField(db_column='TipoControl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dueñocontrol = models.CharField(db_column='DueñoControl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    frecuenciacontrol = models.CharField(db_column='FrecuenciaControl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estadoregistro = models.CharField(db_column='EstadoRegistro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', blank=True, null=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_Control'


class RiesgoControlAutoevaluacion(models.Model):
    idcontrol = models.CharField(db_column='IdControl', max_length=255)  # Field name made lowercase.
    idriesgo = models.CharField(db_column='IdRiesgo', max_length=255)  # Field name made lowercase.
    eficacia = models.CharField(db_column='Eficacia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    eficiencia = models.CharField(db_column='Eficiencia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    efectividad = models.CharField(db_column='Efectividad', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', primary_key=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_Control_Autoevaluacion'


class RiesgoControlCausa(models.Model):
    idcontrol = models.CharField(db_column='IdControl', max_length=255)  # Field name made lowercase.
    idriesgo = models.CharField(db_column='IdRiesgo', max_length=255)  # Field name made lowercase.
    idcausa = models.CharField(db_column='IdCausa', max_length=255)  # Field name made lowercase.
    estadoregistro = models.CharField(db_column='EstadoRegistro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', primary_key=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_Control_Causa'


class RiesgoControlConsecuencia(models.Model):
    idcontrol = models.CharField(db_column='IdControl', max_length=255)  # Field name made lowercase.
    idriesgo = models.CharField(db_column='IdRiesgo', max_length=255)  # Field name made lowercase.
    idconsecuencia = models.CharField(db_column='IdConsecuencia', max_length=255)  # Field name made lowercase.
    estadoregistro = models.CharField(db_column='EstadoRegistro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', primary_key=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_Control_Consecuencia'


class RiesgoControlEvidencia(models.Model):
    idcontrol = models.CharField(db_column='IdControl', max_length=255)  # Field name made lowercase.
    tipo_de_contenido = models.CharField(db_column='Tipo de contenido', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    archivo = models.CharField(db_column='Archivo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estadoregistro = models.CharField(db_column='EstadoRegistro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', primary_key=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_Control_Evidencia'


class RiesgoControlMonitoreo(models.Model):
    idcontrol = models.CharField(db_column='IdControl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idriesgo = models.CharField(db_column='IdRiesgo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    frecuenciamonitoreo = models.CharField(db_column='FrecuenciaMonitoreo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inicio = models.CharField(db_column='Inicio', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fin = models.CharField(db_column='Fin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    evidencia = models.CharField(db_column='Evidencia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estadoregistro = models.CharField(db_column='EstadoRegistro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gestionriesgocritico = models.CharField(db_column='GestionRiesgoCritico', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', primary_key=True)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado por', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    modificado_por = models.CharField(db_column='Modificado por', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'RIESGO_Control_Monitoreo'


class RiesgoEliminado(models.Model):
    idriesgo = models.CharField(db_column='IdRiesgo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fechaeliminacion = models.DateTimeField(db_column='FechaEliminacion', blank=True, null=True)  # Field name made lowercase.
    usuarioqueelimina = models.CharField(db_column='UsuarioQueElimina', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', primary_key=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_Eliminado'


class RiesgoEnvios(models.Model):
    idriesgo = models.CharField(db_column='IdRiesgo', max_length=255)  # Field name made lowercase.
    enviadoa = models.CharField(db_column='EnviadoA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cuentaenviadoa = models.CharField(db_column='CuentaEnviadoA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enviadopor = models.CharField(db_column='EnviadoPor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fechaenvio = models.DateTimeField(db_column='FechaEnvio', blank=True, null=True)  # Field name made lowercase.
    asunto = models.CharField(db_column='Asunto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mensaje = models.TextField(db_column='Mensaje', blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', primary_key=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_Envios'


class RiesgoEvaluacioncualitativainherente(models.Model):
    idriesgo = models.CharField(db_column='IdRiesgo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ideci = models.CharField(db_column='IdECI', max_length=255, primary_key=True)  # Field name made lowercase.
    probabilidad = models.FloatField(db_column='Probabilidad', blank=True, null=True)  # Field name made lowercase.
    impacto = models.FloatField(db_column='Impacto', blank=True, null=True)  # Field name made lowercase.
    impactocapex = models.FloatField(db_column='ImpactoCAPEX', blank=True, null=True)  # Field name made lowercase.
    impactoplazo = models.FloatField(db_column='ImpactoPlazo', blank=True, null=True)  # Field name made lowercase.
    impactoeconomico = models.FloatField(db_column='ImpactoEconomico', blank=True, null=True)  # Field name made lowercase.
    impactosso = models.FloatField(db_column='ImpactoSSO', blank=True, null=True)  # Field name made lowercase.
    impactomedioambiente = models.FloatField(db_column='ImpactoMedioambiente', blank=True, null=True)  # Field name made lowercase.
    impactocomunitario = models.FloatField(db_column='ImpactoComunitario', blank=True, null=True)  # Field name made lowercase.
    impactoreputacional = models.FloatField(db_column='ImpactoReputacional', blank=True, null=True)  # Field name made lowercase.
    impactolegal = models.FloatField(db_column='ImpactoLegal', blank=True, null=True)  # Field name made lowercase.
    ambitodominante = models.CharField(db_column='AmbitoDominante', max_length=255, blank=True, null=True)  # Field name made lowercase.
    magnitudriesgo = models.FloatField(db_column='MagnitudRiesgo', blank=True, null=True)  # Field name made lowercase.
    nivelriesgo = models.CharField(db_column='NivelRiesgo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', blank=True, null=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_EvaluacionCualitativaInherente'


class RiesgoEvaluacioncualitativaobjetivo(models.Model):
    idriesgo = models.CharField(db_column='IdRiesgo', max_length=255)  # Field name made lowercase.
    ideco = models.CharField(db_column='IdECO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    probabilidadcontrol = models.CharField(db_column='ProbabilidadControl', max_length=255, primary_key=True)  # Field name made lowercase.
    impactocontrol = models.CharField(db_column='ImpactoControl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impactocapexcontrol = models.CharField(db_column='ImpactoCapexControl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impactoplazocontrol = models.CharField(db_column='ImpactoPlazoControl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impactoeconomicocontrol = models.CharField(db_column='ImpactoEconomicoControl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impactossocontrol = models.CharField(db_column='ImpactoSSOControl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impactomedioambientecontrol = models.CharField(db_column='ImpactoMedioambienteControl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impactocomunitariocontrol = models.CharField(db_column='ImpactoComunitarioControl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impactoreputacionalcontrol = models.CharField(db_column='ImpactoReputacionalControl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impactolegalcontrol = models.CharField(db_column='ImpactoLegalControl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ambitodominantecontrol = models.CharField(db_column='AmbitoDominanteControl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    magnitudriesgocontrol = models.CharField(db_column='MagnitudRiesgoControl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nivelriesgocontrol = models.CharField(db_column='NivelRiesgoControl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', blank=True, null=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_EvaluacionCualitativaObjetivo'


class RiesgoEvaluacioncualitativaresidual(models.Model):
    idriesgo = models.CharField(db_column='IdRiesgo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idecr = models.CharField(db_column='IdECR', max_length=255, primary_key=True)  # Field name made lowercase.
    probabilidadresidual = models.FloatField(db_column='ProbabilidadResidual', blank=True, null=True)  # Field name made lowercase.
    impactoresidual = models.FloatField(db_column='ImpactoResidual', blank=True, null=True)  # Field name made lowercase.
    impactocapexresidual = models.FloatField(db_column='ImpactoCapexResidual', blank=True, null=True)  # Field name made lowercase.
    impactoplazoresidual = models.FloatField(db_column='ImpactoPlazoResidual', blank=True, null=True)  # Field name made lowercase.
    impactoeconomicoresidual = models.FloatField(db_column='ImpactoEconomicoResidual', blank=True, null=True)  # Field name made lowercase.
    impactossoresidual = models.FloatField(db_column='ImpactoSSOResidual', blank=True, null=True)  # Field name made lowercase.
    impactomedioambienteresidual = models.FloatField(db_column='ImpactoMedioambienteResidual', blank=True, null=True)  # Field name made lowercase.
    impactocomunitarioresidual = models.FloatField(db_column='ImpactoComunitarioResidual', blank=True, null=True)  # Field name made lowercase.
    impactoreputacionalresidual = models.FloatField(db_column='ImpactoReputacionalResidual', blank=True, null=True)  # Field name made lowercase.
    impactolegalresidual = models.FloatField(db_column='ImpactoLegalResidual', blank=True, null=True)  # Field name made lowercase.
    ambitodominanteresidual = models.FloatField(db_column='AmbitoDominanteResidual', blank=True, null=True)  # Field name made lowercase.
    magnitudriesgoresidual = models.FloatField(db_column='MagnitudRiesgoResidual', blank=True, null=True)  # Field name made lowercase.
    nivelriesgoresidual = models.CharField(db_column='NivelRiesgoResidual', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', blank=True, null=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_EvaluacionCualitativaResidual'


class RiesgoEvaluacioncualitativaresidualupdate(models.Model):
    idriesgo = models.CharField(db_column='IdRiesgo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idecr = models.CharField(db_column='IdECR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    probabilidadresidual = models.FloatField(db_column='ProbabilidadResidual', blank=True, null=True)  # Field name made lowercase.
    impactoresidual = models.FloatField(db_column='ImpactoResidual', blank=True, null=True)  # Field name made lowercase.
    impactocapexresidual = models.FloatField(db_column='ImpactoCapexResidual', blank=True, null=True)  # Field name made lowercase.
    impactoplazoresidual = models.FloatField(db_column='ImpactoPlazoResidual', blank=True, null=True)  # Field name made lowercase.
    impactoeconomicoresidual = models.FloatField(db_column='ImpactoEconomicoResidual', blank=True, null=True)  # Field name made lowercase.
    impactossoresidual = models.FloatField(db_column='ImpactoSSOResidual', blank=True, null=True)  # Field name made lowercase.
    impactomedioambienteresidual = models.FloatField(db_column='ImpactoMedioambienteResidual', blank=True, null=True)  # Field name made lowercase.
    impactocomunitarioresidual = models.FloatField(db_column='ImpactoComunitarioResidual', blank=True, null=True)  # Field name made lowercase.
    impactoreputacionalresidual = models.FloatField(db_column='ImpactoReputacionalResidual', blank=True, null=True)  # Field name made lowercase.
    impactolegalresidual = models.FloatField(db_column='ImpactoLegalResidual', blank=True, null=True)  # Field name made lowercase.
    ambitodominanteresidual = models.FloatField(db_column='AmbitoDominanteResidual', blank=True, null=True)  # Field name made lowercase.
    magnitudriesgoresidual = models.FloatField(db_column='MagnitudRiesgoResidual', blank=True, null=True)  # Field name made lowercase.
    nivelriesgoresidual = models.CharField(db_column='NivelRiesgoResidual', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', primary_key=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_EvaluacionCualitativaResidualUpdate'


class RiesgoKpi(models.Model):
    idriesgokpi = models.CharField(db_column='IdRiesgoKpi', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.
    porcavance = models.FloatField(db_column='PorcAvance', blank=True, null=True)  # Field name made lowercase.
    mes = models.CharField(db_column='Mes', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ano = models.IntegerField(db_column='Ano', blank=True, null=True)  # Field name made lowercase.
    fecreg = models.DateTimeField(db_column='FecReg', primary_key=True)  # Field name made lowercase.
    fecmod = models.DateTimeField(db_column='Fecmod', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_Kpi'


class RiesgoListas(models.Model):
    tipo = models.CharField(db_column='Tipo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    glosa = models.CharField(db_column='Glosa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orden = models.FloatField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', primary_key=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_Listas'


class RiesgoMagnitudnivel(models.Model):
    probabilidad = models.IntegerField(db_column='Probabilidad', blank=True, null=True)  # Field name made lowercase.
    impacto = models.IntegerField(db_column='Impacto', blank=True, null=True)  # Field name made lowercase.
    magnitud = models.IntegerField(db_column='Magnitud', blank=True, null=True)  # Field name made lowercase.
    nivel = models.CharField(db_column='Nivel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'RIESGO_MagnitudNivel'


class RiesgoNCausariesgo(models.Model):
    idcausa = models.CharField(db_column='IdCausa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idriesgo = models.CharField(db_column='IdRiesgo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estadoregistro = models.CharField(db_column='EstadoRegistro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', primary_key=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_N_CausaRiesgo'


class RiesgoNRiesgoconsecuencia(models.Model):
    idriesgo = models.CharField(db_column='IdRiesgo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idconsecuencia = models.CharField(db_column='IdConsecuencia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    estadoregistro = models.CharField(db_column='EstadoRegistro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', primary_key=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_N_RiesgoConsecuencia'


class RiesgoProbImp(models.Model):
    probabilidad = models.IntegerField(db_column='Probabilidad', blank=True, null=True)  # Field name made lowercase.
    impacto = models.IntegerField(db_column='Impacto', blank=True, null=True)  # Field name made lowercase.
    color_hex = models.CharField(db_column='Color_hex', max_length=255, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_PROB_IMP'


class RiesgoPlanderespuesta(models.Model):
    idplanrespuesta = models.CharField(db_column='IdPlanRespuesta', max_length=255, primary_key=True)  # Field name made lowercase.
    idriesgo = models.CharField(db_column='IdRiesgo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estrategia = models.CharField(db_column='Estrategia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    trigger = models.CharField(db_column='Trigger', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dueñoplanderespuesta = models.CharField(db_column='DueñoPlanDeRespuesta', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cargodueñoplan = models.CharField(db_column='CargoDueñoPlan', max_length=255, blank=True, null=True)  # Field name made lowercase.
    costo = models.DecimalField(db_column='Costo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fechainicio = models.DateTimeField(db_column='FechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechatermino = models.DateTimeField(db_column='FechaTermino', blank=True, null=True)  # Field name made lowercase.
    avancereal = models.FloatField(db_column='AvanceReal', blank=True, null=True)  # Field name made lowercase.
    avanceplanificado = models.FloatField(db_column='AvancePlanificado', blank=True, null=True)  # Field name made lowercase.
    estadoplanderespuesta = models.CharField(db_column='EstadoPlanDeRespuesta', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    estadoregistro = models.CharField(db_column='EstadoRegistro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', blank=True, null=True)  # Field name made lowercase.
    creado_por = models.CharField(db_column='Creado por', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    modificado_por = models.CharField(db_column='Modificado por', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'RIESGO_PlanDeRespuesta'


class RiesgoPlanderespuestaActividad(models.Model):
    idplanderespuesta = models.CharField(db_column='IdPlanDeRespuesta', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idactividad = models.CharField(db_column='IdActividad', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nombreactividad = models.CharField(db_column='NombreActividad', max_length=255, blank=True, null=True)  # Field name made lowercase.
    responsable = models.CharField(db_column='Responsable', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estrategia = models.CharField(db_column='Estrategia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    costo = models.DecimalField(db_column='Costo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    estadoactividad = models.CharField(db_column='EstadoActividad', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inicio = models.DateTimeField(db_column='Inicio', blank=True, null=True)  # Field name made lowercase.
    termino = models.DateTimeField(db_column='Termino', blank=True, null=True)  # Field name made lowercase.
    detalleactividad = models.TextField(db_column='DetalleActividad', blank=True, null=True)  # Field name made lowercase.
    pesoespecifico = models.FloatField(db_column='PesoEspecifico', blank=True, null=True)  # Field name made lowercase.
    estadoregistro = models.CharField(db_column='EstadoRegistro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', primary_key=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avancereal = models.FloatField(db_column='AvanceReal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_PlanDeRespuesta_Actividad'


class RiesgoPlanderespuestaEvidencia(models.Model):
    idcontrol = models.CharField(db_column='IdControl', max_length=255)  # Field name made lowercase.
    tipo_de_contenido = models.CharField(db_column='Tipo de contenido', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    archivo = models.CharField(db_column='Archivo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estadoregistro = models.CharField(db_column='EstadoRegistro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', primary_key=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idactividad = models.CharField(db_column='idActividad', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_PlanDeRespuesta_Evidencia'


class RiesgoRbsfamilia(models.Model):
    idrbs = models.CharField(db_column='IdRBS', max_length=255, primary_key=True)  # Field name made lowercase.
    familia = models.CharField(db_column='Familia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subproceso = models.CharField(db_column='SubProceso', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado', blank=True, null=True)  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado', blank=True, null=True)  # Field name made lowercase.
    creadopor = models.CharField(db_column='Creadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modificadopor = models.CharField(db_column='Modificadopor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_RBSFamilia'


class RiesgoUnifica(models.Model):
    idregistro = models.CharField(db_column='IdRegistro', max_length=100, primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    superintendencia = models.CharField(db_column='SuperIntendencia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    unidadoperacional = models.CharField(db_column='UnidadOperacional', max_length=100, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lugar = models.CharField(db_column='Lugar', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipoobjeto = models.CharField(db_column='TipoObjeto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    evento = models.CharField(db_column='Evento', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nivelimpacto = models.CharField(db_column='NivelImpacto', max_length=200, blank=True, null=True)  # Field name made lowercase.
    comentarios = models.CharField(db_column='Comentarios', max_length=500, blank=True, null=True)  # Field name made lowercase.
    qhorasdetencion = models.CharField(db_column='QHorasDetencion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    qdiasdetencion = models.CharField(db_column='QDiasDetencion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    qktsperdida = models.CharField(db_column='QKtsPerdida', max_length=500, blank=True, null=True)  # Field name made lowercase.
    qtmfperdida = models.CharField(db_column='QTMFperdida', max_length=500, blank=True, null=True)  # Field name made lowercase.
    qlibrasperdida = models.CharField(db_column='QLibrasPerdida', max_length=500, blank=True, null=True)  # Field name made lowercase.
    montoperdidakusd = models.CharField(db_column='MontoPerdidaKUSD', max_length=500, blank=True, null=True)  # Field name made lowercase.
    idriesgoasociado = models.CharField(db_column='IdRiesgoAsociado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    familia = models.CharField(db_column='Familia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subproceso = models.CharField(db_column='SubProceso', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipofalla = models.CharField(db_column='TipoFalla', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_UNIFICA'


class RiesgoUnificaControles(models.Model):
    idregistro = models.CharField(db_column='IdRegistro', max_length=100, primary_key=True)  # Field name made lowercase.
    idcontrol = models.CharField(db_column='IdControl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    control = models.CharField(db_column='Control', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_UNIFICA_CONTROLES'
