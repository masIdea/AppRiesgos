from core.models import *
from kpiDashboard.models import RiesgoKpi

class Id():
    def __init__(self, modelo, prefix, id_model):
        self.modelo = modelo
        self.prefix = prefix
        self.id_model = id_model

class GetId(Id):        
    def get_id(self):                
        if eval(self.modelo).objects.all().exists():            
            num_model = list(eval(self.modelo).objects.all().values(self.id_model))
            arr_nums_model = []
            for num in num_model:
                arr_nums_model.append(int(num[self.id_model].split('_')[1]))
            num_max = max(arr_nums_model)
            num_model_gen = (num_max + 1)
            num_model_gen = self.prefix+'_'+str(num_model_gen)
        else:                    
            num_model_gen = 1
            num_model_gen = self.prefix+'_'+str(num_model_gen)

        return num_model_gen


class GetIdCons(Id):        
    def get_id(self):
        if eval(self.modelo).objects.all().exists():            
            num_model = list(eval(self.modelo).objects.all().values(self.id_model).order_by("-creado"))
            arr_nums_model = []
            for num in num_model:
                arr_nums_model.append(int(num[self.id_model]))
            num_max = max(arr_nums_model)
            num_model_gen = (num_max + 1)
            num_model_gen = str(num_model_gen)
        else:                    
            num_model_gen = 1
            num_model_gen = str(num_model_gen)

        return num_model_gen

class GetIdGui(Id):        
    def get_id(self):                
        if eval(self.modelo).objects.all().exists():            
            num_model = list(eval(self.modelo).objects.all().values(self.id_model))
            arr_nums_model = []
            for num in num_model:
                arr_nums_model.append(int(num[self.id_model].split('-')[1]))
            num_max = max(arr_nums_model)
            num_model_gen = (num_max + 1)
            num_model_gen = self.prefix+'-'+str(num_model_gen)
        else:                    
            num_model_gen = 1
            num_model_gen = self.prefix+'-'+str(num_model_gen)

        return num_model_gen