import uuid
from datetime import datetime
from peewee import UUIDField, CharField, DateTimeField
from database.db import BaseModel, database
from werkzeug.security import generate_password_hash


class User(BaseModel):

    id = UUIDField(primary_key=True, default=uuid.uuid4)
    username = CharField(max_length=250, null=False)
    password: str = CharField(max_length=250, null=False)
    fullname = CharField(max_length=250, null=False)
    initial = CharField(max_length=250, null=False)

    class Meta:
        table_name = "users"

    @classmethod
    def create(cls, **query):
        if 'password' in query:
            query['password'] = generate_password_hash(query['password'], method="pbkdf2:sha256", salt_length=18)
        return super(BaseModel, cls).create(**query)

