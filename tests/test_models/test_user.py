import unittest
import time
from models.base_model import BaseModel
from models.user import User
from models import storage


class Testinguser(unittest.TestCase):
    def setUp(self):
        self.obj = User()
        self.obj.email = 'asaaziza574@gmail.com'
        self.obj.password = '132436'
        self.obj.first_name = 'aziza'
        self.obj.last_name = 'solace'
        self.obj.save()

    def test_email(self):
        key = f"{self.obj.__class__.__name__}.{self.obj.id}"
        objects = storage.all()
        self.assertIn(key, objects)
        stored = objects[key]
        self.assertEqual('asaaziza574@gmail.com', stored.email)

    def test_password(self):
        key = f"{self.obj.__class__.__name__}.{self.obj.id}"
        objects = storage.all()
        stored = objects[key]
        self.assertEqual(stored.password, '132436')

    def test_firtname(self):

        key = f"{self.obj.__class__.__name__}.{self.obj.id}"
        objects = storage.all()
        stored = objects[key]
        self.assertEqual(stored.first_name, 'aziza')

    def test_lastname(self):
        key = f"{self.obj.__class__.__name__}.{self.obj.id}"
        objects = storage.all()
        stored = objects[key]
        self.assertEqual(stored.last_name, 'solace')

    def tearDown(self):
        storage._FileStorage__objects.clear()
        storage.save()


if __name__ == '__main__':
    unittest.main()
