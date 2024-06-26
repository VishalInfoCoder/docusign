from uuid import uuid4
from datetime import datetime
from models.User import User
from database.db import BaseModel, database
from peewee import UUIDField, CharField, ForeignKeyField


class Signature(BaseModel):

    id = UUIDField(primary_key=True, default=uuid4)
    font_name = CharField(max_length=250, null=False)
    signature_name = CharField(max_length=250, null=False)
    initial_name = CharField(max_length=250, null=False)
    user_id = ForeignKeyField(User, unique=True, backref="Signatures")

    class Meta:
        table_name = "signatures"

    # class Meta:
    #     database = database
    #     table_name = "signatures"

