from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.employee import EmployeeModel
from datetime import datetime

class Employee(Resource):
    Parser =reqparse.RequestParser()
    Parser.add_argument('first_name',
        type =str,
        required =True,
        help ='First name is required'
    )
    Parser.add_argument('last_name',
        type =str,
        required =True,
        help ="last name is required"
    )
    Parser.add_argument('sex',
        type =str,
        required =True,
        help ='Sex is required'
    )
    Parser.add_argument('super_id',
        type =int,
        required =True,
        help ='Date of birth is required'
    )
    Parser.add_argument('salary',
        type =int,
        required =True,
        help ='Date of birth is required'
    )
    Parser.add_argument('branch_id',
        type =int,
        required =True,
        help ="Branch ID is required"
    )
    def get(self,emp_id):
        employee =EmployeeModel.find_employee(emp_id)
        if employee is None:
            return 404
        else:
            data =EmployeeModel.convert_to_dict(employee)
            return data,200

    def post(self, emp_id):
        data =Employee.Parser.parse_args()
        EmployeeModel.save_to_db(EmployeeModel.convert_to_obj(emp_id, data))
        return {"Message":f"{data['first_name']} employee created successfully"}

    @jwt_required()    
    def delete(self,emp_id):
        employee =EmployeeModel.find_employee(emp_id)
        EmployeeModel.delete_from_db(employee)
    
    def put(self, emp_id):
        data =Employee.Parser.parse_args()
        employee =EmployeeModel.find_employee(emp_id)
        if employee is None:
            employee = EmployeeModel.convert_to_obj(emp_id, data)
            EmployeeModel.save_to_db(employee)
            return {"Message":f"{employee.first_name} added"},201
        employee = EmployeeModel.convert_to_obj(emp_id, data)
        EmployeeModel.update_a_record(employee)
        return {"Message":f"{employee.first_name} updated"},200

class Employees(Resource):
    def get(self):
        emplist =[]
        for x in EmployeeModel.query.all():
            emp =EmployeeModel.convert_to_dict(x)
            emplist.append(emp)
        return {"Employees":emplist}
        #return {"Employees":list(map(lambda x : x.json(),EmployeeModel.query.all()))}