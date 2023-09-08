from Base import Base, PersistenceBase
import unittest
import os.path


#class TestBase(unittest.TestCase):
    #    def setUp(self):
        #        self.base = Base("База номер 1","Поле",10)

    #    def test_change_name(self):
        #        self.base.change_name('База номер 2')
        #        self.assertEqual(self.base.name,'База номер 2')

    #    def test_add_part(self):
        #        self.base.add_part(6)
        #        self.assertEqual(self.base.parts_count,16)


#if __name__ == "__main__":
    #    unittest.main()


class Test_Base(unittest.TestCase):
    def setUp(self):
        self.test_b = Base("База номер 1","Поле",10)

    def test_del_Person(self):
        del self.test_b
        self.assertFalse(os.path.exists('base.pkl'))  # проверяем отсутствие файла после удаления объекта

class TestPersistenceBase(unittest.TestCase):
    def setUp(self):
        self.test_bb = PersistenceBase()
        self.test_b = Base("База номер 1","Поле",10)

    def test_serialize(self):
        self.test_bb.serialize(self.test_b)
        self.assertTrue(os.path.exists('base.pkl'))  # проверяем наличие файла после сериализации

    def test_deserialize(self):
        self.test_bb.serialize(self.test_b)
        base = self.test_bb.deserialize()
        self.assertEqual(base.name, "База номер 1")  # проверяем корректность десериализованных данных

    def tearDown(self):
        if os.path.exists('base.pkl'):
            os.remove('base.pkl')

if __name__ == '__main__':
    unittest.main()


