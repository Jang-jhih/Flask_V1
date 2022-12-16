from resources.user import *


api.add_resource(Todo, '/api/v1/<email>')
api.add_resource(TodoList, '/api/v1')
api.add_resource(GetStringQuery, '/api/v1')



if __name__ == '__main__':
    app.run(debug=True,
        port= 3000)