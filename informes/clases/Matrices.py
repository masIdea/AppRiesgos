#from core.utils import image_as_base64
from django.conf import settings
import pdfkit
import os.path
from django.contrib.auth.models import User
from core.utils import daterange
from datetime import datetime
from core.models import RiesgoEvaluacioncualitativainherente, RiesgoEvaluacioncualitativaresidual, RiesgoEvaluacioncualitativaobjetivo, RiesgoEvaluacioncualitativaresidualupdate, RiesgoEvaluacioncualitativainherenteupdate


class Html():
    def __init__(self, titulo=None, subtitulo=None, id_riesgo=None, gerencia=None, fecha_inicio=None, fecha_termino=None):
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self.id_riesgo = id_riesgo
        self.gerencia = gerencia
    
    def imagesToBase64(self):
        img_to_b64 = image_as_base64(settings.MEDIA_ROOT + self.logo)
        img_to_b64 = img_to_b64.split("'")        
        return img_to_b64[1]

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
                    <br />                    
                    <table border="0" style="width: 100%; margin-top:-3%;">
                        <tbody>
                            <tr>
                                <td><span align="left" style="font-size: 25px;">""" + self.titulo + """</span></td>
                            </tr>
                            <tr>
                                <td>
                                    <center>
                                        <p align="left" style="font-size: 20px;">
                                                """+self.subtitulo+"""
                                        </p>
                                    </center>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <br />
                    <br />"""

        for fecha in daterange(datetime.strptime(self.fecha_inicio, '%Y-%m-%d'), datetime.strptime(self.fecha_termino, '%Y-%m-%d')):
            #print(fecha)
            inherente = False
            residual = False
            residual_update = False
            objetivo = False
            print("la fecha consultada es ", fecha)
            inherente = RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=self.id_riesgo, modificado__year=fecha.year, modificado__month=fecha.month, modificado__day=fecha.day).exists()            
            inherente_update = RiesgoEvaluacioncualitativainherenteupdate.objects.filter(idriesgo=self.id_riesgo, fecha__year=fecha.year, fecha__month=fecha.month, fecha__day=fecha.day).exists()
            residual = RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=self.id_riesgo, modificado__year=fecha.year, modificado__month=fecha.month, modificado__day=fecha.day).exists()
            residual_update = RiesgoEvaluacioncualitativaresidualupdate.objects.filter(idriesgo=self.id_riesgo, fecha__year=fecha.year, fecha__month=fecha.month, fecha__day=fecha.day).exists()
            objetivo = RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=self.id_riesgo, creado__year=fecha.year, creado__month=fecha.month, creado__day=fecha.day).exists()
            if inherente or residual or objetivo or residual_update or inherente_update:
                print("La fecha es --> ", fecha)
                datos_inherente = None
                datos_residual = None                
                datos_objetivo = None
                datos_inherente = list(RiesgoEvaluacioncualitativainherente.objects.filter(idriesgo=self.id_riesgo, modificado__year=fecha.year, modificado__month=fecha.month, modificado__day=fecha.day).values("probabilidad", "impacto"))
                datos_inherente_update = list(RiesgoEvaluacioncualitativainherenteupdate.objects.filter(idriesgo=self.id_riesgo, fecha__year=fecha.year, fecha__month=fecha.month, fecha__day=fecha.day).values("probabilidad", "impacto"))
                datos_residual = list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=self.id_riesgo, modificado__year=fecha.year, modificado__month=fecha.month, modificado__day=fecha.day).values("probabilidadresidual", "impactoresidual"))                
                datos_residual_update = list(RiesgoEvaluacioncualitativaresidualupdate.objects.filter(idriesgo=self.id_riesgo, fecha__year=fecha.year, fecha__month=fecha.month, fecha__day=fecha.day).values("probabilidadresidual", "impactoresidual"))
                datos_objetivo = list(RiesgoEvaluacioncualitativaobjetivo.objects.filter(idriesgo=self.id_riesgo, creado__year=fecha.year, creado__month=fecha.month, creado__day=fecha.day).values("probabilidadcontrol", "impactocontrol"))
                
                html+="""<br />                    
                    <table border="0" style="width: 100%; margin-top:-3%;">
                        <tbody>                            
                            <tr>
                                <td>
                                    <center>
                                        <p align="left" style="font-size: 15px;">
                                                """+str(fecha.day)+'/'+str(fecha.month)+'/'+str(fecha.year)+"""
                                        </p>
                                    </center>
                                </td>
                            </tr>
                        </tbody>
                    </table> """
                probabilidad_inherente = 0
                impacto_inherente = 0

                probabilidad_residual = 0
                impacto_residual = 0

                probabilidad_objetivo = 0
                impacto_objetivo = 0

                if len(datos_inherente)>0:
                    probabilidad_inherente = int(datos_inherente[0]['probabilidad'])
                    impacto_inherente =int(datos_inherente[0]['impacto'])
                elif len(datos_inherente_update)>0:
                    probabilidad_inherente = int(datos_inherente_update[0]['probabilidad'])
                    impacto_inherente =int(datos_inherente_update[0]['impacto'])
                
                if len(datos_objetivo)>0:
                    probabilidad_objetivo = int(datos_objetivo[0]['probabilidadcontrol'])
                    impacto_objetivo = int(datos_objetivo[0]['impactocontrol'])
                    
                if len(datos_residual)>0:
                    probabilidad_residual = int(datos_residual[0]['probabilidadresidual'])
                    impacto_residual = int(datos_residual[0]['impactoresidual'])
                elif len(datos_residual_update)>0:                    
                    probabilidad_residual = int(datos_residual_update[0]['probabilidadresidual'])
                    impacto_residual = int(datos_residual_update[0]['impactoresidual'])
                
                

                html+= self.matrizResidual(impacto_residual, probabilidad_residual, fecha)
                html+= self.matrizInherente(impacto_inherente, probabilidad_inherente, fecha)
                html+= self.matrizObjetivo(impacto_objetivo, probabilidad_objetivo, fecha)
                html+="""<br />"""
        
                       
        html+= """ </div>
                        </body>
                    </html>
               """
        return html

                    
    def joinHtml(self):
        html = self.createHeader() + self.createBodySPM()        
        return html
    
    def matrizInherente(self, impacto, probabilidad, fecha):
        fecha = str(fecha.year) +""+str(fecha.month)+""+str(fecha.day)
        matrizInherente = """
                    <style>
    #inhe_"""+fecha+"""_1_1,#inhe_"""+fecha+"""_1_2,#inhe_"""+fecha+"""_1_3,#inhe_"""+fecha+"""_1_4,#inhe_"""+fecha+"""_1_5,#inhe_"""+fecha+"""_1_6,#inhe_"""+fecha+"""_2_1,#inhe_"""+fecha+"""_2_2,#inhe_"""+fecha+"""_2_3,#inhe_"""+fecha+"""_2_4,#inhe_"""+fecha+"""_3_1,#inhe_"""+fecha+"""_3_2,#inhe_"""+fecha+"""_3_3{
        background-color: #00B050;
    }
    #inhe_"""+fecha+"""_1_7,#inhe_"""+fecha+"""_2_5,#inhe_"""+fecha+"""_2_6,#inhe_"""+fecha+"""_3_4,#inhe_"""+fecha+"""_3_5,#inhe_"""+fecha+"""_3_4,#inhe_"""+fecha+"""_4_1,#inhe_"""+fecha+"""_4_2,#inhe_"""+fecha+"""_4_3,#inhe_"""+fecha+"""_4_4,#inhe_"""+fecha+"""_4_5,#inhe_"""+fecha+"""_5_1,#inhe_"""+fecha+"""_5_2,#inhe_"""+fecha+"""_5_3,#inhe_"""+fecha+"""_5_4{
        background-color: #FFFF00;
    }
    #inhe_"""+fecha+"""_6_1,#inhe_"""+fecha+"""_6_2,#inhe_"""+fecha+"""_6_3,#inhe_"""+fecha+"""_6_4,#inhe_"""+fecha+"""_6_5,#inhe_"""+fecha+"""_6_6,#inhe_"""+fecha+"""_6_7,#inhe_"""+fecha+"""_7_1,#inhe_"""+fecha+"""_7_2,#inhe_"""+fecha+"""_7_3,#inhe_"""+fecha+"""_7_4,#inhe_"""+fecha+"""_7_5,#inhe_"""+fecha+"""_7_6,#inhe_"""+fecha+"""_7_7,#inhe_"""+fecha+"""_5_5,#inhe_"""+fecha+"""_5_6,#inhe_"""+fecha+"""_5_7,#inhe_"""+fecha+"""_4_6,#inhe_"""+fecha+"""_4_7,#inhe_"""+fecha+"""_3_6,#inhe_"""+fecha+"""_3_7,#inhe_"""+fecha+"""_2_7{
        background-color: #FF0000;
    }
    .coords{
        border:1px solid #babdc1;
        width: 12.5%;
        text-align: center;
    }
    #label_impacto{
        writing-mode:tb-rl;
        -webkit-transform:rotate(-180deg);
        -moz-transform:rotate(-180deg);
        -o-transform: rotate(-180deg);
        -ms-transform:rotate(-180deg);
        transform: rotate(-180deg);
        color: black;
        font-size: 19px;
    }
    .num_prob{
        font-size: 10px !important;
    }
    .impacto-vertical{
        width: 12.5%;
        border: 1px solid transparent;
        text-align: center;
    }
    .impacto-horizontal{
        width: 12.5%;
        border: 1px solid transparent;
        text-align: center;        
    }
    .label_horizontal{
        font-size: 10px !important;
    }

    .r-circle {
        background: black;
        color: #fff;
        padding: 6% 4%;
        border-radius: 50%;
        font-size: 11px;
        display: none;
        width: 77%;
        cursor: pointer;
    }
    </style>    

    <table style="float:left">
        <caption style="margin-left: 19%;font-size: 17px;color: black;">Riesgo Inherente</caption>
        <tbody>
            <tr>
                <td rowspan="7" style="width: 1%;">
                    
                </td>
            <td style="width: 12.5%;" class="impacto-vertical"> 
                <label class="num_prob">7</label>
            </td>
            <td id="inhe_"""+fecha+"""_7_1" class="coords">                
                    
                    <center><span class="r-circle" id="inhe_"""+fecha+"""_label_7_1">R</span></center>
            </td>

            <td id="inhe_"""+fecha+"""_7_2" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_7_2">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_7_3" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_7_3">R</span></center>
                </div>            
            </td>
            <td id="inhe_"""+fecha+"""_7_4" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_7_4">R</span></center>
                </div>            
            </td>
            <td id="inhe_"""+fecha+"""_7_5" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_7_5">R</span></center>
                </div>            
            </td>
            <td id="inhe_"""+fecha+"""_7_6" class="coords">
                <div class="parent">                                                                
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_7_6">R</span></center>
                </div>            
            </td>
            <td id="inhe_"""+fecha+"""_7_7" class="coords">
                <div class="parent">                                                            
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_7_7">R</span></center>
                </div>
                
            </td>
        </tr>

        <tr>
            <td class="impacto-vertical">
                <center><label class="num_prob">6</label></center>
            </td>
            <td id="inhe_"""+fecha+"""_6_1" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_6_1">R</span></center>
                </div>            		
            </td>
            <td id="inhe_"""+fecha+"""_6_2" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_6_2">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_6_3" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_6_3">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_6_4" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_6_4">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_6_5" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_6_5">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_6_6" class="coords">
                <div class="parent">
                    <center>
                        <span class="r-circle"  id="inhe_"""+fecha+"""_label_6_6">R</span>
                    </center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_6_7" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_6_7">R</span></center>
                </div>
            </td>
        </tr>
        
        <tr>
            <td class="impacto-vertical">
                <label class="num_prob">5</label>
            </td>
            <td id="inhe_"""+fecha+"""_5_1" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_5_1">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_5_2" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_5_2">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_5_3" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_5_3">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_5_4" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_5_4">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_5_5" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_5_5">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_5_6" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_5_6">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_5_7" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_5_7">R</span></center>
                </div>
            </td>
        </tr>
        
        <tr>
            <td class="impacto-vertical">
                <label class="num_prob">4</label>
            </td>
            <td id="inhe_"""+fecha+"""_4_1" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_4_1">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_4_2" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_4_2">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_4_3" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_4_3">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_4_4" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_4_4">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_4_5" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_4_5">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_4_6" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_4_6">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_4_7" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_4_7">R</span></center>
                </div>
            </td>
        </tr>
        
        <tr>
            <td class="impacto-vertical">
                <label class="num_prob">3</label>
            </td>
            <td id="inhe_"""+fecha+"""_3_1" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_3_1">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_3_2" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_3_2">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_3_3" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_3_3">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_3_4" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_3_4">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_3_5" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_3_5">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_3_6" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_3_6">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_3_7" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_3_7">R</span></center>
                </div>
            </td>
        </tr>

        <tr>   
            <td class="impacto-vertical">
                <label class="num_prob">2</label>
            </td>     
            <td id="inhe_"""+fecha+"""_2_1" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_2_1">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_2_2" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_2_2">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_2_3" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_2_3">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_2_4" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_2_4">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_2_5" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_2_5">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_2_6" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_2_6">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_2_7" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_2_7">R</span></center>
                </div>
            </td>
        </tr>
        
        <tr>
            <td class="impacto-vertical">
                <label class="num_prob">1</label>
            </td>
            <td id="inhe_"""+fecha+"""_1_1" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_1_1">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_1_2" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_1_2">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_1_3" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_1_3">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_1_4" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_1_4">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_1_5" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_1_5">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_1_6" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_1_6">R</span></center>
                </div>
            </td>
            <td id="inhe_"""+fecha+"""_1_7" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="inhe_"""+fecha+"""_label_1_7">R</span></center>
                </div>
            </td>
        </tr>
        <tr style="height: 0px;">
            <td></td>
            <td></td>
            <td class="impacto-horizontal"><center><label class="label_horizontal">1</label></center></td>
            <td class="impacto-horizontal"><center><label class="label_horizontal">2</label></center></td>
            <td class="impacto-horizontal"><center><label class="label_horizontal">3</label></center></td>
            <td class="impacto-horizontal"><center><label class="label_horizontal">4</label></center></td>
            <td class="impacto-horizontal"><center><label class="label_horizontal">5</label></center></td>
            <td class="impacto-horizontal"><center><label class="label_horizontal">6</label></center></td>
            <td class="impacto-horizontal"><center><label class="label_horizontal">7</label></center></td>                
        </tr>
        <tr style="height: 0px;">
            <td colspan="9">
                
            </td>
        </tr>
    </tbody>
    </table>
    <script>
        document.getElementById("inhe_"""+fecha+"""_label_"""+str(impacto)+"""_"""+str(probabilidad)+"""").style.display = "block";
    </script>
         """

        return matrizInherente

    def matrizResidual(self, impacto, probabilidad, fecha):
        print("la residual es ", impacto, probabilidad)
        fecha = str(fecha.year) +""+str(fecha.month)+""+str(fecha.day)
        matrizResidual = """ 
        <style>
    #res_"""+fecha+"""_1_1,#res_"""+fecha+"""_1_2,#res_"""+fecha+"""_1_3,#res_"""+fecha+"""_1_4,#res_"""+fecha+"""_1_5,#res_"""+fecha+"""_1_6,#res_"""+fecha+"""_2_1,#res_"""+fecha+"""_2_2,#res_"""+fecha+"""_2_3,#res_"""+fecha+"""_2_4,#res_"""+fecha+"""_3_1,#res_"""+fecha+"""_3_2,#res_"""+fecha+"""_3_3{
        background-color: #00B050;
    }
    #res_"""+fecha+"""_1_7,#res_"""+fecha+"""_2_5,#res_"""+fecha+"""_2_6,#res_"""+fecha+"""_3_4,#res_"""+fecha+"""_3_5,#res_"""+fecha+"""_3_4,#res_"""+fecha+"""_4_1,#res_"""+fecha+"""_4_2,#res_"""+fecha+"""_4_3,#res_"""+fecha+"""_4_4,#res_"""+fecha+"""_4_5,#res_"""+fecha+"""_5_1,#res_"""+fecha+"""_5_2,#res_"""+fecha+"""_5_3,#res_"""+fecha+"""_5_4{
        background-color: #FFFF00;
    }
    #res_"""+fecha+"""_6_1,#res_"""+fecha+"""_6_2,#res_"""+fecha+"""_6_3,#res_"""+fecha+"""_6_4,#res_"""+fecha+"""_6_5,#res_"""+fecha+"""_6_6,#res_"""+fecha+"""_6_7,#res_"""+fecha+"""_7_1,#res_"""+fecha+"""_7_2,#res_"""+fecha+"""_7_3,#res_"""+fecha+"""_7_4,#res_"""+fecha+"""_7_5,#res_"""+fecha+"""_7_6,#res_"""+fecha+"""_7_7,#res_"""+fecha+"""_5_5,#res_"""+fecha+"""_5_6,#res_"""+fecha+"""_5_7,#res_"""+fecha+"""_4_6,#res_"""+fecha+"""_4_7,#res_"""+fecha+"""_3_6,#res_"""+fecha+"""_3_7,#res_"""+fecha+"""_2_7{
        background-color: #FF0000;
    }
    .coords{
        border:1px solid #babdc1;
        width: 12.5%;
        text-align: center;
    }
    #label_impacto{
        writing-mode:tb-rl;
        -webkit-transform:rotate(-180deg);
        -moz-transform:rotate(-180deg);
        -o-transform: rotate(-180deg);
        -ms-transform:rotate(-180deg);
        transform: rotate(-180deg);
        color: black;
        font-size: 19px;
    }
    .num_prob{
        font-size: 10px !important;
    }
    .impacto-vertical{
        width: 12.5%;
        border: 1px solid transparent;
        text-align: center;
    }
    .impacto-horizontal{
        width: 12.5%;
        border: 1px solid transparent;
        text-align: center;        
    }
    .label_horizontal{
        font-size: 10px !important;
    }

    .r-circle {
        background: black;
        color: #fff;
        padding: 6% 4%;
        border-radius: 50%;
        font-size: 11px;
        display: none;
        width: 77%;
        cursor: pointer;
    }
    </style>    

    <table style="float:left;">
        <caption style="margin-left: 19%;font-size: 17px;color: black;">Riesgo Residual</caption>
        <tbody>
            <tr>
                <td rowspan="7" style="width: 1%;">
                    
                </td>
            <td style="width: 12.5%;" class="impacto-vertical"> 
                <label class="num_prob">7</label>
            </td>
            <td id="res_"""+fecha+"""_7_1" class="coords">                
                    
                    <center><span class="r-circle" id="res_"""+fecha+"""_label_7_1">R</span></center>
            </td>

            <td id="res_"""+fecha+"""_7_2" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_7_2">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_7_3" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_7_3">R</span></center>
                </div>            
            </td>
            <td id="res_"""+fecha+"""_7_4" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_7_4">R</span></center>
                </div>            
            </td>
            <td id="res_"""+fecha+"""_7_5" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_7_5">R</span></center>
                </div>            
            </td>
            <td id="res_"""+fecha+"""_7_6" class="coords">
                <div class="parent">                                                                
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_7_6">R</span></center>
                </div>            
            </td>
            <td id="res_"""+fecha+"""_7_7" class="coords">
                <div class="parent">                                                            
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_7_7">R</span></center>
                </div>
                
            </td>
        </tr>

        <tr>
            <td class="impacto-vertical">
                <center><label class="num_prob">6</label></center>
            </td>
            <td id="res_"""+fecha+"""_6_1" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_6_1">R</span></center>
                </div>            		
            </td>
            <td id="res_"""+fecha+"""_6_2" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_6_2">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_6_3" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_6_3">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_6_4" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_6_4">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_6_5" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_6_5">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_6_6" class="coords">
                <div class="parent">
                    <center>
                        <span class="r-circle"  id="res_"""+fecha+"""_label_6_6">R</span>
                    </center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_6_7" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_6_7">R</span></center>
                </div>
            </td>
        </tr>
        
        <tr>
            <td class="impacto-vertical">
                <label class="num_prob">5</label>
            </td>
            <td id="res_"""+fecha+"""_5_1" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_5_1">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_5_2" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_5_2">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_5_3" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_5_3">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_5_4" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_5_4">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_5_5" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_5_5">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_5_6" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_5_6">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_5_7" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_5_7">R</span></center>
                </div>
            </td>
        </tr>
        
        <tr>
            <td class="impacto-vertical">
                <label class="num_prob">4</label>
            </td>
            <td id="res_"""+fecha+"""_4_1" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_4_1">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_4_2" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_4_2">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_4_3" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_4_3">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_4_4" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_4_4">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_4_5" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_4_5">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_4_6" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_4_6">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_4_7" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_4_7">R</span></center>
                </div>
            </td>
        </tr>
        
        <tr>
            <td class="impacto-vertical">
                <label class="num_prob">3</label>
            </td>
            <td id="res_"""+fecha+"""_3_1" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_3_1">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_3_2" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_3_2">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_3_3" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_3_3">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_3_4" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_3_4">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_3_5" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_3_5">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_3_6" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_3_6">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_3_7" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_3_7">R</span></center>
                </div>
            </td>
        </tr>

        <tr>   
            <td class="impacto-vertical">
                <label class="num_prob">2</label>
            </td>     
            <td id="res_"""+fecha+"""_2_1" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_2_1">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_2_2" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_2_2">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_2_3" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_2_3">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_2_4" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_2_4">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_2_5" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_2_5">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_2_6" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_2_6">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_2_7" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_2_7">R</span></center>
                </div>
            </td>
        </tr>
        
        <tr>
            <td class="impacto-vertical">
                <label class="num_prob">1</label>
            </td>
            <td id="res_"""+fecha+"""_1_1" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_1_1">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_1_2" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_1_2">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_1_3" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_1_3">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_1_4" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_1_4">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_1_5" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_1_5">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_1_6" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_1_6">R</span></center>
                </div>
            </td>
            <td id="res_"""+fecha+"""_1_7" class="coords">
                <div class="parent">
                    
                    <center><span class="r-circle"  id="res_"""+fecha+"""_label_1_7">R</span></center>
                </div>
            </td>
        </tr>
        <tr style="height: 0px;">
            <td></td>
            <td></td>
            <td class="impacto-horizontal"><center><label class="label_horizontal">1</label></center></td>
            <td class="impacto-horizontal"><center><label class="label_horizontal">2</label></center></td>
            <td class="impacto-horizontal"><center><label class="label_horizontal">3</label></center></td>
            <td class="impacto-horizontal"><center><label class="label_horizontal">4</label></center></td>
            <td class="impacto-horizontal"><center><label class="label_horizontal">5</label></center></td>
            <td class="impacto-horizontal"><center><label class="label_horizontal">6</label></center></td>
            <td class="impacto-horizontal"><center><label class="label_horizontal">7</label></center></td>                
        </tr>
        <tr style="height: 0px;">
            <td colspan="9">
                
            </td>
        </tr>
    </tbody>
    </table>
    <script>
        document.getElementById("res_"""+fecha+"""_label_"""+str(impacto)+"""_"""+str(probabilidad)+"""").style.display = "block";
    </script>
         """
        return matrizResidual
    
    def matrizObjetivo(self, impacto, probabilidad, fecha):
        fecha = str(fecha.year) +""+str(fecha.month)+""+str(fecha.day)
        matrizObjetivo = """ <style>
                #obj_"""+fecha+"""_1_1,#obj_"""+fecha+"""_1_2,#obj_"""+fecha+"""_1_3,#obj_"""+fecha+"""_1_4,#obj_"""+fecha+"""_1_5,#obj_"""+fecha+"""_1_6,#obj_"""+fecha+"""_2_1,#obj_"""+fecha+"""_2_2,#obj_"""+fecha+"""_2_3,#obj_"""+fecha+"""_2_4,#obj_"""+fecha+"""_3_1,#obj_"""+fecha+"""_3_2,#obj_"""+fecha+"""_3_3{
                    background-color: #00B050;
                }
                #obj_"""+fecha+"""_1_7,#obj_"""+fecha+"""_2_5,#obj_"""+fecha+"""_2_6,#obj_"""+fecha+"""_3_4,#obj_"""+fecha+"""_3_5,#obj_"""+fecha+"""_3_4,#obj_"""+fecha+"""_4_1,#obj_"""+fecha+"""_4_2,#obj_"""+fecha+"""_4_3,#obj_"""+fecha+"""_4_4,#obj_"""+fecha+"""_4_5,#obj_"""+fecha+"""_5_1,#obj_"""+fecha+"""_5_2,#obj_"""+fecha+"""_5_3,#obj_"""+fecha+"""_5_4{
                    background-color: #FFFF00;
                }
                #obj_"""+fecha+"""_6_1,#obj_"""+fecha+"""_6_2,#obj_"""+fecha+"""_6_3,#obj_"""+fecha+"""_6_4,#obj_"""+fecha+"""_6_5,#obj_"""+fecha+"""_6_6,#obj_"""+fecha+"""_6_7,#obj_"""+fecha+"""_7_1,#obj_"""+fecha+"""_7_2,#obj_"""+fecha+"""_7_3,#obj_"""+fecha+"""_7_4,#obj_"""+fecha+"""_7_5,#obj_"""+fecha+"""_7_6,#obj_"""+fecha+"""_7_7,#obj_"""+fecha+"""_5_5,#obj_"""+fecha+"""_5_6,#obj_"""+fecha+"""_5_7,#obj_"""+fecha+"""_4_6,#obj_"""+fecha+"""_4_7,#obj_"""+fecha+"""_3_6,#obj_"""+fecha+"""_3_7,#obj_"""+fecha+"""_2_7{
                    background-color: #FF0000;
                }
                .coords{
                    border:1px solid #babdc1;
                    width: 12.5%;
                    text-align: center;
                }

                .num_prob{
                    font-size: 10px !important;
                }
                .impacto-vertical{
                    width: 12.5%;
                    border: 1px solid transparent;
                    text-align: center;
                }
  
                .label_horizontal{
                    font-size: 10px !important;
                }

                .r-circle {
                    background: black;
                    color: #fff;
                    padding: 6% 4%;
                    border-radius: 50%;
                    font-size: 11px;
                    display: none;
                    width: 77%;
                    cursor: pointer;
                }
                </style>    
            
                <table style="float:left;">
                    <caption style="margin-left: 19%;font-size: 17px;color: black;">Riesgo Objetivo</caption>
                    <tbody>
                        <tr>
                            <td rowspan="7" style="width: 1%;">
                                
                            </td>
                        <td style="width: 12.5%;" class="impacto-vertical"> 
                            <label class="num_prob">7</label>
                        </td>
                        <td id="obj_"""+fecha+"""_7_1" class="coords">                
                                
                                <center><span class="r-circle" id="obj_"""+fecha+"""_label_7_1">R</span></center>
                        </td>

                        <td id="obj_"""+fecha+"""_7_2" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_7_2">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_7_3" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_7_3">R</span></center>
                            </div>            
                        </td>
                        <td id="obj_"""+fecha+"""_7_4" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_7_4">R</span></center>
                            </div>            
                        </td>
                        <td id="obj_"""+fecha+"""_7_5" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_7_5">R</span></center>
                            </div>            
                        </td>
                        <td id="obj_"""+fecha+"""_7_6" class="coords">
                            <div class="parent">                                                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_7_6">R</span></center>
                            </div>            
                        </td>
                        <td id="obj_"""+fecha+"""_7_7" class="coords">
                            <div class="parent">                                                            
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_7_7">R</span></center>
                            </div>
                            
                        </td>
                    </tr>

                    <tr>
                        <td class="impacto-vertical">
                            <center><label class="num_prob">6</label></center>
                        </td>
                        <td id="obj_"""+fecha+"""_6_1" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_6_1">R</span></center>
                            </div>            		
                        </td>
                        <td id="obj_"""+fecha+"""_6_2" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_6_2">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_6_3" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_6_3">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_6_4" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_6_4">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_6_5" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_6_5">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_6_6" class="coords">
                            <div class="parent">
                                <center>
                                    <span class="r-circle"  id="obj_"""+fecha+"""_label_6_6">R</span>
                                </center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_6_7" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_6_7">R</span></center>
                            </div>
                        </td>
                    </tr>
                    
                    <tr>
                        <td class="impacto-vertical">
                            <label class="num_prob">5</label>
                        </td>
                        <td id="obj_"""+fecha+"""_5_1" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_5_1">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_5_2" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_5_2">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_5_3" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_5_3">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_5_4" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_5_4">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_5_5" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_5_5">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_5_6" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_5_6">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_5_7" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_5_7">R</span></center>
                            </div>
                        </td>
                    </tr>
                    
                    <tr>
                        <td class="impacto-vertical">
                            <label class="num_prob">4</label>
                        </td>
                        <td id="obj_"""+fecha+"""_4_1" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_4_1">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_4_2" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_4_2">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_4_3" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_4_3">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_4_4" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_4_4">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_4_5" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_4_5">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_4_6" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_4_6">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_4_7" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_4_7">R</span></center>
                            </div>
                        </td>
                    </tr>
                    
                    <tr>
                        <td class="impacto-vertical">
                            <label class="num_prob">3</label>
                        </td>
                        <td id="obj_"""+fecha+"""_3_1" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_3_1">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_3_2" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_3_2">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_3_3" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_3_3">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_3_4" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_3_4">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_3_5" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_3_5">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_3_6" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_3_6">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_3_7" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_3_7">R</span></center>
                            </div>
                        </td>
                    </tr>

                    <tr>   
                        <td class="impacto-vertical">
                            <label class="num_prob">2</label>
                        </td>     
                        <td id="obj_"""+fecha+"""_2_1" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_2_1">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_2_2" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_2_2">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_2_3" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_2_3">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_2_4" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_2_4">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_2_5" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_2_5">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_2_6" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_2_6">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_2_7" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_2_7">R</span></center>
                            </div>
                        </td>
                    </tr>
                    
                    <tr>
                        <td class="impacto-vertical">
                            <label class="num_prob">1</label>
                        </td>
                        <td id="obj_"""+fecha+"""_1_1" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_1_1">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_1_2" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_1_2">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_1_3" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_1_3">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_1_4" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_1_4">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_1_5" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_1_5">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_1_6" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_1_6">R</span></center>
                            </div>
                        </td>
                        <td id="obj_"""+fecha+"""_1_7" class="coords">
                            <div class="parent">
                                
                                <center><span class="r-circle"  id="obj_"""+fecha+"""_label_1_7">R</span></center>
                            </div>
                        </td>
                    </tr>
                    <tr style="height: 0px;">
                        <td></td>
                        <td></td>
                        <td class="impacto-horizontal"><center><label class="label_horizontal">1</label></center></td>
                        <td class="impacto-horizontal"><center><label class="label_horizontal">2</label></center></td>
                        <td class="impacto-horizontal"><center><label class="label_horizontal">3</label></center></td>
                        <td class="impacto-horizontal"><center><label class="label_horizontal">4</label></center></td>
                        <td class="impacto-horizontal"><center><label class="label_horizontal">5</label></center></td>
                        <td class="impacto-horizontal"><center><label class="label_horizontal">6</label></center></td>
                        <td class="impacto-horizontal"><center><label class="label_horizontal">7</label></center></td>                
                    </tr>
                    <tr style="height: 0px;">
                        <td colspan="9">
                            
                        </td>
                    </tr>
                </tbody>
                </table>
                <script>
                    document.getElementById("obj_"""+fecha+"""_label_"""+str(impacto)+"""_"""+str(probabilidad)+"""").style.display = "block";
                </script> """

        return matrizObjetivo

