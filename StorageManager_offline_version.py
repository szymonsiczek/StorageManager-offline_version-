
class Storage:
    def __init__(self, name, model, quantity):
        self.name = name
        self.model = model
        self.quantity = quantity

    @property
    def full(self):
        return self.name + ' ' + self.model


class Sound(Storage):
    pass


class Light(Storage):
    pass


class Stage(Storage)


class Power(Storage):
    pass


class Extra(Storage):
    pass


sound1 = Sound('Mixer', 'Midas M32', 1)
