def make_report(response_data, full_info):
    data = []

    data.append('#'*40)
    data.append('HTTP Response Analyzer')
    data.append('#'*40)

    data.append('\nURL')
    data.append('-'*40)

    for key, value in response_data['URL'].items():
        data.append(f'{key}: {value}')

    data.append('\nResponse')
    data.append('-'*40)
    data.append(f"Status: {response_data['Status']}")
    data.append(f"Server: {response_data['Server']}")
    data.append(f"Content-Type: {response_data['Content-Type']}")
    data.append(f"Content-Length: {response_data['Content-Length']}")

    data.append('\nRedirects')
    data.append('-'*40)

    if response_data['Redirects']['Detected']:
        data.append('Redirect detected')
        data.append(f"Final URL: {response_data['Redirects']['Final-URL']}")
    else:
        data.append('No redirects')

    data.append(f"\nCookies: {len(response_data['Cookies'])}")

    if full_info:
        data.append('\nHeaders')
        data.append('-'*40)

        for key, value in response_data['Headers'].items():
            data.append(f'{key}: {value}')

        data.append('\nCookies')
        data.append('-'*40)

        for cookie in response_data['Cookies']:
            data.append(f"{cookie['Name']} = {cookie['Value']}")
            data.append(f"Domain: {cookie['Domain']}")
            data.append(f"Path: {cookie['Path']}")
            data.append(f"Expires: {cookie['Expires']}\n")

        data.append('\nBody Preview (first 1000 letters)')
        data.append('-'*40)

        body = response_data['Body'][:1000].decode()

        data.append(body)

    return '\n'.join(data)

def save_report(report, response_data):
    with open('report.txt', 'w') as f:
        f.write(report)
    with open('page.html', 'wb') as f:
        f.write(response_data['Body'])