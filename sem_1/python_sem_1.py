# Задача 1

for i in range(2, 10, 4):
    for j in range(2, 11):
        for k in range(i, i + 4):
            print(f"{k} * {j} = {k*j}", end="\t")
        print()
    print()

# Задача 2

def check_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Некорректные значения сторон треугольника"

    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Равносторонний треугольник"
        elif a == b or a == c or b == c:
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"
    else:
        return "Треугольник не существует"


a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))

result = check_triangle(a, b, c)
print(result)

# Задача 3

num = int(input("Введите число: "))

if num < 0 or num > 100000:
    print("Число должно быть от 0 до 100000")
else:
    is_prime = True
    if num == 0:
        print('Ноль не является натуральным числом, соответственно и не является ни простым, ни составным числом')
    if num == 1:
        print('У единицы только один делитель, она тоже не простое ни составное число')
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print("Простое число")
        else:
            print("Составное число")

# Задача 4

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
target_number = randint(LOWER_LIMIT, UPPER_LIMIT)

for _ in range(10):
    guess = int(input(f"Введите вашу догадку ({LOWER_LIMIT} - {UPPER_LIMIT}): "))

    if guess < target_number:
        print("Больше")
    elif guess > target_number:
        print("Меньше")
    else:
        print("Вы угадали!")
        break
else:
    print(f"Попытки закончились. Загаданное число: {target_number}")
