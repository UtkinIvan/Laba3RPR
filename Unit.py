import BankTransaction
import pickle


class Unit:
	def __init__(self,number,base,place,military_type):
		self.number = number
		self.base = base
		self.place = place
		self.military_type = military_type
	def change_number(self,new_number):
		self.number = new_number
		print('Номер части был изменён')
	def change_place(self,new_place):
		self.place = new_place
		print('Часть базируется в другом месте')
	def show_info(self):
		print(f'Номер базы - {self.number}')
		print(f'Место базирования - {self.place}')
		print(f'Вид войск - {self.military_type}')


class PersistenceUnit(object):
	@staticmethod
	def serialize(unit):
		with open('unit.pkl', 'wb') as f:
			pickle.dump(unit, f)

	@staticmethod
	def deserialize():
		with open('unit.pkl', 'rb') as f:
			unit = pickle.load(f)
		return unit

	def __del__(self):
		print("Вызван деструктор класса PersistenceUnit")