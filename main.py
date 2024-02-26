import random

choices = ["Rock", "Paper", "Scissors"]

def rock_paper_scissors():
  print()
  player_choice = input("Awesome! Make your move and I'll make mine: ")
  computer_choice = choices[random.randint(0, 2)]
  
  if(player_choice.upper() == "ROCK" and computer_choice == "Rock"):
    print(f"We tied! I also chose {computer_choice}!\n")
  elif(player_choice.upper() == "ROCK" and computer_choice == "Paper"):
    print(f"Sorry! Since I chose {computer_choice}, you lose!\n")
  elif(player_choice.upper() == "ROCK" and computer_choice == "Scissors"):
    print(f"Oh man! Since I chose {computer_choice}, you win!\n")
  elif(player_choice.upper() == "PAPER" and computer_choice == "Rock"):
    print(f"Oh man! Since I chose {computer_choice}, you win!\n")
  elif(player_choice.upper() == "PAPER" and computer_choice == "Paper"):
    print(f"We tied! I also chose {computer_choice}!\n")
  elif(player_choice.upper() == "PAPER" and computer_choice == "Scissors"):
    print(f"Sorry! Since I chose {computer_choice}, you lose!\n")
  elif(player_choice.upper() == "SCISSORS" and computer_choice == "Rock"):
    print(f"Sorry! I chose {computer_choice}, so you lose!\n")
  elif(player_choice.upper() == "SCISSORS" and computer_choice == "Paper"):
    print(f"Oh man! Since I chose {computer_choice}, you win!\n")
  elif(player_choice.upper() == "SCISSORS" and computer_choice == "Scissors"):
    print(f"We tied! I also chose {computer_choice}!\n")
  else:
    print("Nice try, that's not a legal move!\n")

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