class Account:
    """Class to represent Account

        Attributes: It keeps record of all the attributes.
            name(char):the name of the client
            balance(float): the balance of the client

    Methods:
            withdraw()
            deposit()

    """
    def __init__(self, name, balance):

        """initmethod of Account class

                This is the initialie method of the Account class which is automated"

            Args:
                name(char): initialises the name attributes
                balance(float): it initialisee the balance attributes.

        """
        self.name = name
        self.balance = balance



#help(Account)
print(Account.__doc__)

#following line gives the doc of the init method.
print(Account.__init__.__doc__)


Account.__init__.__doc__= """
                              This is the another method of giving the documentation.                      
                                """
help(Account)