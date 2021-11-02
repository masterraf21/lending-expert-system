import json
import sys


def json_file_to_dict(file_path: str) -> dict:
    try:
        f = open(file_path)
        data = json.load(f)
        return dict(data)
    except:
        sys.exit("File not found")
