
class Item:
    instances = []
    subclasses = ['Sound', 'Light', 'Stage', 'Power', 'Extra']
    item_instance_data = ['Category',
                          'Type of item:', 'Model', 'Quantity']

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

    @staticmethod
    def add_item():
        item = Item.get_new_item_data()
        Item.create_instance_and_add_item_to_item_list(item)

    @staticmethod
    def get_new_item_data():
        print('\nPlease type new item data:')
        new_item_data = []
        for data_type in Item.item_instance_data:
            print('\n' + data_type + ':')
            if data_type == 'Category':
                Item.show_user_all_subclasses()
            input_data = get_user_choice(None)
            while data_type == 'Category' and input_data not in Item.subclasses and input_data != 'menu':
                input_data = get_user_choice(
                    'Please type one of the categories from the list (start with capital letter)')
            if input_data == 'menu':
                start_program_interface()
            new_item_data.append(input_data)
        return new_item_data

    @staticmethod
    def create_instance_and_add_item_to_item_list(list):
        eval(list[0])(list[0], list[1], list[2], int(list[3]))
        File = open(file, 'a')
        string = ', '.join(list)
        File.write('\n' + string)
        File.close()

    @staticmethod
    def load_items_from_file():
        Item.instances = []
        File = open(file)
        for line in File.readlines():
            item = line.split(', ')
            if item[0] in Item.subclasses and item[0] != 'Sound':
                eval(item[0])(item[0], item[1], item[2], int(item[3]))
            elif item[0] in Item.subclasses and item[0] == 'Sound':
                eval(item[0])(item[0], item[1], item[2],
                              int(item[3]), int(item[4]))

    @staticmethod
    def delete_item():
        File = open(file, 'r')
        items_in_file = File.readlines()
        File.close()
        choice = get_user_choice(
            'Which item would you like to delete? Please provide specific info about type or model.')
        for item in items_in_file:
            if choice.lower() in item.lower():
                confirmation = None
                while confirmation != 'y' and confirmation != 'n':
                    confirmation = get_user_choice(
                        'Please confirm (Y/N) that you want to delete item: ' + item).lower()
                    if confirmation == 'y':
                        Item.delete_item_from_file(items_in_file, item, file)
                    elif confirmation == 'n':
                        pass
        Item.load_items_from_file()

    @staticmethod
    def delete_item_from_file(item_list, item, file):
        item_list.remove(item)
        File = open(file, 'w')
        for line in item_list:
            File.write(line)
        File.close()

    @staticmethod
    def delete_all_items():
        delete_all_confirmation = get_user_choice(
            'Please confirm (YES/NO) that you want to delete all items')
        if delete_all_confirmation.lower() == 'yes':
            File = open(file, 'w')
            File.close()
            Item.load_items_from_file()
        else:
            pass

    @staticmethod
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
        get_user_choice(None)

    @staticmethod
    def show_all_instances_of_subclass():
        Item.show_user_all_subclasses()
        category = get_user_choice('Show items in category:')
        while category not in Item.subclasses and category != 'menu':
            print('\nPlease choose one of the categories, starting with capital letter.')
            Item.show_user_all_subclasses()
            category = get_user_choice(None)
        if category == 'menu':
            start_program_interface()
        for item in eval(category).instances:
            print(item.sub_type_and_name)
        get_user_choice('\nPress enter to go back to menu')

    @staticmethod
    def show_user_all_subclasses():
        print('Categories are: ', end='')
        for subclass in Item.subclasses:
            print(subclass + ', ', end='')
        print('')


class Sound(Item):
    instances = []

    def __init__(self, subclass, type, model, quantity, spl=None):
        super().__init__(subclass, type, model, quantity)
        self.spl = spl

    @staticmethod
    def show_spl_level():
        sound_item = get_user_choice(
            'Please provide type or model of an object to show its SPL level').lower()
        for instance in Sound.instances:
            if sound_item in instance.sub_type_and_name.lower():
                Sound.prompt_item_spl_level(instance)

    def prompt_item_spl_level(self):
        if self.spl != 0:
            print(
                f'\n{self.type} {self.model} sound pressure level is: {self.spl} dB\n')
        else:
            print(f"\nI'm {self.type} {self.model}, I don't make noise\n")


class Light(Item):
    instances = []


class Stage(Item):
    instances = []


class Power(Item):
    instances = []


class Extra(Item):
    instances = []


def initialize():
    Item.load_items_from_file()
    start_program_interface()


def start_program_interface():
    print('What would you like to do? Type a number. \n\n')
    show_action_options_and_execute_user_choice()


def show_action_options_and_execute_user_choice():
    menu = create_option_menu()
    show_menu(menu)
    choice = get_user_choice(None)
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
                                                 'Item.show_all()'], ['Show list of items from a certain category', 'Item.show_all_instances_of_subclass()'], ['Delete item', 'Item.delete_item()'], ['Delete all items', 'Item.delete_all_items()'], ['Show Sound Pressure Level', 'Sound.show_spl_level()']]
    option_menu = {}
    for action in actions:
        option_menu.update({(actions.index(action) + 1): action})
    return option_menu


def show_menu(menu):
    for number, action in menu.items():
        print(f'{number}. {action[0]}')


def get_user_choice(prompt_info):
    if prompt_info != None:
        print('\n' + prompt_info)
    user_choice = input()
    return user_choice


file = 'C:\\Users\\User\\Dropbox\\Python\\my_projects\\storageManager\\item_list.txt'

initialize()
