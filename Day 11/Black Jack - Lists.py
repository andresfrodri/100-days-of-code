# -*- coding: utf-8 -*-


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random as rd

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def calculate_score(list):
  if sum(list)==21 and len(list)==2:
    return 0
  if 11 in list and sum(list) > 21:
    list.remove(11)
    list.append(1)
  return sum(list)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "Both went over. You lose "

  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return 'The computer won has a blackjack'
  elif user_score == 0:
    return 'You won with a blackjack'
  elif user_score>21:
    return 'The computer won!'
  elif computer_score>21:
    return 'You won!'
  elif user_score > computer_score:
    return "You won!"
  else:
    return "You lost!"

def blackjack():
  print(logo)

  player_cards=[]

  dealer_cards=[]

  primal_flag=True


  for i in range(2):
    player_cards.append(rd.choice(cards))
    dealer_cards.append(rd.choice(cards))

  while primal_flag:
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {dealer_cards[0]}")
    if dealer_score == 0 or player_score == 0 or player_score > 21:
      primal_flag = False
    else:
      q=input("Type 'y' to get another card, type 'n' to pass: ")
      if q != "y":
        primal_flag = False
      else:
        player_cards.append(rd.choice(cards))
        
  while dealer_score < 17 and dealer_score != 0:
    dealer_cards.append(rd.choice(cards))
    dealer_score = calculate_score(dealer_cards)
  print(f"   Your final hand: {player_cards}, final score: {player_score}")
  print(f"   Computer's final hand: {dealer_cards}, final score: {dealer_score}")
  print(compare(player_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  blackjack()