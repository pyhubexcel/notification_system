
import unittest
from json import dumps
from json.decoder import JSONDecodeError
from requests.exceptions import ConnectionError
import json
from app.api_tests.test_message_create_apis import app
from bson import ObjectId
from app import mongo
from app.config import secret_key,account_name

class AllTestSettingApis(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def json_of_response(self, response):
        return json.loads(response.data.decode('utf8'))

    def create_system_settings(self):
        payload = {
                "pdf":True
            }
        mongo.db.system_settings.insert_one(payload).inserted_id

    #Test case for put test system setting
    def test_put_settings(self):

        #making data
        self.create_system_settings()

        payload = json.dumps({
                "pdf":False
            })

        # act
        response = self.app.put('/settings?account-name='+account_name,headers={"Content-Type": "application/json","Secretkey":str(secret_key)}, data=payload)

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertIn('upserted',response.get_data(as_text=True))



    #Test case for get system setting api
    def test_get_settings(self):
        #making data
        self.create_system_settings()
        
        # act
        response = self.app.get('/settings?account-name='+account_name,headers={"Secretkey":str(secret_key)})
        jsonResponse = self.json_of_response(response)

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertIn('pdf',jsonResponse)
