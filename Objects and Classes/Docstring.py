class Account:
    """
    Attributes: It keeps record of all the attributes.
    Methods:
            withdraw()
            deposit()

    """
    def __init__(self,name,balance):

        """
            This is the initialie method of the Account class which is automated"
        """
        self.name=name
        self.balance=balance



#help(Account)
print(Account.__doc__)

#following line gives the doc of the init method.
print(Account.__init__.__doc__)


