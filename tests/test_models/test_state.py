import unittest
from models import storage
import time
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class childclassestest(unittest.TestCase):
    def setUp(self):
        self.stat = State()
        self.cit = City()
        self.plac = Place()
        self.amenit = Amenity()
        self.revie = Review()

        self.stat.save()
        self.cit.save()
        self.plac.save()
        self.amenit.save()
        self.revie.save()

    def test_state(self):

        objects = storage.all()

        key = f"{self.stat.__class__.__name__}.{self.stat.id}"

        stored = objects[key]

        self.assertIn(key, objects)

    def test_city(self):

        objects = storage.all()

        key = f"{self.cit.__class__.__name__}.{self.cit.id}"

        stored = objects[key]
        self.assertIn(key, objects)

    def test_amenity(self):

        objects = storage.all()

        key = f"{self.amenit.__class__.__name__}.{self.amenit.id}"

        stored = objects[key]
        self.assertIn(key, objects)

    def test_review(self):

        objects = storage.all()

        key = f"{self.revie.__class__.__name__}.{self.revie.id}"

        stored = objects[key]
        self.assertIn(key, objects)

    def test_place(self):

        objects = storage.all()

        key = f"{self.plac.__class__.__name__}.{self.plac.id}"

        stored = objects[key]
        self.assertIn(key, objects)


if __name__ == '__main__':
    unittest.main()
