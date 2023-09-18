# chess_module.py
import random


def place_queens_on_board(queens):
    board = [[0 for _ in range(8)] for _ in range(8)]
    for q in queens:
        x, y = q
        board[x - 1][y - 1] = 1
    return board


def is_under_attack(board, x, y):
    # Проверка по горизонтали и вертикали
    for i in range(8):
        if board[x][i] == 1 or board[i][y] == 1:
            return True
    # Проверка по диагоналям
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1 and abs(i - x) == abs(j - y):
                return True
    return False


def are_queens_safe(queens):
    board = place_queens_on_board(queens)
    for q in queens:
        x, y = q
        board[x - 1][y - 1] = 0
        if is_under_attack(board, x - 1, y - 1):
            return False
        board[x - 1][y - 1] = 1
    return True


def generate_random_positions(n=8):
    """Генерация случайной расстановки ферзей."""
    rows = list(range(1, n + 1))
    random.shuffle(rows)
    return [(i + 1, row) for i, row in enumerate(rows)]


def find_four_successful_positions():
    """Поиск 4 успешных расстановок."""
    successful_positions = []

    while len(successful_positions) < 4:
        positions = generate_random_positions()
        if are_queens_safe(positions) and positions not in successful_positions:
            successful_positions.append(positions)

    return successful_positions
