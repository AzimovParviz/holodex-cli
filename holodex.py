#!/usr/bin/env python3
import subprocess
import requests
import re
import sys, getopt
import os


def main(argv):
    url = "https://holodex.net/api/v2/live"
    req_body = url
    try:
        opts, args = getopt.getopt(argv,"hlo")
    except getopt.GetoptError:
        print ('holodex.py -h for help')
        sys.exit(2)
        #use argparse instead please
    for opt, arg in opts:
        if opt == '-h':
            print ('-l for language: en,ja,ch,es,ru\
            -o for organization: Hololive, Nijisanji')
            sys.exit()
        if opt == "-l":
            limit = arg #limit the output
            print("lang ="+language)
            req_body += "?lang="+language
        if opt == "-o":
            org = arg #filter by organization, ex: Hololive, Nijisanji
            print("org ="+org)
            req_body += "?org="+org
    api_key = input("api_key: ")
    r = requests.get(req_body,headers={'X-APIKEY': '%s' % api_key})
    data = r.json()
    for stream in data:
        print('title: ' + stream['title'])
        print('name: ' + stream['channel']['name'])
        
if __name__ == "__main__":
   main(sys.argv[1:])
