#from core.utils import image_as_base64
from django.conf import settings
import pdfkit
import os.path
from django.contrib.auth.models import User
from core.models import RiesgoControl, RiesgoControlAutoevaluacion, RiesgoControlMonitoreo, RiesgoControlCausa, RiesgoControlConsecuencia, RiesgoCausas, RiesgoConsecuencias


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
                                    <th><p align="left">Dueño del plan</p></th>                                    
                                </tr>
                            </thead>
                            <tbody>
                            <tr>
                                <td class="cell-border">""" + str(self.data_riesgo['probabilidad_residual']) +  """</td>
                                <td class="cell-border">""" + str(self.data_riesgo['impacto_residual']) +  """</td>
                                <td class="cell-border">""" + str(self.data_riesgo['nivel_residual']) +  """</td>
                                <td class="cell-border"></td>                                
                            </tr>
                            </tbody>
                        </table>
                       <br />
                       <hr />
                       <span style="float:left; font-size:15px;"><b><u>Control</u></b></span>
                       <br>
                        <table style='font-size:11px'>
                            <thead>
                                <tr>
                                    <th><p align="left">Probabilidad</p></th>
                                    <th><p align="left">Impacto</p></th>
                                    <th><p align="left">Nivel Inherente</p></th>                                                                   
                                </tr>
                            </thead>
                            <tbody>
                            <tr>                            
                                <td class="cell-border">""" + str(self.data_riesgo['probabilidad']) +  """</td>
                                <td class="cell-border">""" + str(self.data_riesgo['impacto']) +  """</td>
                                <td class="cell-border">""" + str(self.data_riesgo['nivel_inherente']) +  """</td>                                
                            </tr>
                            </tbody>
                        </table>   
                     
                        <br />
                        <table border="0" style="width:100%;margin-top: 1%;font-size:11px;">                        
                            <thead>
                                <tr>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                    <td class="cell-border" colspan="3"><center>Monitoreo</center></td>
                                </tr>
                                <tr>                                    
                                    <th class="cell-border"><p align="left">Id.</p></th>
                                    <th class="cell-border"><p align="left">Nombre</p></th>
                                    <th class="cell-border"><p align="left">Causas</p></th>                                    
                                    <th class="cell-border"><p align="left">Consecuencias</p></th>
                                    <th class="cell-border"><p align="left">Tipo</p></th>
                                    <th class="cell-border"><p align="left">Dueño</p></th>
                                    <th class="cell-border"><p align="left">Frecuencia</p></th>
                                    <th class="cell-border"><p align="left">Eficacia</p></th>
                                    <th class="cell-border"><p align="left">Eficiencia</p></th>
                                    <th class="cell-border"><p align="left">Efectividad</p></th>

                                    <th class="cell-border"><p align="left">Frecuencia</p></th>
                                    <th class="cell-border"><p align="left">Fecha Inicio</p></th>
                                    <th class="cell-border"><p align="left">Fecha Term.</p></th>
                                </tr>
                            </thead>
                            <tbody style="font-size:11px;">
                            """ +self.tablaDetalleControl()+ """
                            </tbody>
                        </table>  
                       
                    </div>
                </body>
            </html>
         """
        return html
    
    def tablaDetalleControl(self):
        datos_control = self.getDatosControl()
        tbody = ""
        for k, v in datos_control.items():
            tbody+="""
            <tr>
            <td>"""+v['contador']+"""</td>
            <td>"""+k+"""</td>
            <td>"""+v['causas']+"""</td>
            <td>"""+v['consecuencias']+"""</td>            
            <td>"""+v['tipo']+"""</td>
            <td>"""+v['dueno']+"""</td>
            <td>"""+v['frecuenciacontrol']+"""</td>
            <td>"""+v['eficacia']+"""</td>
            <td>"""+v['eficiencia']+"""</td>
            <td>"""+v['efectividad']+"""</td>
            <td>"""+v['frecuencia']+"""</td>
            <td>"""+v['fecha_inicio']+"""</td>
            <td>"""+v['fecha_termino']+"""</td>

            </tr>
            """
        return tbody


    def getDatosControl(self):                             
        print(self.id_riesgo)
        controles = list(RiesgoControl.objects.filter(idriesgo=self.id_riesgo).values())
        print("los controles ", controles)
        dict_controles = {}
        contador = 0
        for control in controles:
            contador+=1
            causas = self.getCausasControl(control['idcontrol'])
            consecuencias = self.getConsecuenciasControl(control['idcontrol'])
            autoevaluaciones=[{'eficacia':'', 'eficiencia':'', 'efectividad':''}]
            monitoreos=[{'frecuenciamonitoreo':'', 'inicio':'', 'fin':''}]
            if RiesgoControlAutoevaluacion.objects.filter(idcontrol=control['idcontrol']).exists():
                autoevaluaciones = list(RiesgoControlAutoevaluacion.objects.filter(idcontrol=control['idcontrol']).values())
            if RiesgoControlMonitoreo.objects.filter(idcontrol=control['idcontrol']).exists():
                monitoreos = list(RiesgoControlMonitoreo.objects.filter(idcontrol=control['idcontrol']).values())
            dict_controles[control['nombrecontrol']]={
                'causas':causas,
                'consecuencias':consecuencias,
                'tipo':str(control['tipocontrol'] or ''),
                'dueno':str(control['dueñocontrol'] or ''),
                'frecuenciacontrol':str(control['frecuenciacontrol'] or ''),
                'eficacia':str(autoevaluaciones[0]['eficacia'] or ''),
                'eficiencia':str(autoevaluaciones[0]['eficiencia'] or ''),
                'efectividad':str(autoevaluaciones[0]['efectividad'] or ''),
                'frecuencia':str(monitoreos[0]['frecuenciamonitoreo'] or ''),
                'fecha_inicio':str(monitoreos[0]['inicio'] or ''),
                'fecha_termino':str(monitoreos[0]['fin'] or ''),
                'contador':str(contador)
            }            
        
        return dict_controles
    
    def getCausasControl(self, id_control):
        causas =""
        if RiesgoControlCausa.objects.filter(idcontrol=id_control).exists():
            ids_causas_control = list(RiesgoControlCausa.objects.filter(idcontrol=id_control).values_list("idcausa", flat=True))
            for id_causa in ids_causas_control:                
                causa = list(RiesgoCausas.objects.filter(idcausa=id_causa).values("causa"))[0]['causa']
                causas+="- "+str(causa)+"<br>"
        return causas
    
    def getConsecuenciasControl(self, id_control):
        consecuencias =""
        if RiesgoControlConsecuencia.objects.filter(idcontrol=id_control).exists():
            ids_consecuencias_control = list(RiesgoControlConsecuencia.objects.filter(idcontrol=id_control).values_list("idconsecuencia", flat=True))
            for id_consecuencia in ids_consecuencias_control:
                consecuencia = list(RiesgoConsecuencias.objects.filter(idconsecuencia=id_consecuencia).values("consecuencia"))[0]['consecuencia']
                consecuencias+="- "+str(consecuencia)+"<br>"
        return consecuencias
                    
    def joinHtml(self):
        datos = self.getDatosControl()
        print(datos)
        html = self.createHeader() + self.createBodySPM()        
        return html

