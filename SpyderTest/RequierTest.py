# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 15:30:30 2022

@author: -
"""
from CRUD.CRUD import *
import requests
import json


nikename = RandomWord()
password= RandomWord()
email = RandomAccount()
data = {'nikename':nikename,
        'email':email,
        'password':password
        }

url = 'http://127.0.0.1:5000/'
# data = {'task': 'test'}

# PUT = requests.put(f'{url}todo2', data=data).json()
# GET = requests.get(f'{url}api').json()

Response = requests.post(f'{url}api', data=data)
Response.headers
Response.json()
