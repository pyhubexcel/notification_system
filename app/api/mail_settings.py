from app import mongo
from app import token
from flask import (Blueprint, flash, jsonify, abort, request)
from app.util import serialize_doc
import json
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_current_user, jwt_refresh_token_required,
    verify_jwt_in_request
)
from flask import current_app as app
from bson import ObjectId
from app.mail_util import send_email
import smtplib
import datetime


bp = Blueprint('mail_settings', __name__, url_prefix='/smtp')

@bp.route('/settings/<string:origin>', methods=["POST", "GET"])
@bp.route('/settings/<string:origin>/<string:id>', methods=["DELETE","PUT"])
# @token.admin_required
def mail_setings(origin,id=None):
    if request.method == "GET":
       mail = mongo.db.mail_settings.find({"origin":origin},{"mail_password":0})
       mail = [serialize_doc(doc) for doc in mail]
       return jsonify (mail)
    if request.method == "DELETE":
        prior = mongo.db.mail_settings.find_one({"origin":origin,"_id": ObjectId(str(id))})
        if origin == "CAMPAIGN":
            priority = prior['priority']
        else:
            pass     
        mail = mongo.db.mail_settings.remove({"origin":origin,"_id": ObjectId(str(id))})
        if origin == "CAMPAIGN":
            campaign_smtp = mongo.db.mail_settings.update({"priority":{ "$gt": priority } },{
                        "$inc" :{
                            "priority": -1
                        }

                    },multi=True)
        return jsonify ({"Message": "Smtp conf deleted"}), 200
    if request.method == "PUT":
        ret = mongo.db.mail_settings.update({"origin":origin,"active":True},{
            "$set":{
                "active" : False
            }

        },multi=True)
        mail = mongo.db.mail_settings.update({"origin":origin,"_id": ObjectId(str(id))},{
            "$set":{
                "active" : True
            }

        })
        return jsonify ({"Message": "Smtp conf set as active"}), 200


    if request.method == "POST":
        if not request.json:
            abort(500)
        if origin == "HR":    
            mail_server = request.json.get("mail_server", None)
            mail_port = request.json.get("mail_port", 0)
            mail_use_tls = request.json.get("mail_use_tls", True)
            mail_username = request.json.get("mail_username", None)
            mail_password = request.json.get("mail_password", None)
            
            
            if not mail_server and mail_password and mail_port and mail_use_tls and mail_username:
                return jsonify({"msg": "Invalid Request"}), 400    
                    
            ret = mongo.db.mail_settings.update({}, {
                "$set": {
                    "mail_server": mail_server,
                    "mail_port": mail_port,
                    "origin": origin,
                    "mail_use_tls": mail_use_tls,
                    "mail_username":mail_username,
                    "mail_password":mail_password
                }
            },upsert=True)
            return jsonify({"MSG":"upsert"}),200
        elif origin == "RECRUIT":
            mail_server = request.json.get("mail_server", None)
            mail_port = request.json.get("mail_port", 0)
            mail_use_tls = request.json.get("mail_use_tls", True)
            mail_username = request.json.get("mail_username", None)
            mail_password = request.json.get("mail_password", None)
            active = request.json.get("active",True)
            type_s = request.json.get("type", "tls")
            
            if not mail_server and mail_password and mail_port and mail_use_tls and mail_username:
                return jsonify({"msg": "Invalid Request"}), 400  
            email = app.config['to']
            smtp_right = True
            unregister = False
            try:
                send_email(message="SMTP WORKING!",recipients=[email],subject="SMTP TESTING MAIL!",sending_mail=mail_username,sending_password=mail_password,sending_port=mail_port,sending_server=mail_server)
            except smtplib.SMTPDataError:
                unregister = True
            except Exception:    
                smtp_right = False
            if unregister is False:    
                if smtp_right is True:                     
                    vet = mongo.db.mail_settings.find_one({"mail_username":mail_username,
                            "mail_password":mail_password,"origin":origin})
                    if vet is None:
                        exist = mongo.db.mail_settings.find_one({"origin":origin})
                        if exist is None:
                            active = True
                        else:
                            active = False    
                        ret = mongo.db.mail_settings.insert_one({
                            "mail_server": mail_server,
                                "mail_port": mail_port,
                                "origin": origin,
                                "mail_use_tls": mail_use_tls,
                                "mail_username":mail_username,
                                "mail_password":mail_password,
                                "active": active,
                                "type": type_s
                        })
                        return jsonify({"MSG":"upsert"}),200
                    else:
                        return jsonify({"MSG":"Smtp already exists"}),400
                else:
                    return jsonify({"MSG":"Invalid SMTP"}),400
            else:
                return jsonify({"MSG":"Mail account in not registered"}),400
        elif origin == "CAMPAIGN":
            mail_server = request.json.get("mail_server", None)
            mail_port = request.json.get("mail_port", 0)
            mail_use_tls = request.json.get("mail_use_tls", True)
            mail_username = request.json.get("mail_username", None)
            mail_password = request.json.get("mail_password", None)
            active = request.json.get("active",True)
            type_s = request.json.get("type", "tls")
            
            if not mail_server and mail_password and mail_port and mail_use_tls and mail_username:
                return jsonify({"msg": "Invalid Request"}), 400  
            email = app.config['to']
            smtp_right = True
            unregister = False
            try:
                send_email(message="SMTP WORKING!",recipients=[email],subject="SMTP TESTING MAIL!",sending_mail=mail_username,sending_password=mail_password,sending_port=mail_port,sending_server=mail_server)
            except smtplib.SMTPDataError:
                unregister = True
            except Exception:    
                smtp_right = False
            if unregister is False:    
                if smtp_right is True:                     
                    vet = mongo.db.mail_settings.find_one({"mail_username":mail_username,
                            "mail_password":mail_password,"origin":origin})
                    if vet is None:
                        priority = 1
                        previous =  mongo.db.mail_settings.find({"origin":"CAMPAIGN"}).sort("priority", -1).limit(1)
                        prior_check = [serialize_doc(doc) for doc in previous]
                        if prior_check:
                            for data in prior_check:
                                priority = data['priority'] + 1
                        ret = mongo.db.mail_settings.insert_one({
                                "mail_server": mail_server,
                                "mail_port": mail_port,
                                "origin": origin,
                                "mail_use_tls": mail_use_tls,
                                "mail_username":mail_username,
                                "mail_password":mail_password,
                                "active": active,
                                "type": type_s,
                                "priority": priority,
                                "created_at": datetime.datetime.today()


                        })
                        return jsonify({"MSG":"upsert"}),200
                    else:
                        return jsonify({"MSG":"Smtp already exists"}),400
                else:
                    return jsonify({"MSG":"Invalid SMTP"}),400
            else:
                return jsonify({"MSG":"Mail account in not registered"}),400

@bp.route('/smtp_priority/<string:Id>/<int:position>', methods=["POST"])
def smtp_priority(Id,position):
    prior_check = mongo.db.mail_settings.find({"origin": "CAMPAIGN"}).sort("priority",1)
    prior_check = [serialize_doc(doc) for doc in prior_check]
    index = 0
    value = 0
    for data in prior_check:
        if str(data['_id']) == str(Id):
            value = index
        index = index + 1
    val = None
    if position == 1:
        val = value - 1
    elif position == 0:
        val = value + 1    
    final = prior_check[val]
    current = prior_check[value]
    ret = mongo.db.mail_settings.update({"_id":ObjectId(Id)},{
        "$set":{
            "priority": final['priority']
        }
    },upsert=False)
    vet = mongo.db.mail_settings.update({"_id":ObjectId(final['_id'])},{
        "$set":{
            "priority": current['priority']
        }
    },upsert=False) 

    return jsonify({"message": "priority changed"}), 200