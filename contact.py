contacts = []
class contact:
    def __init__(self, name, surname, number, id, email):
        self.__name = name
        self.__surname = surname
        self.__number = number
        self.__id = id
        self.__email = email
    def __str__(self):
        return f'Name: {self.__name}\nSurname: {self.__surname}\nNumber: {self.__number}\nID: {self.__id}\nemail: {self.__email}'
    @property
    def contact_name(self):
        return self.__name
    @property
    def contact_surname(self):
        return self.__surname
    @property
    def contact_number(self):
        return self.__number
    @propertys
    def contact_id(self):
        return self.__id
    @property
    def contact_email(self):
        return self.__email
    @contact_email.setter
    def contact_email(self, email):
        self.__email = email
    @contact_name.setter
    def contact_name(self, name):
        self.__name = name
    @contact_surname.setter
    def contact_surname(self, surname):
        self.__surname = surname
    @contact_number.setter
    def contact_number(self,number):
        self.__number = number
    



def print_all():
    for i in contacts:
        print(i)
        print('___________________')
def print_contact():
    print('Выберите вариант поиска контакта: ')
    search = int(input('Введите (1) для поиска по ID \nВведите (2) для поиска по имени \nВведите (3) для поиска по фамилии\nВведите нужное число: '))
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
    elif search == 2:
        value = input('Введите имя: ')
        for n in contacts:
            if n.contact_name == value:
                print('___________________')
                print(n)
        return
    elif search == 3:
        value = input('Введите фамилию: ')
        for s in contacts:
            if s.contact_surname == value:
                print('___________________')
                print(s)
        return
    else:
        print('Ошибка ввода.')
    
        
            




def create_contact():
    create_name = input('Введите имя: ')
    create_surname = input('Введите фамилию: ')
    create_number = input('Введите номер телефона: ')
    create_email = input('Введите адрес почты: ')
    if contacts :
        create_id = contacts[-1].contact_id + 1
    else:
        create_id = 0
        
    new_contact = contact(create_name, create_surname, create_number, create_id, create_email)
    contacts.append(new_contact)

def update_contact():
    value = int(input('Введите ID: '))
    index_to_update = 0
    if value <= contacts[-1].contact_id:
        left = 0
        right = len(contacts)
        while left <= right:
            mid = (left + right) // 2
            if contacts[mid].contact_id == value:
                index_to_update = mid
            elif contacts[mid].contact_id < value:
                left = mid + 1
            else:
                right = mid - 1
    if contacts[index_to_update]:
        print(contact[index_to_update])
        upd = int(input('Выберите поле, которе хотите изменить: имя(1), фамилию(2), телефон(3), почта(4).\nВведите число: '))
        if upd == 1:
            prev_name = contact[index_to_update].contact_name
            contact[index_to_update].contact_name = input('Введите новое имя для пользователя: ')
            print('Готово! Имя {prev_name} изменено на: {contact[index_to_update].contact_name} ')
        elif upd == 2:
            prev_surname = contact[index_to_update].contact_surname
            contact[index_to_update].contact_surname = input('Введите новое имя для пользователя: ')
            print('Готово! Фамилия {prev_surname} изменена на: {contact[index_to_update].contact_surname} ')
        elif upd == 3:
            prev_number = contact[index_to_update].contact_number
            contact[index_to_update].contact_number = input('Введите новое имя для пользователя: ')
            print('Готово! Номер телефона {prev_surname} изменен на: {contact[index_to_update].contact_number} ')
        elif upd == 4:
            prev_email = contact[index_to_update].contact_email
            contact[index_to_update].contact_email = input('Введите новое имя для пользователя: ')
            print('Готово! Адрес почты {prev_surname} изменен на: {contact[index_to_update].contact_email} ')

    else:
        print('Ошибка. Контакт не найден.')


create_contact()
create_contact()
create_contact()
print_all()
update_contact()
update_contact()
update_contact()