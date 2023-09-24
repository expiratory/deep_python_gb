from modules import walk_dir, save_results

if __name__ == "__main__":
    path = input("Enter the directory path: ")
    total_size, content = walk_dir(path)
    save_results(path, content)