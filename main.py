#!/usr/bin/python3

from requests import get
from time import sleep
import sys


def main(url, filename):
    test = get(url)
    if test.status_code == 200:
        print('\033[1;32m[+]\033[m OK')
        sleep(0.1)
        print('testing...')
        print()
        with open(filename, 'r') as f:
            lines = f.readlines()
            for l in lines:
                new_url = f'{url}/{l}'
                r = get(f'{new_url}')
                if r.status_code == 200:
                    print(f'\033[1;32m[+] True\033[m {new_url}')
                else:
                    print(f'\033[1;31m[-] False\033[m {new_url}')

    else:
        print('\033[1;31mError:\033[m ', test.status_code)
        sys.exit(1)
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./main.py https://site.com wordlist.txt")
        sys.exit(1)
    
    url = sys.argv[1]
    filename = sys.argv[2]
    main(url, filename)


