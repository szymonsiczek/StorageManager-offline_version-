
class Storage:
    instances = []

    def __init__(self, subclass, name, model, quantity):
        self.subclass = subclass
        self.name = name
        self.model = model
        self.quantity = quantity
        Storage.instances.append(self)

    @property
    def full(self):
        return self.name + ' ' + self.model


class Sound(Storage):
    instances = []


class Light(Storage):
    pass


class Stage(Storage):
    pass


class Power(Storage):
    pass


class Extra(Storage):
    pass


sound1 = Storage('sound', 'Mixer', 'Midas M32', 1)
sound2 = Storage('sound', 'Stagebox', 'DL32', 1)

print(Sound.instances)
