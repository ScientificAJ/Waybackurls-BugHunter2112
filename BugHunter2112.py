#!/usr/bin/env python3


import json
import requests
import sys




print(""" 

Hi, This is a variant of the original Waybackurls on Github for finding subdomains modified by AJ called BugHunter2212 to make .txt files instead of .json if wanted, decodes the url if wanted and uses the original site (non-Wayback Machine site) if wanted prompted by input


Happy Bug Hunting!

""")

x = input("Do you want to decode the URL (y/n")
y = input("Do you want .txt Yes or No (y/n) ")
z = input("Do you want to use Wayback machine to find suburls (y/n): ")


def waybackurls(host, with_subs):
    if with_subs:
        url = 'http://web.archive.org/cdx/search/cdx?url=*.%s/*&output=json&fl=original&collapse=urlkey' % host

    elif z.lower() == "n":
        url = "http://" + host
    else:
        url = 'http://web.archive.org/cdx/search/cdx?url=%s/*&output=json&fl=original&collapse=urlkey' % host
    r = requests.get(url)
    results = str(r.json()).replace("[", "").replace("]", "").replace(", ", "\n").replace("'", "")
    return results[1:]


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 2:
        print('Usage:\n\tpython3 BugHunter2212.py <url> <include_subdomains:optional> <decode_url:optional(Yes or No)> <want_txt:optional(Yes or No)>?')
        sys.exit()

    host = sys.argv[1]
    with_subs = False
    if argc > 3:
        with_subs = True
    urls = waybackurls(host, with_subs)
    if urls:
        if y.lower() == "n":
            filename = '%s-waybackurls.json' % host
            with open(filename, 'w') as f:
                if x.lower() == "y":
                    urls = requests.utils.unquote(urls).replace(" /", "")
                    urls = json.dumps(urls)

        elif y.lower() == "y":
            filename = '%s-waybackurls.txt' % host

        else:
            print("Please enter either yes or no in your next attempt")
        with open(filename, 'w') as f:
            if x.lower() == "y":
                urls = requests.utils.unquote(urls).replace(" /", "")

                f.write(urls)
        print('[*] Saved results to %s' % filename)

    else:
        print('[-] Found nothing in the URL, Try Using Another URL')
