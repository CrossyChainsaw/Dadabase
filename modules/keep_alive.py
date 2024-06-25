import os
from flask import Flask, request
from threading import Thread
from Dadabase.modules.data_management import read_data, CLANS_DATA_PATH, SERVERS_DATA_PATH
from Dadabase.modules.env import env_variable

DADABASE_API_KEY = env_variable("DADABASE_API_KEY")
HOST_PORT = env_variable("HOST_PORT")
API_ERROR_MSG = "please provide a valid api_key"
ID_ERROR_MSG = "please provide a valid ID"

app = Flask('')

@app.route('/')
def home():
  return "Hello World!"

@app.route(f'/get_server_data')
def get_server_data():
  api_key = request.args.get('api_key')
  server_id = request.args.get('id')
  if api_key == DADABASE_API_KEY:
    try:
      return read_data(SERVERS_DATA_PATH, server_id)
    except FileNotFoundError:
      return ID_ERROR_MSG
  else:
    return API_ERROR_MSG

@app.route(f'/get_clan_data')
def get_clan_data():
  api_key = request.args.get('api_key')
  clan_id = request.args.get('id')
  if api_key == DADABASE_API_KEY:
    try:
      return read_data(CLANS_DATA_PATH, clan_id)
    except FileNotFoundError:
      return ID_ERROR_MSG
  else:
    return API_ERROR_MSG

def run():
  app.run(host='0.0.0.0', port=HOST_PORT)


def keep_alive():
  t = Thread(target=run)
  t.start()
