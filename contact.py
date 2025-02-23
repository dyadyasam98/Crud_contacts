
contacts = []
class contact:
    def __init__(self, name, surname, number, id):
        self.__name = name
        self.__surname = surname
        self.__number = number
        self.__id = id
    def __str__(self):
        return f'Name: {self.__name}\nSurname: {self.__surname}\nNumber: {self.__number}\nID: {self.__id}'
    @property
    def contact_namer(self):
        return self.__name
    @property
    def contact_surnamer(self):
        return self.__surname
    @property
    def contact_number(self):
        return self.__number
    @property
    def contact_id(self):
        return self.__id

def print_all():
    for i in contacts:
        print(i)
        print('___________________')
def print_contact():
    print('Выберите вариант поиска контакта: ')
    search = int(input('Введите (1) для поиска по ID \nВведите (2) для поиска по имени \nВведите (3) для поиска по фамилии\n '))
    if search == 1:
        value = int(input('Введите ID: '))
        if value <= contacts[-1].contact_id:
            left = 0
            right = len(contacts)
            while left <= right:
                mid = (left + right) // 2
                if contacts[mid].contact_id == value:
                    print(contacts[mid])
                    return
                elif contacts[mid].contact_id < value:
                    left = mid
                else:
                    right = mid
        else:
            return 'Ошибка: введен несуществующий ID.'




def create_contact():
    create_name = input('Введите имя: ')
    create_surname = input('Введите фамилию: ')
    create_number = input('Введите номер телефона: ')
    if contacts :
        create_id = contacts[-1].contact_id + 1
    else:
        create_id = 0
        
    new_contact = contact(create_name, create_surname, create_number, create_id)
    contacts.append(new_contact)

create_contact()
create_contact()
create_contact()
create_contact()
print_all()
print_contact()