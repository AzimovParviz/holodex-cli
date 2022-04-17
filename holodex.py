#!/usr/bin/env python3
import subprocess
import requests
import re
import sys
import os
import argparse

def main(argv):
    url = "https://holodex.net/api/v2/live"
    req_body = url
    parser = argparse.ArgumentParser(description='fetch current live vtubers from holodex')
    parser.add_argument('--org',
                        help='filter by organization e.g Hololive, Nijisanji')
    parser.add_argument('-l', type=int,
                        help='limit the output by an integer')
    parser.add_argument('--key',
                        help='API key')
    args = parser.parse_args()
    if args.org:
        req_body += "?org="+args.org
    if args.l:
        req_body += "&?limit="+str(args.l)    
    r = requests.get(req_body,headers={'X-APIKEY': '%s' % args.key})
    data = r.json()
    for stream in data:
        print('title: ' + stream['title'])
        print('name: ' + stream['channel']['name'])
        
if __name__ == "__main__":
   main(sys.argv[1:])
