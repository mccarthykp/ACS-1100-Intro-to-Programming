# import random library
from random import randint

# make an array
roles = ["bear", "ninja", "cowboy"]

# generate a random number to pick a random element from the array
computer = roles[randint(0, 2)]

player = False

while player == False:
    # intro
    print("Get ready!\n")
    print(". . .\n")
    print(". . .\n")
    print(". . .\n")
    # get player input
    player = input("Bear, Ninja or Cowboy? ")

    # compare computer and player role
    if computer == player:
        print("DRAW!")
    elif computer == "cowboy":
        if player == "bear":
            print(f"You lose! {player} is shot by {computer}")
        else:
            print(f"You win! {player} defeats {computer}")
    elif computer == "bear":
        if player == "cowboy":
            print(f"You win! {player} shoots {computer}")
        else:
            print(f"You lose! {player} is eaten by {computer}")
    elif computer == "ninja":
        if player == "cowboy":
            print(f"You lose! {player} is defeated by {computer}")
        else:
            print(f"You win! {player} eats {computer}")

    play_again = input("Would you like to play again? (Y/N) ").lower()
    if play_again == "y":
        player = False
        computer = roles[randint(0, 2)]
    else:
        break
