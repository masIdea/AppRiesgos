#from core.utils import image_as_base64
from django.conf import settings
import pdfkit
import os.path
from django.contrib.auth.models import User
from core.models import RiesgoPlanderespuesta, Riesgo, RiesgoPlanderespuestaActividad


class Html():
    def __init__(self, titulo=None, subtitulo=None, logo=None, id_gerencia=None, data_riesgo=None):
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.logo = logo
        self.id_gerencia = id_gerencia
        self.data_riesgo = data_riesgo        
    
    def imagesToBase64(self):
        img_to_b64 = image_as_base64(settings.MEDIA_ROOT + self.logo)
        img_to_b64 = img_to_b64.split("'")        
        return img_to_b64[1]

    def getCausas(self):
        causas = ""
        for causa in self.data_riesgo['causas']:
            causas+="- "+causa+"<br>"
        return causas
    
    def getDatosRiesgo(self):
        riesgos_gerencia = list(Riesgo.objects.filter(gerencia=self.id_gerencia).values_list("idriesgo", flat=True))  
        riesgos_plan = list(RiesgoPlanderespuesta.objects.filter(idriesgo__in=riesgos_gerencia).values_list("idriesgo", flat=True))
        arreglo_datos = []      
        for riesgo in riesgos_plan:
            dict_datos = {}
            planes = list(RiesgoPlanderespuesta.objects.filter(idriesgo=riesgo).values())
            for plan in planes:
                actividades = []
                if RiesgoPlanderespuestaActividad.objects.filter(idplanderespuesta=plan['idplanrespuesta']).exists():
                    actividades = list(RiesgoPlanderespuestaActividad.objects.filter(idplanderespuesta=plan['idplanrespuesta']).values())
                dict_datos[riesgo] = {
                    'plan_accion':plan['descripcion'],
                    'responsable':plan['dueñoplanderespuesta'],
                    'inicio_plan':plan['fechainicio'],
                    'termino_plan':plan['fechatermino'],
                    'actividades':actividades
                }
            arreglo_datos.append(dict_datos.copy())

        print(arreglo_datos)
        return arreglo_datos

    def getConsecuencias(self):
        consecuencias = ""
        for consecuencia in self.data_riesgo['consecuencias']:
            consecuencias+="- "+consecuencia+"<br>"    
        return consecuencias
    

    def createHeader(self):
        html = """ 
            <html>
                <head>
                    <meta charset="utf-8">
                    <meta namee="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <title>""" + self.titulo +  """</title>
                    <style>
                        .border{
                            border-width: 3px;border: double; border-color: gray;
                        }
                        body{
                            font-family: Century Gothic,CenturyGothic,AppleGothic,sans-serif;
                        }
                        #background{
                            position:absolute;
                            z-index:0;
                            background:white;
                            display:block;
                            min-height:50%;
                            min-width:50%;
                            top:20%;
                            left:10%;
                            color:yellow;
                        }
                        #content{
                            position:absolute;
                            z-index:1;
                        }
                        #bg-text
                        {
                            color:lightgrey;
                            font-size:120px;
                            transform:rotate(300deg);
                            -webkit-transform:rotate(300deg);
                        }
                        .cell-border{
                            border-top: 1px solid gray;
                            border-left: 1px solid gray;
                            border-right: 1px solid gray;
                            border-bottom: 1px solid gray;
                            background-color: #80808040;
                        }
                    </style>
                </head>
        """

        return html

    def createBodySPM(self):
        html = """

<body><style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<div id="background">
                        <p id="bg-text"> </p>
                    </div>

                    <div id="content">
                                                <table border="0" style="width: 100%; margin-top:1%;">
                            <tbody>
                                <tr>
                                    <td><span align="left" style="font-size: 25px; color:orange;">""" + self.titulo + """</span></td>
                                </tr>
                                <tr>
                                    <td>
                                        <center>
                                            <p align="left" style="font-size: 12px;">
                                                    """+self.subtitulo+"""
                                            </p>
                                        </center>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <br />
<table class="tg">
<thead>
  <tr>
	<td>Id Riesgo</td>
	<td>Descripción Riesgo</td>
	<td>Plan de Acción</td>
	<td>Responsable Plan de Acción</td>
	<td>Actividad</td>
	<td>Responsable Actividad</td>
	<td>Fecha Inicio</td>
	<td>Fecha Fin</td>
	<td>Fecha Inicio Plan.</td>
	<td>Fecha Fin Plan.</td>
	<td>Estatus</td>
	<td>%Av.Real</td>
	<td>%Av. Prog.</td>
	<td>Comentarios - Restricción</td>
  </tr>
</thead>
<tbody>
"""+self.tableDetalleSeguimientoPlan()+"""

</tbody>
</table>
</tbody>
</table>
</body>
</html>
         """
        return html

    def tableDetalleSeguimientoPlan(self):                             
        tbody = ""
        datos = self.getDatosRiesgo()
        for dato in datos:
            for k, v in dato.items():
                cantidad_actividades = len(v['actividades'])
                descripcion_riesgo = list(Riesgo.objects.filter(idriesgo=k).values("riesgo"))[0]['riesgo']
                tbody="""<tr>
                <td class="tg-0lax" rowspan="""+str(cantidad_actividades)+"""">"""+str(k)+"""</td>
                <td class="tg-0lax" rowspan="""+str(cantidad_actividades)+"""">"""+str(descripcion_riesgo)+"""</td>
                <td class="tg-0lax" rowspan="""+str(cantidad_actividades)+"""">"""+str(v['plan_accion'])+"""</td>
                <td class="tg-0lax" rowspan="""+str(cantidad_actividades)+"""">"""+str(v['responsable'])+"""</td>
                """ 
                

                contador_actividades = 1
                for actividad in v['actividades']:
                    if contador_actividades==1:
                        tbody+="""
                        <td class="tg-0lax">"""+str(actividad['nombreactividad'])+"""</td>
                        <td class="tg-0lax">"""+str(actividad['responsable'])+"""</td>
                        <td class="tg-0lax">"""+str(actividad['inicio'])+"""</td>
                        <td class="tg-0lax">"""+str(actividad['termino'])+"""</td>
                        <td class="tg-0lax">"""+str(v['inicio_plan'])+"""</td>
                        <td class="tg-0lax">"""+str(v['termino_plan'])+"""</td>
                        <td class="tg-0lax">"""+str(actividad['estadoactividad'])+"""</td>
                        <td class="tg-0lax">"""+str(actividad['avancereal'])+"""</td>
                        <td class="tg-0lax"></td>
                        <td class="tg-0lax"></td>
                        </tr>"""
                    else:
                        tbody+="""
                        <tr>
                        <td class="tg-0lax">"""+str(actividad['nombreactividad'])+"""</td>
                        <td class="tg-0lax">"""+str(actividad['responsable'])+"""</td>
                        <td class="tg-0lax">"""+str(actividad['inicio'])+"""</td>
                        <td class="tg-0lax">"""+str(actividad['termino'])+"""</td>
                        <td class="tg-0lax">"""+str(v['inicio_plan'])+"""</td>
                        <td class="tg-0lax">"""+str(v['termino_plan'])+"""</td>
                        <td class="tg-0lax">"""+str(actividad['estadoactividad'])+"""</td>
                        <td class="tg-0lax">"""+str(actividad['avancereal'])+"""</td>
                        <td class="tg-0lax"></td>
                        <td class="tg-0lax"></td>
                        </tr>"""


        return tbody
                    
    def joinHtml(self):
        self.getDatosRiesgo()
        html = self.createHeader() + self.createBodySPM()        
        return html

