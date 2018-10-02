
#update list
from update_json import add_item

def add_grocery(item):
    if item != '':
        #items.append(item)
        add_item('data.json', item)



