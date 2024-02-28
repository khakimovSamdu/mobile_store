from tinydb import TinyDB
import random
import requests
tindb = TinyDB('db.json', indent=4)
def get_brends():
    brends = tindb.tables()
    return list(brends)
def get_brend():
    brend = random.choice(get_brends())
    return brend
def get_brend_document():
    brend = tindb.table(get_brend()).all()
    brend = random.choice(brend)
    return brend

def send_data():
    url = 'http://127.0.0.1:8000/mobile/add/'
    data = get_brend_document()
    r = requests.post(url, json=data)
    return r.status_code

print(send_data())

