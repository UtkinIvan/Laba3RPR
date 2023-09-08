from Unit import Unit, PersistenceUnit
import unittest
import os.path


#class TestUnit(unittest.TestCase):
#	def setUp(self):
#		self.unit = Unit(5,"База 1","Место 1","Морская пехота")
#	def test_change_number(self):
#		self.unit.change_number(10)
#		self.assertEqual(self.unit.number,10)
#	def test_change_place(self):
#		self.unit.change_place('Место 2')
#		self.assertEqual(self.unit.place,'Место 2')


#if __name__ == "__main__":
#    unittest.main()


class Test_Unit(unittest.TestCase):
    def setUp(self):
        self.test_u = Unit(5,"База 1","Место 1","Морская пехота")

    def test_del_Person(self):
        del self.test_u
        self.assertFalse(os.path.exists('unit.pkl'))  # проверяем отсутствие файла после удаления объекта

class Test_PersistencePerson(unittest.TestCase):
    def setUp(self):
        self.test_uu = PersistenceUnit()
        self.test_u = Unit(5,"База 1","Место 1","Морская пехота")

    def test_serialize(self):
        self.test_uu.serialize(self.test_u)
        self.assertTrue(os.path.exists('unit.pkl'))  # проверяем наличие файла после сериализации

    def test_deserialize(self):
        self.test_uu.serialize(self.test_u)
        unit = self.test_uu.deserialize()
        self.assertEqual(unit.number, 5)  # проверяем корректность десериализованных данных

    def tearDown(self):
        if os.path.exists('unit.pkl'):
            os.remove('unit.pkl')

if __name__ == '__main__':
    unittest.main()