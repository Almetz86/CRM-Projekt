from helper_functions import rahme_ein
from entities import entities
from .crud_menu import CRUD_menu

def main_menu():
    while True:
        rahme_ein("0 > Exit\n1 > Customers\n2 > Leads\n3 > Tasks")

        choice = int(input("> "))

        if choice == 0:
            rahme_ein("Program finished")
            return

        CRUD_menu(entities(choice))