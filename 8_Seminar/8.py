import json

FIRST_NAME = 'first_name'
LAST_NAME = 'last_name'
PHONE = 'phone'
ID = 'id'
PEOPLE = 'people'

class PhoneBook():
    def __init__(self, path):
        self.path = path
        self.data:dict = self.read()
       
    def read(self):
        with open(self.path, 'r') as data:
            return json.load(data)

    def save(self):
        with open(self.path, 'w') as data:
            json.dump(self.data, data)

    def append(self):
        person = {}
        person[ID] = self.data[ID] = self.data[ID] + 1
        person[LAST_NAME] = input('Введите фамилию: ')
        person[FIRST_NAME] = input('Введите имя: ')
        person[PHONE] = input('Введите телефон: ')
        self.data[PEOPLE].append(person)
        self.save()

    def print_all(self):
        for person in self.data[PEOPLE]:
            self.print_concrete(person)

    def print_concrete(self, person):
        print(f'{person[ID]}, {person[FIRST_NAME]} {person[LAST_NAME]}, {person[PHONE]}')

    def find(self, substring:str):
        for person in self.data[PEOPLE]:
            if substring in person[FIRST_NAME] or substring in person[LAST_NAME]:
                self.print_concrete(person)

    def delete(self, id:int):
        for person in self.data[PEOPLE]:           
            if person[ID] == id:             
                self.data[PEOPLE].remove(person)
                self.save()

    def change(self, id:int):
        for person in self.data[PEOPLE]:           
            if person[ID] == id:
                name = input(f'Введите фамилию: ')             
                if name != '': person[LAST_NAME] = name
                name = input(f'Введите имя: ')             
                if name != '': person[FIRST_NAME] = name
                phone = input(f'Введите телефон: ')             
                if phone != '': person[PHONE] = phone
                self.save()
                

def welcome():
    print('1 - Распечатать все записи')    
    print('2 - Добавить запись')    
    print('3 - Найти запись')    
    print('4 - Удалить запись по id') 
    print('5 - Изменить запись по id')
    print('6. Выход')

def main():
    book = PhoneBook('file.json') 
    while True:
        welcome()    
        command = input('> ')
        if command == '1':
            book.print_all()
        elif command == '2':
            book.append()
        elif command == '3':
            substring = input('Введите имя: ')
            book.find(substring)
        elif command == '4':
            id = int(input('Введите id: '))
            book.delete(id)
        elif command == '5':
            id = int(input('Введите id: '))
            book.change(id)
        elif command == '6':
            break
        else: print('Некорректный ввод\n', '\r>')

main()