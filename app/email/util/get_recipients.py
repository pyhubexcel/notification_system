from flask import current_app as app
import re
from app.config import dev_accounts

def get_recipients_from_request(req,account_name):
    to = None
    bcc = None
    cc = None
    if account_name in dev_accounts:
        if 'to' in req:
            for email in req.get('to'):
                full_domain = re.search("@[\w.]+", email)  
                domain = full_domain.group().split(".")
                if domain[0] == "@excellencetechnologies":
                    to = [email]
                else:
                    to = [app.config['to']]
        bcc = [app.config['bcc']]
        cc = [app.config['cc']]
    else:
        if 'to' in req:
            if not req['to']:
                to = None
            else:     
                to = req['to']
        else:
            to = None
        if 'bcc' in req:    
            if not req['bcc']:
                bcc = None
            else:
                bcc = req['bcc']
        else:
            bcc = None
        
        if 'cc' in req: 
            if not req['cc']:
                cc = None
            else:
                cc = req['cc']
        else:        
            cc = None            
    return to,bcc,cc