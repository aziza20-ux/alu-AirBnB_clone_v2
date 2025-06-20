import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import column, string, table, text
from sqlalchemy import sessionmaker, scoped_session
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

from models.base_model import Base, BaseModel
classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "Review": Review,
    "City": City,
    "Amenity": Amenity
}
load_dotenv(".env")


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        host = os.getenv("HBNB_MYSQL_HOST")
        password = os.getenv("HBNB_MYSQL_PWD")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")
        connection_string = f"mysql+mysqldb://{user}:{password}@{host}/{db}"
        self.__engine = create_engine(connection_string, pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        dict_re = {}
        if cls:
            results = self.__session.query(cls).all()

        else:
            results = []
            for class_str, class_obj in classes.items():
                if class_str == "BaseModel":
                    continue
                results.extend(self.__session.query(class_obj).all())
        for obj in results:
            key = f"{obj.__class__.__name__}.{obj.id}"
            dict_re[key] = obj
        return dict_re

    def new(self, obj):
        self.__session.add(obj)

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)
        else:
            return

    def save(self):
        self.__session.commit()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
