import os
import json

def load_json_files_from_folders(root_folder):
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            min_food_id, max_food_id = map(int, folder_name.split('-'))
            json_file_path = os.path.join(folder_path, 'response_food_data.json')
            if os.path.exists(json_file_path):
                print(f'opening file {json_file_path}')
                with open(json_file_path, 'r') as json_file:
                    data = json.load(json_file)
                    check_missing_data(data, min_food_id, max_food_id, folder_path)

def check_missing_data(data, min_food_id, max_food_id, folder_path):
    food_ids = set(entry['food_id'] for entry in data['foods'])
    
    missing_data = [str(food_id) for food_id in range(min_food_id, max_food_id + 1) if food_id not in food_ids]

    if missing_data:
        print(f"Missing data in {folder_path}: {', '.join(missing_data)}")
        with open(os.path.join(folder_path, 'missing_data.txt'), 'w') as missing_file:
            missing_file.write('\n'.join(missing_data))

root_folder = 'D:\Temp\healthifyme-food-data'  # Update this with the path to your root folder
load_json_files_from_folders(root_folder)