# coding: utf-8
import pandas as pd
import numpy as np
from datetime import datetime
import time
import json
import redis
import xlrd

# offer_content
content = pd.read_excel("offerData_image.xlsm")
# 設定Redis
# redis_ip = "localhost"
redis_ip = "redis"
conn = redis.Redis(host=redis_ip, port=6379, db=0)




# offer to dict
def offerDB_tran(data):
    offer_DB =[]
    rows = len(data)
    for row in range(rows):
        offer ={}
        offer["offerId"] = data["offerId"][row]
        offer["moduleId"] = data["moduleId"][row]
        offer["itemId"] = data["moduleId"][row] + str(data["offerId"][row])
        #meta內放置的內容
        meta = {}
        meta["bannerImage"] = data["bannerImage"][row]
        meta["offerLink"] = data["offerLink"][row]
        offer["metaData"] = meta
        offer_DB.append(offer)
    return(offer_DB)

# put dict into Redis
def contentDB_ETL(data):

    for i in range(len(data)):
        content ={}
        content["offerId"] = data[i]["offerId"]
        content["moduleId"] = data[i]["moduleId"]
        content["metaData"] = data[i]["metaData"]
        conn.set(data[i]["itemId"].decode("utf-8"),json.dumps(content, ensure_ascii=False))

# put offerData to redis
offer = offerDB_tran(content)
offer_to_Redis = contentDB_ETL(offer)
