from django.db import models

# Create your models here.
class RiesgoKpi(models.Model):
    idriesgokpi = models.CharField(db_column='IdRiesgoKpi', max_length=255, primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.
    porcavance = models.FloatField(db_column='PorcAvance', blank=True, null=True)  # Field name made lowercase.
    mes = models.CharField(db_column='Mes', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ano = models.IntegerField(db_column='Ano', blank=True, null=True)  # Field name made lowercase.
    fecreg = models.DateTimeField(db_column='FecReg', blank=True, null=True)  # Field name made lowercase.
    fecmod = models.DateTimeField(db_column='Fecmod', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIESGO_Kpi'