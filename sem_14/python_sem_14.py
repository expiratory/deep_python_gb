import json


class BaseError(Exception):
    def __init__(self, message):
        super().__init__(message)


class AccessError(BaseError):
    pass


class LevelError(BaseError):
    pass


class User:
    def __init__(self, name, id, access_level):
        self.name = name
        self.id = id
        self.access_level = access_level

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"Пользователь: {self.name}, ID: {self.id}, Уровень доступа: {self.access_level}"


def read_users_from_file(file_path):
    users = set()
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for user_data in data:
                user = User(user_data['name'], user_data['id'], user_data['access_level'])
                users.add(user)
    except FileNotFoundError:
        users = set()
    return users


class Project:
    def __init__(self, user_file_path):
        self.users = read_users_from_file(user_file_path)

    def login(self, name, id):
        user_to_find = User(name, id, 0)
        if user_to_find not in self.users:
            raise AccessError(f"Ошибка доступа. Пользователь {name} с ID {id} не найден.")
        user = next(user for user in self.users if user == user_to_find)
        return user.access_level

    def add_user(self, user):
        if user.access_level < self.login(user.name, user.id):
            raise LevelError(
                f"Ошибка уровня доступа. Уровень доступа недостаточен для добавления пользователя {user.name}.")
        self.users.add(user)

    def save_users_to_file(self, file_path):
        data = [{'name': user.name, 'id': user.id, 'access_level': user.access_level} for user in self.users]
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


try:
    project = Project("users.json")
    user1 = User("Пользователь1", 1, 3)
    project.add_user(user1)
    project.save_users_to_file("users.json")
except AccessError as e:
    print(f"Ошибка доступа: {str(e)}")
except LevelError as e:
    print(f"Ошибка уровня доступа: {str(e)}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {str(e)}")
