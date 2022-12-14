#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 09:52:08 2022

@author: jacob
"""
from CRUD.CRUD import *
import pymongo

Response = CRUD()


#隨機新增帳號
for _ in range(1):
    # print(_)
    nikename = RandomWord()
    password= RandomWord()
    email = RandomAccount()
    
    Response.signup(nikename,email,password,PriHea = True)



# 修改密碼
print(Response.admin())
Response.revise(email,password)




# 刪除所有帳號
accounts = Response.admin()
for account in accounts:
    Response.remove(account['email'])
    print(f'已刪除{account}')


ServerPassword = 'test123'

client = pymongo.MongoClient(f"mongodb+srv://test:{ServerPassword}@test.qk4mnho.mongodb.net/?retryWrites=true&w=majority"
 ,tlsAllowInvalidCertificates=True)

db = client.member_system
collection = db.user
cursor = collection.find()


