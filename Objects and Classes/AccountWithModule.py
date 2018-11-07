import datetime
import pytz

class Account:

    @staticmethod               #we can make static method by removing self and adding @staticmethod.
    def _current_time():
        utc_time=datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)


    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.trasaction_list=[]

    def deposit(self,amt):
        self.balance+=amt
        #self.trasaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()),amt))
        self.trasaction_list.append((Account._current_time(),amt))#Static method call of class Account.

        self.show_balance()
    def withdraw(self,amt):
        if self.balance>amt>0:
            self.balance-=amt
            self.show_balance()
            self.trasaction_list.append((Account._current_time(),-amt))
        else:
            print("Insufficient Amount")
            self.show_balance()
    def show_balance(self):
        print("Balance is {}".format(self.balance))
    def show_transaction(self):
        for date,amt in self.trasaction_list:
            if amt>0:
                tran_type="Deposited"
            else:
                tran_type="Withdrawn"
                amt*-1
            print("{} {} on {} (local time was {})".format(amt,tran_type,date,date.astimezone()))

if __name__== '__main__':
    anuj=Account('Anuj',100)
    anuj.deposit(50)
    anuj.withdraw(200)
    anuj.show_transaction()

