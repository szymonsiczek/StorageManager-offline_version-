

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

    def add_item(self, string_with_new_item_data):
        try:
            list_from_string_with_new_item_data = string_with_new_item_data.split(
                ', ')
            quantity = int(list_from_string_with_new_item_data.pop(3))
            new_item_data_without_quantity = ', '.join(
                list_from_string_with_new_item_data)
            for i in range(1, (quantity + 1)):
                Item.create_instance_from_string_and_write_to_database_file(
                    new_item_data_without_quantity)
            self.clear_self_items_list_and_load_items_from_file()
            return True
        except (IndexError, ValueError):
            return False

    def return_all_items_as_list_of_attributes(self):
        all_items_as_string_from_attributes = []
        if self.items:
            for item in self.items:
                all_items_as_string_from_attributes.append(
                    f'({item.category})  {item.type} {item.model}')
        return all_items_as_string_from_attributes

    def find_items_by_category_or_type(self, category_or_type):
        items_from_specified_category = []
        for item in self.items:
            if category_or_type.lower().strip() == item.category.lower():
                items_from_specified_category.append(item)
            elif category_or_type.lower().strip() == item.type.lower():
                items_from_specified_category.append(item)
        return items_from_specified_category

    def find_specific_item(self, info_about_item):
        File = open(self.database_file, 'r')
        items_in_database_file = File.readlines()
        File.close()
        founded_items = []
        for item in items_in_database_file:
            if info_about_item.lower() in item.lower():
                founded_items.append(item)
        return founded_items

    def delete_items(self, list_of_items_to_delete):
        File = open(self.database_file, 'r')
        items_in_file = File.readlines()
        File.close()
        for item in list_of_items_to_delete:
            items_in_file.remove(item)
            File = open(Storage.database_file, 'w')
            for line in items_in_file:
                File.write(line)
            File.close()
        self.clear_self_items_list_and_load_items_from_file()

    def delete_all_items(self):
        File = open(Storage.database_file, 'w')
        File.close()
        self.clear_self_items_list_and_load_items_from_file()


class Item:

    def __init__(self, category, type, model):
        self.category = category
        self.type = type
        self.model = model

    @classmethod
    def create_instance_from_string_and_write_to_database_file(cls, stringified_item):
        instance = Item.create_instance_from_string(stringified_item)
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
                   3: 'Show list of items from a certain category or type', 4: 'Delete item or group of items', 5: 'Delete all items'}

    def __init__(self, name, storage):
        self.storage = storage
        self.start_program_interface()

    def start_process_of_adding_items(self):
        while True:
            new_item_string_data = self.collect_data(
                '\nPlease provide new item data in order: '
                'category, type, model, quantity (Example: Sound, Mixer, Midas M32, 1).\n')
            self.break_if_data_is_menu(new_item_string_data)
            adding_new_item = self.storage.add_item(new_item_string_data)
            if adding_new_item == True:
                self.inform_user('New item was added.')
            else:
                self.inform_user(
                    'Adding item was cancelled because of an error, please try again.')
                break
            add_another_item = self.get_confirmation(
                'Would you like to add another item?')
            if add_another_item == False:
                break

    def start_process_of_showing_all_items(self):
        print('')
        print('----')
        all_items_as_list = self.storage.return_all_items_as_list_of_attributes()
        if all_items_as_list != []:
            for item in sorted(all_items_as_list):
                print(item)
        else:
            self.inform_user('List of items is empty.')
        print('----')

    def start_process_of_showing_items_by_category_or_type(self):
        category_or_type = self.collect_data(
            '\nPrint items from category or type:\n')
        self.break_if_data_is_menu(category_or_type)
        items_in_specified_category = self.storage.find_items_by_category_or_type(
            category_or_type)
        print('')
        print('----')
        if items_in_specified_category != []:
            for item in items_in_specified_category:
                print(f'({item.category})  {item.type} {item.model}')
        else:
            self.inform_user(
                f'Couldn\'t find any item from category/type {category_or_type}')
        print('----')
        print('')

    def start_process_of_deleting_items(self):
        item_to_delete = self.collect_data(
            '\nWhich item would you like to delete? '
            'Please provide specific info about type, model or category.\n')
        self.break_if_data_is_menu(item_to_delete)
        founded_items = self.storage.find_specific_item(item_to_delete)
        if not founded_items:
            self.inform_user('Item was not founded.')
        else:
            self.inform_user(
                f'\nNumber of founded items: {len(founded_items)}')
            print('----')
            for number, item in enumerate(sorted(founded_items)):
                print(str(number + 1) + ': ' + item.rstrip('\n'))
            print('----')
            if len(founded_items) > 1:
                founded_items_dict = {number + 1: item for number,
                                      item in enumerate(sorted(founded_items))}
                item_to_delete = self.collect_data(
                    '\nWhich items would you like to delete? '
                    'Please type their numbers from list above '
                    '(with commas and spaces, like: 1, 3, 6, 9).'
                    '\nType ALL to delete all items froms the list above.\n')
                self.break_if_data_is_menu(item_to_delete)
                if item_to_delete.lower() == 'all':
                    if self.get_confirmation('Are you sure?') == True:
                        self.storage.delete_items(founded_items)
                        self.inform_user('Deleting was successfull.')
                else:
                    try:
                        numbers_of_items_to_delete = [
                            int(num) for num in item_to_delete.split(', ')]
                        final_items_to_delete = [founded_items_dict.get(
                            number) for number in numbers_of_items_to_delete]
                        self.storage.delete_items(final_items_to_delete)
                        self.inform_user('Deleting was successfull.')
                    except ValueError:
                        self.inform_user(
                            'There was an error, please try again'
                            ' (make sure to type list of numbers with commas and spaces, like: 1, 3, 6, 9).')
            elif len(founded_items) == 1:
                if self.get_confirmation('Are you sure?') == True:
                    self.storage.delete_items(founded_items)
                    self.inform_user('Deleting was successfull.')

    def start_process_of_deleting_all_items(self):
        if self.get_confirmation('Are you sure that you want to delete all items?') == True:
            self.storage.delete_all_items()
            self.inform_user('All items were successfully removed.')

    def start_program_interface(self):
        while True:
            self.inform_user('What would you like to do? Type a number.')
            self.show_option_menu_and_execute_user_choice_from_menu()

    def show_option_menu_and_execute_user_choice_from_menu(self):
        self.show_option_menu()
        self.execute_user_choice_from_menu()

    def show_option_menu(self):
        for number, action in self.option_dict.items():
            print(f'{number}. {action}')

    def execute_user_choice_from_menu(self):
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            self.inform_user(
                'Please pick number from the options printed above.')
            self.start_program_interface()
        if choice in self.option_dict.keys():
            if choice == 1:
                self.start_process_of_adding_items()
            elif choice == 2:
                self.start_process_of_showing_all_items()
            elif choice == 3:
                self.start_process_of_showing_items_by_category_or_type()
            elif choice == 4:
                self.start_process_of_deleting_items()
            elif choice == 5:
                self.start_process_of_deleting_all_items()
        elif choice not in self.option_dict.keys():
            self.inform_user(
                'Please pick number from the options printed above.')
            self.start_program_interface()

    def break_if_data_is_menu(self, data):
        if data.lower() == 'menu':
            self.start_program_interface()

    @staticmethod
    def collect_data(info_to_prompt=None):
        data = input(info_to_prompt)
        return data

    def get_confirmation(self, decision_to_make):
        print('\n' + decision_to_make + ' Please type YES or NO.')
        user_decision = input().lower()
        if user_decision == 'yes':
            return True
        elif user_decision != 'yes':
            self.start_program_interface()

    @staticmethod
    def inform_user(info_string):
        print('\n' + info_string + '\n')


def initialize():
    my_storage = Storage('Main Storage')
    Interface('Main Menu', my_storage)


initialize()
