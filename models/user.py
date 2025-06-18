from models.base_model import BaseModel,Base
from sqlalchemy import column
from sqlalchemy import string
from sqlalchemy import table
from sqlalchemy.orm import relationship

class User(BaseModel,Base):
    __tablename__ = "users"

    email = column(string(128) nullable=False)
    password = column(string(128) nullable=False)
    first_name = column(string(128) nullable=False)
    last_name = column(string(128) nullable=False)
    places = relationship(
        "Places"
        backref="user"
        cascading="all, delete_orphan"
    )
    reviews = relationship(
        "Review"
        backref="user"
        cascading="all,delete_orphan"
    )


