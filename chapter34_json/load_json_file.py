# load_json_file.py

import json

def load_json_file(path):
    with open(path) as fh:
        j_obj = json.load(fh)
    print(type(j_obj))


if __name__ == '__main__':
    load_json_file('example.json')