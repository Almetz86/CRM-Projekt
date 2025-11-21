
def entities(x):
    customers = ["id", "name", "email", "phone", "address", "created_at"]
    leads = ["id", "name", "email", "phone", "address", "created_at"]
    tasks = ["id", "task", "note", "created_at"]
    if x == 1:
        x = customers
        y = "customers"
    elif x == 2:
        x = leads
        y = "leads"
    elif x == 3:
        x = tasks
        y = "tasks"
    return x,y