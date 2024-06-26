from uuid import uuid4
from datetime import datetime
from database.db import BaseModel
from peewee import UUIDField, CharField, ForeignKeyField, TextField
from models.User import User
from models.DocumentStatus import DocumentStatus


class Document(BaseModel):

    id = UUIDField(primary_key=True, default=uuid4)
    document = CharField(max_length=250, null=False)
    status = ForeignKeyField(DocumentStatus, default="INITIALIZED", field=DocumentStatus.status, null=False)
    user_id = ForeignKeyField(User)
    sign_coordinates = TextField(null=False)
    initial_coordinates = TextField(null=False)
    to = CharField(250)
    to_id = ForeignKeyField(User, null=True)

    class Meta:
        table_name = "documents"
