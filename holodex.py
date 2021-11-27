import subprocess
import requests
import re
import sys, getopt
import os


def main(argv):
    api_key = input("api_key: ")
    url = "https://holodex.net/api/v2/live"
    req_body = url
    try:
        opts, args = getopt.getopt(argv,"hlu")
    except getopt.GetoptError:
        print ('holodex.py -h for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('see github or something, maybe i will make a man page in the future lol')
            sys.exit()
        if opt == "-l":
            language = arg #filter by language
            print("lang ="+language)
            req_body += "?lang="+language
        if opt == "-o":
            org = arg #filter by organization
            print("org ="+org)
            req_body += "?org="+org
    r = requests.get(req_body)
    print(r.text)
if __name__ == "__main__":
   main(sys.argv[1:])
