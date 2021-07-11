from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from admin import AdminRegister

app =Flask(__name__)
app.secret_key ='e869d610efc6ad9acf45ee57797a48d3'
jwt =JWT(app,authenticate,identity)

api =Api(app)

employees =[
    {
        "name": "Raj",
        "salary":50000
    },
]

class Employee(Resource):
    Parser =reqparse.RequestParser()
    Parser.add_argument('salary',
            type =float,
            required =True,
            help ="Salary is required"
    )
    def get(self,name):
        data =next(filter(lambda x: x['name'] == name,employees),None)
        return {"item":data},200 if data is not None else 404

    def post(self, name):
        data =Employee.Parser.parse_args()
        price =data['salary']
        employee ={ "name":name,
                "price":price}
        employees.append(employee)
        return employee,200

    @jwt_required()    
    def delete(self,name):
        global employees
        employees =list(filter(lambda x: x['name'] != name,employees))
        return {"Message":"{} deleted".format(name)}
    
    def put(self, name):
        data =Employee.Parser.parse_args()
        salary =data['salary']
        employee =next(filter(lambda x: x['name'] == name,employees),None)
        if employee is None:
            employee ={
                "name":name,
                "salary":salary
            }
            employees.append(salary)
            return salary
        employee.update(data)

class Employees(Resource):
    def get(self):
        return {'Employees':employees}

api.add_resource(Employee, '/employee/<string:name>')
api.add_resource(Employees, '/employees')
api.add_resource(AdminRegister, '/register')

if __name__ == "__main__":
    app.run(debug=True, port=5000)