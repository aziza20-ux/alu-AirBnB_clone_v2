from models.base_model import BaseModel,Base
from sqlalchemy import column
from sqlalchemy import string
from sqlalchemy import table
from sqlalchemy import relationship


class Amenity(BaseModel,Base):
    __tablename__ ="amenities"


    name = column(string(128) nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                viewonly=False)


