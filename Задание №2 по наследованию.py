# Задание №2. Создать класс Man содержащий информацию о человеке (фио, возраст, пол и т.д.). Описать методы для него(ввод, вывод, сериализация, запись в файл и т.д.)
# Создать класс User унаследованный от класса Man. В котором добавить почтовый ящик, логин, пароль и методы для работы с ними.
import json
# Создаем новый класс Man
class Man:
    # Функция конструктор класса Man
    def _init_(self):
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.age = None
        self.gender = None
        self.nationality = None
    # Функция ввода данных пользователя
    def input_info(self):
        self.first_name = input("Input First Name: ")
        self.middle_name = input("Input Middle Name: ")
        self.last_name = input("Input Last Name: ")
        self.age = input("Input Age: ")
        self.gender = input("Input Gender: ")
        self.nationality = input("Input Nationality: ")
    # Функция сериализации данных в удобный вид для чтения на экране
    def serialize(self):
        return "First name: {}\n" \
               "Middle name: {}\n"\
               "Last name: {}\n" \
               "Age : {}\n"\
               "Gender : {}\n"\
               "Nationality : {}\n"\
            .format(self.first_name, self.middle_name, self.last_name, self.age, self.gender, self.nationality)
    # Функция записи данных  в отдельный файл (например 1.txt)
    def fail_save(self):
        fil = str(input("Введите с клавиатуры имя файла для сохранения данных:  "))
        with open(fil, "w") as f:
            data = {"first_name": self.first_name,
                    "middle_name": self.middle_name,
                    "last_name": self.last_name,
                    "age": self.age,
                    "gender": self.gender,
                    "nationality": self.nationality}
            json.dump(data, f)
    # Функция загрузки данных  из отдельного файла
    def fail_load(self):
        fil = str(input("Введите с клавиатуры имя файла для загрузки данных:  "))
        with open(fil, "r") as f:
            data = json.loads(f.read())
            self.first_name = data["first_name"]
            self.last_name = data["last_name"]
            self.middle_name = data["middle_name"]
            self.age = data["age"]
            self.gender = data["gender"]
            self.nationality = data["nationality"]
            print(data)
# Создаем дочерний класс User
class User(Man):
    # Функция регистрации данных пользователя
    def reg(self):
        self.login = input("Введите свой логин :")
        self.password = input("Введите свой пароль :")
        self.confirm_password = input("Подтвердите свой пароль : ")
        self.email = input("Введите свой email : ")
        # Запишем все регистрационные данные в файл(например 2.txt)
        fil = input("Введите название файла для записи данных пользователя")
        with open(fil, "w") as f:
            data = {}
            data["login"] = self.login
            data["password"] = self.password
            data["email"] = self.email
            json.dump(data, f)
            print(data)
    # Функция проверки введенных данных пользователя
    def log(self):
        login = input("Введите ваш логин: ")
        password = input("Введите ваш пароль:  ")
        fil = str(input("Введите с клавиатуры имя файла для загрузки данных:  "))
        with open(fil, "r") as f:
            data = json.load(f)
            self.login = data["login"]
            self.password = data["password"]
        if self.login == login and self.password == password:
            print("Данные введены корректно, авторизация прошла успешно")
        else:
            print("Некорректно введены логин или пароль")
# Вызываем методы для выполнения кода
user = User()
print(user.input_info())
print(user.serialize())
print(user.fail_save())
print(user.fail_load())
user.reg()
user.log()
print(user)