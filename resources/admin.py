from flask_restful import Resource, reqparse
from models.admin import AdminModel

class AdminResource(Resource):
    def post(self):
        parser =reqparse.RequestParser()
        parser.add_argument('username',
            type =str,
            required =True,
            help ="username is must"
        )
        parser.add_argument('password',
            type =str,
            required =True,
            help ="Password is must"
        )
        data =parser.parse_args()
        if AdminModel.find_by_username(data['username']):
            return {"Message":"Admin already exists"},400
        Admin =AdminModel(**data) 
        Admin.save_to_db()
        return {"Message":"User creation successful"},201