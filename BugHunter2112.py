#!/usr/bin/env python3

"""


Hi, This is a variant of the original Waybackurls by mhmdiaa on Github for finding subdomains modified by AJ called BugHunter2212 to make .txt files instead of .json if wanted and decodes the url if wanted prompted by input


Happy Bug Hunting!

Credits


Orignal Code by @mhmdiaa

""


import json
import requests
import sys




print(""" 

Hi, This is a variant of th original Waybackurls on Github for finding subdomains modified by AJ called BugHunter2212 to make .txt files instead of .json if wanted and decodes the url if wanted prompted by input


Happy Bug Hunting!

""")

x = input("Do you want to decode the URL Yes or No: ")
y = input("Do you want .txt Yes or No: ")

def waybackurls(host, with_subs):
    if with_subs:
        url = 'http://web.archive.org/cdx/search/cdx?url=*.%s/*&output=json&fl=original&collapse=urlkey' % host
    else:
        url = 'http://web.archive.org/cdx/search/cdx?url=%s/*&output=json&fl=original&collapse=urlkey' % host
    r = requests.get(url)
    results = str(r.json()).replace("[", "").replace("]", "").replace(", ", "\n").replace("'", "")
    return results[1:]


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 2:
        print('Usage:\n\tpython3 BugHunter2212.py <url> <include_subdomains:optional>')
        sys.exit()

    host = sys.argv[1]
    with_subs = False
    if argc > 3:
        with_subs = True

    urls = waybackurls(host, with_subs)
    if urls:
        if y.lower() == "no":
            filename = '%s-waybackurls.json' % host
            with open(filename, 'w') as f:
                if x.lower() == "yes":
                    urls = requests.utils.unquote(urls).replace(" /", "")
                    urls = json.dumps(urls)

        elif y.lower() == "yes":
            filename = '%s-waybackurls.txt' % host

        else:
            print("Please enter either yes or no in your next attempt")
        with open(filename, 'w') as f:
            if x.lower() == "yes":
                urls = requests.utils.unquote(urls).replace(" /", "")

                f.write(urls)
        print('[*] Saved results to %s' % filename)

    else:
        print('[-] Found nothing in the URL, Try Using Another URL')
        
        
        