

class Storage:
    database_file = 'C:\\Users\\User\\Dropbox\\Python\\my_projects\\items_in_store_manager\\item_list.txt'

    def __init__(self, name):
        self.name = name
        self.items = []
        self.clear_self_items_list_and_load_items_from_file()

    def clear_self_items_list_and_load_items_from_file(self):
        self.items.clear()
        File = open(Storage.database_file, 'r')
        for line in File.readlines():
            line = line.rstrip('\n')
            self.items.append(Item.create_instance_from_string(line))

    def add_item(self):
        # Collect new item data
        new_items_data = []
        while True:
            new_item = input(
                'Please provide new item data in order: category, type, model, quantity (Example: Sound, Mixer, Midas M32, 1).\n')
            if new_item.lower() != 'menu':
                new_items_data.append(new_item)
            else:
                break
            ask_for_more = input(
                'Would you like to add another item? Please type Y/N\n')
            if ask_for_more.lower() == 'n':
                break
        # Create item instance and write to database file
        for string in new_items_data:
            try:
                list_from_string = string.split(', ')
                quantity = int(list_from_string.pop(3))
                string_data = ', '.join(list_from_string)
                for i in range(1, (quantity + 1)):
                    Item.create_instance_from_string_and_write_to_database_file(
                        string_data)
                    print(f'{string_data} was added successfully.')
            except IndexError:
                pass
        print('')
        self.clear_self_items_list_and_load_items_from_file()

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
        File = open(self.database_file, 'r')
        items_in_file = File.readlines()
        File.close()
        item_to_delete = input(
            'Which item would you like to delete? Please provide specific info about type or model.\n')
        for item in items_in_file:
            if item_to_delete.lower() in item.lower():
                confirmation = None
                while confirmation not in ('yes', 'no', 'menu'):
                    confirmation = input(
                        '\nPlease confirm (YES/NO) that you want to delete item: ' + item).lower()
                    if confirmation == 'yes':
                        items_in_file.remove(item)
                        File = open(Storage.database_file, 'w')
                        for line in items_in_file:
                            File.write(line)
                        File.close()
                        self.clear_self_items_list_and_load_items_from_file()
                        print(f'{item}'.rstrip('\n') +
                              ' was removed successfully.\n')
                    elif confirmation == 'no':
                        break
                    elif confirmation == 'menu':
                        break

    def delete_all_items(self):
        delete_all_confirmation = input(
            'Please confirm (YES/NO) that you want to delete all items\n')
        if delete_all_confirmation.lower() == 'yes':
            File = open(Storage.database_file, 'w')
            File.close()
            print('\nAll items were successfully removed.\n')
            self.clear_self_items_list_and_load_items_from_file()
        else:
            print('Deleting all items was aborted.')


class Item:

    def __init__(self, category, type, model):
        self.category = category
        self.type = type
        self.model = model

    @classmethod
    def create_instance_from_string_and_write_to_database_file(cls, string):
        instance = Item.create_instance_from_string(string)
        instance.write_to_database_file()

    @classmethod
    def create_instance_from_string(cls, stringified_item):
        (category, type, model) = stringified_item.split(', ')
        return cls(category, type, model)

    def write_to_database_file(self):
        File = open(Storage.database_file, 'a')
        File.write(f'{self.category}, {self.type}, {self.model}\n')
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
            self.show_option_menu_and_execute_user_choice_from_menu(storage)

    def show_option_menu_and_execute_user_choice_from_menu(self, storage):
        self.show_option_menu()
        self.execute_user_choice_from_menu(storage)

    def show_option_menu(self):
        for number, action in self.option_dict.items():
            print(f'{number}. {action}')

    def execute_user_choice_from_menu(self, storage):
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
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


def initialize():
    storage = Storage('Main Storage')
    Interface('Main Menu', storage)


initialize()
