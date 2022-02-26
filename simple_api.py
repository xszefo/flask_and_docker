from flask import Flask
from flask_restful import Resource, Api
import mysql.connector
from creds import user, password, db_name, table_name

app = Flask(__name__)
api = Api(app)

def execute_mysql(command):
    try:
        cnx = mysql.connector.connect(user=user, 
                                      password=password,
                                      host='some-mysql',
                                      database=db_name)
        cursor = cnx.cursor()
        cursor.execute(command)
        result = {str(user[0]): {'first_name': user[1], 'last_name': user[2]} for user in cursor}
        return result
    except Exception as err:
        print(err)
        return False
    finally:
        cursor.close()
        cnx.close()

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class GetUsers(Resource):
    def get(self):
        table = table_name
        command = f'SELECT * FROM {table};'
        return execute_mysql(command)

class GetUser(Resource):
    def get(self, user_id):
        table = 'users'
        command = f'SELECT * FROM {table} where id={user_id};'
        return execute_mysql(command)
        
api.add_resource(HelloWorld, '/')
api.add_resource(GetUsers, '/users')
api.add_resource(GetUser, '/users/<int:user_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
