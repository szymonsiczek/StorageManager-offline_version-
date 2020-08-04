
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

    def add_item():
        item = Item.get_new_item_data()
        if item.lower() == 'menu':
            return None
        else:
            Item.create_instance_and_add_item_to_item_list(item)

    def get_new_item_data():
        print('\nPlease type new item data in comma-separated format: category, name, model, quantity\nFor example: Sound, Mixer, Midas M32, 2')
        Item.show_user_all_subclasses()
        print('\n\n(Or type "menu" to go back to menu)')
        new_item_data = input()
        return new_item_data

    def create_instance_and_add_item_to_item_list(string):
        File = open(file, 'a')
        File.write('\n' + string)
        File.close()
        item = string.split(', ')
        if item[0] in Item.subclasses:
            eval(item[0])(item[0], item[1], item[2], int(item[3]))

    def read_items_from_file():
        File = open(file)
        for line in File.readlines():
            item = line.split(', ')
            if item[0] in Item.subclasses:
                eval(item[0])(item[0], item[1], item[2], int(item[3]))

    def delete_item():
        delete_item_from_file()
        read_items_from_file()

    def delete_item_from_file(file):
        pass

    def delete_all_items():
        pass

    def show_all():
        Item.read_items_from_file()
        for item in Item.instances:
            print(item.fullname)
        print('\nPress enter to go back to menu')
        input()

    def show_all_instances_of_subclass(subclass):
        pass

    def show_user_all_subclasses():
        print('Categories are: ', end='')
        for subclass in Item.subclasses:
            print(subclass + ', ', end='')


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


def start_program():
    print('What would you like to do? Type a number. \n\n')
    show_action_options_and_execute_user_choice()


def show_action_options_and_execute_user_choice():
    menu = create_option_menu()
    show_menu(menu)
    choice = int(input())
    if choice in menu.keys():
        eval(menu.get(choice)[1])
    else:
        print('\nPlease pick number from the options printed above.\n')
    start_program()


def create_option_menu():
    actions = [['Add item', 'Item.add_item()'], ['Show all items',
                                                 'Item.show_all()'], ['Show list of items from a certain category', 'Item. show_all_instances_of_subclass()'], ['Delete item', 'Item.delete_item()'], ['Delete all items', 'Item.delete_all_items()']]
    option_menu = {}
    for action in actions:
        option_menu.update({(actions.index(action) + 1): action})
    return option_menu


def show_menu(menu):
    for number, action in menu.items():
        print(f'{number}. {action[0]}')


file = 'C:\\Users\\User\\Dropbox\\Python\\my_projects\\storageManager\\item_list.txt'

start_program()
