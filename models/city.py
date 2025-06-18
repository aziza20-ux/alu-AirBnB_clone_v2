from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import column, string, table, float
from sqlalchemy.orm import ForeignKey, relationship


class City(BaseModel, Base):
    __tablename__ = "cities"
    name = column(string(128), nullable=False)
    state_id = column(string(60), nullable=False ForeignKey("states.id"))
    places = relationship(
        "Place"
        backref="cities"
        cascading="all,delete_orphan")
