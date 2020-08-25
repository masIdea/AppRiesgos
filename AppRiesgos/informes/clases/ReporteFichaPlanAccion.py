#from core.utils import image_as_base64
from django.conf import settings
import pdfkit
import os.path
from django.contrib.auth.models import User
from core.models import RiesgoPlanderespuesta


class Html():
    def __init__(self, titulo=None, subtitulo=None, logo=None, id_riesgo=None, data_riesgo=None):
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.logo = logo
        self.id_riesgo = id_riesgo
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
    
    def getPlanRespuesta(self):
        print(self.id_riesgo)
        detalle_plan = list(RiesgoPlanderespuesta.objects.filter(idriesgo=self.id_riesgo).values())
        print("el detalle del plan", detalle_plan)
        return detalle_plan

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
                <body>
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

                        <table border="0" style="width:100%;margin-top: 1%;">
                            <thead>
                                <tr>
                                    <th><p align="left" style="font-size:12px;">FICHA CONTROL</p></th>                                    
                                    <th><p align="left">&nbsp;</p></th>
                                    <th><p align="left">&nbsp;</p></th>
                                    <th><p align="right">Fecha Act. """ +str(self.data_riesgo['fechacreacion'].day)+"/"+str(self.data_riesgo['fechacreacion'].month)+"/"+str(self.data_riesgo['fechacreacion'].year)+ """</p></th>
                                </tr>
                            </thead>
                            <tbody>
                            
                            </tbody>
                        </table>
                        <hr />
                        <br />
                        <table border="0" style="width:100%;margin-top: 2%; font-size:13px;">                        
                            <thead>
                                <tr>
                                    <th><p align="left">SuperIntendencia/Dirección</p></th>
                                    <th><p align="left">Área/Proyecto</p></th>
                                    <th><p align="left">Codigo SuperIntendencia</p></th>
                                    <th><p align="left">Codigo Área/API</p></th>
                                </tr>
                            </thead>
                            <tbody>
                            <tr>
                                <td class="cell-border">""" + str(self.data_riesgo['direccion']) +  """</td>
                                <td class="cell-border">""" + str(self.data_riesgo['codigoproyecto']) +  """</td>
                                <td class="cell-border">""" + str(self.data_riesgo['codigodireccion']) +  """</td>
                                <td class="cell-border">""" + str(self.data_riesgo['codigoarea']) +  """</td>
                            </tr>
                            </tbody>
                        </table>
                        <hr />
                        <br />
                        <span style="float:left; font-size:15px;"><b><u>Riesgo</u></b></span>
                        <br>
                        <table style='font-size:11px'>
                            <thead>
                                <tr>
                                    <th><p align="left">Id.</p></th>
                                    <th><p align="left">Causas</p></th>
                                    <th><p align="left">Descripción</p></th>
                                    <th><p align="left">Consecuencias</p></th>
                                    <th><p align="left">Dueño</p></th>
                                </tr>
                            </thead>
                            <tbody>
                            <tr>
                                <td class="cell-border">""" + str(self.data_riesgo['id_riesgo']) +  """</td>
                                <td class="cell-border">""" + str(self.getCausas()) +  """</td>
                                <td class="cell-border">""" + str(self.data_riesgo['descripcionriesgo']) +  """</td>
                                <td class="cell-border">""" + str(self.getConsecuencias()) +  """</td>
                                <td class="cell-border">""" + str(self.data_riesgo['dueno']) +  """</td>
                            </tr>
                            </tbody>
                        </table>
                        <br />                        
                        <table style='font-size:11px'>
                            <thead>
                                <tr>
                                    <th><p align="left">Probabilidad</p></th>
                                    <th><p align="left">Impacto</p></th>
                                    <th><p align="left">Nivel Residual</p></th>                                                                  
                                </tr>
                            </thead>
                            <tbody>
                            <tr>
                                <td class="cell-border">""" + str(self.data_riesgo['probabilidad']) +  """</td>
                                <td class="cell-border">""" + str(self.data_riesgo['impacto']) +  """</td>
                                <td class="cell-border">""" + str(self.data_riesgo['nivel_residual']) +  """</td>                                
                            </tr>
                            </tbody>
                        </table>
                       <br />
                       <hr />
                       <span style="float:left; font-size:15px;"><b><u>Plan de Respuesta</u></b></span>
                       <br>
                        <table style='font-size:11px'>
                            <thead>
                                <tr>
                                    <th><p align="left">Probabilidad</p></th>
                                    <th><p align="left">Impacto</p></th>
                                    <th><p align="left">Nivel Objetivo</p></th>                                                                   
                                    <th><p align="left">Trigger</p></th>      
                                    <th><p align="left">Dueño del Plan</p></th>    
                                </tr>
                            </thead>
                            <tbody>
                            <tr>                            
                                <td class="cell-border">""" + str(self.data_riesgo['probabilidad']) +  """</td>
                                <td class="cell-border">""" + str(self.data_riesgo['impacto']) +  """</td>
                                <td class="cell-border">""" + str(self.data_riesgo['nivel_objetivo']) +  """</td>                                
                                <td class="cell-border">""" + str(self.data_riesgo['trigger']) +  """</td>     
                                <td class="cell-border">""" + str(self.data_riesgo['dueno_plan']) +  """</td>     
                            </tr>
                            </tbody>
                        </table>   
                     
                        <br />
                        <table border="0" style="width:100%;margin-top: 1%;font-size:11px;">                        
                            <thead>
                                <tr>                                    
                                    <th class="cell-border"><p align="left">N°</p></th>
                                    <th class="cell-border"><p align="left">Detalle de Entregables</p></th>
                                    <th class="cell-border"><p align="left">Resp.</p></th>                                    
                                    <th class="cell-border"><p align="left">% del Plan</p></th>
                                    <th class="cell-border"><p align="left">F. Inicio</p></th>
                                    <th class="cell-border"><p align="left">F. Término</p></th>
                                    <th class="cell-border"><p align="left">Real</p></th>
                                    <th class="cell-border"><p align="left">Planificado</p></th>
                                    <th class="cell-border"><p align="left">Costo [kUS$]</p></th>
                                </tr>
                            </thead>
                            <tbody style="font-size:11px;">
                                """ +self.tableDetallePlan()+ """
                            </tbody>
                          
                        </table>  
                       
                    </div>
                </body>
            </html>
         """
        return html

    def tableDetallePlan(self):                             
        tbody = ""
        plan_respuesta = self.getPlanRespuesta()
        contador = 0
        porc_plan = 0
        real = 0
        plan = 0
        costo = 0
        for plan in plan_respuesta:            
            contador+=1
            if plan['avanceplanificado']:
                porc_plan += int(plan['avanceplanificado'])
            if plan['avancereal']:
                real += int(plan['avancereal'])
            if plan['costo']:
                costo += int(plan['costo'])

            tbody+="<tr>"
            tbody+="<td>"+str(contador)+"</td>"
            if plan['descripcion']:
                tbody+="<td>"+plan['descripcion']+"</td>"
            else:
                tbody+="<td></td>"
            if plan['dueñoplanderespuesta']:
                tbody+="<td>"+plan['dueñoplanderespuesta']+"</td>"
            else:
                 tbody+="<td></td>"
            if plan['avanceplanificado']:
                tbody+="<td>"+plan['avanceplanificado']+"</td>"
            else:
                 tbody+="<td></td>"
            if plan['fechainicio']:
                tbody+="<td>"+plan['fechainicio']+"</td>"
            else:
                 tbody+="<td></td>"
            if plan['fechatermino']:
                tbody+="<td>"+plan['fechatermino']+"</td>"
            else:
                 tbody+="<td></td>"
            if plan['avancereal']:
                tbody+="<td>"+plan['avancereal']+"</td>"
            else:
                 tbody+="<td></td>"
            if plan['avanceplanificado']:
                tbody+="<td>"+plan['avanceplanificado']+"</td>"
            else:
                 tbody+="<td></td>"
            if plan['costo']:
                tbody+="<td>"+plan['costo']+"</td>"
            else:
                 tbody+="<td></td>"
            tbody+="</tr>"

        tbody+="<tr>"
        tbody+="<td colspan='3'>Total</td>"
        tbody+="<td>"+str(porc_plan)+"</td>"
        tbody+="<td></td>"
        tbody+="<td></td>"
        tbody+="<td>"+str(real)+"</td>"
        tbody+="<td>"+str(porc_plan)+"</td>"
        tbody+="<td>"+str(costo)+"</td>"
        tbody+="</tr>"                
        
        print(tbody)
        return tbody
                    
    def joinHtml(self):
        html = self.createHeader() + self.createBodySPM()        
        return html

