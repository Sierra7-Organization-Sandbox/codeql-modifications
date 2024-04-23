import base64
import os

import requests

# Store as environment variable for future Repo>Settings>Secrets & Variables>Actions>Repository Secret
auth_key = os.environ.get('API_SECRET')
# auth_key = 'github_pat_faketogetALERT15613215646546511'

# Get all repos in organization
url = 'https://api.github.com/repos/Sierra7-Organization-Sandbox/codeql-modifications/code-scanning/alerts'
# If not on Production url = 'https://api.github.com/repos/Sierra7-Organization-Sandbox/codeql-modifications/code
# -scanning/alerts?ref=development'

# Request headers
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"Bearer {auth_key}",
    "X-GitHub-Api-Version": "2022-11-28"
}

response = requests.get(url, headers=headers)

# Check the response status
if response.status_code == 200:
    print("Request for issues made successfully.")
    print(response.text)
else:
    print(f"Failed request. Status code: {response.status_code}")
    print(response.text)


def issue_exists():
    search_url = f'https://api.github.com/repos/Sierra7-Organization-Sandbox/codeql-modifications/issues'

    # Make the request to search for existing issues with the same title
    search_response = requests.get(search_url, headers=headers)

    issue_list = []

    # you'll want to check if the json response is not empty in the future
    for issue in search_response.json():
        print(issue['title'])
        issue_list.append(issue['title'])

    return issue_list


for alert in response.json():
    alert_title = alert['rule']['name']
    alert_body = alert['most_recent_instance']['message']['text']
    file_name = alert['most_recent_instance']['location']['path']
    line_number = alert['most_recent_instance']['location']['start_line']
    username = 'efrabell-S7'

    print(alert_title)
    print(alert_body)
    print(file_name)
    print(line_number)

    create_issue_url = f'https://api.github.com/repos/Sierra7-Organization-Sandbox/codeql-modifications/issues'

    formatted_title = f'CodeQL Alert: {alert_title} in {file_name}'

    issue_data = {
        'title': f'{formatted_title}',
        'body': f'{alert_body}\n\nFile: {file_name}\nLine: {line_number}',
        'labels': ['codeql', 'security'],
        'assignees': [username]  # Assign the issue to yourself
    }

    issue_titles = issue_exists()

    # This will need to be more sophisticated in the future (closed, open, file, etc.)
    if formatted_title in issue_titles:
        # Make the request to create an issue
        create_issue_response = requests.post(create_issue_url, headers=headers, json=issue_data)

        if create_issue_response.status_code == 201:
            print(f"Issue created for alert: {alert_title}")
        else:
            print(f"Failed to create issue for alert: {alert_title}. Status code: {create_issue_response.status_code}")
    else:
        print(f'Issue for alert ({alert_title}) has already been created.')