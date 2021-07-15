from db import db

class EmployeeModel(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String(30))
    salary =db.Column(db.String(30))

    def __init__(self, _id,name, salary):
        self.id =_id
        self.name =name
        self.salary =salary
    
    @classmethod
    def find_employee(cls,_id):
        return cls.query.filter_by(id =_id).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def update_a_record(self):
        employee =EmployeeModel.query.filter_by(id =self.id).first()
        employee.name =self.name
        employee.salary =self.salary
        db.session.commit()