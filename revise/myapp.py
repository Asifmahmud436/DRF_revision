import requests
import json

URL = "http://127.0.0.1:8000/studentApi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    response = requests.get(url = URL, data = json_data)
    data = response.json()
    print(data)

# get_data()

def post_data():
    data = {
        'name':'Rohit',
        'roll':100,
        'city': "Mohesshori"
    }
    
    json_data = json.dumps(data)
    response = requests.post(url=URL, data=json_data)
    print(response.json())
    
def update_data():
    data = {
        'id':1,
        'name':'Asif',
        
    }
    
    json_data = json.dumps(data)
    response = requests.put(url=URL, data=json_data)
    print(response.json())

def delete_data():
    data = {'id':4 }
    
    json_data = json.dumps(data)
    response = requests.delete(url=URL, data=json_data)
    print(response.json())
    
# post_data()
get_data()
# update_data()
# delete_data()