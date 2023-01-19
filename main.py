import random

options = ["rock", "paper", "scissors"]
computer = (random.choice(options))
user = None
0<1
1<2
0>2


while user not in options:
  user = input("Pick Rock, Paper, or Scissors: ").lower()
print("You Picked: " + user)
print("I Picked: " + computer)
if user == computer:
  print("Tie Lame")


elif user == 0 and computer == 2:
  print("WOW it Worked You're a Winner")

elif user == 1 and computer ==2:
  print("Goodjob you LOSE!")
