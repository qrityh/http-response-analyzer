from http.cookiejar import CookieJar
from urllib.request import *
from urllib.parse import urlparse
from urllib.error import HTTPError, URLError

def get_url_info(url):
    cookie_jar=CookieJar()
    opener=build_opener(HTTPCookieProcessor(cookie_jar))
    req=Request(url)
    try:
        resp=opener.open(req, timeout=10)
    except HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        return
    except URLError as e:
        print(f"URL Error: {e.reason}")
        return
    except Exception as e:
        print(f'Something went wrong! {e}')
        return
    parsed_resp=urlparse(url)
    cookies = list(cookie_jar)
    request_dictionary={
        'Response': resp,
        'Parsed-Response': parsed_resp,
        'Cookies': cookies
    }
    return request_dictionary