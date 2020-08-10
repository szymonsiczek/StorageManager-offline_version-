

class Storage:
    database_file = 'C:\\Users\\User\\Dropbox\\Python\\my_projects\\items_in_store_manager\\item_list.txt'

    def __init__(self, name):
        self.name = name

    def load_items_from_file(self):
        File = open(Storage.database_file, 'r')
        for line in File.readlines():
            Item.instance_from_file(line)

    def add_item(self):
        pass

    def show_all_items(self):
        pass

    def show_items_from_category(self):
        pass

    def delete_item(self):
        pass

    def delete_all_items(self):
        pass


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


class Interface:
    def __init__(self, name, option_1, option_2, option_3, option_4, option_5):
        self.name = name
        self.option_1 = option_1
        self.option_2 = option_2
        self.option_3 = option_3
        self.option_4 = option_4
        self.option_5 = option_5

    def menu_option_list(self):
        option_list = [self.option_1, self.option_2,
                       self.option_3, self.option_4, self.option_5]
        return option_list

    def start_program_interface(self, storage):
        print('What would you like to do? Type a number. \n\n')
        self.show_action_options_and_execute_user_choice(storage)

    def show_action_options_and_execute_user_choice(self, storage):
        menu = self.create_and_show_option_menu()
        choice = Interface.get_user_choice(None)
        try:
            choice = int(choice)
        except:
            print('\nPlease pick number from the options printed above.\n')
            self.start_program_interface(storage)
        if choice in menu.keys():
            if choice == 1:
                storage.add_item()
            elif choice == 2:
                storage.show_all_items()
            elif choice == 3:
                storage.show_items_from_category()
            elif choice == 4:
                storage.delete_item()
            elif choice == 5:
                storage.delete_all_items()
        elif choice not in menu.keys():
            print('\nPlease pick number from the options printed above.\n')
            self.start_program_interface(storage)
        self.start_program_interface(storage)

    def create_and_show_option_menu(self):
        option_dict = {}
        for action in self.menu_option_list():
            option_dict.update(
                {(self.menu_option_list().index(action) + 1): action})
        for number, action in option_dict.items():
            print(f'{number}. {action}')
        return option_dict

    @staticmethod
    def get_user_choice(prompt_info):
        if prompt_info != None:
            print('\n' + prompt_info)
        user_choice = input()
        return user_choice


def initialize():
    main_storage = Storage('Main Storage')
    main_storage.load_items_from_file()
    main_menu = Interface('Main Menu', 'Add item', 'Show all items',
                          'Show list of items from a certain category', 'Delete item', 'Delete all items')
    main_menu.start_program_interface(main_storage)


initialize()
