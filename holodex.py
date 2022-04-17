#!/usr/bin/env python3
import requests
import re
import sys
import argparse
from datetime import datetime

def main(argv):
    url = "https://holodex.net/api/v2/live?"
    watch = "https://holodex.net/watch/"
    req_body = url
    parser = argparse.ArgumentParser(description='fetch current live vtubers from holodex')
    parser.add_argument('--org',
                        help='filter by organization e.g Hololive, Nijisanji')
    parser.add_argument('-l', type=int,
                        help='limit the output by an integer')
    parser.add_argument('--key',
                        help='API key')
    parser.add_argument('--status',
                        help='status of the video: new,upcoming,live,past,missing')
    args = parser.parse_args()
    r = requests.get(req_body,headers={'X-APIKEY': '%s' % args.key}, params = {'org': args.org, 'limit': args.l, 'status' : args.status})
    data = r.json()
    for stream in data:
        print('title: ' + stream['title'])
        if stream['channel']['english_name']:
            print('name: ' + stream['channel']['english_name'])
        else:
            print('name: ' + stream['channel']['name'])
        print('starts: ' + str(datetime.strptime(stream['available_at'], '%Y-%m-%dT%H:%M:%S.%fZ')))
        print('url: ' + watch+stream['id']+'\n')
        
if __name__ == "__main__":
   main(sys.argv[1:])
