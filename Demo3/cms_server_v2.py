
# coding: utf-8

import pandas as pd
import json
import datetime
import calendar
from flask import Flask ,request, jsonify

import time
import redis

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
redis_ip = "redis"
# redis_ip = "localhost"
redis_store = redis.Redis(host= redis_ip, port=6379, db=0)
# redis_store = redis.Redis(host="localhost", port=6379, db=0)



@app.route("/offer",methods=["POST"])
def getItemId():
  content = request.get_json(force=True)
  return jsonify([json.loads(redis_store.get(c["moduleId"]+c["offerId"])) for c in content])



# get one metadata at one time
# @app.route("/offer",methods=["GET"])
# def getItemId():
#   moduleId = request.args.get("moduleId")
#   print moduleId
#   offerId = request.args.get("offerId")
#   print type(offerId)
#   metaData = (redis_store.get(moduleId + offerId))
#   metaData = json.loads(metaData)
#   res = jsonify(metaData) #在網頁上轉為json
#   res.headers["Content-Type"] = "application/json; charset=utf-8"
#   return res


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=6020)
