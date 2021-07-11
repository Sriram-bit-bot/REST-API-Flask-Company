from werkzeug.security import safe_str_cmp
from models.admin import AdminModel

def authenticate(username, password):
    admin =AdminModel.find_by_username(username)
    if admin and safe_str_cmp(admin.password ,password):
        return admin

def identity(payload):
    user_id =payload['identity']
    return AdminModel.find_by_id(user_id)