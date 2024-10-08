import re
#from app import mongo
from app.util.serializer import serialize_doc
import datetime
import dateutil.parser
from bson.objectid import ObjectId
from app.email.model.sendmail import send_email
from flask import current_app as app
import time
import email
import os
from app.utils import fetching_validated_account
from app.account import initDB

def reject_mail():
    accounts,account_config = fetching_validated_account()
    for account in accounts:  
        account_mongo = account_config[account]
        mongo = initDB(account,account_mongo)   
        if mongo is not None: 
            try: 
                ret = mongo.rejection_handling.find_one({"send_status":False})
                if ret is not None:
                    message = ret['message']
                    time = ret['rejection_time']  
                    mail_subject = ret['subject']
                    sender_name = ret['sender_name']
                    time_update = dateutil.parser.parse(time).strftime("%Y-%m-%dT%H:%M:%SZ")
                    rejected_time = datetime.datetime.strptime(time_update,'%Y-%m-%dT%H:%M:%SZ')
                    diffrence = datetime.datetime.utcnow() - rejected_time
                    if diffrence.days >= 1:
                        to = []
                        mail = ret['email']  
                        to.append(mail)
                        mail_details = mongo.mail_settings.find_one({"mail_username":str(ret['smtp_email']),"origin": "RECRUIT"})
                        if mail_details is not None:
                            send_email(mongo,message=message,recipients=to,sender_name=sender_name,subject=mail_subject,sending_mail=mail_details['mail_username'],sending_password=mail_details['mail_password'],sending_port=mail_details['mail_port'],sending_server=mail_details['mail_server'])
                            user_status = mongo.rejection_handling.remove({"_id":ObjectId(ret['_id'])})
                        else:
                            mail_details = {"mail_server":"smtp.sendgrid.net","mail_port":587,"origin":"RECRUIT","mail_use_tls":True,"mail_username":"apikey","mail_password":os.getenv('send_grid_key'),"active":True,"type":"tls","mail_from":"noreply@excellencetechnologies.in"}
                            send_email(mongo,message=message,recipients=to,sender_name=sender_name,subject=mail_subject,sending_mail=mail_details['mail_username'],sending_password=mail_details['mail_password'],sending_port=mail_details['mail_port'],sending_server=mail_details['mail_server'])
                            user_status = mongo.rejection_handling.remove({"_id":ObjectId(ret['_id'])})
                    else:
                        pass
                else:
                    pass
            except Exception as err:
                print(str(err),'<<<<<<<<< ERROR OF REJCTION CRON')
