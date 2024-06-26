from datetime import datetime

from peewee import MySQLDatabase, DateTimeField, Model
from playhouse.shortcuts import model_to_dict

database = MySQLDatabase(
    "docusign_new",
    user="nsai_user",
    password="helloworld",
    host="localhost",
    port=3306
)


class BaseModel(Model):
    class Meta:
        database = database

    createdAt = DateTimeField(default=datetime.now)
    updatedAt = DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        self.updatedAt = datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)

    def remove_none_values(self, nested_dict):
        cleaned_dict = {}
        for key, value in nested_dict.items():
            if isinstance(value, dict):
                cleaned_value = self.remove_none_values(value)
                if cleaned_value:  # Only add if cleaned_value is not empty
                    cleaned_dict[key] = cleaned_value
            elif value is not None:
                cleaned_dict[key] = value
        return cleaned_dict

    @classmethod
    def to_dict(cls, model_instances, backrefs=True):
        if isinstance(model_instances, list):
            return [cls.to_dict_single(instance, backrefs=backrefs) for instance in model_instances]
        else:
            return cls.to_dict_single(model_instances, backrefs=backrefs)

    @classmethod
    def to_dict_single(cls, model_instance, backrefs=True):
        model_dict = model_to_dict(model_instance, backrefs=backrefs)
        cleaned_dict = cls().remove_none_values(model_dict)
        return cleaned_dict



