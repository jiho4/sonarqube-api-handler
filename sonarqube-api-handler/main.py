from datetime import datetime
import file_handler as fh
import sonarqube_api_parser as sq
import yaml

with open('config/config.yaml') as f:
    __conf = yaml.safe_load(f)

INPUT_JSON_DIR = __conf['input_json_dir']
OUTPUT_EXCEL_DIR = __conf['output_excel_dir']


def main():
    json_data_dict = fh.read_all_json_from_path(INPUT_JSON_DIR)

    parsed_data_dict = sq.parse_json_files(json_data_dict)

    output_file_name = 'sonar-report-' + str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

    for data_type, data in parsed_data_dict.items():
        fh.convert_dict_to_excel(OUTPUT_EXCEL_DIR, output_file_name, parsed_data_dict[data_type], sheet_name=data_type)


if __name__ == "__main__":
    main()
