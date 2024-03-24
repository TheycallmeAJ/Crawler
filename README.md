# Mini-Project_Scanner
This Python script is a simple web vulnerability scanner built using Flask, a popular web framework. Here's a brief description of its functionality:

1. **Flask Application Setup**: The script first sets up a Flask application. Flask is a micro web framework written in Python.

2. **Route Definition**: A route `/scan` is defined which listens for `POST` requests. This route acts as the entry point for the scanning process.

3. **Scanning Process**: When a `POST` request is received at `/scan`, the following steps are performed:
    - The target URL to be scanned is extracted from the request data.
    - The script sends a `GET` request to the target URL and parses the response using BeautifulSoup, a Python library for parsing HTML and XML documents.
    - It then identifies all forms in the parsed HTML that use the `POST` method. The action URLs of these forms are considered as potential points of vulnerability and are added to a list.
    - Each potential point of vulnerability is then checked for common vulnerabilities:
        - **SQL Injection**: This is done by sending a payload that manipulates the SQL query. If the response does not contain 'error', it is considered as a potential SQL injection vulnerability.
        - **Cross-Site Scripting (XSS)**: This is done by sending a payload that includes a script. If the response contains 'alert', it is considered as a potential XSS vulnerability.
    - If any vulnerability is found, a message is returned indicating the type of vulnerability and the URL where it was found. If no vulnerabilities are found, a message indicating the same is returned.

4. **Application Execution**: Finally, the Flask application is run with debugging enabled. This starts a local development server that can be used to interact with the application.

Please note that this is a basic vulnerability scanner and might not catch all vulnerabilities. It is recommended to use professional tools and services for thorough security testing. Also, always ensure you have permission before scanning a website or web application. Unauthorized scanning can be illegal.