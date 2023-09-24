import os
import json
import csv
import pickle


def walk_dir(path, parent=None):
    content = []
    total_size = 0

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            file_size = os.path.getsize(item_path)
            total_size += file_size
            content.append({
                'type': 'file',
                'name': item,
                'parent': parent,
                'size': file_size
            })
        else:
            dir_size, dir_content = walk_dir(item_path, parent=item)
            total_size += dir_size
            content.append({
                'type': 'directory',
                'name': item,
                'parent': parent,
                'size': dir_size
            })
            content.extend(dir_content)

    return total_size, content


def save_results(path, content):
    with open('output.json', 'w', encoding='utf-8') as json_file:
        json.dump(content, json_file, indent=4, ensure_ascii=False)

    with open('output.csv', 'w', newline='') as csv_file:
        fieldnames = ['type', 'name', 'parent', 'size']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for entry in content:
            writer.writerow(entry)

    with open('output.pkl', 'wb') as pkl_file:
        pickle.dump(content, pkl_file)
