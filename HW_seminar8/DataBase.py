import json


def save_db(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, default=lambda obj: obj.__dict__)


def load_db(path):
    with open(path,'r') as f:
        try:
            return json.load(f)
        except ValueError:
            return None