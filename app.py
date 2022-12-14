from flask import *
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from bson.objectid import ObjectId
from bson.json_util import dumps

# from flask_restful import Api, Resource



#%%

ServerPassword = 'test123'

client = pymongo.MongoClient(f"mongodb+srv://test:{ServerPassword}@test.qk4mnho.mongodb.net/?retryWrites=true&w=majority"
 ,tlsAllowInvalidCertificates=True)

db = client.member_system

app = Flask(__name__
            )

app.config["JSON_AS_ASCII"] = False

app.secret_key = 'any string but secret'

#%%
@app.route('/json_value', methods=['POST'])
def JSON_value():
    if request.is_json:
        data = request.get_json()
        result = json.dumps(data)
        print(result)
        print('ok')
    else:
        result = 'Not JSON Data'
    return result




#%%
@app.route('/error')
def error():
    message = request.args.get('msg','msg')
    return render_template('error.html',message=message)


#%% Client

@app.route('/')
def index():
    # ren = render_template('index.html')
    # resp = make_response(render_template('index.html'))
    # resp.headers['test']='test' 
    return render_template('index.html')

@app.route('/member')
def member():
    if 'nikename' in session:
        return render_template('member.html')
        
    else:
        return redirect('/')
#%%
#Server
@app.route('/signup',methods = ['POST'])
def signup():

    data = request.get_json()
    print(type(data))
    collection = db.user
    collection.insert_one({
            'nikename':data['nikename'],
            'email':data['email'],
            'password':data['password']
            })
    JSON = json.dumps(data)
    Response = jsonify(JSON)
    Response.headers['Header_test']='test'
    return Response


@app.route('/signin',methods = ['POST'])
def signin():
    
    data = request.get_json()
    email = data['email']
    password = data['password']


    collection = db.user

    result = collection.find_one({
                        '$and':[
                                {'email':email},
                                {'password':password}
                                ]
                               })

    if result == None:
        return redirect('/error?msg=帳號密碼輸入錯誤')
    else:
        session['nikename'] = result['nikename']
        return redirect('/member')


@app.route('/signout')
def signout():
    del session['nikename']
    return redirect('/')

#%%
@app.route('/admin')
def admin():

    collection = db.user
    cursor = collection.find()
    json = dumps(cursor)
    
    return jsonify(json)


@app.route('/remove',methods = ['POST'])
def remove():

    data = request.get_json()

    collection = db.user
    # result = collection.find_one({'email':data['email']})

    # if result != None:
    collection.delete_one({'email':data['email']})
    #     return redirect('/admin')
    # else:
    #     return redirect('/error?msg=無此會員')
    print(data)
    return jsonify(json.dumps(data))



@app.route('/Revise' , methods = ['POST'])
def Revise():

    data = request.get_json()
    collection = db.user
    print(data)
    collection.update_many({'email':data['email']}
                            ,{'$set':{'password':data['password']}}
                            )
    return jsonify(json.dumps(data))






if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)
# %%
