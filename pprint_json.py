import json
import sys


def load_data(filepath):
    with open(filepath, "rt", encoding="utf8") as data_file:
        return json.loads(data_file.read())


def pretty_print_json(data):
    print(json.dumps(data,indent="    ", ensure_ascii=False))


if __name__ == '__main__':
    pretty_print_json(load_data(sys.argv[1]))
