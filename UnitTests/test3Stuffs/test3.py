#CS133 Test 3
#Raafi Rahman

numLines = 0
longestTweet = ""
hashtagDict = {}

#cleanedup function from notes.
def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz#1234567890'    #includes letters, #, and numbers
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ''
    return cleantext

#Open txt doc
with open('elon-musk.txt') as text:
    for line in text:
        numLines += 1                                     #Increment line number.
        if len(line.split()) > len(longestTweet.split()): #Replace current longest
            longestTweet = line                           #tweet by new longest tweet.
        for word in line.split():
            if '#' in word:                               #Check if hashtag.
                if (cleanedup(word)) in hashtagDict:      #Add hastag to dictionary.
                    hashtagDict[(cleanedup(word))] += 1
                else:
                    hashtagDict[(cleanedup(word))] = 1
       
print("Number of tweets:", numLines, "\n")
print("Tweet with the most number of words:", longestTweet)

while(True):
    hashtag = input("Enter hashtag: ")
    if hashtag in hashtagDict:
        print("Mentioned", hashtagDict[(cleanedup(hashtag))], "times.\n")
    else:
        print("Not mentioned\n")