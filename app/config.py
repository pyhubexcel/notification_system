import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

default_unsub = "<div style='text-align: center'><a href='{}unsubscribe_mail/{}/{}'>Unsubscribe</a></div>"

#Sharing slack app with other workspace related urls
slack_redirect_url = 'https://app.slack.com/'   #redirect to slack url
oauth_url = 'https://slack.com/api/oauth.v2.access' #Authentication api url
client_id = '124720392913.1231106322194'          #Client id you will get from https://api.slack.com/apps/ url
client_secret = '0405e4f1150a7a9dcbaa4442e3aeea4f' #client secret id you will get bfb0560221da34c4a5af72190dec2a42
client_redirect_uri = 'http://176.9.137.77:8012/slack/redirect'   #in this url ip and port will be server domain and slack/redirect same route.



base_url = os.getenv("base_url")
if os.getenv("origin") == "recruit":
    if base_url is None:
        raise Exception ('missing base url')

smtp_counts = {
    'smtp.gmail.com' : 100,
    'smtp.office365.com' : 50,
    'smtp.mail.yahoo.com': 100,
    'smtp.zoho.com': 50,
    'smtp.mail.me.com' : 1000
}

#bounced_mail_since = '1-Jan-2020'
#remind_mail_since = '1-Jan-2020'


hard_bounce_status = ["5.0.0","5.1.0","5.1.1","5.1.2","5.1.3","5.1.4","5.1.5","5.1.6","5.1.7","5.1.8","5.2.3","5.2.4","5.3.0","5.3.2","5.3.3","5.3.2","5.3.3","5.3.4","5.4.0","5.4.1","5.4.2","5.4.3","5.4.4","5.4.6","5.4.7","5.5.0","5.5.1","5.5.2","5.5.4","5.5.5","5.6.0","5.6.1","5.6.2","5.6.3","5.6.4","5.6.5","5.7.0","5.7.1","5.7.2","5.7.3","5.7.4","5.7.5","5.7.6","5.7.7"]
soft_bounce_status = ["5.2.0","5.2.1","5.2.2","5.3.1","5.4.5","5.5.3"]


dates_converter = [
    "dateofjoining",
    "dob",
    "date",
    "interview_date",
    "training_completion_date",
    "termination_date",
    "next_increment_date",
    "start_increment_date",
    "fromDate",
    "toDate",
    "reporting_date"
    ]
message_needs={
    "simple_message":[
            "message_type",

            "message_key",

            ],

    "notfication_message":[

            "message_type",
            
            "user",
            
            "message_key"],
            
    "button_message":[

            "message_type",
            
            "message_key"
                ]        
            }


fcm_api_key = "AIzaSyBO2S6xvT5qD2KuTYw-emCpNaJMVFZrzU0"
