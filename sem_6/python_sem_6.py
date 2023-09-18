from modules import date
from modules import chess
import sys

if __name__ == "__main__":
    test_positions = [
        [(1, 1), (2, 5), (3, 8), (4, 6), (5, 3), (6, 7), (7, 2), (8, 4)],  # безопасная расстановка
        [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)],  # ферзи бьют друг друга по диагонали
        [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)],  # ферзи бьют друг друга по горизонтали
    ]

    for pos in test_positions:
        print(f"Позиции: {pos} - Безопасные? {'Да' if chess.are_queens_safe(pos) else 'Нет'}")

    print("\n4 успешные расстановки:")
    for pos in chess.find_four_successful_positions():
        print(pos)

    if len(sys.argv) > 1:
        date_str = sys.argv[1]
        print(f"\n{date_str} такая дата {'существует' if date.is_valid_date(date_str) else 'не существует'}")
    else:
        print("Пожалуйста, укажите дату в формате DD.MM.YYYY.")
