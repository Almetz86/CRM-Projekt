from helper_functions import rahme_ein
from CRUD import create,read,update,delete

def crud_sub_menu(x,y):
    if y == 0:
        return
    
    elif y == 1:
        create(x)

    elif y == 2:
        read(x)

    elif y == 3:
        update(x)

    elif y == 4:
        delete(x)
    
    