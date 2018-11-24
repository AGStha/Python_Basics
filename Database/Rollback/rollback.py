class Account(object):
    def __init__(self, name: str, opening_balance: float = 0.0):
        self.name = name
        self._balance = opening_balance
        print("Account for {} is created".format(self.name))
        self.show_balance()

    def deposit(self, amount: float) -> float:
        if amount > 0.0:
            self._balance += amount
            print("{} deposited on {} Account".format(amount, self.name))
        else:
            print("Balance is negative")
        return self._balance

    def withdraw(self, amount: float) -> float:
        if 0.0 < amount < self._balance:
            self._balance -= amount
            print("{} withdrwawn from {}".format(amount, self.name))
            return amount
        else:
            print("amount should be lesser than current balance and greater than 0 ")
            return 0.0

    def show_balance(self):
        print("Balance for {} is {} ".format(self.name, self._balance))


if __name__ == '__main__':
    acc = Account("Anuj")
    acc.deposit(20.0)
    acc.deposit(10.0)
    acc.withdraw(15.0)
    acc.withdraw(0.0)
    acc.show_balance()
