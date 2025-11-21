import json
from helper_functions import rahme_ein
from CRUD import create,read,update,delete

def CRUD_menu(x):
    while True:
        rahme_ein("0 > Exit\n1 > create\n2 > read\n3 > update\n4 > delete")
        choice = int(input("> "))

        if choice == 0:
            return

        elif choice == 1:
            create(x[0],x[1])

        elif choice == 2:
            read(x[1])

        elif choice == 3:
            update(x[0],x[1])

        elif choice == 4:
            delete(x[1])

