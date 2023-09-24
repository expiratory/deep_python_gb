import csv
import random
import json
import cmath


def find_roots(a, b, c):
    discriminant = cmath.sqrt(b ** 2 - 4 * a * c)
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)
    return root1, root2


def generate_csv(filename, rows=100):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            writer.writerow([random.randint(1, 1000) for _ in range(3)])


def from_csv_decorator(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    a, b, c = map(int, row)
                    result = func(a, b, c)
                    results.append(result)
            return results
        return wrapper
    return decorator


def save_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                "arguments": args,
                "result": [str(item) for item in result]
            }
            with open(filename, 'w') as file:
                json.dump(data, file)
            return result
        return wrapper
    return decorator


# Применение
generate_csv('random_numbers.csv', 1000)


@from_csv_decorator('random_numbers.csv')
@save_to_json('results.json')
def roots_from_csv(a, b, c):
    return find_roots(a, b, c)


results = roots_from_csv()
