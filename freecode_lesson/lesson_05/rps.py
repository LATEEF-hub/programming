


print("")
line1 = '********************' #header and footer
line2 = '*                  *' #wrapper
line3 = '*     WELCOME      *' #message

print(line1)
print(line2)
print(line3)
print(line2)
print(line1)
print('')

playerchoice = input("Enter your choice:\n1.Rock,\n2.Paper,or\n3.Scissors\n")

player = int(playerchoice)

if player < 1 | player > 3:
    print("Invalid Entry! Please enter a number between 1-3.")