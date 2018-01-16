
# coding: utf-8

import pandas as pd
import json
import datetime
import calendar
from flask import Flask ,request, jsonify

import time
import redis
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

redis_ip = "redis_huang"
# redis_ip = "localhost"
pool = redis.ConnectionPool(host= redis_ip, port=6379, db=0, socket_timeout =  0.5)
redis_store = redis.Redis(connection_pool = pool)
# redis_store = redis.Redis(host="localhost", port=6379, db=0)


@app.route('/offer', methods = ['POST'])
def get_offer():
    try:
        content = request.get_json(force=True)
        resp = jsonify([json.loads(redis_store.get(c["moduleId"]+c["offerId"])) for c in content])
        resp.headers['Content_Type'] = 'application/json; charset=utf-8'
        resp.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'POST'

        return resp

    except:
        return jsonify([{'error': 'Your request moduleId or offerId not exist, no results', 'status': 404}])


# resp.headers['Content_Type'] = 'application/json'

# def hello2():
#   try:
#     response = requests.get('http://localhost:6020/offertest', timeout=0.4)
#   except requests.exceptions.Timeout:
#     return 'timeout'
#   return response.text




if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=6020)
