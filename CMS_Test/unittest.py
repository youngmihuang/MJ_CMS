

import os, sys
import unittest
import pandas as pd
import json
import datetime
import calendar
from flask import Flask
from flask import jsonify
import inspect, os

import requests
import urllib


class CalculatorTestCase(unittest.TestCase):

    #all named add test_
    def test_basic(self):
        self.assertEqual(1, 1)

    def test_add(self):
        pass

    def test_ResponseStatus(self):
        url = "http://0.0.0.0:6020/offer"
        data = [{'moduleId': 'A2', 'offerId': 'OFF0001'}]
        headers = {'Content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        self.assertEqual(response.status_code,200)

    def test_ResponseKey(self):
        url = "http://0.0.0.0:6020/offer"
        key = [u'moduleId',u'offerId',u'metaData' ]
        data = [{'moduleId': 'A2', 'offerId': 'OFF0001'}]
        headers = {'Content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        # list to json format
        r_trans = (response.text)[1: len(response.text)-2]
        # json to dict format
        r = json.loads(r_trans)
        # check dict key
        rk = r.keys()
        self.assertEqual(rk, key)

# def test_ResponseKey():
#     url = "http://0.0.0.0:6020/offer"
#     key = [u'metaData',u'moduleId',u'offerId']
#     data = [{'moduleId': 'A2', 'offerId': 'OFF0001'}]
#     headers = {'Content-type': 'application/json'}
#     response = requests.post(url, data=json.dumps(data), headers=headers)
#     print (response.text)[1: len(response.text)-2]
#     print type((response.text)[1: len(response.text)-2])


if __name__ == "__main__":
    # test_ResponseKey();
    unittest.main(verbosity=2)
