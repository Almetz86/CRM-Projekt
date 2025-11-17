import json
from helper_functions import rahme_ein


def CRUD_menu(x):
    while True:
        rahme_ein(f"Current list\n\n{json.dumps(x,indent=4,ensure_ascii=False)}")
        rahme_ein("0 > Exit\n1 > create\n2 > read\n3 > update\n4 > delete")

        choice = int(input("> "))

        if choice == 0:
            return
