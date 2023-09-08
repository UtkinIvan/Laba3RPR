from Ship import Ship, PersistenceShip
import unittest
import os.path

#class TestShip(unittest.TestCase):
	#def setUp(self):


#	self.ship = Ship(31,"Корабль1","Военный","19.01.2000","Наработка 1 Наработка 2",50,"Пароход","Подводная лодка")
	#def test_change_id(self):
		#	self.ship.change_id(50)


#	self.assertEqual(self.ship.id,50)
	#def test_add_seats(self):
		#		self.ship.add_seats(5)
#		self.assertEqual(self.ship.seats,55)


#if __name__ == "__main__":


#    unittest.main()


class TestShip11(unittest.TestCase):
    def setUp(self):
        self.test_s = Ship(31,"Корабль1","Военный","19.01.2000","Наработка 1 Наработка 2",50,"Пароход","Подводная лодка")

    def test_del_Person(self):
        del self.test_s
        self.assertFalse(os.path.exists('ship.pkl'))  # проверяем отсутствие файла после удаления объекта

class TestPersistenceShip(unittest.TestCase):
    def setUp(self):
        self.test_ss = PersistenceShip()
        self.test_s = Ship(31,"Корабль1","Военный","19.01.2000","Наработка 1 Наработка 2",50,"Пароход","Подводная лодка")

    def test_serialize(self):
        self.test_ss.serialize(self.test_s)
        self.assertTrue(os.path.exists('ship.pkl'))  # проверяем наличие файла после сериализации

    def test_deserialize(self):
        self.test_ss.serialize(self.test_s)
        ship = self.test_ss.deserialize()
        self.assertEqual(ship.id, 31)  # проверяем корректность десериализованных данных

    def tearDown(self):
        if os.path.exists('ship.pkl'):
            os.remove('ship.pkl')

if __name__ == '__main__':
    unittest.main()
