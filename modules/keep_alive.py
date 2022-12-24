import os
from flask import Flask, request
from threading import Thread
from modules.data import read_link_data 
from modules.ps4.ps4 import load_data

app = Flask('')

@app.route('/')
def home():
  return "Hello World!"

@app.route('/get_links/api_key=' + os.environ['API_KEY_DADABASE'])
def show_links():
  return read_link_data()

@app.route('/get_ps4_players/api_key=' + os.environ['API_KEY_DADABASE'])
def show_ps4_players():
  server_id = request.args.get('id')
  return load_data(server_id)

def run():
  app.run(host='0.0.0.0', port=1001)


def keep_alive():
  t = Thread(target=run)
  t.start()
