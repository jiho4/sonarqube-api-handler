import requests
import yaml

with open('config/config.yaml') as f:
    __conf = yaml.safe_load(f)

# Replace these with your actual details
SONARQUBE_URL = __conf['sonarqube_api']['sonarqube_url']
API_ENDPOINT_SEARCH_ISSUES = __conf['sonarqube_api']['endpoint_search_issues']
PROJECT_KEY = __conf['sonarqube_api']['project_key']
AUTH_TOKEN = __conf['sonarqube_api']['auth_token']


def _fetch_issues():
    url = f"{SONARQUBE_URL}{API_ENDPOINT_SEARCH_ISSUES}"
    params = {
        'projects': PROJECT_KEY,
        'statuses': 'OPEN',
        'types': 'BUG,VULNERABILITY'
    }
    headers = {
        'Authorization': f'Bearer {AUTH_TOKEN}'
    }
    response = requests.get(url, params=params, headers=headers)

    # request
    print(f"Request URL: {response.request.url}")
    print(f"Request Headers: {response.request.headers}")
    if response.request.body:
        print(f"Request Body: {response.request.body}")

    # response
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    if response.content:
        print("Response Content:", response.json())  # Assuming JSON response for readability

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch issues")
        return None


def _simplify_issues(issues_json):
    simplified_issues = []
    for issue in issues_json['issues']:
        simplified_issue = {
            'key': issue['key'],
            'message': issue['message'],
            'component': issue['component']
        }
        simplified_issues.append(simplified_issue)
    return simplified_issues


def get_issues():
    issues_json = _fetch_issues()

    if issues_json:
        return _simplify_issues(issues_json)
    else:
        return None
