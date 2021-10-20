#CS133 Test 7
#Raafi Rahman

#goalSeek seems similar to bisection method to finding roots

def goalSeek(function, lowLimit, highLimit, target, maxError=.000001):
    error = maxError + 1

    while error > maxError:
        guess = (lowLimit + highLimit) / 2
        result = function(guess)
        error = abs(result-target)

        if result > target:
            highLimit = guess

        if result < target:
            lowLimit = guess

    return guess

def p1(x):
    return x**3 - x**2 + 4*x - 10

print(goalSeek(p1, -5, 5, 20, .00001), '\n')

def makePoly(A, B, C, D): #Make polynomial function
    def newFunction(x):
        return A*x*x*x + B*x*x + C*x + D
    return newFunction

output = "{0:4.2f}  {1:7.2f}  {2:7.2f}  {3:7.2f}  =  {4:7.2f}  at  {5:7.2f}"

print("test print\n")

with open("poly.txt") as text: #Test print
    for line in text:
        if line[0] != '#':
            items = line.split()
            for i in range(6):
                print(float(items[i]), end = '\t')
            print(float(items[7]))

print("\nroots\n")

#I would have used seek(0) to return back to the top but i didn't see it in any of our note so i did this instead
with open("poly.txt") as text: #Print coeffs, y, and root
    for line in text:
        if line[0] != '#':
            items = line.split()
            poly = makePoly(float(items[0]), float(items[1]), float(items[2]), float(items[3]))
            root = goalSeek(poly, float(items[5]), float(items[6]), float(items[4]))
            print(output.format(float(items[0]), float(items[1]), float(items[2]), float(items[3]), float(items[4]), root))

