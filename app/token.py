from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_current_user, jwt_refresh_token_required,
    verify_jwt_in_request
)
from functools import wraps
from flask import (Blueprint, flash, jsonify, abort, request)
import re
from flask import g, current_app, jsonify

from bson.objectid import ObjectId

from app import mongo

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if 'Authorization' in request.headers:
            project_secret_key = request.headers.get('Authorization')
        token = project_secret_key.split()
        token = token[-1]
        user = jwt.decode(token,None,False)    
        if 'role' in user:
            if user["role"] == "Admin" or user['role'] == "HR":
                return fn(*args, **kwargs)
            else:
                return jsonify(msg='Unauthorized!'), 403
        else:
            if 'user_claims' in user:
                if user["user_claims"]['role'] == "Admin" or user["user_claims"]['role'] == "HR":
                    return fn(*args, **kwargs)
                else:
                    return jsonify(msg='Unauthorized!'), 403
    return wrapper
    