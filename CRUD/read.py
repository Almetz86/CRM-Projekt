import json
from helper_functions import rahme_ein

def read(x):
    with open(r"data/data.json","r",encoding="utf-8") as file:
        data = json.load(file)
        entity = data.get(x)
    rahme_ein(json.dumps(entity,indent=4,ensure_ascii=False))