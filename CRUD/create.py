import json
from helper_functions import rahme_ein

def create(x):
    for i in x:
        keys = list(i.keys())
        break
    new_entity = {}
    for key in keys:
        if key.lower() != "id":
            rahme_ein(f"Enter the new {key}")
            value = input("> ")
            new_entity[key] = value
        else:
            value = max([a[key] for a in x]) + 1
            new_entity[key] = value
    x.append(new_entity)
    rahme_ein(json.dumps(x,indent=4,ensure_ascii=False))