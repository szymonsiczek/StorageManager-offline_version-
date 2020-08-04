
class Item:
    instances = []
    subclasses = ['Sound', 'Light', 'Stage', 'Power', 'Extra']
    item_instance_data = ['Category', 'Type of item:', 'Model', 'Quantity']

    def __init__(self, subclass, type, model, quantity):
        self.subclass = subclass
        self.type = type
        self.model = model
        self.quantity = quantity
        Item.instances.append(self)
        if self.subclass in Item.subclasses:
            eval(self.subclass).instances.append(self)

    @property
    def sub_type_and_name(self):
        return '(' + self.subclass + ')  ' + self.type + ' ' + self.model

    def add_item():
        item = Item.get_new_item_data()
        Item.create_instance_and_add_item_to_item_list(item)

    def get_new_item_data():
        print('\nPlease type new item data:')
        new_item_data = []
        for data_type in Item.item_instance_data:
            print('\n' + data_type + ':')
            if data_type == 'Category':
                Item.show_user_all_subclasses()
                print('')
            input_data = input()
            while data_type == 'Category' and input_data not in Item.subclasses and input_data != 'menu':
                print(
                    'Please type one of the categories from the list (start with capital letter)')
                input_data = input()
            if input_data == 'menu':
                start_program_interface()
            new_item_data.append(input_data)
        print(new_item_data)
        return new_item_data

    def create_instance_and_add_item_to_item_list(list):
        eval(list[0])(list[0], list[1], list[2], int(list[3]))
        File = open(file, 'a')
        string = ', '.join(list)
        File.write('\n' + string)
        File.close()

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
        print('')
        print('---')
        items_to_show = []
        for item in Item.instances:
            items_to_show.append(item.sub_type_and_name)
        for item in sorted(items_to_show):
            print(item)
        print('---')
        print('\nPress enter to go back to menu')
        input()

    def show_all_instances_of_subclass():
        Item.show_user_all_subclasses()
        print('Show items in category:')
        category = input()
        while category not in Item.subclasses and category != 'menu':
            print('\nPlease choose one of the categories, starting with capital letter.')
            Item.show_user_all_subclasses()
            category = input()
        if category == 'menu':
            start_program_interface()
        for item in eval(category).instances:
            print(item.sub_type_and_name)
        print('\nPress enter to go back to menu')
        input()

    def show_user_all_subclasses():
        print('Categories are: ', end='')
        for subclass in Item.subclasses:
            print(subclass + ', ', end='')
        print('')


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


def initialize():
    Item.read_items_from_file()
    start_program_interface()


def start_program_interface():
    print('What would you like to do? Type a number. \n\n')
    show_action_options_and_execute_user_choice()


def show_action_options_and_execute_user_choice():
    menu = create_option_menu()
    show_menu(menu)
    choice = input()
    try:
        choice = int(choice)
    except:
        print('\nPlease pick number from the options printed above.\n')
        start_program_interface()
    if choice in menu.keys():
        eval(menu.get(choice)[1])
    else:
        print('\nPlease pick number from the options printed above.\n')
    start_program_interface()


def create_option_menu():
    actions = [['Add item', 'Item.add_item()'], ['Show all items',
                                                 'Item.show_all()'], ['Show list of items from a certain category', 'Item.show_all_instances_of_subclass()'], ['Delete item', 'Item.delete_item()'], ['Delete all items', 'Item.delete_all_items()']]
    option_menu = {}
    for action in actions:
        option_menu.update({(actions.index(action) + 1): action})
    return option_menu


def show_menu(menu):
    for number, action in menu.items():
        print(f'{number}. {action[0]}')


file = 'C:\\Users\\User\\Dropbox\\Python\\my_projects\\storageManager\\item_list.txt'

initialize()
