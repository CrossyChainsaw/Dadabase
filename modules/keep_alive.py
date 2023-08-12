from classes.Xos import Xos
os = Xos()

#import os
from flask import Flask, request
from threading import Thread
from modules.data import read_link_data 
from modules.ps4.ps4 import load_data

app = Flask('')

brawlhalla_nl_server_id = 1047987261905584128

@app.route('/')
def home():
  return "Hello World!"



@app.route("/test")
def test():
  id = request.args.get('id')
  print("id i got: " + str(id))
  return read_link_data()

@app.route("/get_links")
def show():
  api_key = request.args.get('api_key')
  id = request.args.get('id')
  if api_key == os.environ[3]:
    return read_link_data(id)

@app.route("/get_ps4_players/api_key=" + os.environ[3])
def show_ps4_players():
  server_id = request.args.get('id')
  return load_data(server_id)

def run():
  app.run(host='0.0.0.0', port=27046)


def keep_alive():
  t = Thread(target=run)
  t.start()