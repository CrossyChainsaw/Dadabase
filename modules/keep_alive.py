import os
from flask import Flask
from threading import Thread
from modules.data import read_link_data 

app = Flask('')

@app.route('/')
def home():
    return "Hello World!"

@app.route('/get_links/api_key=' + os.environ['API_KEY_DADABASE'])
def show():
  return read_link_data()

def run():
    app.run(host='0.0.0.0', port=1001)


def keep_alive():
    t = Thread(target=run)
    t.start()
