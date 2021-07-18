from sqlalchemy.orm import backref
from db import db

class EmployeeModel(db.Model):
    __tablename__ = "employee"
    emp_id =db.Column(db.Integer, primary_key=True)
    first_name =db.Column(db.String(30))
    last_name =db.Column(db.String(30))
    sex =db.Column(db.String(1))
    super_id =db.Column(db.Integer)
    salary =db.Column(db.Integer)

    branch_id =db.Column(db.Integer, db.ForeignKey('branch.branch_id'))
    branch =db.relationship('BranchModel')

    def __init__(self, emp_id,fname,lname,sex,super_id, salary,branch_id):
        self.emp_id =emp_id
        self.first_name =fname
        self.last_name =lname
        self.sex =sex
        self.super_id =super_id
        self.salary =salary
        self.branch_id =branch_id
    
    @classmethod
    def find_employee(cls,emp_id):
        return cls.query.filter_by(emp_id =emp_id).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def update_a_record(self):
        employee =EmployeeModel.query.filter_by(emp_id =self.emp_id).first()
        employee.first_name =self.first_name
        employee.last_name =self.last_name
        employee.sex =self.sex
        employee.super_id =self.super_id
        employee.salary =self.salary
        employee.branch_id =self.branch_id
        db.session.commit()
    
    def convert_to_dict(self):
        return {
            "employee_id":self.emp_id,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "sex":self.sex,
            "supervisor_id":self.super_id,
            "salary":self.salary,
            "branch_id":self.branch_id
        }
    @classmethod
    def convert_to_obj(cls,my_id,my_dict):
        return EmployeeModel(my_id,my_dict['first_name'],my_dict['last_name'],
                    my_dict['sex'],my_dict['super_id'],my_dict['salary'],my_dict['branch_id'])
