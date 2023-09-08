from datetime import datetime

class BankTransaction(object):

    def __init__(self, operation):
        self.when = datetime.today().replace(microsecond=0)
        self.operation = operation

    def __del__ (self):
        print("Вызван деструктор класса BankTransaction")
        with open ('transaction.txt', 'a') as f:
            f.write('when {0} : amount {1} \n'.format(self.when, self.operation))
        f.close


