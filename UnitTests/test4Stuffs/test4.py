#CS133 Test 4
#Raafi Rahman

import cards #import cards module

def playGame(initial):  #function to run an instance of the game
    double = initial*2  #Takes in initial amount and returns number of rounds
    counter = 0
    while 0 < initial < double: 
        counter += 1
        heartsInHand = 0
        deck = cards.shuffledDeck()

        for i in range(4):
            if cards.suitOf(deck[i]) == 'hearts':
                heartsInHand += 1

        if heartsInHand == 0:
            initial -= 1

        initial += heartsInHand

    return counter

while True: #Keep asking for initial bankroll
    initial = int(input("Enter initial amount: "))
    summation = 0

    for j in range(1000): #repeat game 1000 times
        summation += playGame(initial)

    print("Average number of rounds:", summation / 1000, "\n") #calculate and print avg num of rounds