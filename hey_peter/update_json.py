import json

def create_json():
    data = dict()

    data['name'] = 'grocery list'
    data['list'] = []

    with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

def add_item(filename, new_elem):
    #read json
    with open(filename) as json_file:
        data = json.load(json_file)
        value = data['list']

        #rewrite
        data['list'].append(str(new_elem))
        print(data)
    with open(filename, 'w') as outfile:
            json.dump(data, outfile)

def delete_items(filename):
    with open(filename) as json_file:
        data = json.load(json_file)

    #rewrite
        data['list']=[]
    with open(filename, 'w') as outfile:
            json.dump(data, outfile)

#create_json()
#update_json('data.json', 123)
delete_items('data.json')
