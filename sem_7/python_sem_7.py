from modules import files


if __name__ == "__main__":
    directory_path = "/home/alexandr/PycharmProjects/deep_python_gb/sem_7/test_files"

    base_name = "new_"
    number_digits = 3
    original_ext = "old"
    new_ext = "new"
    original_name_range = (2, 6)

    files.rename_files_in_directory(directory_path, base_name, number_digits, original_ext, new_ext,
                                    original_name_range)
