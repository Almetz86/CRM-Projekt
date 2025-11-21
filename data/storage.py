import json

def write(x,y):
    
    with open(r"data/data.json","r",encoding="utf-8") as file:
        data = json.load(file)

    entity = data.get(y,[])
    entity.append(x)
    data[y] = entity

    with open(r"data/data.json","w",encoding="utf-8") as file:
        json.dump(data,file,indent=4,ensure_ascii=False)

def get_id(x):
    with open(r"data/data.json","r",encoding="utf-8") as file:
        data = json.load(file)
    
    entity = data.get(x,[])
    all_id = [item["id"] for item in entity] or [0]
    free_id = [i for i in range(1,max(all_id) + 2) if i not in all_id]
    new_id = min(free_id)
    return new_id 
