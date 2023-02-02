import random

options = ["rock", "paper", "scissors"]
computer = (random.choice(options))
user = None
print('Lets Play Rock, Paper, Sciccors.\n')


while user not in options:
  user = input("\nPick Rock, Paper, or Scissors: ").lower()
print("You Picked: " + user)
print("I Picked: " + computer)
if user == computer:
  print("\nTie Lame")


elif user == 'rock' and computer == 'scissors':
  print("\nWOW it Worked You're a Winner")

elif user == 'paper' and computer == 'scissors':
  print("\nGoodjob you LOSE!")

elif user == 'rock' and computer == 'paper':
  print("\nYou lost Loser")

elif user == 'Scissors'and computer == 'paper':
  print("\nI guess you Won")

elif user == 'paper' and computer == 'rock':
  print("\nUSER: I Beat You")
  print("\nComputer: Shut Up")