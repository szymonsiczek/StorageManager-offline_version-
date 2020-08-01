

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


def read_gear_from_file():
    File = open(file)
    for line in File.readlines():
        gear = line.split(', ')
        if gear[0] in Storage.subclasses:
            eval(gear[0])(gear[0], gear[1], gear[2], int(gear[3]))


def add_item_to_gear_file(string):
    File = open(file, 'a')
    File.write('\n' + string)
    File.close()
    gear = string.split(', ')
    if gear[0] in Storage.subclasses:
        eval(gear[0])(gear[0], gear[1], gear[2], int(gear[3]))


def delete_item_from_file(file):
    pass


def show_all_instances_of_subclass(subclass):
    pass


def show_all():
    for item in Storage.instances:
        print(item.full)


file = 'C:\\Users\\User\\Dropbox\\Python\\my_projects\\storageManager\\gear_list.txt'
