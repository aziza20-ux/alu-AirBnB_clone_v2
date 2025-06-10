from models.base_model import BaseModel,Base
from sqlalchemy import column,string,table,integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import os
from models.review import Review
from models.amenity import Amenity



Place_amenity = table('place_amenity',Base.metadata,
                        column('place_id',string(60),
                                ForeignKey('places.id'),primary_key=True,nullable=False),
                        column('amenity_id',string(60),
                                ForeignKey('amenities.id'),primary_key=True,nullable=False)
                                )
class Place(BaseModel,Base):
    __tablename__ = "places"
    city_id = column(string(60), ForeignKey('cities.id'),nullable=False,)
    user_id = column(string(60), ForeignKey('users.id'),nullable=False)
    name = column(string(128), nullable=False)
    description = column(string(1024), nullable=False)
    number_rooms = column(integer,default=0)
    number_bathrooms = column(integer,default=0)
    max_guest = column(integer,default=0)
    price_by_night = column(integer,default=0)
    latitude = column(float)
    longitude = column(float)
    amenity_id = []
    reviews = relationship(
        "Review"
        backref="place"
        cascading="all,delete_orphan"
        )
    amenities = relationship(
        "Amenity"
        secondary="Place_amenity"
        viewonly=False
        backref="Place"
        )

    
    type_storage = os.getenv("HBNB_TYPE_STORAGE")
    if type_storage == "fs":
        @property
        def reviews(self):
            from models import storage
            all_reviews = [obj for obj in storage.all().values()
                           if isinstance(obj,Review)]
            review_place = []
            for obj in all_reviews:
                if obj.place_id == self.id:
                    review_place.append(obj)
            return review_place
        @property
        def amenities(self):
            from models import storage
            all_amenities = storage.all(Amenity).values()
            linked_amenities = []
            for amenity in all_amenities:
                if amenity.id in self.amenity_ids:
                    linked_amenities.append(amenity)
            return linked_amenities
        @amenities.setter
        def amenities(self, obj):

            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)




            


