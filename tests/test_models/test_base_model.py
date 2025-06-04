import unittest
from models import storage
import time
from models.base_model import BaseModel


class TestId(unittest.TestCase):
    def setUp(self):

        d = BaseModel()

        b = BaseModel()

    def test_id(self):
        d = BaseModel()
        b = BaseModel()

        self.assertNotEqual(d, b)

    def test_todict(self):
        d = BaseModel()

        dic = d.to_dict()

        self.assertIn('__class__', dic)
        self.assertEqual(dic['__class__'], 'BaseModel')

        self.assertIsInstance(dic, dict)

    def test_str(self):
        s = BaseModel()

        st = str(s)

        self.assertIn("[BaseModel]", st)

        self.assertIn(s.id, st)

    def test_save(self):
        b = BaseModel()

        original_time = b.updated_at

        time.sleep(0.01)

        b.save()

        self.assertGreater(b.updated_at, original_time)

    def tearDown(self):
        storage._FileStorage__objects.clear()
        storage.save()


if __name__ == '__main__':
    unittest.main()
