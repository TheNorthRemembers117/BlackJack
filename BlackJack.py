from random import shuffle
Ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
RankValues = [2,3,4,5,6,7,8,9,10,11,12,13,14]
Suits = ['Clubs','Diamonds','Hearts','Spades']

class _card:
    def __init__(self,_rank,_suit):
        self.Rank = _rank
        self.Suit = _suit

class _player:
    def __init__(self):
        self.Hand = []
        self.Score = 0

Deck = []

for x in range(6):
    for Suit in Suits:
        for Rank in RankValues:
            Card = _card(Rank,Suit)
            Deck.append(Card)

shuffle(Deck)

for Card in Deck:
    CardCount += 1
    RankIndex = RankValues.index(Card.Rank)
    Rank = Ranks[RankIndex]
    Suit = Card.Suit
    print(Rank, "of", Suit)

