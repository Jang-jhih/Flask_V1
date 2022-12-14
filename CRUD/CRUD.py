

import requests
import json
from fake_useragent import UserAgent


class CRUD:
    def __init__(self):
        
        self.url = 'http://127.0.0.1:3000'
        self.headers = {'Content-Type': 'application/json',
                   'user-agent' : UserAgent().google}
        
    def signup(self,nikename,email,password,PriHea=False):
        url = f'{self.url}/signup'
        headers = self.headers

        Dict = {'nikename':nikename,
                'email':email,
                'password':password
                }
        
        req = requests.post(url, headers=headers
                            ,data=json.dumps(Dict))
        
        
        
        data = json.loads(req.json())
        
        if PriHea == True:
            PrintHeader(req)
        else:
            print('已新增',Dict)
        return data
    
    
    
    def remove(self,email,PriHea=False):
        url = f'{self.url}/remove'
        headers = self.headers
        
        
        Dict = {'email':email}
        
        req = requests.post(url
                            ,headers=headers
                            ,data=json.dumps(Dict))
        
        if PriHea == True:
            PrintHeader(req)
            
        
        data = json.loads(req.json())
    
        return data
    
    def revise(self,email,password,PriHea=False):
        url = f'{self.url}/Revise'
        headers = self.headers
        
        
        Dict = {'email':email
                ,'password':password}
        
        req = requests.post(url
                            ,headers=headers
                            ,data=json.dumps(Dict))
        
        if PriHea == True:
            PrintHeader(req)
        
        data = json.loads(req.json())
    
        return data
    
    
    def admin(self,PriHea=False):
        url = f'{self.url}/admin'
        headers = self.headers
        req = requests.get(url)
        
        if PriHea == True:
            PrintHeader(req)
        
        data = json.loads(req.json())
    
        return data


#%%
def PrintHeader(Response):
    
    # Dict = {}
    # Dict['text'] = is_json(Response.text)
    # Dict['encoding'] =  Response.encoding #列出編碼
    # Dict['status_code'] = Response.status_code #列出 HTTP 狀態碼
    # Dict['headers'] = Response.headers #列出 HTTP Response Headers
    # Dict['Header_test'] = Response.headers['Header_test']
    # Dict['Content-Type'] = r.headers['Content-Type'] #印出 Header 中的 Content-Type
    # print(Dict)
    print(Response.headers)

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return myjson
  return json.loads(myjson)

#%%隨機建立帳號及密碼

import random
def RandomWord():
    list = []
    for _ in range(random.randrange(2,5)):
        # print(_)
        list.extend(chr(random.randint(ord('a'), ord('z'))))
        list.extend(chr(random.randint(ord('A'), ord('Z'))))
        list.extend(str(random.randrange(5,11)))

    random.shuffle(list)

    word = ''.join(list)
    return word

def RandomAccount():
    Account = RandomWord()
    mail = ['@google.com','@yahoo.com.tw','@microsoft.com']
    dns = random.choice(mail)
    RandonMail = f"{Account}{dns}"
    return RandonMail