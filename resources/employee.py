from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.employee import EmployeeModel


class Employee(Resource):
    Parser =reqparse.RequestParser()
    Parser.add_argument('name',
        type =str,
        required =True,
        help ='Name is required'
    )
    Parser.add_argument('salary',
            type =float,
            required =True,
            help ="Salary is required"
    )
    def get(self,_id):
        employee =EmployeeModel.find_employee(_id)
        if employee is None:
            return 404
        else:
            data ={"Id":employee.id,"Name":employee.name,"Salary":employee.salary}
            return data,200

    def post(self, _id):
        data =Employee.Parser.parse_args()
        EmployeeModel.save_to_db(EmployeeModel(_id,data['name'],data['salary']))
        return {"Message":f"{data['name']} employee created successfully"}

    @jwt_required()    
    def delete(self,_id):
        employee =EmployeeModel.find_employee(_id)
        EmployeeModel.delete_from_db(employee)
    
    def put(self, _id):
        data =Employee.Parser.parse_args()
        name =data['name']
        salary =data['salary']
        employee =EmployeeModel.find_employee(_id)
        employee = EmployeeModel(_id, name, salary)
        if employee is None:
            EmployeeModel.save_to_db(employee)
            return {"Message":f"{employee.name} added"},201
        EmployeeModel.update_a_record(employee)
        return {"Message":f"{employee.name} updated"},200

class Employees(Resource):
    def get(self):
        emplist =[]
        for x in EmployeeModel.query.all():
            emp ={
                'id':x.id,
                'name':x.name,
                'salary':x.salary
            }
            emplist.append(emp)
        return {"Employees":emplist}
        #return {"Employees":list(map(lambda x : x.json(),EmployeeModel.query.all()))}