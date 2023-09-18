import sys


def _is_leap(year):
    """Проверка года на високосность."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def is_valid_date(date_str):
    """Проверка даты на валидность."""
    try:
        day, month, year = map(int, date_str.split('.'))
    except ValueError:
        return False

    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        elif month == 2:
            if _is_leap(year) and 1 <= day <= 29:
                return True
            elif not _is_leap(year) and 1 <= day <= 28:
                return True
    return False
