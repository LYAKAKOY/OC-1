import json
import os
import zipfile
import psutil


class TypeFile:
    __slots__ = ['file_name', 'type_file']

    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        try:
            with open(self.file_name, 'r') as file:
                print(file.read())
        except Exception:
            print("Файл пуст или не существует")

    def write_file(self):
        with open(self.file_name, 'a') as file:
            file.write(input('Введите текст, который запишется в файл: '))

    def delete_file(self):
        if os.path.isfile(self.file_name):
            os.remove(self.file_name)
            print("Файл удалён")
        else:
            print("Файла нет")


class TXT(TypeFile):
    type_file = '.txt'


class XML(TypeFile):
    type_file = '.xml'


class JSON(TypeFile):
    type_file = '.json'
    data = {
        'title': 'Главная страница',
        'form': 'RegisterForm',
        'Articles': 10
    }

    def read_file(self):
        try:
            with open(self.file_name, "r") as read_file:
                data = json.load(read_file)
                print(data)
        except Exception:
            print("Файл пуст или не существует")

    def write_file(self):
        with open(self.file_name, "w") as write_file:
            json.dump(self.data, write_file)

    def get_data(self):
        return self.data

    def set_data(self, data: dict):
        self.data = data


class ZIP(TypeFile):
    load_file = 'name.txt'
    type_file = '.zip'

    def read_file(self):
        with zipfile.ZipFile(self.file_name, 'r') as myzip:
            myzip.printdir()

    def write_file(self):
        loadfile = input('Введите название файла, которое поместить в zip-архив: ')
        with zipfile.ZipFile(self.file_name, 'a') as myzip:
            with open(loadfile, 'w') as file:
                pass
            myzip.write(loadfile)

    def get_loadfile(self):
        return self.load_file

    def set_loadfile(self, load_file: str):
        self.load_file = load_file


def DISK() -> None:
    disks = psutil.disk_partitions()
    for d in disks:
        for info in d:
            print(info, end=' ')
        print()


menu = {
    '1': DISK,
    '2': TXT,
    '3': JSON,
    '4': XML,
    '5': ZIP
}

while True:
    print("1)Информация о дисках", "2)TXT", "3)JSON", "4)XML", "5)ZIP", "6)Выход", sep='\n')
    choice = int(input('Выбор: '))

    if choice == 6:
        break

    if 1 < choice < 6:
        file_name = input('Введите название файла: ') + menu.get(str(choice)).type_file
        while True:

            obj = menu.get(str(choice))(file_name)
            print('1)Записать в файл', '2)Прочитать файл', '3)Удалить файл', '4)Выход в меню', sep='\n')
            n = int(input())
            if n == 1:
                obj.write_file()
            elif n == 2:
                obj.read_file()
            elif n == 3:
                obj.delete_file()
                break
            else:
                break
    else:
        DISK()
