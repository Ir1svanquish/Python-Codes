# card.py
# This program defines the class Card for representing a playing card.

class Card:
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
    def value(self):
        if self.rank > 10:
            return 10
        else:
            return self.rank
        
    def __str__(self):
        name = ""
        if self.rank == 1:
            name += "Ace"
        elif self.rank == 11:
            name += "Jack"
        elif self.rank == 12:
            name += "Queen"
        elif self.rank == 13:
            name += "King"
        else:
            name += str(self.rank)
        name += " of "
        if self.suit == "d":
            name += "Diamonds"
        elif self.suit == "c":
            name += "Clubs"
        elif self.suit == "h":
            name += "Hearts"
        else:
            name += "Spades"
        return name
        
    def __repr__(self):
        return "Card({:s}, ’{:s}’)".format(str(self.rank), str(self.suit))
