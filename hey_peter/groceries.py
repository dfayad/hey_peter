
#update list
from update_json import add_item

def add_grocery(item):
    if item != '':
        add_item('data.json', item)
