import json
from helper_functions import rahme_ein
from menus.crud_sub_menu import crud_sub_menu

def CRUD_menu(x):
    while True:
        rahme_ein("0 > Exit\n1 > create\n2 > read\n3 > update\n4 > delete")
        choice = int(input("> "))

        if choice == 0:
            return

        crud_sub_menu(x,choice)

