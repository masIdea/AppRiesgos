#from core.utils import image_as_base64
from django.conf import settings
import pdfkit
import os.path

class ReportePDF():
    def __init__(self, html, nombre_reporte):
        self.html = html
        self.nombre_reporte = nombre_reporte

    def generaPDF(self):
        #config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
        config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
        
        pdfkit.from_string(self.html, settings.MEDIA_ROOT + '/informes/ '+self.nombre_reporte+'.pdf', configuration=config)
        archivo_creado = settings.MEDIA_ROOT + '/informes/ '+self.nombre_reporte+'.pdf'
        print(archivo_creado)


        if os.path.isfile(archivo_creado):
            return self.nombre_reporte
