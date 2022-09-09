# -*- coding: utf-8 -*-


logo = """
  _______                             __   __                                   __               
 |   _   .--.--.-----.-----.-----.   |  |_|  |--.-----.   .-----.--.--.--------|  |--.-----.----.
 |.  |___|  |  |  -__|__ --|__ --|   |   _|     |  -__|   |     |  |  |        |  _  |  -__|   _|
 |.  |   |_____|_____|_____|_____|   |____|__|__|_____|   |__|__|_____|__|__|__|_____|_____|__|  
 |:  1   |                                                                                       
 |::.. . |                                                                                       
 `-------'                                                                                       
                                                                                                 
"""

import random as rd
print("Welcome to guess the number, I'm thinking a number between 1 and 100")

number = rd.choice(range(1,100))

def guesser():
  guess=int(input('Make a guess: '))
  if guess == number:
    return 0
  elif guess < number:
    print("Too low")
    print("Guess again!")
  else:
    print("Too high")
    print("Guess again!")


def game():

  Should_stop = False
  print(logo)
  dif = input("Choose your difficulty type 'easy' or 'hard': ")
  if dif == "easy":
    lives=10
  else:
    lives=5

  while not Should_stop:
    if lives !=0:
      print(f"You have {lives} attempls remaining to guess the number")
      a=guesser()
      lives -= 1
      if a==0:
        print(f"You win the number was {number}")
        return
    else:
      print(f"You've run out of guesses, you lose... The number was {number}")
      return 


game()