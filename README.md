# file-analyzer

A simple Python utility written for analyzing HTTP Responses.

# Technologies

Python

## Features

- Checks HTTP Headers
- Checks Cookies
- Saves data to file
- Checks redirects

## Installation

Clone the repository:

git clone https://github.com/your-username/http-response-analyzer.git
cd http-response-analyzer

## Usage

Run: '''python main.py'''

Example:

'''python3 .\main.py github.com
Return all info?(flags, headers, cookies etc.) (1 or 0, default=0)
0
Save all output to file? (1 or 0, default=0)
1
########################################
HTTP Response Analyzer
########################################

URL
----------------------------------------
scheme: http
netloc: github.com
path: 
params: 
query: 
fragment: 

Response
----------------------------------------
Status: 200
Server: github.com
Content-Type: text/html; charset=utf-8
Content-Length: None

Redirects
----------------------------------------
Redirect detected
Final URL: https://github.com/

Cookies: 3'''

## Author

Daniil - martiniden1707@gmail.com

https://github.com/qrityh/http-response-analyzer

## License

MIT
