from tkinter import *
import random

#Data =====================================================

#Card class -----------------------------------------------
class Card:
    def __init__(self, f, s):
        self.faceValue = f
        self.suit = s
    def getFace(self):
        return self.faceValue
    def getSuit(self):
        return self.suit
    def __str__(self):
        return self.faceValue + ' of ' + self.suit

#Deck class -----------------------------------------------
class Deck:
    faceValues =['ace', '2', '3', '4', '5', '6', '7', 
                 '8', '9', '10', 'jack', 'queen', 'king']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    def __init__(self):
        self.cards = [Card(faceValue, suit) 
                      for faceValue in Deck.faceValues 
                      for suit in Deck.suits]
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        return self.cards.pop()
    def cardsLeft(self):
        return len(self.cards)

#CardsFrame class -----------------------------------------
class CardsFrame(Frame):
    def __init__(self, parent, hand):
        Frame.__init__(self)
        self['width'] = 120
        for card in hand:
            newButton = Button(self)
            newButton['text'] = card
            newButton['width'] = 20
            newButton.pack(fill = X, expand = NO)

#Enhanced entry class -------------------------------------
class enhancedEntry(Frame):
    def __init__(self, parent, prompt, actionText, action):
        Frame.__init__(self, parent)

        self['bg'] = 'light gray'

        self.inputBoxLabel = Label(self)
        self.inputBoxLabel['text'] = prompt
        self.inputBoxLabel['bg'] = 'light gray'
        self.inputBoxLabel.pack(side = LEFT, fill = X)

        self.inputBox = Entry(self)
        self.inputBox.pack(side = LEFT, fill = X)

        self.button = Button(self)
        self.button['text'] = actionText
        self.button['command'] = action
        self.button.pack(side = LEFT, fill = X)

    def get(self):
        return self.inputBox.get()
    
    def setActionText(self, actionText):
        self.button['text'] = actionText

    def setPrompt(self, prompt):
        self.inputBoxLabel['text'] = prompt

    def setAction(self, command):
        self.button['command'] = command

#Deal function --------------------------------------------
def deal(n):
    deck1 = Deck()
    hand = []
    for i in range(n):
        hand.append(deck1.deal())
    return hand

#Evaluate function ----------------------------------------
def evaluate(hand):
    score = 0
    faceValAppearances = {'ace':0, '2':0, '3':0, '4':0, '5':0,
                          '6':0, '7':0, '8':0, '9':0, '10':0, 
                          'jack':0, 'queen':0, 'king':0}
    for i in range(len(hand)):
        if hand[i].getFace() in faceValAppearances:
            faceValAppearances[hand[i].getFace()] += 1
    for key in faceValAppearances:
        if faceValAppearances[key] == 4:
            score += 100
        elif faceValAppearances[key] == 3:
            score += 10
        elif faceValAppearances[key] == 2:
            score += 1
    return score

#Function -------------------------------------------------
iterator = 0
def doThing():
    global iterator, newFrame
    if iterator > 0:
        newFrame.destroy()
    userInput = textBar.get()
    if userInput.isdigit():
        num = int(userInput)
        if num >= 0 and num <= 52:
            hand1 = deal(num)
            
            print('Number of cards:', num)

            for i in range(len(hand1)):
                print('    ',hand1[i])

            print('     -----------> Score:',evaluate(hand1), '\n')

            score['text'] = 'Score: {0}'.format(evaluate(hand1))

            newFrame = CardsFrame(root, hand1)

            newFrame.pack(side = BOTTOM)

            iterator += 1

#Window ===================================================
root = Tk()
root['bg'] = 'light gray'
root.title('Hand of Cards')

textBarFrame = Frame(root)
textBarFrame.pack(side = TOP)
textBar = enhancedEntry(textBarFrame, 'Number of cards: ', 'Deal', doThing)

scoreFrame = Frame(root)
score = Label(scoreFrame)
score['text'] = 'Score: 0'
score['bg'] = 'light gray'
scoreFrame.pack()
score.pack()

textBar.pack()

mainloop()