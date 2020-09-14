import xlsxwriter
from core.models import RiesgoListas, RiesgoRbsfamilia, Gerencias, Direcciones
from datetime import datetime

class XlsxWriterObj():
    def __init__(self, columns, list_columns, header, body, styles, workbook, dateColumns):
        self.columns = columns
        self.header = header
        self.body = body
        self.styles = styles
        self.workbook = workbook
        self.list_columns = list_columns        
        self.worksheet = self.workbook.add_worksheet("Tabla")
        self.worksheet2 = self.workbook.add_worksheet("Datos")
        self.dateColumns = dateColumns

    def headerFormat(self):
        header_format = self.workbook.add_format({
            'border': 1,
            'bg_color': '#C6EFCE',
            'bold': True,        
            'valign': 'vcenter',
            'indent': 1,
        })
        return header_format
        
    def headerBookLists(self):
        for lista in self.list_columns:
            columna_xlsx = lista['columna_xlsx']
            modelo = lista['modelo']
            columna = lista['columna']
            tipo = lista['tipo']
            if tipo == "Familia":
                datos_lista = list(eval(modelo).objects.values('familia').distinct())
                arreglo_datos = []            
                for dato in datos_lista:                    
                    arreglo_datos.append(dato['familia'])                
                hasta = self.createLists(arreglo_datos, lista['columna_lista'])                
                self.worksheet.data_validation(columna_xlsx+':'+columna_xlsx+'5000', {'validate': 'list','source': '=Datos!$'+lista['columna_lista']+'$1:$'+lista['columna_lista']+'$'+str(hasta)+'',})
            elif tipo == "SubProceso":
                print("es un subproceso")
                datos_lista = list(eval(modelo).objects.values('subproceso').distinct())
                arreglo_datos = []            
                for dato in datos_lista:                    
                    arreglo_datos.append(dato['subproceso'])
                hasta = self.createLists(arreglo_datos, lista['columna_lista'])                
                self.worksheet.data_validation(columna_xlsx+':'+columna_xlsx+'5000', {'validate': 'list','source': '=Datos!$'+lista['columna_lista']+'$1:$'+lista['columna_lista']+'$'+str(hasta)+'',}) 
            elif tipo == "Gerencias":                
                datos_lista = list(eval(modelo).objects.values('sigla').distinct())
                arreglo_datos = []            
                for dato in datos_lista:                    
                    arreglo_datos.append(dato['sigla'])
                hasta = self.createLists(arreglo_datos, lista['columna_lista'])                
                self.worksheet.data_validation(columna_xlsx+':'+columna_xlsx+'5000', {'validate': 'list','source': '=Datos!$'+lista['columna_lista']+'$1:$'+lista['columna_lista']+'$'+str(hasta)+'',}) 
            elif tipo == "Direcciones":                
                datos_lista = list(eval(modelo).objects.values('sigla').distinct())
                arreglo_datos = []            
                for dato in datos_lista:                    
                    arreglo_datos.append(dato['sigla'])
                hasta = self.createLists(arreglo_datos, lista['columna_lista'])                
                self.worksheet.data_validation(columna_xlsx+':'+columna_xlsx+'5000', {'validate': 'list','source': '=Datos!$'+lista['columna_lista']+'$1:$'+lista['columna_lista']+'$'+str(hasta)+'',})                
            else:
                datos_lista = list(eval(modelo).objects.filter(estado = "ACTIVO", tipo=tipo).order_by('orden').values())
                arreglo_datos = []            
                for dato in datos_lista:
                    arreglo_datos.append(dato['glosa'])            
                hasta = self.createLists(arreglo_datos, lista['columna_lista'])                
                self.worksheet.data_validation(columna_xlsx+':'+columna_xlsx+'5000', {'validate': 'list','source': '=Datos!$'+lista['columna_lista']+'$1:$'+lista['columna_lista']+'$'+str(hasta)+'',})
            self.worksheet.write(columna_xlsx, columna, self.headerFormat())
            
               

    def headerColumns(self):
        for columna in self.columns:
            self.worksheet.write(columna['columna_xlsx'], columna['columna'], self.headerFormat())
    
    def headerColumnsDateFormat(self):
     
        #print(self.worksheet.write_datetime("W1", 'Fecha_prueba',None, None))
        date_time = datetime.strptime(str(datetime.now().day)+'-'+str(datetime.now().month)+'-'+str(datetime.now().year), '%d-%m-%Y')
        date_format = self.workbook.add_format({'num_format': 'dd/mm/yy'})        
        for columna in self.dateColumns:                        
            self.worksheet.write(columna['columna_xlsx'], columna['columna'], self.headerFormat())
            self.worksheet.write_datetime(columna['letra_columna']+'2:'+columna['letra_columna']+'5000', date_time, date_format)

    
    def createLists(self, datos, columna):
        contador = 1
        for dato in datos:
            self.worksheet2.write(columna+str(contador), dato)
            contador+=1        
        return contador

    def closeBook(self):
        self.headerColumns()
        self.headerBookLists()
        self.headerColumnsDateFormat()
        #self.workbook.close()
                
            
