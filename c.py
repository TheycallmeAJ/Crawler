from flask import Flask, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    target_url = request.json['url']
    vulnerabilities = []

    # Crawl the target application
    response = requests.get(target_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Identify potential points of vulnerability
    for form in soup.find_all('form'):
        if form['method'] == 'post':
            action_url = target_url + form['action']
            vulnerabilities.append(action_url)

    # Scan for common vulnerabilities
    for vulnerability in vulnerabilities:
        # Check for SQL injection
        payload = "' OR 1=1 --"
        response = requests.get(vulnerability, params={'data': payload})
        if 'error' not in response.text:
            return 'Vulnerability found at {}: SQL injection'.format(vulnerability)

        # Check for cross-site scripting (XSS)
        payload = "<script>alert('XSS')</script>"
        response = requests.get(vulnerability, params={'data': payload})
        if 'alert' in response.text:
            return 'Vulnerability found at {}: cross-site scripting (XSS)'.format(vulnerability)

    return 'No vulnerabilities found.'

if __name__ == '__main__':
    app.run(debug=True)
