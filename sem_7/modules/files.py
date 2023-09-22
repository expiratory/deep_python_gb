import os
import random
import string


# 1. Функция для добавления в файл случайных пар чисел
def fill_file_with_numbers(file_name, lines_count):
    with open(file_name, 'a') as file:
        for _ in range(lines_count):
            int_num = random.randint(-1000, 1000)
            float_num = random.uniform(-1000, 1000)
            file.write(f"{int_num}|{float_num:.2f}\n")


# 2. Генерация псевдоимен
def generate_name():
    vowels = 'aeiou'
    all_letters = 'abcdefghijklmnopqrstuvwxyz'
    name_length = random.randint(4, 7)
    name = random.choice(vowels).upper()
    for _ in range(name_length - 1):
        name += random.choice(all_letters)
    return name


def save_names_to_file(file_name, count=100):
    with open(file_name, 'w') as file:
        for _ in range(count):
            file.write(generate_name() + '\n')


# 3. Функция для перемножения чисел и сохранения результата
def multiply_numbers_and_save(names_file, numbers_file, output_file):
    with open(names_file, 'r') as names, open(numbers_file, 'r') as nums, open(output_file, 'w') as out:
        name_lines = names.readlines()
        num_lines = nums.readlines()

        max_len = max(len(name_lines), len(num_lines))

        for i in range(max_len):
            name = name_lines[i % len(name_lines)].strip()
            int_num, float_num = map(float, num_lines[i % len(num_lines)].strip().split('|'))

            result = int_num * float_num

            if result < 0:
                out.write(f"{name.lower()}|{-result:.2f}\n")
            else:
                out.write(f"{name.upper()}|{round(result)}\n")


# 4. Создание файла с указанным расширением
def generate_random_file_name(min_len=6, max_len=30):
    length = random.randint(min_len, max_len)
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def create_files_with_extension(extension, min_name_len=6, max_name_len=30, min_file_size=256, max_file_size=4096,
                                files_count=42, directory='.'):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for _ in range(files_count):
        file_name = generate_random_file_name(min_name_len, max_name_len) + "." + extension
        file_path = os.path.join(directory, file_name)

        if not os.path.exists(file_path):
            with open(file_path, 'wb') as file:
                file.write(os.urandom(random.randint(min_file_size, max_file_size)))


# 5. Генерация файлов с разными расширениями
def create_files_with_extensions(extensions, files_counts, **kwargs):
    for ext, count in zip(extensions, files_counts):
        create_files_with_extension(ext, files_count=count, **kwargs)


# 7. Сортировка файлов по директориям
def sort_files_by_type(directory):
    file_types = {
        'video': ['.mp4', '.mkv', '.avi'],
        'images': ['.jpg', '.png', '.bmp'],
        'text': ['.txt', '.doc', '.pdf']
    }

    for dir_name, extensions in file_types.items():
        dir_path = os.path.join(directory, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        for file in os.listdir(directory):
            if file.endswith(tuple(extensions)):
                os.rename(os.path.join(directory, file), os.path.join(dir_path, file))


# 8. Групповое переименование файлов
def rename_files_in_directory(directory, base_name, number_digits, original_ext, new_ext, original_name_range=None):
    count = 1
    for file in os.listdir(directory):
        if file.endswith(original_ext):
            if original_name_range:
                original_part = file[original_name_range[0]:original_name_range[1]]
            else:
                original_part = ""
            new_name = f"{original_part}{base_name}{str(count).zfill(number_digits)}.{new_ext}"
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            count += 1
