from sqlalchemy.orm import backref, lazyload
from db import db

class BranchModel(db.Model):
    __tablename__ ="branch"
    branch_id =db.Column(db.Integer,primary_key =True)
    branch_name =db.Column(db.String(25))
    mgr_id =db.Column(db.Integer)
    branch_index =db.Column(db.Float(precision =2))
    employees =db.relationship('EmployeeModel',lazy='dynamic')
    
    def __init__(self,branch_id,branch_name,mgr_id,branch_index):
        self.branch_id =branch_id
        self.branch_name =branch_name
        self.mgr_id =mgr_id
        self.branch_index =branch_index
    
    @classmethod
    def find_branch(cls,branch_id):
        return cls.query.filter_by(branch_id =branch_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def update_a_branch(self):
        branch =BranchModel.query.filter_by(branch_id =self.branch_id).first()
        branch.branch_name =self.branch_name
        branch.mgr_id =self.mgr_id
        branch.branch_index =self.branch_index
        db.session.commit()

    def convert_to_dict(self):
        return {
            'branch_id':self.branch_id,
            'branch_name':self.branch_name,
            'mgr_id':self.mgr_id,
            'branch_index':self.branch_index,
            'Employees':
               [{'Name':x.first_name,'Id':x.emp_id} for x in self.employees.all()]
        }
        

        