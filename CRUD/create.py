import json
from datetime import datetime
from helper_functions import rahme_ein
from data import write,get_id

def create(x,y):
    new_entity = {}

    for key in x:
        if key == "created_at":
            continue

        elif key != "id":
            rahme_ein(f"Enter the new {key}")
            value = input("> ")
            new_entity[key] = value

        else:
            value = get_id(y)
            new_entity[key] = value

    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    new_entity["created_at"] = timestamp
    write(new_entity,y)