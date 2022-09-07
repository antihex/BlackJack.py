from random import shuffle
from tkinter import *
from PIL import Image, ImageTk
import os

def resize_card(card):
    img = Image.open(card)
    sizedImg = img.resize((75,109))
    global cardImg 
    cardImg = ImageTk.PhotoImage(sizedImg)
    
    return cardImg 

class Deck:
    def __init__(self):
        self.cards = []
        self.shuffleEightDecks()     

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

    def shuffle(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards\
                    .append(Card(i,
                                 j))
        shuffle(self.cards)

    def shuffleTwoDecks(self):
        self.cards = []
        for k in range (2):
            for i in range(2, 15):
                for j in range(4):
                    self.cards\
                        .append(Card(i,
                                    j))
        shuffle(self.cards)

    def shuffleEightDecks(self):
        self.cards = []
        for k in range (8):
            for i in range(2, 15):
                for j in range(4):
                    self.cards\
                        .append(Card(i,
                                    j))
        shuffle(self.cards)

class Card:
    # suits = ["spades",
    #          "hearts",
    #          "diamonds",
    #          "clubs"]
    
    suits = ["♤","♥","♧","♦"]

    values = [None, None,"2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.suit < c2.suit:
            return True
        if self.suit == c2.suit:
            if self.value < c2.value:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.suit > c2.suit:
            return True
        if self.suit == c2.suit:
            if self.value > c2.value:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] +\
            self.suits[self.suit]
        return v

    def __eq__(self, other):
        return (self.suit == other.suit and self.value == other.value)

class Game:
    def __init__(self):
        self.deck = Deck()
        self.name = "Me"
        self.dealerName = "Dealer"
        self.dealer = Player()
        self.player = Player()

        global cardImage1, cardImage2, cardImage3, cardImage4, cardImage5, cardImage6
        global dealerCardImage1, dealerCardImage2, dealerCardImage3, dealerCardImage4, dealerCardImage5, dealerCardImage6
        global cardBack

        global finished
        finished = False

        self.wins = 0
        self.losses = 0

        self.path = r"\bridge/Cards/{}.png"

        self.count = Count()

    def gui(self):
        self.root = Tk()
        self.root.title("BlackJack.py")
        self.root.geometry("1000x800")
        self.root.configure(background="green")

        self.my_frame = Frame(self.root, bg="green")
        self.my_frame.pack(side = LEFT,pady=20, padx=20)

        self.tableFrame = Frame(self.root, bg="green")
        self.tableFrame.pack(side=RIGHT, pady=20, padx=20) 

        tableImage = Image.open(os.getcwd() + r"/bridge/Basic Strategy/blackjack-basic-strategy-card.png")
        sizedtable = tableImage.resize((450,600))
        tableFinalImage = ImageTk.PhotoImage(sizedtable)

        self.table = Label(self.tableFrame)
        self.table.pack(pady=20)
        self.table.config(image=tableFinalImage)
        
               

        self.dealer_frame = LabelFrame(self.my_frame, text=self.dealerName, bd=0)          
        self.dealer_frame.grid(row=0,column=0,padx=20,pady=20)

        self.player_frame = LabelFrame(self.my_frame, text=self.name, bd=0)
        self.player_frame.grid(row=1,column=0,padx=20,pady=20)                          

        self.player_label1 = Label(self.player_frame, text='')
        self.player_label1.grid(row=0,column=0)

        self.player_label2 = Label(self.player_frame, text='')
        self.player_label2.grid(row=0,column=1)

        self.player_label3 = Label(self.player_frame, text='')
        self.player_label3.grid(row=0,column=2)

        self.player_label4 = Label(self.player_frame, text='')
        self.player_label4.grid(row=0,column=3)

        self.player_label5 = Label(self.player_frame, text='')
        self.player_label5.grid(row=0,column=4)

        self.player_label6 = Label(self.player_frame, text='')
        self.player_label6.grid(row=0,column=5)

        self.player_label7 = Label(self.player_frame, text='')
        self.player_label7.grid(row=0,column=6)

        self.player_label8 = Label(self.player_frame, text='')
        self.player_label8.grid(row=0,column=7)

        self.player_label9 = Label(self.player_frame, text='')
        self.player_label9.grid(row=0,column=8)

        self.player_label10 = Label(self.player_frame, text='')
        self.player_label10.grid(row=0,column=9)

        self.player_label11 = Label(self.player_frame, text='')
        self.player_label11.grid(row=0,column=10)

        self.player_label12 = Label(self.player_frame, text='')
        self.player_label12.grid(row=0,column=11)

        self.player_label13 = Label(self.player_frame, text='')
        self.player_label13.grid(row=0,column=12)    

        self.dealer_label1 = Label(self.dealer_frame, text='')
        self.dealer_label1.grid(row=0,column=0)

        self.dealer_label2 = Label(self.dealer_frame, text='')
        self.dealer_label2.grid(row=0,column=1)

        self.dealer_label3 = Label(self.dealer_frame, text='')
        self.dealer_label3.grid(row=0,column=2)

        self.dealer_label4 = Label(self.dealer_frame, text='')
        self.dealer_label4.grid(row=0,column=3)

        self.dealer_label5 = Label(self.dealer_frame, text='')
        self.dealer_label5.grid(row=0,column=4)

        self.dealer_label6 = Label(self.dealer_frame, text='')
        self.dealer_label6.grid(row=0,column=5)

        self.dealer_label7 = Label(self.dealer_frame, text='')
        self.dealer_label7.grid(row=0,column=6)

        self.dealer_label8 = Label(self.dealer_frame, text='')
        self.dealer_label8.grid(row=0,column=7)

        self.dealer_label9 = Label(self.dealer_frame, text='')
        self.dealer_label9.grid(row=0,column=8)

        self.dealer_label10 = Label(self.dealer_frame, text='')
        self.dealer_label10.grid(row=0,column=9)

        self.dealer_label11 = Label(self.dealer_frame, text='')
        self.dealer_label11.grid(row=0,column=10)

        self.dealer_label12 = Label(self.dealer_frame, text='')
        self.dealer_label12.grid(row=0,column=11)

        self.dealer_label13 = Label(self.dealer_frame, text='')
        self.dealer_label13.grid(row=0,column=12)   

        self.player_total = Label(self.player_frame, text='', font=("Helvetica", 14))
        self.player_total.grid(row=0,column=13)

        self.dealer_total = Label(self.dealer_frame, text='', font=("Helvetica", 14))
        self.dealer_total.grid(row=0,column=13)   

        # Buttons

        self.buttonFrame = Frame(self.my_frame, bg="green")
        self.buttonFrame.grid(row = 2, column = 0, pady = 20)


        hitCardsButton = Button(self.buttonFrame,text="Hit", font=("Helvetica", 14),command=self.hit)
        hitCardsButton.grid(row=0, column=0, padx=5)

        standButton = Button(self.buttonFrame, text="Stand", font=("Helvetica", 14),command=self.dealerTurn)
        standButton.grid(row=0, column=1, padx=5)

        splitButton = Button(self.buttonFrame, text="Split", font=("Helvetica", 14))
        splitButton.grid(row=0, column=2, padx=5)

        doubleButton = Button(self.buttonFrame, text="Double", font=("Helvetica", 14), command=self.double)
        doubleButton.grid(row=0, column=3, padx=5)     

        self.dealButton = Button(self.buttonFrame, text='Next Hand', font=("Helvetica", 14), command=self.dealAgain)
        self.dealButton.grid(row = 0, column = 4, padx = 5)


        self.cardsLeftFrame = Frame(self.my_frame, bg="green")
        self.cardsLeftFrame.grid(row = 3, column = 0, pady = 20)

        self.cardsLeft = len(self.deck.cards)
        self.cardsLeftLabel = Label(self.cardsLeftFrame, text = 'Cards remaining: ' + str(self.cardsLeft), font=("Helvetica", 14))
        self.cardsLeftLabel.grid(row = 0, column=0, pady=5)

        self.winLosses = Label(self.cardsLeftFrame, text = 'Wins-Losses: ' + str(self.wins) + '-' + str(self.losses) , font=("Helvetica", 14))
        self.winLosses.grid(row = 0, column = 1, padx = 5)

        


        
        self.guiDealCards()    

        self.root.mainloop()

    def hit(self):
        global finished
        if not finished:
            self.player.cards.append(self.deck.rm_card())

            global cardImage3, cardImage4, cardImage5

            self.cardsLeft = len(self.deck.cards)
            self.cardsLeftLabel.config(text='Cards remaining: ' + str(self.cardsLeft))

            x = len(self.player.cards)

            pwd = os.getcwd()

            if x == 3:
                cardImage3 = resize_card(pwd + self.path.format(self.player.cards[x-1]))
                self.player_label3.config(image=cardImage3)
                self.count.updateCount(self.player.cards[x-1])
            
            elif x == 4:
                cardImage4 = resize_card(pwd + self.path.format(self.player.cards[x-1]))
                self.player_label4.config(image=cardImage4)
                self.count.updateCount(self.player.cards[x-1])

            elif x == 5:
                cardImage5 = resize_card(pwd + self.path.format(self.player.cards[x-1]))
                self.player_label5.config(image=cardImage5)
                self.count.updateCount(self.player.cards[x-1])

            self.player.calcPoints()

            self.player_total.config(text = 'Total: ' + str(self.player.points))

            if self.player.points > 21:
                self.dealerTurn()

    def dealerTurn(self):

        global finished
        if not finished:
            pwd = os.getcwd()
            self.path = r"\bridge/Cards/{}.png"

            global dealerCardImage2, dealerCardImage3, dealerCardImage4, dealerCardImage5, dealerCardImage6


            self.dealer_label2.config(image='')

            dealerCardImage2 = resize_card(pwd + self.path.format(self.dealer.cards[1]))
            self.dealer_label2.config(image=dealerCardImage2)
            self.count.updateCount(self.dealer.cards[1])

            self.dealer.calcPoints()

            while self.dealer.points < 17:
                self.dealer.cards.append(self.deck.rm_card())

                self.cardsLeft = len(self.deck.cards)
                self.cardsLeftLabel.config(text='Cards remaining: ' + str(self.cardsLeft))
            
                self.dealer.calcPoints()

                x = len(self.dealer.cards) 

                if x == 3:
                    dealerCardImage3 = resize_card(pwd + self.path.format(self.dealer.cards[x-1]))
                    self.dealer_label3.config(image=dealerCardImage3)
                    self.count.updateCount(self.dealer.cards[x-1])
                elif x == 4:
                    dealerCardImage4 = resize_card(pwd + self.path.format(self.dealer.cards[x-1]))
                    self.dealer_label4.config(image=dealerCardImage4)
                    self.count.updateCount(self.dealer.cards[x-1])
                elif x == 5:
                    dealerCardImage5 = resize_card(pwd + self.path.format(self.dealer.cards[x-1]))
                    self.dealer_label5.config(image=dealerCardImage5)
                    self.count.updateCount(self.dealer.cards[x-1])
                elif x == 6:
                    dealerCardImage6 = resize_card(pwd + self.path.format(self.dealer.cards[x-1]))
                    self.dealer_label6.config(image=dealerCardImage6)
                    self.count.updateCount(self.dealer.cards[x-1])
                    
            if self.dealer.points > 21 and self.player.points > 21: 
                print("Dealer Wins! Both Busted")
                self.losses += 1
                
            elif self.dealer.points <= 21 and self.player.points > 21:
                print("Dealer Wins! Player Busted")
                self.losses += 1

            elif self.dealer.points > 21 and self.player.points <= 21:
                print("Player Wins! Dealer Busted")
                self.wins += 1

            elif self.dealer.points <= 21 and self.dealer.points <= 21:
                if self.dealer.points < self.player.points:
                    print("Player Wins!")
                    self.wins += 1
                elif self.dealer.points > self.player.points:
                    print("Dealer Wins!")
                    self.losses += 1
                else:
                    print("Push")

            self.dealer_total.config(text = 'Total: ' + str(self.dealer.points))

            self.winLosses.config(text = 'Wins-Losses: ' + str(self.wins) + '-' + str(self.losses))

            self.count.printCount(self.cardsLeft)

            finished = True
    
    def dealerTurn2(self, blackJack):

        global finished
        if not finished:
            pwd = os.getcwd()
            self.path = r"\bridge/Cards/{}.png"

            doubleBlackJack = False

            global dealerCardImage2, dealerCardImage3, dealerCardImage4, dealerCardImage5, dealerCardImage6


            self.dealer_label2.config(image='')

            dealerCardImage2 = resize_card(pwd + self.path.format(self.dealer.cards[1]))
            self.dealer_label2.config(image=dealerCardImage2)
            self.count.updateCount(self.dealer.cards[1])

            self.dealer.calcPoints()

            if self.dealer.points == 21:
                print("Double Black Jack")

            while self.dealer.points < 17:
                self.dealer.cards.append(self.deck.rm_card())

                self.cardsLeft = len(self.deck.cards)
                self.cardsLeftLabel.config(text='Cards remaining: ' + str(self.cardsLeft))
            
                self.dealer.calcPoints()

                x = len(self.dealer.cards) 

                if x == 3:
                    dealerCardImage3 = resize_card(pwd + self.path.format(self.dealer.cards[x-1]))
                    self.dealer_label3.config(image=dealerCardImage3)
                    self.count.updateCount(self.dealer.cards[x-1])
                elif x == 4:
                    dealerCardImage4 = resize_card(pwd + self.path.format(self.dealer.cards[x-1]))
                    self.dealer_label4.config(image=dealerCardImage4)
                    self.count.updateCount(self.dealer.cards[x-1])
                elif x == 5:
                    dealerCardImage5 = resize_card(pwd + self.path.format(self.dealer.cards[x-1]))
                    self.dealer_label5.config(image=dealerCardImage5)
                    self.count.updateCount(self.dealer.cards[x-1])
                elif x == 6:
                    dealerCardImage6 = resize_card(pwd + self.path.format(self.dealer.cards[x-1]))
                    self.dealer_label6.config(image=dealerCardImage6)
                    self.count.updateCount(self.dealer.cards[x-1])

            self.dealer_total.config(text = 'Total: ' + str(self.dealer.points))

            self.winLosses.config(text = 'Wins-Losses: ' + str(self.wins) + '-' + str(self.losses))

            self.count.printCount(self.cardsLeft)

            if doubleBlackJack:
                print("Push")
            else:
                print("BlackJack!")
                self.wins+=1

            finished = True

    def guiDealCards(self):
        if len(self.deck.cards) < 20:
            self.deck.shuffleEightDecks()
            self.count.reset()
            print("Shuffling Deck")
        
        for x in range(2):
            self.dealer.cards.append(self.deck.rm_card())
            self.player.cards.append(self.deck.rm_card())

        self.count.updateCount(self.player.cards[0])
        self.count.updateCount(self.player.cards[1])
        self.count.updateCount(self.dealer.cards[0])


        global cardImage1, cardImage2
        global dealerCardImage1, cardBack


        self.dealer_label3.config(image='')
        self.dealer_label4.config(image='')
        self.dealer_label5.config(image='')
        self.dealer_label6.config(image='')

        self.player_label3.config(image='')
        self.player_label4.config(image='')
        self.player_label5.config(image='')
        self.player_label6.config(image='')


        pwd = os.getcwd()
        

        for x in range(len(self.player.cards)):
            match x:
                case 0:
                    cardImage1 = resize_card(pwd + self.path.format(self.player.cards[x]))
                    self.player_label1.config(image=cardImage1)
                    
                    dealerCardImage1 = resize_card(pwd + self.path.format(self.dealer.cards[x]))
                    self.dealer_label1.config(image=dealerCardImage1)

                case 1:
                    cardImage2 = resize_card(pwd + self.path.format(self.player.cards[x]))
                    self.player_label2.config(image=cardImage2)

                    cardBack = resize_card(pwd + r"/bridge/Cards/CardBack.png")
                    self.dealer_label2.config(image=cardBack)

        self.cardsLeft = len(self.deck.cards)
        self.cardsLeftLabel.config(text='Cards remaining: ' + str(self.cardsLeft))

        self.player.calcPoints()

        if self.player.calcPoints == 21:
            self.dealerTurn2(True)
            

        self.player_total.config(text = 'Total: ' + str(self.player.points))
        self.dealer_total.config(text = 'Total: ???')

    def dealCards(self):
        self.player.reset()
        self.dealer.reset()
        self.guiDealCards()

    def dealAgain(self):
        global finished

        if finished:
            finished = False
            self.dealCards()
        
    def double(self):
        global finished
        if not finished:
            self.player.cards.append(self.deck.rm_card())

            global cardImage3, cardImage4, cardImage5

            self.cardsLeft = len(self.deck.cards)
            self.cardsLeftLabel.config(text='Cards remaining: ' + str(self.cardsLeft))

            x = len(self.player.cards)

            pwd = os.getcwd()

            if x == 3:
                cardImage3 = resize_card(pwd + self.path.format(self.player.cards[x-1]))
                self.player_label3.config(image=cardImage3)
                self.count.updateCount(self.player.cards[x-1])

            self.player.calcPoints()

            self.player_total.config(text = 'Total: ' + str(self.player.points))

            self.dealerTurn()

    def split(self):
        if self.player.cards[0].value == self.player.cards[1].value and len(self.player.cards) == 2:
            print("NOT IMPLIMENTED")



class Player:
    def __init__(self):
        self.cards = []
        self.points = 0
        self.numAces = 0
        self.cards2 = []

    def calcPoints(self):
        self.points = 0
        self.numAces = 0

        for x in self.cards:
            if x.value < 11:
                self.points += x.value
            elif x.value == 14:
                self.points += 11
                self.numAces += 1
            else:
                self.points += 10

        while self.numAces > 0 and self.points > 21:
            self.points -= 10
            self.numAces -= 1
        
        # print(self.points)

    def reset(self):
        self.cards = []
        self.points = 0
        self.numAces = 0

class Count:
    def __init__(self):
        self.hiLo = 0

    def updateCount(self, card):
        self.updateHiLoCount(card)

    def updateHiLoCount(self,card):
        if card.value >=2 and card.value <=6:
            self.hiLo += 1
        elif card.value >= 10:
            self.hiLo -= 1

    def printCount(self, cardRemaining):
        print("HiLo Running Count: " + str(self.hiLo))
        print("HiLo TrueCount: " + str(self.hiLo/(cardRemaining/52)))

    def reset(self):
        self.hiLo = 0

game = Game()
game.gui()




