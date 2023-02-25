import sys
import json

"""
Simple script to extract all keys from a given JSON input file.

The script currently handles JSON objects and JSON lists

usage: python3 extract_keys.py <path_to_json_file>
"""

# Load the JSON file
with open(sys.argv[1], encoding='utf-8') as f:
    data = json.load(f)

# Extract all keys from the JSON data
keys = []


def extract_keys(obj, parent_key=''):
    if isinstance(obj, dict):
        for key in obj:
            if parent_key:
                new_key = parent_key + '.' + key
            else:
                new_key = key
            keys.append(new_key)
            extract_keys(obj[key], new_key)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            new_key = parent_key + '.' + str(i) if parent_key else str(i)
            extract_keys(item, new_key)


extract_keys(data)

# Print all the keys joined with dots to the console
for key in keys:
    print(key)
