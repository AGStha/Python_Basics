import sqlite3


db = sqlite3.connect("accounts.sqlite")
db.execute("create table if not exists accounts (name text primary key not null,"
           " balance integer not null")
db.execute("create table if not exists transactions (time timestamp not null,"
           " account text not null, amount integer not null, primary key (time, account)) ")


class Account(object):
    def __init__(self, name: str, opening_balance: float = 0.0):
        self.name = name
        self._balance = opening_balance
        print("Account for {} is created".format(self.name))
        self.show_balance()

    def deposit(self, amount: float) -> float:
        if amount > 0.0:
            self._balance += amount
            print("{} deposited on {} Account".format(amount/100, self.name))
        else:
            print("Balance is negative")
        return self._balance/100

    def withdraw(self, amount: float) -> float:
        if 0.0 < amount < self._balance:
            self._balance -= amount
            print("{} withdrwawn from {}".format(amount, self.name))
            return amount/100
        else:
            print("amount should be lesser than current balance and greater than 0 ")
            return 0.0

    def show_balance(self):
        print("Balance for {} is {} ".format(self.name, self._balance/100))


if __name__ == '__main__':
    acc = Account("Anuj")
    acc.deposit(2000)
    acc.deposit(1000)
    acc.withdraw(1500)
    acc.withdraw(0)
    acc.show_balance()
