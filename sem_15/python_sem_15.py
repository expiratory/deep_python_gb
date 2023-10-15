import os
import logging
from collections import namedtuple

# Определение и настройка логгера
logging.basicConfig(filename='file_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Определение namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def process_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            name, extension = os.path.splitext(file_name)
            file_info = FileInfo(name, extension, False, os.path.basename(root))
            logging.info(f'Файл: {file_info}')

        for dir_name in dirs:
            dir_info = FileInfo(dir_name, None, True, os.path.basename(root))
            logging.info(f'Каталог: {dir_info}')


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Использование: python python_sem_15.py /путь/к/директории")
    else:
        directory_path = sys.argv[1]
        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            process_directory(directory_path)
        else:
            print(f"Указанный путь '{directory_path}' не является действительным каталогом.")
