from contextlib import nullcontext

import requests
import hashlib
import sys

# encoding password
def api_password_checker(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first5_char)
    # print(response.text)
    # print(sha1_password)
    return separate_and_loop(response, tail)

# running pasword through server
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'
    res = requests.get(url + query_char)
    if res.status_code != 200:
        raise RuntimeError(res.status_code)
    return res

# decoding output and getting count
def separate_and_loop(hash_counter, tail_hash):
    separate_response = (line.split(':') for line in hash_counter.text.splitlines())
    for hashes, count in separate_response:
        if hashes == tail_hash:
            # print(count)
            return count
    # print(separate_response)


def main():
    with open('passwords.txt', 'r') as f:
        each_password = [item for line in f.read().splitlines() for item in line.split(' ') if item != ''] # splitting each passwoords in passwords.txt
        for password in each_password:
            count = api_password_checker(password)
            if count:
                print(f'{password} has been pawned {count} times')
            else:
                print(f'congratulations!! {password} has not been pawned')
            # print(password)
        # print(each_password)





main()
# api_password_checker('123')

# request_api_data('aaf4c')
