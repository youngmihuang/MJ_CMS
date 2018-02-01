# coding: utf-8
import pandas as pd
import numpy as np
from datetime import datetime
import time
import json
import redis
import xlrd

# set up redis
redis_ip = "redis_huang"
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
        # metadata
        meta = {}
        meta["bannerImage"] = "https://youngmihuang.github.io/MJ_CMS/Demo3/adjust" + data["bannerImage"][row]
        meta["offerLink"] = data["offerLink"][row]
        meta["offerName"] = data["offerName"][row]
        offer["metaData"] = meta
        offer_DB.append(offer)
    return(offer_DB)

# put dict into Redis
def contentDB_ETL(data):

    for i in range(len(data)):
        contentDB ={}
        contentDB["offerId"] = data[i]["offerId"]
        contentDB["moduleId"] = data[i]["moduleId"]
        contentDB["metaData"] = data[i]["metaData"]
        conn.set(data[i]["itemId"].decode("utf-8"),json.dumps(contentDB, ensure_ascii=False)) # to json

# put offerData to redis
# offer_content
content = pd.read_excel("data/offerData_image.xlsm")
offer = offerDB_tran(content)
offer_to_Redis = contentDB_ETL(offer)
