#CS133 Test 1
#Raafi Rahman

fNames = ["JACK", "JIM", "JOHNNIE", "JAMES", "RAAFI"] #First name list
lNames = ["JACKSON", "BENJIMIN", "JAMESON", "RAHMAN"] #Last name list

#======================================

for name in fNames: #Print first names
    print(name)

print("---")

#======================================

for name in lNames: #Print last names
    print(name)

print("---")

#======================================

for fName in fNames: #Check if first name contained in last name character array
    for lName in lNames:
        print(fName, lName)

print("---")

#======================================

for fName in fNames: #Check if first name contained in last name character array
    for lName in lNames:
        if fName in lName:
            print(fName, lName)