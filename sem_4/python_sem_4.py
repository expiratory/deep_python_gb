"""
Задача 1
"""


def transpose(matrix):
    result = []
    for row in zip(*matrix):
        print(list(row))
        result.append(list(row))


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix)

"""
Задача 2
"""


def reverse_kwargs(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            hash(value)
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result


print(reverse_kwargs(a=1, b="test", c=[1, 2, 3]))
