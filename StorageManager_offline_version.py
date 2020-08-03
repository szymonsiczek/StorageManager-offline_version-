

class Item:
    instances = []
    subclasses = ['Sound', 'Light', 'Stage', 'Power', 'Extra']

    def __init__(self, subclass, name, model, quantity):
        self.subclass = subclass
        self.name = name
        self.model = model
        self.quantity = quantity
        Item.instances.append(self)
        if self.subclass in Item.subclasses:
            eval(self.subclass).instances.append(self)

    @property
    def fullname(self):
        return self.name + ' ' + self.model

    def create_item():
        pass

    def read_items_from_file():
        File = open(file)
        for line in File.readlines():
            item = line.split(', ')
            if item[0] in Item.subclasses:
                eval(item[0])(item[0], item[1], item[2], int(item[3]))

    def add_item_to_item_file(string):
        File = open(file, 'a')
        File.write('\n' + string)
        File.close()
        item = string.split(', ')
        if item[0] in Item.subclasses:
            eval(item[0])(item[0], item[1], item[2], int(item[3]))

    def delete_item_from_file(file):
        pass

    def show_all_instances_of_subclass(subclass):
        pass

    def show_all():
        for item in Item.instances:
            print(item.fullname)


class Sound(Item):
    instances = []


class Light(Item):
    instances = []


class Stage(Item):
    instances = []


class Power(Item):
    instances = []


class Extra(Item):
    instances = []


def starting_program():
    print('What would you like to do? Type a number. \n\n')
    show_options_and_get_user_choice()


def show_actions_options_and_get_user_choice():
    # Work on that! Do you need to get show actions, get choice and eval() actions in the same func? If so, change the name of this func.
    '1. Add item\n2. Show all items\n3. Show list of items from a certain category\n4. Delete item\n5.Delete all items\n\n'
    action_options = {}
    choice = input()


file = 'C:\\Users\\User\\Dropbox\\Python\\my_projects\\storageManager\\item_list.txt'
