# Задание №1. Взять задание из предыдущей лекции и отделить функции сохранения и загрузки в отдельный класс

import json
# Создаем новый класс User
class User:
    # Функция конструктор класса User
    def _init_(self):
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.age = None
    # Функция ввода данных пользователя
    def input_info(self):
        self.first_name = input("Input First Name: ")
        self.middle_name = input("Input Middle Name: ")
        self.last_name = input("Input Last Name: ")
        self.age = input("Input Age: ")
    # Функция сериализации данных в удобный вид для чтения на экране
    def serialize(self):
        return "First name: {}\n" \
               "Middle name: {}\n"\
               "Last name: {}\n" \
               "Age : {}\n"\
            .format(self.first_name, self.middle_name, self.last_name, self.age)
# Создаем дочерний класс Save_load_data (User)
class Save_load_data(User):
    # Функция записи данных  в отдельный файл
    def fail_save(self):
        fil = str(input("Введите с клавиатуры имя файла для записи на диск:  "))
        with open(fil, "w") as f:
            data = {"first_name": self.first_name,
                    "middle_name": self.middle_name,
                    "last_name": self.last_name,
                    "age": self.age}
            json.dump(data, f)
    # Функция загрузки данных  из отдельного файла
    def fail_load(self):
        fil = str(input("Введите с клавиатуры имя файла для загрузки с диска:  "))
        with open(fil, "r") as f:
            data = json.loads(f.read())
            self.first_name = data["first_name"]
            self.last_name = data["last_name"]
            self.middle_name = data["middle_name"]
            self.age = data["age"]
            print(data)
user = Save_load_data()
user.input_info()
print(user.serialize())
print(user.fail_save())
print(user.fail_load())
print(user)

