import random

'''Local Variable Declaration'''
suits = ('Hearts', 'Diamonds', 'Spades', 'Club')
ranks = ('Two', 'Three', 'Four', 'Five',
         'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King'
         , 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
          'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'King': 10, 'Queen': 10
    , 'Ace': 11}
playing = True


class Card:
    """Class To Represent Cards
    Attributes:
                Suits(str): Represents suits like diamond,spade. etc.
                Rank: It represents different rank
                value: Represents the value to each rank
    Methods:
                __Init_(): It initialises the variables.
                __str__():It is string representation method.

    """
    def __init__(self):
        self.suits = suits
        self.ranks = ranks
        self.values = values
        pass

    def __str__(self):
        return " {} of {}".format(self.ranks,self.suits)
        pass

a=Card()
print(a)