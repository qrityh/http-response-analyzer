from urllib.request import *
from client import get_url_info
from output_data import *

def analyze(url, full_info, save_to_file):
    request_dictionary=get_url_info(url)
    if request_dictionary == None: return
    data=collect_data(
        url,
        request_dictionary
    )
    report=make_report(data, full_info)
    if save_to_file:
        save_report(report,data)
    print(report)

def collect_data(url, request_dictionary):
    response_data={
            'URL':{},
            'Headers':{},
            'Cookies':[],
            'Redirects':{
                'Detected':False,
                'Final-URL':''
            },
            'Status':0,
            'Server':"",
            'Content-Type':"",
            'Content-Length':0,
            'Body':""
        }
    resp=request_dictionary['Response']
    parsed_resp=request_dictionary['Parsed-Response']
    cookies=request_dictionary['Cookies']
    response_data['Status']=resp.status
    response_data['Server']=resp.getheader('Server')
    for key, value in parsed_resp._asdict().items():
        response_data['URL'][key]=value
    for key,value in resp.headers.items():
        response_data['Headers'][key]=value
    for cookie in cookies:
        response_data['Cookies'].append({
                                'Name': cookie.name,
                                'Value': cookie.value,
                                'Domain': cookie.domain,
                                'Path': cookie.path,
                                'Expires': cookie.expires}
                                )
    response_data['Content-Type']=resp.getheader('Content-Type')
    response_data['Content-Length']=resp.getheader('Content-Length')
    response_data['Redirects']['Detected']=(url!=resp.geturl())
    response_data['Redirects']['Final-URL']=resp.geturl()
    response_data['Body']=resp.read()
    resp.close()
    return response_data