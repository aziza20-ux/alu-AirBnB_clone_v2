#!/usr/bin/python3

import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import column
from sqlalchemy import string
from sqlalchemy import table
from sqlalchemy import float


Base = declarative_base()
class BaseModel:
    id = column(string(60), nullable=False, primary_key=True)
    created_at = column(datetime, nullable=False, default=datetime.now())
    updated_at = column(datetime, nullable=False, default=datetime.now())

    """the constructor of the class '__init__'"""

    def __init__(self, *args, **kwargvs):

        if kwargvs:
            for k, v in kwargvs.items():
                if k == '__class__':
                    continue

                elif k in ["created_at", "updated_at"]:
                    setattr(self, k, datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            

    def __str__(self):
        """it will return the string represation of object"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """this method will save the last time object was modified"""

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """the method to returm dictionary of the attributes of any object"""
        obj_dict = self.__dict__.copy()

        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict.pop("_sa_instance_state", None)

        return obj_dict
    def delete(self):
        models.storage.delete(self)


if __name__ == '__main__':

    c = BaseModel(city="aziza", id="2")
    c.save()
