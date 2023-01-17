import random

list = ["Rock, Paper, Scissor"]

boolean = True
playing = True
while boolean and playing:
  user = input("Pick Rock, Paper, or Scissors: ").lower()
  print("You Picked: " + user)