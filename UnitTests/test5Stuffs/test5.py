#CS133 Test 5
#Raafi Rahman

import os

def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz@_1234567890'    #includes letters, @, _, and numbers
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' ' #Just in case extra characters after mention i.e "!", ":", "'", etc...
    return cleantext

def findMentions(filename):
    if filename[len(filename) - 6:] == ".tweet": #check if file ends in ".tweet"
        mentionsDict = {}
        mentionsList = []
        with open(filename, encoding='utf-8') as text:
            for line in text:
                line1 = cleanedup(line)
                for word in line1.split():
                    if word[0] == '@': #check if word is a mention
                        if word in mentionsDict: #Add mention to dictionary.
                            mentionsDict[word] += 1
                        else:
                            mentionsDict[word] = 1
            print(filename)

            for mention in mentionsDict:
                mentionsList.append([mentionsDict[mention], mention])
            
            mentionsList.sort()

            for i in range(5):
                print("    ", mentionsList[len(mentionsList) - (5 - i)][1], mentionsList[len(mentionsList) - (5 - i)][0])
            print("")

for filename in os.listdir('.'): #loop through path
    findMentions(filename)