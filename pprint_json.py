import json
import sys


def load_data(filepath):
    with open(filepath, "rt", encoding="utf8") as file_with_data:
        return json.loads(file_with_data.read())


def pretty_print_json(json_string):
    print(json.dumps(json_string, indent="    ", ensure_ascii=False))


if __name__ == '__main__':
    pretty_print_json(load_data(sys.argv[1]))
