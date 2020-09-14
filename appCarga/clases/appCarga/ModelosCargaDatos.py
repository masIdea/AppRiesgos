class ModelosCargaDatos():
    def __init__(self, tipo_archivo):
        self.tipo_archivo = tipo_archivo
    
    def datosColumnasArchivo(self):
        datos = dict()
        datos = {
            'ArchivoCargaSistemaCIO':{
                'arreglo_listas': [
                     {'columna_xlsx':'L1', 'modelo':'RiesgoListas', 'columna':'AreaDeEvento', 'tipo':'AreaDeEvento', 'columna_lista':'A'}
                    ,{'columna_xlsx':'M1', 'modelo':'RiesgoListas', 'columna':'SuperIntendenciaEvento', 'tipo':'SuperIntendenciaEvento', 'columna_lista':'B'}
                    ,{'columna_xlsx':'N1', 'modelo':'RiesgoListas', 'columna':'Proyecto', 'tipo':'Proyecto', 'columna_lista':'C'}

                    ,{'columna_xlsx':'O1', 'modelo':'RiesgoRbsfamilia', 'columna':'Familia', 'tipo':'Familia', 'columna_lista':'D'}
                    ,{'columna_xlsx':'P1', 'modelo':'RiesgoRbsfamilia', 'columna':'SubProceso', 'tipo':'SubProceso', 'columna_lista':'E'}
                    ,{'columna_xlsx':'Q1', 'modelo':'RiesgoListas', 'columna':'Clasificacion', 'tipo':'Clasificaciones', 'columna_lista':'F'}
                    
                    ,{'columna_xlsx':'R1', 'modelo':'RiesgoListas', 'columna':'ControlesQueNoFuncionaron', 'tipo':'ControlesQueNoFuncionaron', 'columna_lista':'G'}
                    ,{'columna_xlsx':'S1', 'modelo':'RiesgoListas', 'columna':'TipoFalla', 'tipo':'TipoFalla', 'columna_lista':'H'}
                    ],
                'arreglo_columnas': [
                         {'columna_xlsx':'A1', 'columna':'IdCosto'}
                        
                        ,{'columna_xlsx':'C1', 'columna':'Gerencia'}
                        ,{'columna_xlsx':'D1', 'columna':'SuperIntendencia'}
                        ,{'columna_xlsx':'E1', 'columna':'UnidadOperacional'}
                        ,{'columna_xlsx':'F1', 'columna':'TipoObjeto'}
                        ,{'columna_xlsx':'G1', 'columna':'Evento'}
                        ,{'columna_xlsx':'H1', 'columna':'NivelImpacto'}
                        ,{'columna_xlsx':'I1', 'columna':'Comentarios'}
                        ,{'columna_xlsx':'J1', 'columna':'CantidadDiasDetencion'}
                        ,{'columna_xlsx':'K1', 'columna':'CantidadTMFPerdidas'}
                        ,{'columna_xlsx':'T1', 'columna':'MontoDePerdida'}
                        ,{'columna_xlsx':'U1', 'columna':'RepeticionDelEvento'}
                        ,{'columna_xlsx':'V1', 'columna':'Estadistica'}
                    ],
                'arreglo_fechas': [
                        {'columna_xlsx':'B1', 'columna':'Fecha', 'letra_columna':'B'}

                ]
            },
            'N1':{
                'arreglo_listas': [
                     {'columna_xlsx':'X1', 'modelo':'RiesgoListas', 'columna':'AreaDeEvento', 'tipo':'AreaDeEvento', 'columna_lista':'A'}
                    ,{'columna_xlsx':'Y1', 'modelo':'RiesgoListas', 'columna':'SuperIntendenciaEvento', 'tipo':'SuperIntendenciaEvento', 'columna_lista':'B'}
                    ,{'columna_xlsx':'Z1', 'modelo':'RiesgoListas', 'columna':'Proyecto', 'tipo':'Proyecto', 'columna_lista':'C'}

                    
                    ,{'columna_xlsx':'AA1', 'modelo':'RiesgoRbsfamilia', 'columna':'Familia', 'tipo':'Familia', 'columna_lista':'D'}
                    ,{'columna_xlsx':'AB1', 'modelo':'RiesgoRbsfamilia', 'columna':'SubProceso', 'tipo':'SubProceso', 'columna_lista':'E'}
                    ,{'columna_xlsx':'AE1', 'modelo':'RiesgoListas', 'columna':'Clasificacion', 'tipo':'Clasificaciones', 'columna_lista':'F'}
                    
                    
                    ,{'columna_xlsx':'AF1', 'modelo':'RiesgoListas', 'columna':'ControlesQueNoFuncionaron', 'tipo':'ControlesQueNoFuncionaron', 'columna_lista':'H'}
                    ,{'columna_xlsx':'AG1', 'modelo':'RiesgoListas', 'columna':'TipoFalla', 'tipo':'TipoFalla', 'columna_lista':'I'}
                    ],
                'arreglo_columnas': [
                         {'columna_xlsx':'A1', 'columna':'CodigoRSSO'}
                        ,{'columna_xlsx':'B1', 'columna':'TipoRSSO'}
                        ,{'columna_xlsx':'C1', 'columna':'Estado'}
                        ,{'columna_xlsx':'D1', 'columna':'Causal'}
                        ,{'columna_xlsx':'E1', 'columna':'NivelRSSO'}
                        ,{'columna_xlsx':'F1', 'columna':'FechaCreacion'}
                        ,{'columna_xlsx':'G1', 'columna':'FechaHallazgo'}
                        ,{'columna_xlsx':'H1', 'columna':'Division'}
                        ,{'columna_xlsx':'I1', 'columna':'Gerencia'}
                        ,{'columna_xlsx':'J1', 'columna':'Superintendencia'}
                        ,{'columna_xlsx':'K1', 'columna':'Area'}
                        ,{'columna_xlsx':'L1', 'columna':'SAPInformante'}
                        ,{'columna_xlsx':'M1', 'columna':'Informante'}
                        ,{'columna_xlsx':'N1', 'columna':'SAPResponsable'}
                        ,{'columna_xlsx':'O1', 'columna':'Responsable'}
                        
                        ,{'columna_xlsx':'Q1', 'columna':'DescripcionIncidente'}
                        ,{'columna_xlsx':'R1', 'columna':'AccionRealizada'}
                        ,{'columna_xlsx':'S1', 'columna':'Estandar'}
                        ,{'columna_xlsx':'T1', 'columna':'RiesgoCritico'}
                        ,{'columna_xlsx':'U1', 'columna':'IdEvento'}
                        ,{'columna_xlsx':'V1', 'columna':'CantidadDiasDetencion'}
                        ,{'columna_xlsx':'W1', 'columna':'CantidadTMFPerdidas'}
                        ,{'columna_xlsx':'AC1', 'columna':'MontoDePerdida'}
                        ,{'columna_xlsx':'AD1', 'columna':'RepeticionDelEvento'}
                        ,{'columna_xlsx':'AH1', 'columna':'Estadistica'}
                    ],
                    'arreglo_fechas': [
                         {'columna_xlsx':'P1', 'columna':'FechaCierre', 'letra_columna':'P'}

                    ]
            },
            'Unifica':{
                'arreglo_listas': [
                    {'columna_xlsx':'B1', 'modelo':'Gerencias', 'columna':'Gerencia', 'tipo':'Gerencias', 'columna_lista':'A'}
                    ,{'columna_xlsx':'C1', 'modelo':'Direcciones', 'columna':'SuperIntendencia', 'tipo':'Direcciones', 'columna_lista':'B'}


                    ,{'columna_xlsx':'E1', 'modelo':'RiesgoListas', 'columna':'Area', 'tipo':'area', 'columna_lista':'C'}

                    ,{'columna_xlsx':'S1', 'modelo':'RiesgoRbsfamilia', 'columna':'Familia', 'tipo':'Familia', 'columna_lista':'D'}
                    ,{'columna_xlsx':'T1', 'modelo':'RiesgoRbsfamilia', 'columna':'SubProceso', 'tipo':'SubProceso', 'columna_lista':'E'}
                    ,{'columna_xlsx':'U1', 'modelo':'RiesgoListas', 'columna':'Clasificacion', 'tipo':'Clasificaciones', 'columna_lista':'F'}
                    ,{'columna_xlsx':'V1', 'modelo':'RiesgoListas', 'columna':'TipoFalla', 'tipo':'TipoFalla', 'columna_lista':'G'}                                                                       
                    ],
                'arreglo_columnas': [                         
                         {'columna_xlsx':'D1', 'columna':'UnidadOperacional'}
                        ,{'columna_xlsx':'F1', 'columna':'Sector'}
                        ,{'columna_xlsx':'G1', 'columna':'Lugar'}
                        ,{'columna_xlsx':'H1', 'columna':'TipoObjeto'}
                        ,{'columna_xlsx':'I1', 'columna':'Evento'}
                        ,{'columna_xlsx':'J1', 'columna':'NivelImpacto'}
                        ,{'columna_xlsx':'K1', 'columna':'Comentarios'}
                        ,{'columna_xlsx':'L1', 'columna':'QHorasDetencion'}
                        ,{'columna_xlsx':'M1', 'columna':'QDiasDetencion'}
                        ,{'columna_xlsx':'N1', 'columna':'QKtsPerdida'}
                        ,{'columna_xlsx':'O1', 'columna':'QTMFperdida'}
                        ,{'columna_xlsx':'P1', 'columna':'QLibrasPerdida'}
                        ,{'columna_xlsx':'Q1', 'columna':'MontoPerdidaKUSD'}
                        ,{'columna_xlsx':'R1', 'columna':'IdRiesgoAsociado'}

                    ],
                    'arreglo_fechas': [
                         {'columna_xlsx':'A1', 'columna':'Fecha', 'letra_columna':'A'}

                    ]
            },  
        }
        
        
        return datos[self.tipo_archivo]


