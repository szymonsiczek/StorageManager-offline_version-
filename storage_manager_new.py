

class Storage:
    database_file = 'C:\\Users\\User\\Dropbox\\Python\\my_projects\\items_in_store_manager\\item_list.txt'

    def __init__(self, name):
        self.name = name

    def load_items_from_file(self):
        Item.instances = []
        File = open(Storage.database_file, 'r')
        for line in File.readlines():
            line = line.rstrip('\n')
            Item.instance_from_string(line)

    def add_item(self):
        # collect_new_item_data
        new_items_data = []
        add_more = True
        while add_more == True:
            new_item = Interface.get_user_choice(
                'Please provide new item data in order: category, type, model, quantity (Example: Sound, Mixer, Midas M32, 1).')
            if new_item.lower() != 'menu':
                new_items_data.append(new_item)
            else:
                break
            ask_for_more = Interface.get_user_choice(
                'Would you like to add another item? Please type Y/N')
            if ask_for_more.lower() == 'n':
                add_more = False
        # create_item_instance and write to database_file
        for string in new_items_data:
            data = string.split(', ')
            quantity = int(data.pop(3))
            string_data = ', '.join(data)
            for i in range(1, (quantity + 1)):
                Item.instance_from_string(string_data)
                Item.write_to_database_file(string_data)

    def show_all_items(self):
        print('')
        items_to_show = []
        if Item.instances != []:
            for item in Item.instances:
                items_to_show.append(
                    f'({item.category})  {item.type} {item.model}')
            for item in sorted(items_to_show):
                print(item)
        else:
            print('---\nList of items is empty\n---')
        print('\n')

    def show_items_from_category(self):
        category = Interface.get_user_choice(
            'Print items from category:').lower()
        for item in Item.instances:
            if category == item.category.lower():
                print(f'({item.category})  {item.type} {item.model}')
        print('\n')

    def delete_item(self):
        File = open(Storage.database_file, 'r')
        items_in_file = File.readlines()
        File.close()
        choice = Interface.get_user_choice(
            'Which item would you like to delete? Please provide specific info about type or model.')
        for item in items_in_file:
            if choice.lower() in item.lower():
                confirmation = None
                while confirmation != 'y' and confirmation != 'n':
                    confirmation = Interface.get_user_choice(
                        'Please confirm (Y/N) that you want to delete item: ' + item).lower()
                    if confirmation == 'y':
                        items_in_file.remove(item)
                        File = open(Storage.database_file, 'w')
                        for line in items_in_file:
                            File.write(line)
                        File.close()
                        initialize()
                    elif confirmation == 'n':
                        break
                    elif confirmation == 'menu':
                        break

    def delete_all_items(self):
        delete_all_confirmation = Interface.get_user_choice(
            'Please confirm (YES/NO) that you want to delete all items')
        if delete_all_confirmation.lower() == 'yes':
            File = open(Storage.database_file, 'w')
            File.close()
            initialize()
        else:
            pass


class Item:
    instances = []

    def __init__(self, category, type, model):
        self.category = category
        self.type = type
        self.model = model
        Item.instances.append(self)

    @classmethod
    def instance_from_string(cls, string):
        (category, type, model) = string.split(', ')
        cls(category, type, model)

    @classmethod
    def write_to_database_file(cls, string):
        File = open(Storage.database_file, 'a')
        File.write(string + '\n')
        File.close()


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
        print('What would you like to do? Type a number.\n')
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
