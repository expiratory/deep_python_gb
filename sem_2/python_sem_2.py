# Задача 2

hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
            13: 'D', 14: 'E', 15: 'F'}


def int_to_hex(number):
    hex_number = ''
    while number > 0:
        div_remainder = number % 16
        hex_number = hex_dict[div_remainder] + hex_number
        number = number // 16
    return hex_number


try:
    num = int(input('Введите целое число: '))
    hex_num = int_to_hex(num)
    print(f'Шестнадцатеричное представление введенного вами числа {num}: ' + hex_num)
    print(f'Проверка полученного результата через функцию hex: {hex(num)}')
except Exception as e:
    print(str(e))

# Задача 3

from fractions import Fraction


def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a


def reduce_fraction(numerator, denominator):
    gcd = greatest_common_divisor(numerator, denominator)
    return numerator // gcd, denominator // gcd


def add_fractions(fraction1, fraction2):
    numerator1, denominator1 = map(int, fraction1.split('/'))
    numerator2, denominator2 = map(int, fraction2.split('/'))
    if denominator1 == 0 or denominator2 == 0:
        return False
    common_denominator = denominator1 * denominator2
    new_numerator1 = numerator1 * denominator2
    new_numerator2 = numerator2 * denominator1
    sum_numerators = new_numerator1 + new_numerator2
    reduced_fraction = reduce_fraction(sum_numerators, common_denominator)
    return f"{reduced_fraction[0]}/{reduced_fraction[1]}"


try:
    fraction1 = input("Введите первую дробь (в формате a/b): ")
    fraction2 = input("Введите вторую дробь (в формате a/b): ")
    result = add_fractions(fraction1, fraction2)
    if not result:
        print("Знаменатель дроби не может равен нулю")
    else:
        print(f"Сумма дробей: {result}")
        print(f'Проверка результата с помощью fractions: {Fraction(fraction1) + Fraction(fraction2)}')

except Exception as e:
    print(str(e))
