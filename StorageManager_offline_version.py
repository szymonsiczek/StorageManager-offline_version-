

class Storage:
    instances = []
    subclasses = ['Sound', 'Light', 'Stage', 'Power', 'Extra']

    def __init__(self, subclass, name, model, quantity):
        self.subclass = subclass
        self.name = name
        self.model = model
        self.quantity = quantity
        Storage.instances.append(self)
        if self.subclass in Storage.subclasses:
            eval(self.subclass).instances.append(self)

    @property
    def full(self):
        return self.name + ' ' + self.model


class Sound(Storage):
    instances = []


class Light(Storage):
    instances = []
    pass


class Stage(Storage):
    instances = []
    pass


class Power(Storage):
    instances = []
    pass


class Extra(Storage):
    instances = []
    pass


gear1 = Storage('Sound', 'Mixer', 'Midas M32', 1)
gear2 = Storage('Sound', 'Stagebox', 'DL32', 1)
gear3 = Storage('Light', 'Beam', 'Gladiator', 16)
gear4 = Storage('Light', 'Solar 27Q', 'Prolights', 12)
gear5 = Storage('Stage', 'Podest 2x1m', 'Alustage', 18)
gear6 = Storage('Power', 'Rodzielnia 32A', 'Ta w kejsie', 1)
gear7 = Storage('Extra', 'Toolbox', '-', 1)


for i in Storage.instances:
    print(i.full)
