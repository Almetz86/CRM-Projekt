import json
from helper_functions import rahme_ein

def update(x,y):
    rahme_ein("Wich Entry should be updated?\nPlease enter the id!")
    try:
        choice = int(input("> "))
    except ValueError:
        rahme_ein("only full numbers are allowed")

    with open(r"data/data.json","r",encoding="utf-8") as file:
        data = json.load(file)
    
    entity = data.get(y,[])
    all_id = [item["id"] for item in entity]

    try:
        if choice in all_id:
            entry =  [item for item in entity if item["id"] == choice]
            x.remove("id")
            x.remove("created_at")
            rahme_ein(x)
            rahme_ein("Wich key should be updated?")
            key = input("> ")
            if key in x:
                rahme_ein("enter the new value")
                value = input("> ")
                entry[0][key] = value
                
                with open(r"data/data.json", "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
            else:
                rahme_ein("key not found")

        else:
            rahme_ein("id not found")
    except UnboundLocalError:
        rahme_ein("wrong input given")
    