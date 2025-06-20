from models.base_model import BaseModel, Base
from sqlalchemy import column
from sqlalchemy import string, ForeignKey
from sqlalchemy import table
from models.place import Place


class Review(BaseModel, Base):
    __tablename__ = "reviews"

    place_id = column(string(60) nullable=False, ForiegnKey("places.id"))
    user_id = column(string(60) nullable=False, ForiegnKey("users.id"))

    text = column(string(1024) nullable=False)
