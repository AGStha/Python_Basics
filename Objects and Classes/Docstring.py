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


#This is the demo program for string formatting
string_a="this is \n new line and \t\t tabbed"
print(string_a)

raw_string=r'this is raw string \n'
print(raw_string)

char_string='this is '+chr(10) +'a string split'+chr(9)+chr(9)+'and tabbed'
print(char_string)

#Backlash
bs_string="this is \'string"
print(bs_string)
#it prints ' as string

error_string=r'this is \\'
print (error_string)