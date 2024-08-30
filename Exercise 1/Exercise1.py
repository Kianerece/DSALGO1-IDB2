'''userInput = int (input ("How much money do have? "))
wii  = 100
afford = int(userInput/wii)
neededMoney = abs ((userInput % wii) - wii)

print ("You have" ,userInput ,"pesos")
print ("you will have" ,afford, "gaming of Wii's")
print("You  needed",neededMoney,"pesos additional wii's")

sum = 0

for x in range(1, 11):
    sum = sum + x

    print(sum, "is the sum of the number 1 - 10")
'''
'''
Input1 = int(input ("Enter first numbers; " ))
Input2 = int(input ("Enter second numbers; " ))

sum = 0

for x in range(Input1, Input2):
    sum = sum + x
    print("The ",sum, "of the inputed numbers of",Input1,"and",Input2,)
'''
'''
userInt = int (input ("Enter a number: "))
factorial = 1
for x in range (1, userInt + 1):
    factorial = factorial * x
    print("The factorial of",x,"is",factorial,)
'''
'''
userInput = int(input ("Enter first numbers: " ))
print("The fcators of the numbers: ")
for x in range(1,userInput +1):
        if userInput % x == 0:
            print (x)'''

factorList = []
x  = int (input("enter a number"))
for x in range(1,userInput +1):
        if userInput % x == 0:
            factorList.append(a)
            print("The factorial of",x,"are")
