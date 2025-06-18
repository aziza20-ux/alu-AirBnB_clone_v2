from models.base_model import BaseModel, Base
import os
from models.city import City


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import column
from sqlalchemy import string
from sqlalchemy import table
from sqlalchemy import float
from sqlalchemy.orm import relationship, ForeignKey


class State(BaseModel, Base):
    __tablename__ = "states"
    name = column(string(128), nalluble=False)
    cities = relationship(
        "City"
        backref="State"
        Cascading="all, delete_orphan"
    )

    type_storage = os.getenv("HBNB_TYPE_STORAGE")
    if type_storage == "fs":
        @property
        def cities(self):
            from models import storage
            all_cities = [obj for obj in storage.all().values()
                          if isinstance(obj, City)]
            state_cities = []
            for city in all_cities:
                if city.state_id == self.id:
                    state_cities.append(city)
            return state_cities
