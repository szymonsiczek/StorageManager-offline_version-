
class Storage:
    def __init__(self, name, model, quantity):
        self.name = name
        self.model = model
        self.quantity = quantity

    @property
    def full(self):
        return self.name + ' ' + self.model
