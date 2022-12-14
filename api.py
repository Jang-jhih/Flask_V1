from flask import Flask, request,jsonify
from flask_restful import (Resource, Api
                            ,reqparse,abort)
import pymongo
from bson.json_util import dumps
import json


ServerPassword = 'test123'

client = pymongo.MongoClient(f"mongodb+srv://test:{ServerPassword}@test.qk4mnho.mongodb.net/?retryWrites=true&w=majority"
 ,tlsAllowInvalidCertificates=True)

db = client.member_system


app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('nikename')
parser.add_argument('email')
parser.add_argument('password')



def abort_if_todo_doesnt_exist(email):
    if email not in todos[email]:
        abort(404,message = f"Todo {email} does't exist")


class Todo(Resource):
    def get(self, email):
        abort_if_todo_doesnt_exist(email)
        return todos[email]

    def put(self, email):
        arg = parser.parse_args()


        collection = db.user
        collection.update_many({'email':arg['email']}
                            ,{'$set':{'password':arg['password']}}
                            )
        return arg[email],201

    def delete(self,email):
        abort_if_todo_doesnt_exist(email)
        del todos['email']

        return '',204

class TodoList(Resource):
    def get(self):
        collection = db.user
        cursor = collection.find()
        json = dumps(cursor)

        return jsonify(json)

    def post(self):
        arg = parser.parse_args()
        collection = db.user
        collection.insert_one({
                'nikename':arg['nikename'],
                'email':arg['email'],
                'password':arg['password']
                })

        return arg,201,{'Header_test':'test'}



api.add_resource(Todo, '/api/<todo_id>')
api.add_resource(TodoList, '/api')

if __name__ == '__main__':
    app.run(debug=True)