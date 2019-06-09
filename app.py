from models import *
from playhouse.shortcuts import model_to_dict
import json, falcon, os, psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

class UserIdResource():
     def on_get(self, req, resp, user_id):
         try:
             user = OrgUser.get(OrgUser.id == user_id)
             resp.body = json.dumps(model_to_dict(user))
         except OrgUser.DoesNotExist:
             resp.status = falcon.HTTP_404


class UserResource():
     def on_get(self, req, resp):
         users = OrgUser.select().order_by(OrgUser.id)
         resp.body = json.dumps([model_to_dict(u) for u in users])


api = falcon.API()

users = UserResource()
users_id = UserIdResource()

api.add_route('/users/', users)
api.add_route('/users/{user_id}', users_id)

