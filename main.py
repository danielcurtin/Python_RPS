import random

choices = ["Rock", "Paper", "Scissors"]

def rock_paper_scissors():
  player_choice = input("Awesome! Make your move and I'll make mine: ")
  computer_choice = choices[random.randint(0, 2)]
  

player = input("Hi! Want to play a game of Rock Paper Scissors? Y/N: ")

if(player.upper() == "Y" or player.upper() == "YES"):
  rock_paper_scissors()
else:
  print("Okay, Have a great day!")