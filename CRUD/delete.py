import json
from helper_functions import rahme_ein

def delete(y):
    rahme_ein("Wich Entry should be deleted?\nPlease enter the id!")
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
            entry = next((item for item in entity if item["id"] == choice), None)
            entity.remove(entry)
            data[y] = entity
            with open(r"data/data.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            rahme_ein("entry is terminated")
        else:
            rahme_ein("entry not found")
    except UnboundLocalError:
        rahme_ein("wrong input given")