#CS133 Test 2
#Raafi Rahman

#Define & initalize variables
lineNum = 1 #Variable to keep track of line number
charLen = 0 #Variable to keep track of number of character in a line

#Main loop
with open('win95coolest.txt') as text: #Open txt doc
    for line in text:
        for word in line.split():
            charLen = charLen + len(word) #Increment number of characters in a line
        if len(line.split()) == 0: #Avoid divide by zero error
            avgLen = 0
        else:
            avgLen = charLen / len(line.split()) #Average length of words in a line
        print(lineNum, len(line.split()), avgLen, line) #Print
        lineNum = lineNum + 1 #Increment line number
        charLen = 0 #Reset number of characters to zero before moving to next line