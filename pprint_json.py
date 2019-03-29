import json
import sys
import argparse


def load_data(filepath):
    with open(filepath, 'rt', encoding='utf8') as file_with_data:
        return json.loads(file_with_data.read())


def print_pretty_json(json_string):
    print(json.dumps(json_string, indent=4, ensure_ascii=False))

def parse_filepath():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath', required=True)
    namespace = parser.parse_args()
    return namespace.filepath

if __name__ == '__main__':
    filepath = parse_filepath()
    try:
        print_pretty_json(load_data(filepath))
    except FileNotFoundError:
        exit("bars.py: error: the data file was not found.")  
    except json.decoder.JSONDecodeError:
        exit("bars.py: error: the data file is incorrect.")  