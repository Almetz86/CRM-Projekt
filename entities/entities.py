import json
from helper_functions import rahme_ein

def entities(x):
    if x == 1:
        x = "costumers"
    elif x == 2:
        x = "leads"
    elif x == 3:
        x = "tasks"

    with open(r"C:\Umschulung\CRM Projekt\data\data.json","r",encoding="utf-8") as file:
        data = json.load(file)
    entity = data.get(x)
    rahme_ein(entity)
    from menus import CRUD_menu
    CRUD_menu()