def printState():
    print ("Red Light is " + str(redLight))
    print ("Yellow Light is " + str(yellowLight))
    print ("Green Light is " + str(greenLight))

redLight = True
yellowLight = False
greenLight = False

printState()

print (type(redLight))

print (3 + 5)

print (int("3") + 5)

x = int(10)
y = int(2.8)
z = int("3")

print ( str(x) + str(y) + str(z))
print (type(x),type(y),type(z))

day = "Beautiful"
print(day[-3])
print(day[-3:])
print(day[-5:3])
print(day[-5:-3])

day == "Beautiful"
print("Today is " + day)

day = "Beautiful"
print(str(day == "Beautiful") + ": Today is " + day)

operand1 = input("Input a number: ")
print ("You entered " + operand1)
