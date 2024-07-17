import re


def _parse_hotspots(module_name, json_data):
    ordered_keys = ['module', 'vulnerabilityProbability', 'securityCategory', 'message', 'component', 'line', 'key']
    hotspots = []

    for hotspot in json_data['hotspots']:
        hotspot['module'] = module_name
        hotspot_data = {key: hotspot.get(key, '') for key in ordered_keys}

        hotspots.append(hotspot_data)

    return hotspots


def _parse_issues(module_name, json_data):
    ordered_keys = ['module', 'type', 'severity', 'message', 'debt', 'component', 'line', 'rule', 'key']
    issues = []

    for issue in json_data['issues']:
        issue['module'] = module_name
        issue_data = {key: issue.get(key, '') for key in ordered_keys}

        issues.append(issue_data)

    return issues


def _compose_table(files_data):
    table = {}

    # files_data is list of inner list. inner list has dictionaries, each dictionary has key-value pairs
    for file_data in files_data:
        for data in file_data:
            for key, value in data.items():
                if key in table:
                    table[key].append(value)
                else:
                    table[key] = [value]

    return table


def parse_json_files(json_data_dict):
    hotspots = []
    issues = []

    # Parse JSON data
    for file_name, json_data in json_data_dict.items():
        print(f"Parsing {file_name}")

        module_name, data_type = re.split(r'[-.]', file_name)[:2]

        if data_type == 'hotspots':
            hotspots.append(_parse_hotspots(module_name, json_data))
        elif data_type == 'issues':
            issues.append(_parse_issues(module_name, json_data))
        else:
            print(f"Unknown data type: {data_type}")
            raise ValueError

    # Collect issue first and then hotspot (for managing the order of Excel sheets)
    parsed_data_dict = {'issues': _compose_table(issues), 'hotspots': _compose_table(hotspots)}

    return parsed_data_dict
