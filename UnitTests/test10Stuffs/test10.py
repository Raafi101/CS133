#CS133 Test 10
#Raafi Rahman

#  A-1K:  Mean or NastyMirror
#  A-8K:  Mean
#  A-32K: NiceMirror
#
#  B-1K:  NastyMirror
#  B-8K:  Random or NiceMirror or NastyMirror (NastyMirror sometimes wins, but rarely)
#  B-32K: Random or NiceMirror
#
#  C-1K:  NastyMirror
#  C-8K:  NiceMirror or Counting (Although very rare, I had a few outcomes where NiceMirrors and Counting players were both left at the end)
#  C-32K: NiceMirror or Counting (Although very rare, I had a few outcomes where NiceMirrors and Counting players were both left at the end)

import random

#Players Classes ====================================================
class Player:
    idCounter = 0
    def __init__(self):
        self.score = 0
        self.memory = {}
        Player.idCounter += 1
        self.name = 'Player {0}'.format(Player.idCounter)
    def processResult(self, otherName,myResponse,otherResponse):
        result = [myResponse, otherResponse]
        if otherName in self.memory:
            self.memory[otherName].append(result)
        else:
            self.memory[otherName] = [result]
        if myResponse == 'nice' and otherResponse == 'nice':
            self.score += 30
        elif myResponse == 'nice' and otherResponse == 'nasty':
            self.score -= 70
        elif myResponse == 'nasty' and otherResponse == 'nice':
            self.score += 50
        else:
            self.score += 0

class FriendlyPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (friendly)'
    def respondsTo(self, otherName):
        return 'nice'

class MeanPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (mean)'
    def respondsTo(self, otherName):
        return 'nasty'

class NiceMirrorPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (niceMirror)'
    def respondsTo(self, otherName):
        if otherName in self.memory:
            return self.memory[otherName][-1][1]
        else:
            return 'nice'

class NastyMirrorPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (nastyMirror)'
    def respondsTo(self, otherName):
        if otherName in self.memory:
            return self.memory[otherName][-1][1]
        else:
            return 'nasty'

class RandomPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (random)'
    def respondsTo(self, otherName):
        responses = ['nice', 'nasty']
        return random.choice(responses)

class CountingPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (counting)'
    def respondsTo(self, otherName):
        nice = 0
        nasty = 0
        for i in self.memory:
            for j in range(len(self.memory[i])):
                if self.memory[i][j][1] == 'nice':
                    nice += 1
                elif self.memory[i][j][1] == 'nasty':
                    nasty += 1
        if nice > nasty:
            return 'nice'
        elif nasty > nice:
            return 'nasty'
        else:
            return 'nice'

#Functions ==========================================================    
def encounter(player1, player2):
    name1, name2 = player1.name, player2.name
    response1 = player1.respondsTo(name2)
    response2 = player2.respondsTo(name1)
    player1.processResult(name2, response1, response2)
    player2.processResult(name1, response2, response1)
    
def makePopulation(specs):
    population = []
    for playerType, number in specs:
        for player in range(number):
            population.append(playerType())
    return population

def doGeneration(population, numberOfEncounters):
    for encounterNumber in range(numberOfEncounters):
        players = random.sample(population, 2)
        encounter(players[0], players[1])

def sortPopulation(population):
    scoreList = [[player.score, player.name, type(player)]
                 for player in population]
    scoreList.sort()
    return scoreList

def report(scoreList):
    pattern = '{0:23s}{1:6d}'
    for score, name, playerType in scoreList:
        print(pattern.format(name, score))

def summary(allPlayers):
    friend = 0
    mean = 0
    nice = 0
    nasty = 0
    random = 0
    count = 0
    for player in allPlayers:
        if type(player) == FriendlyPlayer:
            friend += 1
        elif type(player) == MeanPlayer:
            mean += 1
        elif type(player) == NiceMirrorPlayer:
            nice += 1
        elif type(player) == NastyMirrorPlayer:
            nasty += 1
        elif type(player) == RandomPlayer:
            random += 1
        elif type(player) == CountingPlayer:
            count += 1
    print('{0:2d}{1:10d}{2:8d}{3:14d}{4:15d}{5:10d}'.format(friend, mean, nice, nasty, random, count))

def makeNextGeneration(scoreList):
    nextGeneration = []
    populationSize = len(scoreList)
    scoreList = scoreList[int(populationSize/2):]
    for score, name, playerType in scoreList:
        for number in range(2):
            nextGeneration.append(playerType())
    return nextGeneration

#Run Game ===========================================================
allPlayers = makePopulation([[FriendlyPlayer, 0],
                             [MeanPlayer, 0],
                             [NiceMirrorPlayer, 10],
                             [NastyMirrorPlayer, 10],
                             [RandomPlayer, 10],
                             [CountingPlayer, 10]
                             ])

print('{0:10.12s}{1:8.12s}{2:14.12s}{3:15.12s}{4:10.12s}{5:10.12s}'.format('Friend', 'Mean', 'NiceMirror', 'NastyMirror', 'Random', 'Counting'))
for generationNumber in range(20):
    doGeneration(allPlayers, 8000)
    sortedResults = sortPopulation(allPlayers)
    summary(allPlayers)
    allPlayers = makeNextGeneration(sortedResults)