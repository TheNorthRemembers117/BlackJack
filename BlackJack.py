
#BlackJack (21)
#Version 1.0
#Developed by Nomad
#(c)2020 by RileyMedia Inc. All Rights Reserved. 

#Shuffle libary import and global constant declaration
from random import shuffle
Ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
Suits = ['Clubs','Diamonds','Hearts','Spades']
PlayerCard = 0
DealerCard = 0

#Card Object Definition 
class _card:
    def __init__(self,_rank,_suit):
        self.Rank = _rank
        self.Suit = _suit

#Player / Dealer Object Definition
class _player:
    def __init__(self):
        self.Hand = []
        self.Score = 0
        self.DealerSwitch = 17

#Deck array creation and Player / Dealer object creation 
Deck = []
Player = _player()
Dealer = _player()

#Deck array population and initialization 
for x in range(6):
    for Suit in Suits:
        for Rank in Ranks:
            Card = _card(Rank,Suit)
            Deck.append(Card)

shuffle(Deck)

#Main game loop
while len(Deck) >= 10:

    #Populate Player and Dealer hands
    for x in range(2):
        PlayerCard = Deck.pop(0)
        DealerCard = Deck.pop(0)
        Player.Hand.append(PlayerCard)
        Dealer.Hand.append(DealerCard)
        
    #Iterate through Player and Dealer hands to calculate score
    #If the card is an ace, it's worth either 11 or 1 depending on the hand score already aquired
    #If it's a face card (Jack, Queen or King), It's worth 10 points
    #Otherwize, if it's a non-face card, It's worth the value of the Card's rank. 
    for Card in Player.Hand:
        if Card.Rank == 'Ace':
            if Player.Score < 11:
                Player.Score += 11

            elif Player.Score >= 11:
                Player.Score += 1

        elif Card.Rank in ['Jack','Queen','King']:
            Player.Score += 10

        elif Card.Rank in [2,3,4,5,6,7,8,9,10]:
            Player.Score += Card.Rank

    for Card in Dealer.Hand:
        if Card.Rank == 'Ace':
            if Dealer.Score < 11:
                Dealer.Score += 11

            elif Dealer.Score >= 11:
                Dealer.Score += 1

        elif Card.Rank in ['Jack','Queen','King']:
            Dealer.Score += 10

        elif Card.Rank in [2,3,4,5,6,7,8,9,10]:
            Dealer.Score += Card.Rank
 
    PlayerAction = 0

    #User (Player) loop
    while PlayerAction < 2 and PlayerAction >= 0 and Player.Score < 21:
      
        #Display Player's score and ask for user choice. 
        print("Your Score =", Player.Score)
        PlayerAction = int(input("Hit or Stay (1 for Hit, 2 for Stay): "))

        #Check user input 
        if PlayerAction == 1:

            #Add card to Player's hand
            print("Hit. ")
            PlayerCard = Deck.pop(0)
            Player.Hand.append(PlayerCard)

            #Repeat scoring logic.
            if PlayerCard.Rank == 'Ace':
                if Player.Score < 11:
                    Player.Score += 11

                elif Player.Score >= 11:
                    Player.Score += 1

            elif PlayerCard.Rank in ['Jack','Queen','King']:
                Player.Score += 10

            elif PlayerCard.Rank in [2,3,4,5,6,7,8,9,10]:
                Player.Score += PlayerCard.Rank

        elif PlayerAction == 2:
            print("Stay. ")
    
    #Automated dealer loop
    while Dealer.Score < Dealer.DealerSwitch:

        #Add card to Dealer's hand
        DealerCard = Deck.pop(0)
        Dealer.Hand.append(DealerCard)

        #Repeat scoring logic
        if DealerCard.Rank == 'Ace':
            if Dealer.Score < 11:
                Dealer.Score += 11

            elif Dealer.Score >= 11:
                Dealer.Score += 1

        elif DealerCard.Rank in ['Jack','Queen','King']:
            Dealer.Score += 10

        elif DealerCard.Rank in [2,3,4,5,6,7,8,9,10]:
            Dealer.Score += Card.Rank

    #Determine Winner
    #If the player has a score of exactly 21, the Player wins automatically, regardless if the dealer has the same
    #If the player has a score of over 21, the Dealer wins automatically, regardless of the dealer's own score
    #If the dealer has a score of over 21, the Player wins automatically, regardless of the player's own score.
    #If the dealer has a score of exactly 21, and the Player does not, the Dealer wins automatically. 
    #Otherwize, if none of these conditions are met, the winner is whomever has the highest. (Ties are accounted for). 
    if Player.Score == 21:
        print("Winner Winner Chicken Dinner!: You got BlackJack!")

    elif Player.Score >= 21:
        print("Big oof!: You done busted.")

    elif Dealer.Score == 21:
        print("Big oof!: The dealer got BlackJack.")

    elif Dealer.Score >= 21:
        print("Uh Oh!: The dealer busted! You win.")

    else:
        if Player.Score > Dealer.Score:
            print("Well done. Your score was better than the dealer's, You win.")

        elif Player.Score < Dealer.Score:
            print("Ah, Shucks. The dealer's score was better than yours. You lose.")

        elif Player.Score == Dealer.Score:
            print("That's a tie. Split the pot?")

    #Reset Player score and empty player hands 
    Player.Score = 0
    Dealer.Score = 0
    Player.Hand = []
    Dealer.Hand = []