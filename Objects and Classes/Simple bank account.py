class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def Deposit(self,dep_amount):
        self.balance+=dep_amount

        print("Deposit Done with {}. So your total balance is {}".format(dep_amount,self.balance))


    def __str__(self):
        return "Owner is {} \n Balance is {}".format(self.owner,self.balance)


    def Withdraw(self,withd_amount):
        if self.balance>withd_amount:
            self.balance-=withd_amount
            print("Withdrawal successfull of {}".format(withd_amount))

        else:
            print("insufficient fund")
a=Account('ram',100)
print(a.balance)
print(a)
print(a.balance)
a.Deposit(50)
a.Withdraw(150)
a.Withdraw(50)
