from Training import Training, PersistenceTraining
import unittest
import os.path


#class TestTraining(unittest.TestCase):
#	def setUp(self):
#		self.training = Training(10,"Корабль 5","01.09.2022","Белое море",4)
#	def test_change_mark(self):
#		self.training.change_mark(3)
#		self.assertEqual(self.training.mark,3)
#	def test_change_ship(self):
#		self.training.change_ship("Корабль 3")
#		self.assertEqual(self.training.ship,'Корабль 3')


#if __name__ == "__main__":
#    unittest.main()


class Test_Training(unittest.TestCase):
    def setUp(self):
        self.test_t = Training(10,"Корабль 5","01.09.2022","Белое море",4)

    def test_del_Person(self):
        del self.test_t
        self.assertFalse(os.path.exists('training.pkl'))  # проверяем отсутствие файла после удаления объекта

class Test_PersistencePerson(unittest.TestCase):
    def setUp(self):
        self.test_tt = PersistenceTraining()
        self.test_t = Training(10,"Корабль 5","01.09.2022","Белое море",4)

    def test_serialize(self):
        self.test_tt.serialize(self.test_t)
        self.assertTrue(os.path.exists('training.pkl'))  # проверяем наличие файла после сериализации

    def test_deserialize(self):
        self.test_tt.serialize(self.test_t)
        training = self.test_tt.deserialize()
        self.assertEqual(training.unit, 10)  # проверяем корректность десериализованных данных

    def tearDown(self):
        if os.path.exists('person.pkl'):
            os.remove('person.pkl')

if __name__ == '__main__':
    unittest.main()