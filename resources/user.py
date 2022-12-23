from flask import (Flask
                    # , request
                    # ,jsonify
                    )
# from flask_marshmallow import Marshmallow
from flask_restful import (Resource, Api
                            ,reqparse,abort)
from bson.json_util import dumps
# from resources.db import *
import json
import pymongo
import os

#取得環境變數
DBhost = os.environ.get('DBhost')




app = Flask(__name__)
api = Api(app)






InDokcer = os.path.exists('/.dockerenv')
if InDokcer == True:
    client = pymongo.MongoClient(f'mongodb://{DBhost}:27017/')
else:
    client = pymongo.MongoClient('localhost', 27017)


db = client.member_system
collection = db.user
# ma = Marshmallow(app)

# class UserSchema(ma.Schema):
#     class Meta:
#         # Fields to expose
#         fields = ("nikename", "email", "password")

#     # Smart hyperlinking
#     _links = ma.Hyperlinks(
#         {
#             "self": ma.URLFor("user_detail", values=dict(id="<id>")),
#             "collection": ma.URLFor("users"),
#         }
#     )  



# user_schema = UserSchema()
# users_schema = UserSchema(many=True)

parser = reqparse.RequestParser()
parser.add_argument('nikename')
parser.add_argument('email')
parser.add_argument('password')



def abort_if_todo_doesnt_exist(email):
    cursor = collection.find({'email':email})
    JSON = json.loads(dumps(cursor))

    if len(JSON) == 0:
        abort(404,message = f"Todo {email} does't exist")


class TodoList(Resource):
    def get(self):
        collection = db.user
        cursor = collection.find()
        data = json.loads(dumps(cursor))
        return data
        # return  users_schema.dump(data)

    def post(self):
        arg = parser.parse_args()

        collection.insert_one({
                'nikename':arg['nikename'],
                'email':arg['email'],
                'password':arg['password']
                })
        return arg,201,{'Header_test':'test'}

class Todo(Resource):
    def get(self, usermail):
        # print('test')
        abort_if_todo_doesnt_exist(usermail)

        JSON = dumps(collection.find({'email':usermail}))
        return json.loads(JSON)
        # return 'test'

    def put(self, usermail):
        print('test')
        arg = parser.parse_args()
        # print(arg['password'])
        collection.update_many({'email':usermail}
                            ,{'$set':{'password':arg['password']}}
                            )

        Message = {usermail:f"Password Change to {arg['password']}"}
        return Message,201
        # return 'test'

    def delete(self,usermail):
        abort_if_todo_doesnt_exist(usermail)
        print(usermail)
        collection.delete_one({'email':usermail})

        Message =  {'DeleteOK':usermail}


        return "",204,Message


class GetStringQuery(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, location='args')
        arg = parser.parse_args()
        print(arg)
        JSON = dumps(collection.find({'email':arg['email']}))
        return json.loads(JSON)
        # return parser