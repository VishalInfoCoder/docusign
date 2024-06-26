from uuid import uuid4
from datetime import datetime
from peewee import UUIDField, CharField
from database.db import BaseModel


class DocumentStatus(BaseModel):
    id = UUIDField(primary_key=True, default=uuid4)
    status = CharField(max_length=250, null=False, unique=True)

    class Meta:
        table_name = "documents_status"
