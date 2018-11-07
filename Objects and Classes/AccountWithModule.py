import datetime
import pytz


class Account:

    @staticmethod               #we can make static method by removing self and adding @staticmethod.
    def _current_time():
        utc_time=datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, _name, _balance):
        self._name = _name      # we use _name to make it private or non-public

        self._balance = _balance
        self.trasaction_list = [(Account._current_time(), _balance)]
        print("Account Created for {}".format(_name))
        self.show_balance()

    def deposit(self , amt):
        self._balance+=amt
        #self.trasaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()),amt))
        self.trasaction_list.append((Account._current_time(),amt))#Static method call of class Account.
        self.show_balance()

    def withdraw(self,amt):
        if self._balance>amt>0:
            self._balance-=amt
            self.show_balance()
            self.trasaction_list.append((Account._current_time(), -amt))
        else:
            print("Insufficient Amount")
            self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self._balance))

    def show_transaction(self):
        for date,amt in self.trasaction_list:
            if amt>0:
                tran_type = "Deposited"
            else:
                tran_type = "Withdrawn"
                amt*-1
            print("{} {} on {} (local time was {})".format(amt, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    bibi= Account('Bibika',0)
    bibi.deposit(100)
    bibi.withdraw(50)
    bibi.show_transaction()

    anuj = Account('Anuj', 100)
    anuj._balance=200        # We should not allow client outside class to add like this.
    #So we use '_' underscore to protect it.in the declaration part.
    #but we can use
    anuj.__balance=200 # we can use this to access the attribute again.
    anuj.deposit(50)
    anuj.withdraw(90)
    anuj.show_transaction()
    anuj.show_balance()
    print(anuj.__dict__)
    anuj._Account__balance=200#This is discouraged.
    anuj.show_balance()

