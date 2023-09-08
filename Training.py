import BankTransaction
import pickle

class Training:
	def __init__(self,unit,ship,date,place,mark):
		self.unit = unit
		self.ship = ship
		self.date = date
		self.place = place
		self.mark = mark
	def change_mark(self,new_mark):
		self.mark = new_mark
		print('Оценка изменена')
	def change_ship(self,new_ship):
		self.ship = new_ship
		print('Корабль был изменён')
	def show_info(self):
		print(f'Дата учения - {self.date}')
		print(f'Место проведения - {self.place}')
		print(f'Оценка - {self.mark}')
	def show_last_date(self):
		action = "Последняя дата учения: {0}".format(self.date)
		print(action)
		self.queue.append(BankTransaction(action))
	def get_transaction(self):
		for i in range(len(self.queue)):
			item = self.queue.pop(0)
			print('when {0} : operation {1}'.format(item.when, item.operation))
	def __repr__(self):
		return "Дата: {0}".format(self.date)
	def __del__(self):
		print("Вызван деструктор класса Training")



class PersistenceTraining:
	@staticmethod
	def serialize(training):
		with open('training.pkl', 'wb') as f:
			pickle.dump(training, f)

	@staticmethod
	def deserialize():
		with open('training.pkl', 'rb') as f:
			training = pickle.load(f)
		return training

	def __del__(self):
		print("Вызван деструктор класса PersistenceTraining")