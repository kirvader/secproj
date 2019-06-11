from peewee import *
import uuid, os
import urlparse

urlparse.uses_netloc.append('postgres')
url = urlparse.urlparse(os.environ['DATABASE_URL'])


psql_db = (database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)


def init_tables():
    psql_db.create_tables([OrgUser], safe=True)


def generate_users(num_users):
    for i in range(num_users):
        user_name = str(uuid.uuid4())[0:8]
        OrgUser(username=user_name).save()


class BaseModel(Model):
    class Meta:
        database = psql_db


class OrgUser(BaseModel):
    username = CharField(unique=True)
