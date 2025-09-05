
# 1. Introduction
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

# 2. Working with String
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# 3. Input String
name = input("what is your name?")
print(name)

#4. Formatting String

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!". format(name,color,animal))

