from moveCheckf import moveCheck
from moveComparef import movecompare
from computerrandf import computerRand
import random

print("Hello! Welcome to the game")
print("The game is rock paper scissors")
print("Please enter your move")
playerM1 = input()
playerM2 = moveCheck(playerM1)
computerM = computerRand(random.random())
print(movecompare(playerM2,computerM))