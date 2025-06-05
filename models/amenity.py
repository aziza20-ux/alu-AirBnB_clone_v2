from models.base_model import BaseModel


class Amenity(BaseModel):

    name = ""

    def __init__(self, *args, **kwargvs):
        super().__init__(*args, **kwargvs)
