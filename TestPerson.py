from Person import Person, PersistencePerson
import unittest
import os.path


#class TestPersistencePerson(unittest.TestCase):

    #    def setUp(self):
        #        self.first_worker = Person("Васильев",5,"Солдат",1987,2006,
                                   #                                   "Заслуга 1","Награда за выслугу, награда за смелость")

    #    def test_serialize(self):
        #        PersistencePerson.serialize(self.first_worker)
        #        get_first_person = PersistencePerson.deserialize()
        #        print(str(get_first_person), "=", str(self.first_person))
     #  self.assertEqual(str(get_first_person), str(self.first_person))


#if __name__ == "__main__":
    #    unittest.main()


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.test_p = Person('Васильев', 5, 'Солдат', 1987, 2006, 'Заслуга 1', 'Награда за выслугу, награда за смелость')

    def test_del_Person(self):
        del self.test_p
        self.assertFalse(os.path.exists('person.pkl'))  # проверяем отсутствие файла после удаления объекта

class Test_PersistencePerson(unittest.TestCase):
    def setUp(self):
        self.test_pp = PersistencePerson()
        self.test_p = Person('Васильев', 5, 'Солдат', 1987,2006, 'Заслуга 1', 'Награда за выслугу, награда за смелость')

    def test_serialize(self):
        self.test_pp.serialize(self.test_p)
        self.assertTrue(os.path.exists('person.pkl'))  # проверяем наличие файла после сериализации

    def test_deserialize(self):
        self.test_pp.serialize(self.test_p)
        person = self.test_pp.deserialize()
        self.assertEqual(person.unit, 5)  # проверяем корректность десериализованных данных

    def tearDown(self):
        if os.path.exists('person.pkl'):
            os.remove('person.pkl')

if __name__ == '__main__':
    unittest.main()

