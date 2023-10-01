# Классы животных

class Dog:
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    def speak(self):
        return "Woof!"


class Cat:
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def speak(self):
        return "Meow!"


class Bird:
    def __init__(self, species, wingspan):
        self.species = species
        self.wingspan = wingspan

    def speak(self):
        return "Tweet!"

# Класс-фабрика


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args, **kwargs):
        if animal_type == "Dog":
            return Dog(*args, **kwargs)
        elif animal_type == "Cat":
            return Cat(*args, **kwargs)
        elif animal_type == "Bird":
            return Bird(*args, **kwargs)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Тестовое использование


dog = AnimalFactory.create_animal("Dog", breed="Labrador", age=3)
print(dog.speak())  # Woof!

cat = AnimalFactory.create_animal("Cat", color="Black", age=2)
print(cat.speak())  # Meow!

bird = AnimalFactory.create_animal("Bird", species="Parrot", wingspan=30)
print(bird.speak())  # Tweet!

# ====================================================================================================================


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def transpose(self):
        result = []
        for row in zip(*self.matrix):
            result.append(list(row))
        self.matrix = result  # Можно также обновить исходную матрицу
        return result

    def display(self):
        for row in self.matrix:
            print(row)


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_triangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "Некорректные значения сторон треугольника"

        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            if self.a == self.b == self.c:
                return "Равносторонний треугольник"
            elif self.a == self.b or self.a == self.c or self.b == self.c:
                return "Равнобедренный треугольник"
            else:
                return "Разносторонний треугольник"
        else:
            return "Треугольник не существует"


# Тестовое использование:

# Матрица
matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix = Matrix(matrix_data)
print("Original matrix:")
matrix.display()

transposed = matrix.transpose()
print("\nTransposed matrix:")
matrix.display()

# Треугольник
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))

triangle = Triangle(a, b, c)
print(triangle.check_triangle())
