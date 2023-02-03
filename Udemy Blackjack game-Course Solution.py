import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10,'Ace':11}
#classes
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return self.rank+ ' of '+self.suit

class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        dec_comp=''
        for card in self.deck:
            deck_comp+=' \n '+card.__str__()
        return 'The deck has: '+deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card=self.deck.pop()
    
class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0

    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value-= 10
            self.aces -= 1
    
class Chips:
    def __init__(self,total=100):
        self.total=total
        self.bet=0

    def win_bet(self):
        self.total+=self.bet
    
    def lose_bet(self):
        self.total-=self.bet

#functions

def take_bet(chips):
    while True:
        try:
            chips.bet=int(input('How many chips would you like to bet? '))
        except ValueError:
            print ('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x=input("Would you like to hit or stand? Enter h or s ").lower()
        if x[0]=='h':
            hit(deck,hand)
        
        elif x[0]=='s':
            print('PLayer stands. Dealer is playing')
            playing=False
        
        else:
            print('Sorry, please try again')
            continue
        break

def show_some(player,dealer):
    print("\nDealers Hand")
    print("<card hidden>")
    print('',dealer.cards[1])
    print("\nPLayer's Hand: ",*player.cards,sep="\n ")

def show_all(player,dealer):
    print("\nDealer's Hand: ",*dealer.cards,sep='\n')
    print("Dealer's Hand =",dealer.value)
    print("\nPLayer's Hand: ",*player.cards,sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print('Player busts!')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('Player wins!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('Dealer wins!')
    chips.lose_bet()

def push(player,dealer):
    print('Dealer and Player tie! Push.')

while True:
    #ignoring opening statement
    #creat and shuffle the deck
    deck=Deck()
    deck.shuffle()

    player_hand=Hand()
    player_hand=add_card(deck.deal_one())
    player_hand.add_card(deck.deal())

    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    #set up Player's chips
    player_chips=Chips()

    #prompt player for their bet
    take_bet(player_chips)

    #show cards(except the one dealer card)
    show_some(player_hand,dealer_hand)

    while playing: #playing is a variable from the hit or stand function
        #prompt player to hit or stand
        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck,dealer_hand)
            
    