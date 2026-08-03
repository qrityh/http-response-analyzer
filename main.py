from analyzer import analyze
from sys import argv

url=argv[1]
if not (url.startswith('http://') or url.startswith('https://')):
    url='http://'+url

try:
    full_info=int(input('Return all info?(flags, headers, cookies etc.) (1 or 0, default=0)\n'))
except:
    full_info=0
try:
    save_to_file=int(input('Save all output to file? (1 or 0, default=0)\n'))
except:
    save_to_file=0

analyze(url, full_info, save_to_file)