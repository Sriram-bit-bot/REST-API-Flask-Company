from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.admin import AdminResource
from resources.employee import Employee, Employees

app =Flask(__name__)
app.secret_key ='e869d610efc6ad9acf45ee57797a48d3'
jwt =JWT(app,authenticate,identity)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

api =Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Employee, '/employee/<int:_id>')
api.add_resource(Employees, '/employees')
api.add_resource(AdminResource, '/register')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True, port=5000)