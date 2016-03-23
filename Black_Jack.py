
# coding: utf-8

# In[2]:

class Deck(object):
    
    def __init__(self):
        self.remaining = 52
        self.card = {'Heart A': 11, 'Heart 2': 2, 'Heart 3': 3, 'Heart 4': 4, 
                    'Heart 5': 5, 'Heart 6': 6, 'Heart 7': 7, 'Heart 8': 8,
                    'Heart 9': 9, 'Heart 10': 10, 'Heart J': 10, 'Heart Q': 10,
                    'Heart K': 10, 'Spade A': 11, 'Spade 2': 2, 'Spade 3': 3, 'Spade 4': 4, 
                    'Spade 5': 5, 'Spade 6': 6, 'Spade 7': 7, 'Spade 8': 8,
                    'Spade 9': 9, 'Spade 10': 10, 'Spade J': 10, 'Spade Q': 10,
                    'Spade K': 10, 'Diamond A': 11, 'Diamond 2': 2, 'Diamond 3': 3, 'Diamond 4': 4, 
                    'Diamond 5': 5, 'Diamond 6': 6, 'Diamond 7': 7, 'Diamond 8': 8,
                    'Diamond 9': 9, 'Diamond 10': 10, 'Diamond J': 10, 'Diamond Q': 10,
                    'Diamond K': 10, 'Club A': 11, 'Club 2': 2, 'Club 3': 3, 'Club 4': 4, 
                    'Club 5': 5, 'Club 6': 6, 'Club 7': 7, 'Club 8': 8,
                    'Club 9': 9, 'Club 10': 10, 'Club J': 10, 'Club Q': 10,
                    'Club K': 10}
    
    def dealt_card(self, card):
        del self.card[card]
        self.remaining -= 1
    
    def check_remaining(self):
        return self.remaining


# In[27]:

class Player(Deck):
    
    def __init__(self, bankroll = 100):
        Deck.__init__(self)
        self.bankroll = bankroll
        self.playersHand = [0, 0]
        self.pot = 0
        self.totalPoint = 0
        
    def adjust_bankroll(self, amount):
        self.bankroll += amount
        
    def check_hands(self):
        print(self.playersHand)
        
    def hit(self, new_card):
        self.playersHand.append(new_card)
        
    def bet(self, amount):
        if amount <= self.bankroll:
            self.adjust_bankroll(-amount)
            self.pot += amount
            return True
        else:
            print("You do not have enough money to place that bet!")
            return False

    def check_pot(self):
        return self.pot
    
    def bust(self):
        self.totalPoint = 0
        self.aceCounter = 0
        for i in self.playersHand:
            if self.card[i] == 11:
                self.aceCounter += 1
            self.totalPoint += int(self.card[i])
        
        if self.totalPoint > 21:
            while self.aceCounter > 0:
                self.totalPoint -= 10
                self.aceCounter -= 1
                if self.totalPoint <= 21:
                    break
                else:
                    continue
                     
        if self.totalPoint > 21:
            print("Busted!")
            return True
        else:
            return False
    
    def check_point(self):
        return self.totalPoint
    
    def check_bankroll(self):
        return self.bankroll
        
    def win(self, num):
        self.adjust_bankroll(self.pot*2)
        self.pot = 0
        self.playersHand = [0, 0]
        print('Player',num, ' won.')
        
    def lose(self, num):
        self.pot = 0
        self.playersHand = [0, 0]
        print('Player',num, ' lost.')
        
    def push(self, num):
        self.adjust_bankroll(self.pot)
        self.pot = 0
        self.playersHand = [0, 0]
        print("Player",num," pushed.")
        


# In[30]:

import random
class Dealer(Deck):    
    
    def __init__(self):
        Deck.__init__(self)
        self.dealersHand = [0, 0]
        self.totalPoint = 0
    
    def deal(self, card):
        return random.choice(list(card.keys()))
        
    def hit(self, new_card):
        self.dealersHand.append(new_card)
        
    def check_hands(self):
        print(self.dealersHand)
        
    def dealer_hit(self):
        self.totalPoint = 0
        self.aceCounter = 0
        for i in self.dealersHand:
            if self.card[i] == 11:
                self.aceCounter += 1
            self.totalPoint += int(self.card[i])
            
        if self.totalPoint > 21:
            while self.aceCounter > 0:
                self.totalPoint -= 10
                self.aceCounter -= 1
                if self.totalPoint <= 21:
                    break
                else:
                    continue
                    
        if self.totalPoint >= 17:
            return False
        else:
            return True
        
    def bust(self):
        if self.totalPoint > 21:
            print("Dealer busted!")
            return True
        else:
            return False
        
    def check_point(self):
        return self.totalPoint
        
    def reset_hand(self):
        self.dealersHand = [0, 0]


# In[29]:

# Blackjack by Claude Chang

print("Welcome to single deck Blackjack")
dealer = Dealer()
deck = Deck()
players = []

# Specify the number of players in the game
try:
    playerNum = int(input("How many players are there?"))
except:
    print("Only whole number is accepted!")

# Specify the bankroll for each player
for i in range(0, playerNum):
    print("Player", i+1, "...")
    try:
        player_created = Player((float(input("How much is your bankroll?"))))
        players.append(player_created)
    except:
        print("Please use dollar amount.")

# Game Start
while True:
    player_lose = []
    for i in range(0, playerNum):
        player_lose.append(False)
    
    print("")
    print("Game started - place your bets")
    print("")

# Asking for the bet from each player
    for i in range(0, playerNum):
        print("Player", i+1, "...")
        try:
            betMoney = float(input("How much bet to start for you?"))
            while not players[i].bet(betMoney):
                betMoney = float(input("How much bet to start for you?"))
        except:
            print("Please use dollar amount.")
            
    print("Dealer dealing cards...")
    
    for i in range(0, playerNum):
        for j in range(0, 2):
            players[i].playersHand[j] = dealer.deal(deck.card)
            deck.dealt_card(players[i].playersHand[j])

    for i in range(0, 2):
        dealer.dealersHand[i] = dealer.deal(deck.card)
        deck.dealt_card(dealer.dealersHand[i])
    
    print("--------------------------------------------")
    print("Dealer's showing hand is " + dealer.dealersHand[1])
    print("--------------------------------------------")
    print("")
    for i in range(0, playerNum):
        print("Player", i+1, "'s hand is: ")
        players[i].check_hands()
        print("--------------------------------------------")
        while not players[i].bust():
            checkHit = input("Do you want to hit? (y/n)")
            if checkHit == 'y':
                players[i].hit(dealer.deal(deck.card))
                players[i].check_hands()
                if players[i].bust():
                    players[i].lose(i+1)
                    player_lose[i] = True
                    break
            else:
                break
                
    print("--------------------------------------------")
    print("Dealer shows both hands")
    dealer.check_hands()
    print("--------------------------------------------")
    while True:
        if dealer.dealer_hit():        
            dealer.hit(dealer.deal(deck.card))
            print("Dealer hits...")
            dealer.check_hands()
            continue
        else:
            break
          
    print("")    
    print("------------------------------")
    print("Dealer has ",dealer.totalPoint)
    print("------------------------------")
    print("")
    
    for i in range(0, playerNum):
        if dealer.bust() and player_lose[i] != True:            
            print("Player",i+1," has ",players[i].check_point())
            players[i].win(i+1)
        elif dealer.check_point() < players[i].check_point() and player_lose[i] != True:
            print("Player",i+1," has ",players[i].check_point())
            players[i].win(i+1)
        elif dealer.check_point() > players[i].check_point():
            print("Player",i+1," has ",players[i].check_point())
            players[i].lose(i+1)
        elif dealer.check_point() == players[i].check_point() and player_lose[i] != True:
            print("Player",i+1," has ",players[i].check_point())
            players[i].push(i+1)
    
    dealer.reset_hand()
    print("")
    for i in range(0, playerNum):
        print("Player",i+1,"'s remaining bankroll is $", players[i].check_bankroll())    
    
    cont = input('Would you like to play again? (y/n)')
    if cont == 'n':
        break
    elif deck.check_remaining() < 12:
        deck = Deck()
        print("Shuffle Deck...")
        print("Remaining cards", deck.check_remaining())
    else:
        print("remaining cards", deck.check_remaining())
        
    


# 

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



