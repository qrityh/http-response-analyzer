import argparse
from analyzer import analyze

parser=argparse.ArgumentParser(
    prog='HTTP-r Analyzer',
    description='HTTP Response analyzer (also analyzes cookies)',
    epilog='Thanks for using %(prog)s!'
)
parser.add_argument('url')
parser.add_argument('-fi', '--fullinfo', 
                    action='store_true',
                    help="Show full information about HTTP response")
parser.add_argument('-sf', '--savefile', 
                    action='store_true',
                    help='Save analysis results to a file')

args=parser.parse_args()

url=args.url
if not (url.startswith('http://') or url.startswith('https://')):
    url='http://'+url

analyze(url, args.fullinfo, args.savefile)