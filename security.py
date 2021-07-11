from admin import Admin
from werkzeug.security import safe_str_cmp
from admin import name_map, id_map

def authenticate(username, password):
    admin =name_map().get(username, None)
    if admin and safe_str_cmp(admin.password ,password):
        return admin

def identity(payload):
    user_id =payload['identity']
    return id_map().get(user_id,None)