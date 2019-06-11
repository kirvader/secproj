from peewee import *
import uuid, os

DATABASE_URL = os.environ['DATABASE_URL']


psql_db = PostgresqlDatabase(
    'orgdb',
    user='orguser',
    password='27701757',
    host=DATABASE_URL)


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
