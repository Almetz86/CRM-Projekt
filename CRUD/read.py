import json
from helper_functions import rahme_ein

def read(x):
    rahme_ein(json.dumps(x,indent=4,ensure_ascii=False))