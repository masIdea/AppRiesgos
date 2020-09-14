class SetModel():
    def __init__(self, model=None, columns_data={}, condition=None):
        self.model = model
        self.columns_data = columns_data
        self.condition = condition

    def set(self):
        Model.objects.filter(id=id).update(field=F('field') +1))
        eval(self.model).objects.filter(self.condition).update(self.columns_data)