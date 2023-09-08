import BankTransaction
import pickle

class BankAccount(object):

    def __init__(self, balance=0):
        self.number = _next_number()
        self.balance = balance
        self.queue = []

    def deposit(self, amount):
        self.balance += amount
        self.queue.append(BankTransaction(amount))

    def get_transaction(self):
        for i in range(len(self.queue)):
            item = self.queue.pop(0)
            print('when {0} : amount {1}'.format(item.when, item.operation))


class PersistenceAccount(object):
    @staticmethod
    def serialization(account):
        with open ('bank_account.pkl', 'wb') as f:
            pickle.dump(account, f)
        f.close

    @staticmethod
    def deserialize():
        with open ('bank_account.pkl', 'rb') as f:
            account = pickle.load(f)
        f.close
        return account

    def __del__(self):
        print("Вызван деструктор класса PersistenceAccount")