from flask_restful import Resource,reqparse
from models.branch import BranchModel

class Branch(Resource):
    parser =reqparse.RequestParser()
    parser.add_argument('branch_name',
        type =str,
        required =True,
        help ="Branch name is compulsory"
    )
    parser.add_argument('mgr_id',
        type =int,
        required =True,
        help ="Manager ID is compulsory"
    )
    parser.add_argument('branch_index',
        type =float,
        required =True,
        help ="Branch index is compulsory"
    )

    def get(self,branch_id):
        branch =BranchModel.find_branch(branch_id)
        if branch is None:
            return {"Message":"Branch unavailable"},404
        return BranchModel.convert_to_dict(branch),200
        
    def post(self,branch_id):
        data =Branch.parser.parse_args()
        branch =BranchModel.find_branch(branch_id)
        if branch is None:
            branch =BranchModel(branch_id,data['branch_name'],data['mgr_id'],data['branch_index'])
            BranchModel.save_to_db(branch)
            return {"Message":f"{data['branch_name']} Branch created"},201
        return {"Message":"Branch already exists"},400

    def delete(self,branch_id):
        branch =BranchModel.find_branch(branch_id)
        if branch is None:
            return {"Message":"Branch does not exist"},404
        BranchModel.delete_from_db(branch)
        return {"Message":f"{branch.branch_name} branch deleted"},200

    def put(self,branch_id):
        data =Branch.parser.parse_args()
        branch =BranchModel.find_branch(branch_id)
        if branch is None:
            branch =BranchModel(branch_id,data['branch_name'],data['mgr_id'],data['branch_index'])
            BranchModel.save_to_db(branch)
            return {"Message":f"{branch.branch_name} branch created"},201
        branch =BranchModel(branch_id,data['branch_name'],data['mgr_id'],data['branch_index'])
        BranchModel.update_a_branch(branch)
        return {"Message":f"{branch.branch_name} branch updated"},200

class Branches(Resource):
    def get(self):
        mylist =[]
        for x in BranchModel.query.all():
            mylist.append(BranchModel.convert_to_dict(x))
        if len(mylist) > 0:
            return {"Branches":mylist}
        else:
            return {"Message":"List is empty"}