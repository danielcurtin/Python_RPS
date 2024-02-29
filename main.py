import random

choices = ["Rock", "Paper", "Scissors"]
wins = 0
losses = 0
ties = 0

def rock_paper_scissors():
  global wins, losses, ties

  print()
  player_choice = input("Awesome! Make your move and I'll make mine: ")
  computer_choice = choices[random.randint(0, 2)]
  
  if(player_choice.upper() == "ROCK" and computer_choice == "Rock"):
    ties += 1
    print(f"We tied! I also chose {computer_choice}!\n")
  elif(player_choice.upper() == "ROCK" and computer_choice == "Paper"):
    losses += 1
    print(f"Sorry! Since I chose {computer_choice}, you lose!\n")
  elif(player_choice.upper() == "ROCK" and computer_choice == "Scissors"):
    wins += 1
    print(f"Oh man! Since I chose {computer_choice}, you win!\n")
  elif(player_choice.upper() == "PAPER" and computer_choice == "Rock"):
    wins += 1
    print(f"Oh man! Since I chose {computer_choice}, you win!\n")
  elif(player_choice.upper() == "PAPER" and computer_choice == "Paper"):
    ties += 1
    print(f"We tied! I also chose {computer_choice}!\n")
  elif(player_choice.upper() == "PAPER" and computer_choice == "Scissors"):
    losses += 1
    print(f"Sorry! Since I chose {computer_choice}, you lose!\n")
  elif(player_choice.upper() == "SCISSORS" and computer_choice == "Rock"):
    losses += 1
    print(f"Sorry! I chose {computer_choice}, so you lose!\n")
  elif(player_choice.upper() == "SCISSORS" and computer_choice == "Paper"):
    wins += 1
    print(f"Oh man! Since I chose {computer_choice}, you win!\n")
  elif(player_choice.upper() == "SCISSORS" and computer_choice == "Scissors"):
    ties += 1
    print(f"We tied! I also chose {computer_choice}!\n")
  else:
    print("Nice try, that's not a legal move!\n")

  print(f"Wins: {wins} Losses: {losses} Ties: {ties}")
  replay = input("Want to play again? Y/N: ")
  if(replay.upper() == "Y" or replay.upper() == "YES"):
    rock_paper_scissors()
  else:
    print("That was fun, Have a great day!")

player = input("Hi! Want to play a game of Rock Paper Scissors? Y/N: ")

if(player.upper() == "Y" or player.upper() == "YES"):
  rock_paper_scissors()
else:
  print("Okay, Have a great day!")