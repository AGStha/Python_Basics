class Account:
    """
    Attributes: It keeps record of all the attributes.
    Methods:
            withdraw()
            deposit()

    """
    def __init__(self,name,balance):
    """
        This is the initialie method of the Account class which is automatically.


    """

        self.name=name
        self.balane=balance


#help(Account)
print(Account.__doc__)
print(Account.__init__().__doc__)
