

class Storage:
    database_file = 'C:\\Users\\User\\Dropbox\\Python\\my_projects\\items_in_store_manager\\item_list.txt'

    def __init__(self, name):
        self.name = name

    def load_items_from_file(self):
        File = open(Storage.database_file, 'r')
        for line in File.readlines():
            Item.instance_from_file(line)


class Item:
    instances = []

    def __init__(self, category, type, model):
        self.category = category
        self.type = type
        self.model = model
        Item.instances.append(self)

    @classmethod
    def instance_from_file(cls, string):
        (category, type, model) = string.split(', ')
        cls(category, type, model)


def initialize():
    main_storage = Storage('Main Storage')
    main_storage.load_items_from_file()
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
        pass  # work on that!
    elif choice not in menu.keys():
        print('\nPlease pick number from the options printed above.\n')
        start_program_interface()
    start_program_interface()


def create_option_menu():
    actions = ['Add item', 'Show all items',
               'Show list of items from a certain category', 'Delete item', 'Delete all items']
    option_menu = {}
    for action in actions:
        option_menu.update({(actions.index(action) + 1): action})
    return option_menu


def show_menu(menu):
    for number, action in menu.items():
        print(f'{number}. {action}')


def get_user_choice(prompt_info):
    if prompt_info != None:
        print('\n' + prompt_info)
    user_choice = input()
    return user_choice


initialize()
