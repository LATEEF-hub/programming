
import sys
import random
from enum import Enum


class RPS(Enum):
    # We use Cap for var that will be const
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


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

playerchoice = input(
    "Enter your choice:\n1.Rock,\n2.Paper, or\n3.Scissors\n\n")

player = int(playerchoice)  # Casting user input to INT

if player < 1 or player > 3: # Validating user Input
    # Here I change to SYS.exit to be able to exit the game
    sys.exit("Invalid Entry! Please enter a number between 1-3.")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace("RPS.", "") + ".") # I use replace method to remove RPS
print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")
# Comparing the choices of both players
if player == 1 and computer == 3:
    print("Congratulations! You Win.")
elif player == 2 and computer == 1:
    print("Congratulations! You Win.")
elif player == 3 and computer == 2:
    print("Congratulations! You Win.")
elif player == computer:
    print("It is a tie!")
else:
    print("Computer wins!")
