import os

"""
Задача 1
"""


def generate_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count, number = 0, 2
    while count < n:
        if is_prime(number):
            yield number
            count += 1
        number += 1


primes = generate_primes(5)
for prime in primes:
    print(prime)


"""
Задача 2
"""


def split_path_generator(path):
    directory, filename = os.path.split(path)
    name, extension = os.path.splitext(filename)
    yield directory
    yield name
    yield extension


# Тестовый пример
path = "/home/user/documents/file.txt"
components = tuple(split_path_generator(path))
print(components)


"""
Задача 3
"""


def bonus_generator(names, salaries, bonuses):
    for name, salary, bonus in zip(names, salaries, bonuses):
        bonus_value = salary * (float(bonus.strip('%')) / 100)
        yield name, bonus_value


# Тестовые данные
names = ["Алексей", "Мария", "Дмитрий"]
salaries = [100000, 120000, 110000]
bonuses = ["10%", "5.5%", "7.5%"]
bonus_dict = dict(bonus_generator(names, salaries, bonuses))
print(bonus_dict)


"""
Задача 4
"""


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
