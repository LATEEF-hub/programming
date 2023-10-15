import sys
import random

print("")
line1 = '********************'  # header and footer
line2 = '*                  *'  # wrapper
line3 = '*     WELCOME      *'  # message

print(line1)
print(line2)
print(line3)
print(line2)
print(line1)
print('')

playerchoice = input("Enter your choice:\n1.Rock,\n2.Paper, or\n3.Scissors\n")

player = int(playerchoice)  # Casting user input to INT

if player < 1 | player > 3:
    # Validating user Input
    sys.exit("Invalid Entry! Please enter a number between 1-3.") #Here I change to SYS.exit to be able to exit the game

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
print("You chose " + playerchoice + ".")
print("Python chose " + computerchoice + ".")
print("")
# Comparing the choices of both players