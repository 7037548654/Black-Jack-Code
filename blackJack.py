class player():
    score=0
    player_card=[]
    player_aces=0
player_object=player()

class dealer():
    score=0
    dealer_card=[]
    dealer_aces=0
dealer_object=dealer()

p=2
d=2
class bank_account():
    balance=1000
    def deposit(self,money):
        self.balance=self.balance+money
    def withdraw(self,money):
        if self.balance>=money:
            self.balance=self.balance-money
        else:
            print("Withdrawal is greater than account balance!")
    def __str__(self):
        return "account balance: Rs{}".format(self.balance)

account_object=bank_account()
        
def player_ace_calculation():
    for j in range(0,len(player_object.player_card)):
        if player_object.player_card[j]=="ace" and player_object.score>21 and player_object.player_aces>0:
            player_object.score=player_object.score-10
            player_object.player_aces=player_object.player_aces-1

def dealer_ace_calculation():
    for a in range(0,len(dealer_object.dealer_card)):
        if dealer_object.dealer_card[a]=="ace" and dealer_object.score>21 and dealer_object.dealer_aces>0:
            dealer_object.score=dealer_object.score-10
            dealer_object.dealer_aces=dealer_object.dealer_aces-1
        if dealer_object.dealer_card[a]=="ace" and dealer_object.score>16 and dealer_object.score<player_object.score and dealer_object.score<22 and dealer_object.dealer_aces>0:
            dealer_object.score=dealer_object.score-10
            dealer_object.dealer_aces=dealer_object.dealer_aces-1
 
 from random import randint
class card():
    cards=["ace","two","three","four","five","six","seven","eight","nine","ten","jack","queen","king"]*4
    points={"ace":11,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"jack":10,"queen":10,"king":10}
    deck=[]
    def distribute(self):
        #num1=randint(0,len(self.cards)-1)
        #num2=randint(0,len(self.cards)-1)
        #num3=randint(0,len(self.cards)-1)
        #num4=randint(0,len(self.cards)-1)
        #while True:
            #if num1!=num2 and num1!=num3 and num1!=num4 and num2!=num3 and num2!=num4 and num3!=num4:
                #global player
                #global dealer
                num1=randint(0,len(self.cards)-1)
                dealer_object.dealer_card=[self.cards[num1]]
                if dealer_object.dealer_card[0]=="ace":
                    dealer_object.dealer_aces=dealer_object.dealer_aces+1
                self.cards.remove(dealer_object.dealer_card[0])
                num2=randint(0,len(self.cards)-1)
                dealer_object.dealer_card.append(self.cards[num2])
                if dealer_object.dealer_card[1]=="ace":
                    dealer_object.dealer_aces=dealer_object.dealer_aces+1
                self.cards.remove(dealer_object.dealer_card[1])
                num3=randint(0,len(self.cards)-1)
                player_object.player_card=[self.cards[num3]]
                if player_object.player_card[0]=="ace":
                    player_object.player_aces=player_object.player_aces+1
                self.cards.remove(player_object.player_card[0])
                num4=randint(0,len(self.cards)-1)
                player_object.player_card.append(self.cards[num4])
                if player_object.player_card[1]=="ace":
                    player_object.player_aces=player_object.player_aces+1
                self.cards.remove(player_object.player_card[1])
                player_object.score=card_object.points[player_object.player_card[0]]+card_object.points[player_object.player_card[1]]
                dealer_object.score=card_object.points[dealer_object.dealer_card[0]]+card_object.points[dealer_object.dealer_card[1]]
                player_ace_calculation()
                dealer_ace_calculation()
                print("\n\nDealer:  First card is {} and second card is face down.".format(dealer_object.dealer_card[0]))
                print("\n\nPlayer:  First card is {} and second card is {} ( {} )".format(player_object.player_card[0],player_object.player_card[1],player_object.score))
                self.deck=self.cards
                #self.cards.remove(dealer[0])
                #self.cards.remove(dealer[1])
                #self.cards.remove(player[0])
                #self.cards.remove(player[1])
                #break
            #else:
                #continue
    #deck=cards
card_object=card()
card_object.deck=card_object.cards

def player_get_21():
    if player_object.score==21:
        return True
    else:
        return False
    
def dealer_get_21():
    if dealer_object.score==21:
        return True
    else:
        return False

def show_player_score():
    return "( {} )".format(player_object.score)

def if_player_busts():
    if player_object.score>21:
        return True

def if_dealer_busts():
    if dealer_object.score>21:
        return True

def player_hit():
    global p
    #global player_score
    #global player
    num5=randint(0,len(card_object.deck)-1)
    player_object.player_card.append(card_object.deck[num5])
    if player_object.player_card[p]=="ace":
        player_object.player_aces=player_object.player_aces+1
    card_object.deck.remove(card_object.deck[num5])
    player_object.score=player_object.score+card_object.points[player_object.player_card[p]]
    print("\n\nPLAYER...")
    for c in player_object.player_card:
        print(c+" ")
    #print("{}th card is {}".format(p+1,player_object.player_card[p]))
    player_ace_calculation()
    print(show_player_score())
    p=p+1

def dealer_hit():
    global d
    #if dealer_object.score>=17:
        #for u in dealer_object.dealer_card:
            #print(u)
        #print("( {} )".format(dealer_object.score))
    #else:
    while dealer_object.score<17:
        num6=randint(0,len(card_object.deck)-1)
        dealer_object.dealer_card.append(card_object.deck[num6])
        if dealer_object.dealer_card[d]=="ace":
            dealer_object.dealer_aces=dealer_object.dealer_aces+1
        card_object.deck.remove(card_object.deck[num6])
        dealer_object.score=dealer_object.score+card_object.points[dealer_object.dealer_card[d]]
        dealer_ace_calculation()
        d=d+1
    for y in dealer_object.dealer_card:
        print(y+" ")
    print("( {} )".format(dealer_object.score))
    if dealer_object.score>21:
        print("\n\nDEALER BUSTED...!")
        print("\n\nYOU WON...")
        account_object.deposit(bet*2)
        print(account_object)
        return True

def player_stand():
    print("\n\nDealer:")
    dealer_hit()

def rearrange_cards():
        global p
        global d
        card_object.cards=["ace","two","three","four","five","six","seven","eight","nine","ten","jack","queen","king"]*4
        card_object.deck=[]
        p=2
        d=2
        player_object.score=0
        dealer_object.score=0
        player_object.player_card=[]
        dealer_object.dealer_card=[]
        player_object.player_aces=0
        dealer_object.dealer_aces=0
        
rebet=''
replay=True
bet=0
deal=''
choice=''
print("LET THE GAME BEGIN!\n\n")
while  replay:
    while True:
        while bet!=10 and bet!=20 and bet!=50:
            bet=int(input("\n\nPLACE A BET(10/20/50)\t"))
        account_object.withdraw(bet)
        print(account_object)
        while deal!='y' and deal!='Y':
            deal=input("\n\nTo make a deal! Press(Y/y)\t")
        card_object.distribute()
        if player_get_21() and dealer_get_21():
            print("\n\nDealer second card is {} ( {} )".format(dealer_object.dealer_card[1],dealer_object.score))
            print("\n\nPUSH...")
            account_object.deposit(bet)
            print(account_object)
            break
        elif player_get_21():
            print("\n\nDealer second card is {} ( {} )".format(dealer_object.dealer_card[1],dealer_object.score))
            print("\n\nPLAYER WINS...")
            account_object.deposit(2*bet)
            print(account_object)
            break
        elif dealer_get_21():
            print("\n\nDealer second card is {} ( {} )".format(dealer_object.dealer_card[1],dealer_object.score))      
            print("\n\nPLAYER LOST...")
            print(account_object)
            break
        else:
            while True:
                choice=''
                while choice!='h' and choice!='H' and choice!='s' and choice!='S':
                    choice=input("\n\nDo you want to hit or stand(h/s)")
                if choice=='h' or choice=='H':
                    player_hit()
                    if if_player_busts():
                        print("\n\nPLAYER BUSTED!")
                        print(account_object)
                        break
                    if player_get_21():
                        print("\n\nDEALER")
                        dealer_hit()
                        if dealer_get_21():
                            print("\n\nPUSH")
                            account_object.deposit(bet)
                            print(account_object)
                            break
                        else:
                            print("\n\nPLAYER WINS...")
                            account_object.deposit(2*bet)
                            print(account_object)
                            break
                else:
                    retr=dealer_hit()
                    if retr==True:
                        break
                    if player_object.score>dealer_object.score:
                        print("\n\nPLAYER WINS!")
                        account_object.deposit(2*bet)
                        print(account_object)
                        break
                    elif dealer_object.score>player_object.score and dealer_object.score<22:
                        print("\n\nYOU LOST!")
                        print(account_object)
                        break
                    elif dealer_object.score==player_object.score:
                        print("\n\nPUSH!")
                        account_object.deposit(bet)
                        print(account_object)
                        break
                    break
        break
    rearrange_cards()
    rebet=''
    while rebet!='y' and rebet!='Y' and rebet!='n' and rebet!="N":
           rebet=input("\n\nDo you want to rebet?(y/Y,n/N)\t")
    if rebet=="y" or rebet=='Y':
        replay=True
    elif rebet=="n" or rebet=='N':
        replay=False

