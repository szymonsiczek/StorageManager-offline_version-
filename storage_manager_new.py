

class Storage:
    database_file = 'C:\\Users\\User\\Dropbox\\Python\\my_projects\\items_in_store_manager\\item_list.txt'

    def __init__(self, name):
        self.name = name
        self.items = []
        self.load_items_from_file()

    def load_items_from_file(self):
        self.items = []
        File = open(Storage.database_file, 'r')
        for line in File.readlines():
            line = line.rstrip('\n')
            # Item function, is that ok?
            self.items.append(Item.create_instance_from_string(line))

    def add_item(self):
        # collect_new_item_data
        new_items_data = []
        add_more = True
        while add_more == True:
            new_item = input(
                'Please provide new item data in order: category, type, model, quantity (Example: Sound, Mixer, Midas M32, 1).\n')
            if new_item.lower() != 'menu':
                new_items_data.append(new_item)
            else:
                break
            ask_for_more = input(
                'Would you like to add another item? Please type Y/N\n')
            if ask_for_more.lower() == 'n':
                add_more = False
        # create_item_instance and write to database_file
        for string in new_items_data:
            try:
                data = string.split(', ')
                quantity = int(data.pop(3))
                string_data = ', '.join(data)
                for i in range(1, (quantity + 1)):
                    Item.create_instance_from_string_and_write_to_database_file(
                        string_data)
            except IndexError:
                pass
        self.load_items_from_file()

    def show_all_items(self):
        print('')
        items_to_show = []
        if self.items != []:
            for item in self.items:
                items_to_show.append(
                    f'({item.category})  {item.type} {item.model}')
            for item in sorted(items_to_show):
                print(item)
        else:
            print('---\nList of items is empty\n---')
        print('\n')

    def show_items_from_category(self):
        category = input(
            'Print items from category:\n').lower()
        print('')
        for item in self.items:
            if category == item.category.lower():
                print(f'({item.category})  {item.type} {item.model}')
        print('\n')

    def delete_item(self):
        File = open(Storage.database_file, 'r')
        items_in_file = File.readlines()
        File.close()
        choice = input(
            'Which item would you like to delete? Please provide specific info about type or model.\n')
        for item in items_in_file:
            if choice.lower() in item.lower():
                confirmation = None
                while confirmation != 'y' and confirmation != 'n':
                    confirmation = input(
                        'Please confirm (Y/N) that you want to delete item: ' + item + '\n').lower()
                    if confirmation == 'y':
                        items_in_file.remove(item)
                        File = open(Storage.database_file, 'w')
                        for line in items_in_file:
                            File.write(line)
                        File.close()
                        self.load_items_from_file()
                    elif confirmation == 'n':
                        break
                    elif confirmation == 'menu':
                        break

    def delete_all_items(self):
        delete_all_confirmation = input(
            'Please confirm (YES/NO) that you want to delete all items\n')
        if delete_all_confirmation.lower() == 'yes':
            File = open(Storage.database_file, 'w')
            File.close()
            self.load_items_from_file()
        else:
            pass


class Item:

    def __init__(self, category, type, model):
        self.category = category
        self.type = type
        self.model = model

    @classmethod
    def create_instance_from_string(cls, stringified_item):
        (category, type, model) = stringified_item.split(', ')
        return cls(category, type, model)

    @classmethod
    def create_instance_from_string_and_write_to_database_file(cls, string):
        Item.create_instance_from_string(string)
        File = open(Storage.database_file, 'a')
        File.write(string + '\n')
        File.close()


class Interface:
    option_dict = {1: 'Add item', 2: 'Show all items',
                   3: 'Show list of items from a certain category', 4: 'Delete item', 5: 'Delete all items'}

    def __init__(self, name, storage):
        self.storage = storage
        self.start_program_interface(storage)

    def start_program_interface(self, storage):
        while True:
            print('What would you like to do? Type a number.\n')
            self.show_option_menu_and_execute_user_choice(storage)

    def show_option_menu_and_execute_user_choice(self, storage):
        self.show_option_menu()
        self.execute_user_choice(storage)

    def execute_user_choice(self, storage):
        choice = input()
        try:
            choice = int(choice)
        except:
            print('\nPlease pick number from the options printed above.\n')
            self.start_program_interface(storage)
        if choice in self.option_dict.keys():
            if choice == 1:
                self.storage.add_item()
            elif choice == 2:
                self.storage.show_all_items()
            elif choice == 3:
                self.storage.show_items_from_category()
            elif choice == 4:
                self.storage.delete_item()
            elif choice == 5:
                self.storage.delete_all_items()
        elif choice not in self.option_dict.keys():
            print('\nPlease pick number from the options printed above.\n')
            self.start_program_interface(storage)

    def show_option_menu(self):
        for number, action in self.option_dict.items():
            print(f'{number}. {action}')


def initialize():
    storage = Storage('Main Storage')
    menu = Interface('Main Menu', storage)


initialize()
