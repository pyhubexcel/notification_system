#from app import mongo
import requests
from slackclient import SlackClient
from flask import jsonify
import datetime

def slack_load_token(mongo):
    token = mongo.slack_settings.find_one({
        "slack_token": {"$exists": True}
    }, {"slack_token": 1, '_id': 0})
    sl_token = token['slack_token']
    return sl_token

def slack_id(email,mongo):
    slack_token = slack_load_token(mongo)
    if slack_token is not None:
        sc = SlackClient(slack_token)
        sl_user_id = sc.api_call("users.lookupByEmail",
                        email=email)
        if sl_user_id['ok'] is True:                   
            return (sl_user_id['user']['id'])
        else:
            raise Exception("Slack profile not available in workspace")  
    else:
        raise Exception("Slack token not available in database")


def recruit_slack_id(email,mongo):
    slack_token = slack_load_token(mongo)
    sc = SlackClient(slack_token)
    sl_user_id = sc.api_call("users.lookupByEmail",
                       email=email)
    if sl_user_id['ok'] is True:                   
        return (sl_user_id['user']['id'])
    else:
        return None


def slack_message(mongo,channel, message,req_json=None,message_detail=None):
    slack_token = slack_load_token(mongo)
    sc = SlackClient(slack_token)
    if req_json is not None:
        if 'button' in req_json:
            color = None
            if 'color' in  req_json['button']:
                color = req_json['button']['color']        
            attachments = [
                {
                "fallback": "Message from "+ message_detail['message_origin'],
                "color" : color, 
                "actions" : req_json['button']['actions']
                }
            ]
        else:
            attachments = None
    else:
        attachments = None
    if message_detail is not None:    
        if message_detail['message_color'] is not None:
            color = message_detail['message_color']
            attachments = [
                {
                "fallback": "Message from "+ message_detail['message_origin'],
                "color" : color,
                "text": message 
                }
            ]
            message = None    
        else:
            pass
    for data in channel:
        a = sc.api_call(
            "chat.postMessage",
            channel=data,
            text=message,
            attachments=attachments
        )
        print("8000000000000000000000000000000000",a)

def slack_profile(mongo,email=None):
    slack_token = slack_load_token(mongo)
    sc = SlackClient(slack_token)
    sl_user_id = sc.api_call("users.lookupByEmail",
                       email=email)

    if sl_user_id['ok'] is True:                   
        return (sl_user_id['user']['id'])
    else:
        raise Exception("Slack profile not available in workspace for " + email)  
                              