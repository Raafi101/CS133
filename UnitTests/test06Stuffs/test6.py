#CS133 Test 6
#Raafi Rahman

import urllib.request, shelve

url = 'http://nancymcohen.com/csci133/cpiai.txt'
file = urllib.request.urlopen(url)
lines = file.readlines()
file.close()

cpi = {}

for line in lines:
    items = line.decode().split()
    if len(items) > 0 and items[0].isdigit():
        cpi[int(items[0])] = [float(item) for item in items[:13]]

shelf = shelve.open('cpi')
shelf['cpi'] = cpi
shelf.close()

while True:
    time = [int(x) for x in input("Enter query: ").split()] #Year and months

    if len(time) == 1: #If only a year is given
        displayList = cpi[time[0]][1:13]
        print(displayList)
        maxNum = displayList[0]
        summation = 0
        for i in displayList:
            summation += i
            if i > maxNum:
                maxNum = i
        print("Max = ", maxNum)
        print("Avg = ", summation / len(displayList), "\n")

    else: #If months are given too
        displayList = [cpi[time[0]][time[month + 1]] for month in range(len(time) - 1)]
        print(displayList)
        maxNum = displayList[0]
        summation = 0
        for i in displayList:
            summation += i
            if i > maxNum:
                maxNum = i
        print("Max = ", maxNum)
        print("Avg = ", summation / len(displayList), "\n")