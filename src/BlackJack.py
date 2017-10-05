class Cards(object):
    '''
    purpose of this class is to describe a the state of a card . Each instant of a card has a suit and number
    attribute. For the rank, numerical value was assigned to the face cards as an easy way to rank the cards
    the _str_ method was overridden for this purpose to translate it
    '''
    def __init__(self,suit,number):
        self.suit=suit
        self.number=number
    def __str__(self):
        if self.number==11:
           self.number="Jack"
        if self.number==12:
            self.number="Queen"
        if self.number==13:
            self.number="King"
        if self.number==14:
            self.number="Ace"
        return str(self.number)+" of "+ self.suit


    suits=("HEARTS","CLUBS","SPADES","DIAMONDS")


ace=Cards("heart",12)
print ace
print Cards("diamond",14)

class Deck(object):
    '''
    This puts the instances of 52 cards and places them in a List that represents a Deck.

    '''

    global Deck_of_Cards
    Deck_of_Cards=[]

    def populate_Deck(self):
        '''
        this will fill an empty list and fill it with 52 instances of Cards to represent a Decj
        :return: Deck
        '''
        for number in range(2,15):
            for suit in Cards.suits:
                Deck_of_Cards.append(Cards(suit,number))
                #print Cards(suit,number)

        for card in Deck_of_Cards:
            print card


    def shuffle_Deck(self,deck):
        '''
        this is shuffling the deck three times
        :param deck: Deck of Cards
        :return:  A shuffled Deck
        '''
        from random import shuffle
        for number in range(0,3):
            shuffle(deck)


class Player(object):
    '''
    Class to represent the player. This is where the players moves are seen, and their hand
    '''
    global player_hand
    player_hand=[]
    def stand(self):
        '''
        technically stand does nothing in the game. But i value has to be added to make sure the player went
        :return:
        '''
        pass
    def hit(self):
        '''
        A card is removed from the deck and placed in the players hand
        :return: players hand
        '''
        player_hand.append(Deck_of_Cards.pop())

d=Deck()
d.populate_Deck()
d.shuffle_Deck(Deck_of_Cards)











