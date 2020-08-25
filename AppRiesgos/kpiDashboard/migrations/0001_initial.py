# Generated by Django 3.0.5 on 2020-04-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RiesgoKpi',
            fields=[
                ('idriesgokpi', models.CharField(db_column='IdRiesgoKpi', max_length=255, primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, db_column='Tipo', max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, db_column='Valor', null=True)),
                ('porcavance', models.FloatField(blank=True, db_column='PorcAvance', null=True)),
                ('mes', models.CharField(blank=True, db_column='Mes', max_length=50, null=True)),
                ('ano', models.IntegerField(blank=True, db_column='Ano', null=True)),
                ('fecreg', models.DateTimeField(blank=True, db_column='FecReg', null=True)),
                ('fecmod', models.DateTimeField(blank=True, db_column='Fecmod', null=True)),
            ],
            options={
                'db_table': 'RIESGO_Kpi',
                'managed': False,
            },
        ),
    ]
