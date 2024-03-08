"""
Subtract a square. This is a two-player mathematical game of strategy. It is played by two
people with a pile of coins (or other tokens) between them. The players take turns removing
coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, ...).
The player who removes the last coin wins.
"""

# Welcome and display status
print("WELCOME TO THE GAME!")
print("this game is played by two players / you must remove a squared non zero number")
input("Press any key to start the game!")

from random import randint
import math


# check if the number is squared or not
def is_perfect_square(num):
    square_root = math.sqrt(num)
    return square_root.is_integer()


# numbers limit is from 10 to 1000
coins = randint(10, 1000)
print("Current number of coins:", coins)

# mechanism of the game
while coins > 0:
    while True:
        try:
           player_num1 = int(input("Player 1, please enter a valid number:"))
        except ValueError:
            print("Error! please try again.")
            continue
        if player_num1 > 0 and is_perfect_square(player_num1) and player_num1 <= coins:
            break
        else:
            print("Invalid number! Please enter a valid number:")

    coins -= player_num1
    print("Remaining coins:", coins)

    if coins == 0:
        print("Player 1 wins!")
        input()
        break

    while True:
        try:
          player_num2 = int(input("Player 2, please enter a valid number:"))
        except ValueError:
            print("Error! please try again.")
            continue
        if player_num2 > 0 and is_perfect_square(player_num2) and player_num2 <= coins:
            break
        else:
            print("Invalid number! Please enter a valid number:")

    coins -= player_num2
    print("Remaining coins:", coins)

    if coins == 0:
        print("Player 2 wins!")
        input()
        break


 


