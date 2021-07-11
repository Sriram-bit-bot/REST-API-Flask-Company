from flask_restful import Resource, reqparse

class Admin():
    def __init__(self, _id, username, password):
        self.id =_id
        self.username =username
        self.password =password

admins =[
    Admin(1,'sriram','123')
]
class AdminRegister(Resource):
    def post(self):
        parser =reqparse.RequestParser()
        parser.add_argument('id',
            type =int,
            required =True,
            help ="Id is must"

        )
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
        dum =[]
        admins.append(Admin(data['id'],data['username'],data['password']))
        for i in admins:
            my_dict ={
                'id':i.id,
                'username':i.username,
                'password':i.password
            }
            dum.append(my_dict)
        return {"id":dum}        

def name_map():
    username_mapping ={u.username: u for u in admins}
    return username_mapping
def id_map():
    userid_mapping ={u.id: u for u in admins}
    return userid_mapping