import BankTransaction
import pickle


class Person:
	def __init__(self,surname,unit,post,born_year,year_military_start,merit,rewards):
		self.surname = surname
		self.unit = unit
		self.post = post
		self.born_year = born_year
		self.year_military_start = year_military_start
		self.merit = merit
		self.rewards = rewards
		self.queue = []
	def change_unit(self,new_unit):
		self.unit = new_unit
		print('Часть изменена')
	def change_post(self,new_post):
		self.post = new_post
		print('Должность сотрудника была изменена')
	def show_info(self):
		print(f'Фамилия сотрудника - {self.surname}')
		print(f'Часть - {self.unit}')
		print(f'Должность - {self.post}')
		print(f'Год рождения - {self.born_year}')
		print(f'Год поступления на службу - {self.year_military_start}')
		print(f'Награды - {self.rewards}')

	def do_work(self):
		action = f'{self.post} {self.surname} сейчас работает!'
		print(action)
		self.queue.append(BankTransaction(action))

	def end_work(self):
		action = f'{self.post} {self.name} закончил работу!'
		print(action)
		self.queue.append(BankTransaction(action))

	def get_transaction(self):
		for i in range(len(self.queue)):
			item = self.queue.pop(0)
			print('when {0} : operation {1}'.format(item.when, item.operation))

	def __repr__(self):
		return self.surname

	def __del__(self):
		print("Вызван деструктор класса Person")

class PersistencePerson(object):
	@staticmethod
	def serialize(person):
		with open('person.pkl', 'wb') as f:
			pickle.dump(person, f)

	@staticmethod
	def deserialize():
		with open('person.pkl', 'rb') as f:
			person = pickle.load(f)
		return person

	def __del__(self):
		print("Вызван деструктор класса PersistencePerson")