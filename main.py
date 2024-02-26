def rock_paper_scissors():
  print("Test")

player = input("Hi! Want to play a game of Rock Paper Scissors? Y/N: ")

if(player.upper() == "Y" or player.upper() == "YES"):
  rock_paper_scissors()
else:
  print("Okay, Have a great day!")