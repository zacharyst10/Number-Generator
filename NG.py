import random


computer_choice = random.randint(1, 100)

player_choice = input("Please chose a number! ")

print (computer_choice)
print (player_choice)

if player_choice == computer_choice:
    print ("YOU WIN!")
else:
    print (player_choice)

