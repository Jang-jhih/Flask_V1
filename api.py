from resources.user import *


MainPath = '/api/v1/users'
UserMailPath = f'{MainPath}/email'
api.add_resource(TodoList, MainPath)
api.add_resource(Todo, f'{UserMailPath}/<usermail>')
api.add_resource(GetStringQuery, f'{UserMailPath}', endpoint='test')



if __name__ == '__main__':
    app.run(debug=True
        ,host='0.0.0.0'
        # 容器接口
        ,port= 80
        )