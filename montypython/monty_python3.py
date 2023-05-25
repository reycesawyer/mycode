#!/usr/bin/env python3

round = 0
answer = " "

while round < 3 and (answer.capitalize() != "Brian" and answer.lower() != "shrubbery"):
    round += 1
    answer = input('Finish the movie title, "Monty Python\'s the Life of _____": ')
    if answer.capitalize() == "Brian":
        print ("Correct")
    elif answer.lower() == "shrubbery":
        print ("You gave the super secret answer!")
    elif round == 3:
        print ("Sorry, the answer was Brian")
    else: 
        print ("Sorry, try again")
