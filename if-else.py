# If statements are used to set conditions for returns - If this, then that

iron_man_suits = 25
if iron_man_suits > 20:
    print("That's too many suits!")
    print("We talked about this!")
    print("I want one!")

# If-then-else statements
suits = 21
print('How many suits is too many?')
if suits >= 20:
    print("That many, Tony.")
else:
    print("You're getting there.")

# If and Elif statements. Elif is short for "else-if"
tony_suits = 26
if tony_suits == 42:
    print("This is a decent amount of suits.")
elif tony_suits >= 26 and tony_suits <= 42:
    print("Well, it never hurts to have spares.")
elif tony_suits > 42:
    print("Please don't tell Pepper.")
elif tony_suits == 0:
    print("Who took my suits!?")
else:
    print("I should make more suits.")

# Variables with no value

myval = None
print(myval)
if myval == None:
    print("The variable myval doesn't have a value.")


# Numbers vs Strings in Python. You can use the function int() to turn a string into a number
comics = "3"
converted_comics = int(comics)
print(converted_comics + 5)

# str() turns an integer into a string
comic_shops = 1
converted_comic_shops = str(comic_shops)
print(converted_comic_shops + " is fine.")

# More practice!

# code was wrong (a space before one of the print statements)
money = 2000
if money > 1000:
    print("I'm rich!")
else:
    print("I'm not rich!")
    print("But I might be later...")

# Create an If statement that checks whether a number of Twinkies (in the variable twinkies) is less than 100 or greater than
# 500. Your program should print the message "Too few or too many" if the condition is true.

twinkies = 600

if twinkies < 100 or twinkies > 500:
    print("Too few or too many.")

# Create an If statement that checks whether the amount of money contained in the variable "money" is between
# 100 and 500 or between 1000 and 5000

money = 150

if money >= 100 and money <= 500 or money >= 1000 and money <= 5000:
    print("true")
else:
    print("false")

# Create an if statement that prints the string "That's too many" if the variable "ninjas" contains a number that's less than
# 50, prints "It'll be a struggle, but I can take 'em" if it's less than 30, and prints "I can fight those ninjas!" if it's less
# than 10.

ninjas = 35
if ninjas < 50 and ninjas >= 30:
    print("That's too many")
elif ninjas < 30 and ninjas >= 10:
    print("That'll be a struggle")
elif ninjas < 10:
    print("I can fight those ninjas!")
