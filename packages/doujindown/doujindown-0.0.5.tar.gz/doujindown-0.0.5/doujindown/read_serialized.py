import pandas as pd
from tabulate import tabulate
import json
import yaml

import os

# reading serialized formats *.json|*.yml etc\

# returns true path to p 
def rootp(path: str) -> str:
    root = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(root, path)

# SIDE EFFECTS - prints
# read csv to pretty repr
def pretty_csv(path: str) -> str:
    pretty = pd.read_csv(path, encoding='utf-8', sep=',')
    pretty = tabulate(pretty, headers='keys', tablefmt='simple', showindex=False)
    return pretty

# read .json
def read_json(path: str) -> dict:
    with open(path, 'r') as registry_file:
        json_dict = json.loads(registry_file.read())

    if not json_dict: 
        print(f'ERROR: empty {path} please add the sites and their associated scrapers as k, v pairs')
        raise ValueError
    
    return json_dict

# read .yml
def read_yml(path: str) -> dict:
    with open(rootp(path), 'r') as settings_yml:
        yml_dict = yaml.safe_load(settings_yml)
    return yml_dict

# read .txt
def read_txt(path: str) -> str:
    with open(path, 'r') as fh:
        txt = fh.read()
    return txt

if __name__ == "__main__":
    mirrors = read_json(rootp('./conf/mirrors.json'))
    print(mirrors['sites'])

if __name__ == '__main__':
    print(read_txt(rootp('./conf/doujindown.txt')))