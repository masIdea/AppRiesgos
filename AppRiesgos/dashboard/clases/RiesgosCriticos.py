from core.models import *
from collections import OrderedDict
import operator
from django.db.models import Sum

class RiesgosCriticos():
    def __init__(self, tipo=None, nivel=None, tipo_nivel=None, tb_riesgos=None):
        self.tipo = tipo
        self.nivel = nivel
        self.tipo_nivel = tipo_nivel
        self.tb_riesgos = tb_riesgos

    def getRiesgosCriticosTabla(self):
        datos = ""     
        datos = self.getDatosRiesgosCriticos()          
        return datos
    
    def getCausasRiesgos(self):
        tipo = self.tipo_nivel
        if tipo == "DET":
            gerencias = list(Gerencias.objects.all().values())
        else:
            gerencias = list(Gerencias.objects.filter(sigla=tipo).values())
        if self.tipo == "riesgos":
            return self.getRiesgosCriticos(gerencias)
        elif self.tipo == "eventos":
            return self.getCausasEventos(gerencias)
        elif self.tipo == "directic":
            return self.getCausasRiesgosDirectic(gerencias)

    def getRiesgosPorDirSup(self):
        tipo = self.tipo_nivel
        if tipo == "DET":
            gerencias = list(Gerencias.objects.all().values())
        else:
            gerencias = list(Gerencias.objects.filter(sigla=tipo).values())
        if self.tipo == "riesgos":
            return self.getRiesgosCriticosDireccion(gerencias)
        elif self.tipo == "eventos":
            return self.getEventosDireccion(gerencias)
        elif self.tipo == "directic":
            return self.getRiesgosCriticosDireccionDirectic(gerencias)
    
    def getRiesgosValorizadosDirSup(self):
        tipo = self.tipo_nivel
        if tipo == "DET":
            gerencias = list(Gerencias.objects.all().values())
        else:
            gerencias = list(Gerencias.objects.filter(sigla=tipo).values())
        if self.tipo == "riesgos":
            return self.getRiesgosValorizadosDireccion(gerencias)
        elif self.tipo == "eventos":
            return self.getEventosValorizadosDireccion(gerencias)
        elif self.tipo == "directic":
            return self.getRiesgosValorizadosDireccionDirectic(gerencias)

    
    def getDatosRiesgosCriticos(self):
        gerencias = list(Gerencias.objects.all().values())
        dict_criticos = {}
        dict_arreglo_ids_criticos = {}
        probabilidad = ""
        impacto = ""
        color = ""
        for gerencia in gerencias:
            rojos = 0
            riesgos_gerencia = list(Riesgo.objects.filter(gerencia=gerencia['sigla']).values())
            arreglo_ids_riesgos_criticos = []
                        
            for riesgo in riesgos_gerencia:
                nombre_color = ''
                if RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).exists():
                    resultado_inherente_riesgo = list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).values('probabilidadresidual', 'impactoresidual'))
                    probabilidad = resultado_inherente_riesgo[0]['probabilidadresidual']
                    impacto = resultado_inherente_riesgo[0]['impactoresidual']
                    color = list(RiesgoProbImp.objects.filter(probabilidad=probabilidad, impacto=impacto).values('color_hex', 'color'))                
                    
                    if len(color) > 0:
                        nombre_color = color[0]['color']                    
                    if nombre_color == 'rojo':
                        arreglo_ids_riesgos_criticos.append(riesgo['idriesgo'])
                        rojos+=1

            dict_criticos[gerencia['gerencia']] = rojos            
            dict_arreglo_ids_criticos[gerencia['gerencia']] = arreglo_ids_riesgos_criticos

        gerencias_ordenadas = sorted(dict_criticos.items(), key=operator.itemgetter(1), reverse=True)
        diccionario_ordenado = OrderedDict()
        
        for key, value in gerencias_ordenadas:
            valor_perdida_total = Riesgo.objects.all().aggregate(Sum('maximaperdidamus'))
            monto_perdida_critica = Riesgo.objects.filter(idriesgo__in=dict_arreglo_ids_criticos[key]).aggregate(Sum('maximaperdidamus'))
            cantidad_riesgos_gerencia = len(list(Riesgo.objects.filter(gerencia=key).values()))
            cantidad_total_riesgos = len(list(Riesgo.objects.all().values()))                        
            porc_riesgos_criticos = 0
            if cantidad_riesgos_gerencia > 0:
                porc_riesgos_criticos = round(((cantidad_riesgos_gerencia / cantidad_total_riesgos)*100) ,1)
            porcentaje_mus_perdida = 0
            if valor_perdida_total['maximaperdidamus__sum'] > 0 and monto_perdida_critica['maximaperdidamus__sum'] is not None:
                porcentaje_mus_perdida = round(((monto_perdida_critica['maximaperdidamus__sum']/valor_perdida_total['maximaperdidamus__sum'])*100), 1)
            diccionario_ordenado[key] = {
                'cantidad_riesgos_gerencia':cantidad_riesgos_gerencia,
                'cantidad_riesgos_criticos':value,
                'porc_riesgos_criticos':porc_riesgos_criticos,
                'monto_perdida_critica':monto_perdida_critica['maximaperdidamus__sum'],
                'porcentaje_mus_perdida':porcentaje_mus_perdida,
            }        
        return diccionario_ordenado
    
    def getRiesgosCriticos(self, gerencias):        
        dict_criticos = {}
        arreglo_ids_riesgos_criticos = []
        probabilidad = ""
        impacto = ""
        color = ""
        for gerencia in gerencias:
            rojos = 0
            riesgos_gerencia = list(Riesgo.objects.filter(gerencia=gerencia['sigla']).values())            
                        
            for riesgo in riesgos_gerencia:
                nombre_color = ''                
                if RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).exists():
                    resultado_inherente_riesgo = list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).values('probabilidadresidual', 'impactoresidual'))
                    probabilidad = resultado_inherente_riesgo[0]['probabilidadresidual']
                    impacto = resultado_inherente_riesgo[0]['impactoresidual']
                    color = list(RiesgoProbImp.objects.filter(probabilidad=probabilidad, impacto=impacto).values('color_hex', 'color'))                
                if len(color) > 0:
                    nombre_color = color[0]['color']                    
                if nombre_color == 'rojo':
                    arreglo_ids_riesgos_criticos.append(riesgo['idriesgo'])
                    rojos+=1
            dict_criticos[gerencia['gerencia']] = rojos
        
        id_causas = list(RiesgoNCausariesgo.objects.filter(idriesgo__in=arreglo_ids_riesgos_criticos).values_list("idcausa", flat=True))
        
        dict_causas_riesgos_criticos = {}
        for causa in id_causas:            
            causa_descripcion = list(RiesgoCausas.objects.filter(idcausa=causa).values("causa"))
            causa_descripcion = causa_descripcion[0]["causa"] + '&&' + causa
            
            if causa_descripcion in dict_causas_riesgos_criticos:
                dict_causas_riesgos_criticos[causa_descripcion] += 1
            else:
                dict_causas_riesgos_criticos[causa_descripcion] = 1
        
        causas_ordenadas = sorted(dict_causas_riesgos_criticos.items(), key=operator.itemgetter(1), reverse=True)
        i_causas = 0
        arreglo_colores = ['#0abb87', '#fd397a', '#ffb822', '#5d78ff', '#36a3f7 ', 'red']
        diccionario_causas_ordenadas = OrderedDict()
        for causa in causas_ordenadas:
            if i_causas < 5:
                id_causa = causa[0].split("&&")[1]
                ids_riesgos = list(RiesgoNCausariesgo.objects.filter(idcausa=id_causa, idriesgo__in=arreglo_ids_riesgos_criticos).values_list('idriesgo', flat=True))
                valores = Riesgo.objects.filter(idriesgo__in=ids_riesgos).aggregate(Sum('maximaperdidamus'))
                
                diccionario_causas_ordenadas[causa[0].split("&&")[0]] = {
                    'cantidad': causa[1],
                    'valor':float(valores['maximaperdidamus__sum'])*100,
                    'color':arreglo_colores[i_causas]
                }
            i_causas += 1   
        
        return diccionario_causas_ordenadas

    def getCausasRiesgosDirectic(self, gerencias):        
        dict_criticos = {}
        arreglo_ids_riesgos_criticos = []
        probabilidad = ""
        impacto = ""
        color = ""        
        for gerencia in gerencias:
            rojos = 0
            riesgos_gerencia = list(Riesgo.objects.filter(gerencia=gerencia['sigla'], directic=1).values())                                       
            for riesgo in riesgos_gerencia:                
                nombre_color = ''                
                if RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).exists():                    
                    resultado_inherente_riesgo = list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).values('probabilidadresidual', 'impactoresidual'))
                    probabilidad = resultado_inherente_riesgo[0]['probabilidadresidual']
                    impacto = resultado_inherente_riesgo[0]['impactoresidual']
                    color = list(RiesgoProbImp.objects.filter(probabilidad=probabilidad, impacto=impacto).values('color_hex', 'color'))                
                if len(color) > 0:
                    nombre_color = color[0]['color']                    
                if nombre_color == 'rojo':
                    arreglo_ids_riesgos_criticos.append(riesgo['idriesgo'])
                    rojos+=1
            dict_criticos[gerencia['gerencia']] = rojos
        
        id_causas = list(RiesgoNCausariesgo.objects.filter(idriesgo__in=arreglo_ids_riesgos_criticos).values_list("idcausa", flat=True))        
        dict_causas_riesgos_criticos = {}
        for causa in id_causas:            
            causa_descripcion = list(RiesgoCausas.objects.filter(idcausa=causa).values("causa"))
            causa_descripcion = causa_descripcion[0]["causa"] + '&&' + causa
            
            if causa_descripcion in dict_causas_riesgos_criticos:
                dict_causas_riesgos_criticos[causa_descripcion] += 1
            else:
                dict_causas_riesgos_criticos[causa_descripcion] = 1
        
        causas_ordenadas = sorted(dict_causas_riesgos_criticos.items(), key=operator.itemgetter(1), reverse=True)
        i_causas = 0
        arreglo_colores = ['#0abb87', '#fd397a', '#ffb822', '#5d78ff', '#36a3f7 ', 'red']
        diccionario_causas_ordenadas = OrderedDict()
        for causa in causas_ordenadas:
            if i_causas < 5:
                id_causa = causa[0].split("&&")[1]
                ids_riesgos = list(RiesgoNCausariesgo.objects.filter(idcausa=id_causa, idriesgo__in=arreglo_ids_riesgos_criticos).values_list('idriesgo', flat=True))
                valores = Riesgo.objects.filter(idriesgo__in=ids_riesgos, directic=1).aggregate(Sum('maximaperdidamus'))
                
                diccionario_causas_ordenadas[causa[0].split("&&")[0]] = {
                    'cantidad': causa[1],
                    'valor':float(valores['maximaperdidamus__sum'])*100,
                    'color':arreglo_colores[i_causas]
                }
            i_causas += 1   
        
        return diccionario_causas_ordenadas
    

    def getCausasEventos(self, gerencias):
        arreglo_colores = ['#0abb87', '#fd397a', '#ffb822', '#5d78ff', '#36a3f7 ', 'red']
        id_riesgos_asociados = []
        for gerencia in gerencias:            
            riesgos_gerencia = list(RiesgoUnifica.objects.filter(gerencia=gerencia['sigla']).values())            
            for riesgo in riesgos_gerencia:
                id_riesgos_asociados.append(riesgo['idriesgoasociado'])

        id_causas = list(RiesgoNCausariesgo.objects.filter(idriesgo__in=id_riesgos_asociados).values_list("idcausa", flat=True))
        dict_causas_riesgos_criticos = {}
        for causa in id_causas:            
            causa_descripcion = list(RiesgoCausas.objects.filter(idcausa=causa).values("causa"))
            causa_descripcion = causa_descripcion[0]["causa"] + '&&' + causa
            
            if causa_descripcion in dict_causas_riesgos_criticos:
                dict_causas_riesgos_criticos[causa_descripcion] += 1
            else:
                dict_causas_riesgos_criticos[causa_descripcion] = 1
        causas_ordenadas = sorted(dict_causas_riesgos_criticos.items(), key=operator.itemgetter(1), reverse=True)

        i_causas = 0
        diccionario_causas_ordenadas = OrderedDict()
        for causa in causas_ordenadas:
            if i_causas < 5:
                id_causa = causa[0].split("&&")[1]
                ids_riesgos = list(RiesgoNCausariesgo.objects.filter(idcausa=id_causa, idriesgo__in=id_riesgos_asociados).values_list('idriesgo', flat=True))
                valores = RiesgoUnifica.objects.filter(idriesgoasociado__in=ids_riesgos).aggregate(Sum('montoperdidakusd'))
                
                diccionario_causas_ordenadas[causa[0].split("&&")[0]] = {
                    'cantidad': causa[1],
                    'valor':float(valores['maximaperdidamus__sum']),
                    'color':arreglo_colores[i_causas]
                }
            i_causas += 1   
        
        return diccionario_causas_ordenadas
        
    def getRiesgosCriticosDireccion(self, gerencias):
        arreglo_ids_riesgos_criticos = []
        dict_direcciones_criticos = {}
        probabilidad = ""
        impacto = ""
        color = ""
        for gerencia in gerencias:
            rojos = 0
            riesgos_gerencia = list(Riesgo.objects.filter(gerencia=gerencia['sigla']).values())            
                        
            for riesgo in riesgos_gerencia:                
                nombre_color = ''
                if RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).exists():
                    resultado_inherente_riesgo = list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).values('probabilidadresidual', 'impactoresidual'))
                    probabilidad = resultado_inherente_riesgo[0]['probabilidadresidual']
                    impacto = resultado_inherente_riesgo[0]['impactoresidual']
                    color = list(RiesgoProbImp.objects.filter(probabilidad=probabilidad, impacto=impacto).values('color_hex', 'color'))                
                    
                if len(color) > 0:
                    nombre_color = color[0]['color']                    
                if nombre_color == 'rojo':
                    arreglo_ids_riesgos_criticos.append(riesgo['idriesgo'])
                    if riesgo['direccion'] != '-' and riesgo['direccion'] is not None:                        
                        if riesgo['direccion'] in dict_direcciones_criticos:
                            dict_direcciones_criticos[riesgo['direccion']] += 1
                        else:
                            dict_direcciones_criticos[riesgo['direccion']] = 1
                    rojos+=1
        
        riesgos_direcciones_ordenados = sorted(dict_direcciones_criticos.items(), key=operator.itemgetter(1), reverse=True)
        riesgos_ordenados = OrderedDict()
        arreglo_colores = ['#0abb87', '#fd397a', '#ffb822', '#5d78ff', '#36a3f7 ', 'red']
        i_riesgos_direccion = 0
        for riesgo_direccion in riesgos_direcciones_ordenados:
            if i_riesgos_direccion <5:
                riesgos_ordenados[riesgo_direccion[0]] = {'cantidad': riesgo_direccion[1], 'color':arreglo_colores[i_riesgos_direccion]}
            i_riesgos_direccion += 1  

        return riesgos_ordenados

    def getRiesgosCriticosDireccionDirectic(self, gerencias):
        arreglo_ids_riesgos_criticos = []
        dict_direcciones_criticos = {}
        probabilidad = ""
        impacto = ""
        color = ""
        for gerencia in gerencias:
            rojos = 0
            riesgos_gerencia = list(Riesgo.objects.filter(gerencia=gerencia['sigla'], directic=1).values())            
                        
            for riesgo in riesgos_gerencia:                
                nombre_color = ''
                if RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).exists():
                    resultado_inherente_riesgo = list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).values('probabilidadresidual', 'impactoresidual'))
                    probabilidad = resultado_inherente_riesgo[0]['probabilidadresidual']
                    impacto = resultado_inherente_riesgo[0]['impactoresidual']
                    color = list(RiesgoProbImp.objects.filter(probabilidad=probabilidad, impacto=impacto).values('color_hex', 'color'))                
                    
                if len(color) > 0:
                    nombre_color = color[0]['color']                    
                if nombre_color == 'rojo':
                    arreglo_ids_riesgos_criticos.append(riesgo['idriesgo'])
                    if riesgo['direccion'] != '-' and riesgo['direccion'] is not None:                        
                        if riesgo['direccion'] in dict_direcciones_criticos:
                            dict_direcciones_criticos[riesgo['direccion']] += 1
                        else:
                            dict_direcciones_criticos[riesgo['direccion']] = 1
                    rojos+=1
        
        riesgos_direcciones_ordenados = sorted(dict_direcciones_criticos.items(), key=operator.itemgetter(1), reverse=True)
        riesgos_ordenados = OrderedDict()
        arreglo_colores = ['#0abb87', '#fd397a', '#ffb822', '#5d78ff', '#36a3f7 ', 'red']
        i_riesgos_direccion = 0
        for riesgo_direccion in riesgos_direcciones_ordenados:
            if i_riesgos_direccion <5:
                riesgos_ordenados[riesgo_direccion[0]] = {'cantidad': riesgo_direccion[1], 'color':arreglo_colores[i_riesgos_direccion]}
            i_riesgos_direccion += 1  

        return riesgos_ordenados
    
    def getEventosDireccion(self, gerencias):
        arreglo_colores = ['#0abb87', '#fd397a', '#ffb822', '#5d78ff', '#36a3f7 ', 'red']        
        arreglo_ids_riesgos_criticos = []
        dict_direcciones_criticos = {}
        for gerencia in gerencias:            
            riesgos_gerencia = list(RiesgoUnifica.objects.filter(gerencia=gerencia['sigla']).values())            
            for riesgo in riesgos_gerencia:
                arreglo_ids_riesgos_criticos.append(riesgo['idriesgoasociado'])
                if riesgo['superintendencia'] != '-' and riesgo['superintendencia'] is not None:
                    if riesgo['montoperdidakusd'] != "-":
                        if float(riesgo['montoperdidakusd']) > 0:
                            if riesgo['superintendencia'] in dict_direcciones_criticos:
                                dict_direcciones_criticos[riesgo['superintendencia']] += 1
                            else:
                                dict_direcciones_criticos[riesgo['superintendencia']] = 1      
        riesgos_direcciones_ordenados = sorted(dict_direcciones_criticos.items(), key=operator.itemgetter(1), reverse=True)
        riesgos_ordenados = OrderedDict()
        arreglo_colores = ['#0abb87', '#fd397a', '#ffb822', '#5d78ff', '#36a3f7 ', 'red']
        i_riesgos_direccion = 0
        for riesgo_direccion in riesgos_direcciones_ordenados:
            if i_riesgos_direccion <5:
                riesgos_ordenados[riesgo_direccion[0]] = {'cantidad': riesgo_direccion[1], 'color':arreglo_colores[i_riesgos_direccion]}
            i_riesgos_direccion += 1  

        return riesgos_ordenados
    
    def getRiesgosValorizadosDireccion(self, gerencias):
        arreglo_ids_riesgos_criticos = []
        dict_direcciones_criticos = {}
        probabilidad = ""
        impacto = ""
        color = ""
        for gerencia in gerencias:
            rojos = 0
            riesgos_gerencia = list(Riesgo.objects.filter(gerencia=gerencia['sigla']).values())            
                        
            for riesgo in riesgos_gerencia:                
                nombre_color = ''
                if RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).exists():
                    resultado_inherente_riesgo = list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).values('probabilidadresidual', 'impactoresidual'))
                    probabilidad = resultado_inherente_riesgo[0]['probabilidadresidual']
                    impacto = resultado_inherente_riesgo[0]['impactoresidual']
                    color = list(RiesgoProbImp.objects.filter(probabilidad=probabilidad, impacto=impacto).values('color_hex', 'color'))                
                    
                if len(color) > 0:
                    nombre_color = color[0]['color']                    
                if nombre_color == 'rojo':
                    arreglo_ids_riesgos_criticos.append(riesgo['idriesgo'])
                    if riesgo['direccion'] != '-' and riesgo['direccion'] is not None:                        
                        if riesgo['direccion'] in dict_direcciones_criticos:
                            dict_direcciones_criticos[riesgo['direccion']] += float(riesgo['maximaperdidamus'])*100
                        else:
                            dict_direcciones_criticos[riesgo['direccion']] = float(riesgo['maximaperdidamus'])*100
                    rojos+=1
        
        riesgos_direcciones_ordenados = sorted(dict_direcciones_criticos.items(), key=operator.itemgetter(1), reverse=True)
        riesgos_ordenados = OrderedDict()
        arreglo_colores = ['#0abb87', '#fd397a', '#ffb822', '#5d78ff', '#36a3f7 ', 'red']
        i_riesgos_direccion = 0
        for riesgo_direccion in riesgos_direcciones_ordenados:
            if i_riesgos_direccion <5:
                riesgos_ordenados[riesgo_direccion[0]] = {'cantidad': riesgo_direccion[1], 'color':arreglo_colores[i_riesgos_direccion]}
            i_riesgos_direccion += 1

        return riesgos_ordenados

    
    def getRiesgosValorizadosDireccionDirectic(self, gerencias):
        arreglo_ids_riesgos_criticos = []
        dict_direcciones_criticos = {}
        probabilidad = ""
        impacto = ""
        color = ""
        for gerencia in gerencias:
            rojos = 0
            riesgos_gerencia = list(Riesgo.objects.filter(gerencia=gerencia['sigla'], directic=1).values())            
                        
            for riesgo in riesgos_gerencia:                
                nombre_color = ''
                if RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).exists():
                    resultado_inherente_riesgo = list(RiesgoEvaluacioncualitativaresidual.objects.filter(idriesgo=riesgo['idriesgo']).values('probabilidadresidual', 'impactoresidual'))
                    probabilidad = resultado_inherente_riesgo[0]['probabilidadresidual']
                    impacto = resultado_inherente_riesgo[0]['impactoresidual']
                    color = list(RiesgoProbImp.objects.filter(probabilidad=probabilidad, impacto=impacto).values('color_hex', 'color'))                
                    
                if len(color) > 0:
                    nombre_color = color[0]['color']                    
                if nombre_color == 'rojo':
                    arreglo_ids_riesgos_criticos.append(riesgo['idriesgo'])
                    if riesgo['direccion'] != '-' and riesgo['direccion'] is not None:                        
                        if riesgo['direccion'] in dict_direcciones_criticos:
                            dict_direcciones_criticos[riesgo['direccion']] += float(riesgo['maximaperdidamus'])*100
                        else:
                            dict_direcciones_criticos[riesgo['direccion']] = float(riesgo['maximaperdidamus'])*100
                    rojos+=1
        
        riesgos_direcciones_ordenados = sorted(dict_direcciones_criticos.items(), key=operator.itemgetter(1), reverse=True)
        riesgos_ordenados = OrderedDict()
        arreglo_colores = ['#0abb87', '#fd397a', '#ffb822', '#5d78ff', '#36a3f7 ', 'red']
        i_riesgos_direccion = 0
        for riesgo_direccion in riesgos_direcciones_ordenados:
            if i_riesgos_direccion <5:
                riesgos_ordenados[riesgo_direccion[0]] = {'cantidad': riesgo_direccion[1], 'color':arreglo_colores[i_riesgos_direccion]}
            i_riesgos_direccion += 1

        return riesgos_ordenados

    def getEventosValorizadosDireccion(self, gerencias):
        arreglo_ids_riesgos_criticos = []
        dict_direcciones_criticos = {}
        riesgos_direcciones_ordenados= {}
        for gerencia in gerencias:            
            riesgos_gerencia = list(RiesgoUnifica.objects.filter(gerencia=gerencia['sigla']).values())  

            for riesgo in riesgos_gerencia:                                                                                                
                arreglo_ids_riesgos_criticos.append(riesgo['idriesgoasociado'])
                if riesgo['superintendencia'] != '-' and riesgo['superintendencia'] is not None and riesgo['montoperdidakusd'] !="-":                        
                    if riesgo['superintendencia'] in dict_direcciones_criticos:
                        dict_direcciones_criticos[riesgo['superintendencia']] += float(riesgo['montoperdidakusd'])
                    else:
                        dict_direcciones_criticos[riesgo['superintendencia']] = float(riesgo['montoperdidakusd'])                
                    riesgos_direcciones_ordenados = sorted(dict_direcciones_criticos.items(), key=operator.itemgetter(1), reverse=True)

        riesgos_ordenados = OrderedDict()
        arreglo_colores = ['#0abb87', '#fd397a', '#ffb822', '#5d78ff', '#36a3f7 ', 'red']
        i_riesgos_direccion = 0
        for riesgo_direccion in riesgos_direcciones_ordenados:
            if i_riesgos_direccion <5:
                riesgos_ordenados[riesgo_direccion[0]] = {'cantidad': riesgo_direccion[1], 'color':arreglo_colores[i_riesgos_direccion]}
            i_riesgos_direccion += 1

        print(riesgos_ordenados)
        return riesgos_ordenados

        






