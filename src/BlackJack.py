class Cards(object):
    def __init__(self,suit,number):
        self.suit=suit
        self.number=number
    def __str__(self):
        if self.number==11:
           self.number="Ace"
        if self.number==12:
            self.number="Jack"
        if self.number==13:
            self.number="Queen"
        if self.number==14:
            self.number="King"
        return self.suit+" of "+self.number
ace=Cards("heart",12)
print ace

class Deck(object):
