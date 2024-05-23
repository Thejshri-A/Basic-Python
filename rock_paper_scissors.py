import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("Alright! Let's Play Rock Paper Scissors \n")

playerChoice = int(input(
    "Enter...\n 1 for Rock \n 2 for Paper or \n 3 for Scissor \n\n"))

if playerChoice < 1 or playerChoice > 3:
    sys.exit("You must enter either 1, 2 or 3 only")

computerChoice = int(random.choice("123"))

print("")
print("You chose " + str(RPS(playerChoice)).replace("RPS.", "") + ".")
print("Computer chose " + str(RPS(computerChoice)).replace("RPS.", "") + ".")
print("")

if (playerChoice == 1 and computerChoice == 3):
    print("🥳🎉🎊🎖 You Win!")
elif playerChoice == 2 and computerChoice == 1:
    print("🥳🎉🎊🎖 You Win!")
elif playerChoice == 3 and computerChoice == 2:
    print("🥳🎉🎊🎖 You Win!")
elif playerChoice == computerChoice:
    print("😁😉😜😎It's a tie")
else:
    print("💻🖥⌨🖱 Computer Wins!")

 # View->Appearance->Panel Position->Right
