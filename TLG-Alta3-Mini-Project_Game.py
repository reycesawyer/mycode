#!/usr/bin/env python3

""" This is Reyce's Mini-Project. It is rouelette"""

import random
import time
from  colorama import Fore, Back, Style

print(Fore.YELLOW + "Welcome to Roulette! The rules are simple. Choose a number between 0 and 37 where 37 will be the placeholder for 00.")
print(Fore.WHITE + "This game is simplified and you can only choose a single number from 0 to 37 where 37 is 00. No multiple options or sets are available.")
choice = int(input(Fore.YELLOW + "Choose a number 0 - 37!\n" + Style.RESET_ALL)) 
wager = int(input(Fore.YELLOW + "Enter the $ amount you'd like to wager.\n" + Style.RESET_ALL)) 
landingspot = random.randint(0, 37)


if choice >= 0 and choice <= 37:
    print(Fore.RED + Style.BRIGHT + "The game is about to start!")
    time.sleep(2)
    print(Fore.WHITE + "The ball has been dropped!")
    time.sleep(1)
    print(Fore.BLUE + Style.BRIGHT + "*SPINNING*")
    time.sleep(1)
    print("*SPINNING*")
    time.sleep(1)
    print("*SPINNING*")
    time.sleep(1)
    print("*SPINNING*")
    time.sleep(1)
    print(Style.RESET_ALL + Fore.BLUE + "*SPINNING*")
    time.sleep(2)
    print(Style.DIM + Fore.CYAN + "*SPINNING*")
    time.sleep(2)
    print(Style.DIM + Fore.CYAN + "*SPINNING*")
    time.sleep(3)
    print(Style.RESET_ALL + Style.BRIGHT + Fore.RED + "The ball is about to STOP!")
    time.sleep(3)
    print(Fore.WHITE + f"The ball has landed on {landingspot}!")
    time.sleep(1)
    if choice == landingspot:
        winningbet = wager * 35
        print(Style.RESET_ALL +  f"You predicted the ball would land on {choice} and it landed on {landingspot}! " + Fore.GREEN + f"Congratulations! You guessed currectly! After wagering ${wager} you have won ${winningbet}!")
    else: 
        print(Style.RESET_ALL + f"You predicted the ball would land on {choice} and it landed on {landingspot}! " + Fore.RED + "Womp Womp! You did not choose the correct landing spot. Remember, you can only lose 100% of your money but you can win back 3500%!")
else:
    print("Please rerun the script and choose between 0 and 37.")
    exit()

exit()
