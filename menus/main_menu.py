from helper_functions import rahme_ein
from entities import entities
from .crud_menu import CRUD_menu

def main_menu():
    while True:
        rahme_ein("0 > Exit\n1 > Customers\n2 > Leads\n3 > Tasks")

        try:
            choice = int(input("> "))
        except ValueError:
            rahme_ein("only full numbers are allowed")
            continue

        if choice == 0:
            rahme_ein("Program finished")
            return
        
        elif -1 < choice < 4 :
            CRUD_menu(entities(choice))
        else:
            rahme_ein("only numbers between 0 and 3 are allowed")

        