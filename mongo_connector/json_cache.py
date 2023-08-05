import json

def result_serialize(file_name:str, obj: dict):
    with open(file_name, 'w') as f:
        json.dump(obj, f)

def read_json(file_name):
    with open(file_name, 'r') as f:
        updated_kv = json.load(f)
    
    return updated_kv