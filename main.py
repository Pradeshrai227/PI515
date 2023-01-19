import random

options = ["Rock", "Paper", "Scissors"]
computer = (random.choice(options))
user = None

while user not in options:
  user = input("Pick Rock, Paper, or Scissors: ")
print("You Picked: " + user)
print("I Picked: " + computer)
if user == computer:
  print("Tie Lame")
elif user != computer:
  print("You are Loser")
  