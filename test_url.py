import json
import requests
import time
import math
import sys

MESSAGE_404 = b"This page could not be found"

def get_url_lst(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data["results"]

def main(file_path):
    url_lst = get_url_lst(file_path)
    print(f"Testing {len(url_lst)} url")

    start = time.time()
    for i, url in enumerate(url_lst):
        res = requests.get(url)
        if res.status_code != 404 or MESSAGE_404 not in res._content:
            print("~~~~ ✅ FOUND SOMETHING ✅ ~~~")
            print("~~~~ ✅ FOUND SOMETHING ✅ ~~~")
            print("~~~~ ✅ FOUND SOMETHING ✅ ~~~")
            print(url)
            print("~~~~ ✅ FOUND SOMETHING ✅ ~~~")
            print("~~~~ ✅ FOUND SOMETHING ✅ ~~~")
            print("~~~~ ✅ FOUND SOMETHING ✅ ~~~")
        else:
            pass
            # print(f"{i} - {url} -> {res.status_code}")
        
        if i % 100 == 0:
            print(f"Tested {i + 1} link [{round(((i + 1) / len(url_lst)) * 100, 2)}%] - since {math.floor(time.time() - start)}s")
        
        # time.sleep(.1)
    
    print(f"Done in {math.floor(time.time() - start)}s")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python test_url.py [path/to/file.json]")
    else:
        main(sys.argv[1])