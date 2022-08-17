#!/usr/bin/env python3


import argparse
import json
import requests
import sys
from termcolor import *
import time







print(colored(""" 
\033[3m


Hi, This is a variant of the original Waybackurls on Github for finding subdomains modified by AJ called BugHunter2112 to make .txt files instead of 
.json (Optional), decodes the url (Optional), and finds You Open Redirect Bugs For Faster Bug Hunting (If Wanted) and uses the original site (non-Wayback Machine site) (Optional) prompted by input and Tell's You The Total Finding Time,  Happy Bug Hunting!


""", 'cyan', attrs=['bold']))


# b = input("How many second time difference do you want to make to not make any noise: ")


parser = argparse.ArgumentParser()

h = input("Do you want to find Open Redirect Vulnerabilities (y/n): ")

i = float(input(("How Much Do You Want The Page Timeout To Be (In Seconds): ")))




x = input("Do you want to decode the URL (y/n): ")
y = input("Do you want .txt (y/n): ")
z = input("Do you want to use Wayback machine to find suburls (y/n): ")



print(colored("\n\n\nIMPORTANT! Please Check If The Site Has The Bug Bounty Program\n\n\n", attrs=['bold']))


time.sleep(2)


presentinrelativetofuture = time.time()

def waybackurls(host, with_subs):
    if with_subs:
        url = 'http://web.archive.org/cdx/search/cdx?url=*.%s/*&output=json&fl=original&collapse=urlkey' % host

    elif z.lower() == "n":
        url = "http://" + host
    else:
        url = 'http://web.archive.org/cdx/search/cdx?url=%s/*&output=json&fl=original&collapse=urlkey' % host
    
    try:

        global presentinrelativetofuture2

        global presentinrelativetofuture



        r = requests.get(url, timeout=i)

        presentinrelativetofuture2 = time.time()



        r.raise_for_status()



    except:

        print("Sorry, An Error Occurred")

    results = str(r.json()).replace("[", "").replace("]", "").replace(", ", "\n").replace("'", "")
    return results[1:]


if __name__ == '__main__':
    argc = len(sys.argv)




    if argc < 2:
        print('Usage:\n\tpython3 BugHunter2212.py <url> <include_subdomains:optional>?')
        sys.exit()

    host = sys.argv[1]
    with_subs = False
    if argc > 3:
        with_subs = True
    urls = waybackurls(host, with_subs)
    if urls:
        if y.lower() == "n":
            filename = '%s-waybackurls.json' % host
            with open(filename, 'w') as file:
                if x.lower() == "y":
                    urls = requests.utils.unquote(urls).replace(" /", "")
                    json.dump(urls, file)


                    print('[*] Saved results to %s' % filename)


        elif y.lower() == "y":
            filename = '%s-waybackurls.txt' % host

        else:
            print("Please enter either (y/n) in your next attempt")
        with open(filename, 'w') as file2:
            if x.lower() == "y":
                urls = requests.utils.unquote(urls).replace(" /", "")

                file2.write(urls)
        print('[*] Saved results to %s' % filename)

        calculatedtime = presentinrelativetofuture + time.time()




        if h.lower() == "y":

            with open(filename) as file:
    
                file = file.readlines()

                for line in file:

                    if "?r" in line.lower():

                        print(line)

        
        print(colored("\n\n[*] Total Finding Time: " + str(calculatedtime) + " Seconds"))








        

    else:
        print('[-] Found nothing in the URL, Try Using Another URL')
