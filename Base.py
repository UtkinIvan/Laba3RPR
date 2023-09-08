import BankTransaction
import pickle

class Base:
    def __init__(self,name,geo,parts_count):
        self.name = name
        self.geo = geo
        self.parts_count = parts_count
    def change_name(self,new_name):
        self.name = new_name
        print('Название базы изменено')
    def add_part(self):
        self.parts_count += 1
        print('Количество баз было увеличено')
    def show_info(self):
        print(f'Название базы - {self.name}')
        print(f'Геопологическое положение - {self.geo}')
        print(f'Количество частей - {self.geo}')

    def show_Base_name(self):
        action = "Название базы: {0}; в ней {1} частей".format(self.name, self.parts_count)
        print(action)
        self.queue.append(BankTransaction(action))

    def get_transaction(self):
        for i in range(len(self.queue)):
            item = self.queue.pop(0)
            print('when {0} : operation {1}'.format(item.when, item.operation))

    def __repr__(self):
        return "На этой базе одна часть"

    def __del__(self):
        print("Вызван деструктор класса Base")


class PersistenceBase(object):
    @staticmethod
    def serialize(base):
        with open('base.pkl', 'wb') as f:
            pickle.dump(base, f)

    @staticmethod
    def deserialize():
        with open('base.pkl', 'rb') as f:
            base = pickle.load(f)
        return base

    def __del__(self):
        print("Вызван деструктор класса PersistenceBase")