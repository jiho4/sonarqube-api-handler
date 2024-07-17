import os

import pandas as pd
import json


def read_all_json_from_path(json_file_dir):
    json_data_dict = {}

    # Get a list of all JSON files in the directory
    json_files = [f for f in os.listdir(json_file_dir) if f.endswith('.json')]

    # Read the target JSON file
    for json_file in json_files:
        with open(os.path.join(json_file_dir, json_file)) as file:
            json_data = json.load(file)

            json_data_dict[json_file] = json_data

    return json_data_dict


def convert_dict_to_excel(output_dir, output_file_name, data, sheet_name=None):
    # Skip if given data is empty
    if not data:
        print("Given data is empty for sheet: " + (sheet_name if sheet_name else 'Sheet1') + '. Skipping...')
        return

    excel_file_path = os.path.join(output_dir, output_file_name + '.xlsx')

    # Convert dict data to a DataFrame
    df = pd.DataFrame(data)

    # Check if the Excel file already exists
    if os.path.exists(excel_file_path):
        mode = 'a'  # Append if already exists
    else:
        mode = 'w'  # Make a new file if not

    with pd.ExcelWriter(excel_file_path, mode=mode, engine='openpyxl') as writer:

        # Write DataFrame to an Excel file
        if sheet_name:
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        else:
            df.to_excel(writer, index=False)

    if mode == 'a':
        print(f"Data is appended to: {excel_file_path}" + f" in sheet: {sheet_name}" if sheet_name else '')
    else:
        print(f"Data is saved to: {excel_file_path}" + f" in sheet: {sheet_name}" if sheet_name else '')
