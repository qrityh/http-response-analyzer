# http-response-analyzer

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
```
git clone https://github.com/your-username/http-response-analyzer.git
cd http-response-analyzer
```
## Usage

```bash
python main.py github.com
```

Full information:

```bash
python main.py github.com --fullinfo
```

Save report:

```bash
python main.py github.com --savefile
```

Example:
```
python3 main.py -sf t.me
########################################
HTTP Response Analyzer
########################################

URL
----------------------------------------
scheme: http
netloc: t.me
path: 
params: 
query: 
fragment: 

----------------------------------------
Status: 200
Server: nginx/1.30.1
Content-Type: text/html; charset=utf-8
Content-Length: 19990

Redirects
----------------------------------------
Final URL: https://telegram.org/

Cookies: 2
```
## Author

Daniil - qrityh

https://github.com/qrityh/http-response-analyzer

## License

MIT
