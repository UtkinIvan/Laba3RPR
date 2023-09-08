import BankTransaction
import pickle

class Ship:
	def __init__(self,id,name,type,date,work,seats,engine,place):
		self.id = id
		self.name = name
		self.type = type
		self.date = date
		self.work = work
		self.seats = seats
		self.engine = engine
		self.place = place
	def change_id(self,new_id):
		self.id = new_id
		print('Кораблю был присвоен новый идентификационный номер')
	def add_seats(self,count):
		self.seats += count
		print(f'Количество мест было увеличено на {count}')
	def show_info(self):
		print(f'Количество посадочных мест - {self.seats}')
		print(f'Устройство двигателя - {self.engine}')
		print(f'Размещение корпуса - {self.place}')
	def show_count_seats(self):
		action = "На корабле {0} находится {1} мест".format(self.name, self.seats)
		print(action)
		self.queue.append(BankTransaction(action))

	def get_transaction(self):
		for i in range(len(self.queue)):
			item = self.queue.pop(0)
			print('when {0} : operation {1}'.format(item.when, item.operation))

	def __repr__(self):
		return "Это грузовой корабль"

	def __del__(self):
		print("Вызван деструктор класса Ship")


class PersistenceShip(object):
	@staticmethod
	def serialize(ship):
		with open('ship.pkl', 'wb') as f:
			pickle.dump(ship, f)

	@staticmethod
	def deserialize():
		with open('ship.pkl', 'rb') as f:
			ship = pickle.load(f)
		return ship

	def __del__(self):
		print("Вызван деструктор класса PersistenceShip")