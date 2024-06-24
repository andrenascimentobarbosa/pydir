#!/usr/bin/python3


"""
like-dirb tool, search for hidden pages on a web application returnin Try or False.
"""
 


# modules
from requests import Session
import sys
from urllib.parse import urlparse


def main(url, file):
    # Parse the URL to extract the domain name
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc.replace('.', '-')
    output_file = f'found_ones-{domain_name}.txt'

    with Session() as session:
        try:
            test = session.get(url)
            if test.status_code == 200:
                print(f'\033[1;32mOK\033[m {test.status_code}')
                print(f'Search for pages on {url}')
                with open(file, 'r') as f:
                    lines = f.readlines()
                    for l in lines:
                        new_url = f'{url}/{l}'
                        r = session.get(new_url)
                        if r.status_code == 200:
                            print(f'\033[1;32m[+]\033[m True: {new_url}'.strip())
                            with open(f'found_ones-{domain_name}.txt', 'a') as f:
                                f.write(f'{new_url}\n')
                        else:
                            print(f'\033[1;31m[-]\033[m False: {new_url}'.strip())

            else:
                print(f'\033[1:31mError:\033[m {test.status_code}')
                if test.status_code == 418:
                    print("I'm a teapot\nsee more: https://stackoverflow.com/questions/52340027/is-418-im-a-teapot-really-an-http-response-code")
                sys.exit(1)
        except Exception as e:
            print(f"\033[1;31mError:\033[m Coundnt't access {url} due the error {e}")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("\nUsage: ./script.py https://site.com list.txt\n")
        sys.exit(1)

    url = sys.argv[1]
    file = sys.argv[2]
    main(url, file)
