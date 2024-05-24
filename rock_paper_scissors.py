import sys
import random
from enum import Enum


def rock_paper_scissors():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    print("Alright! Let's Play Rock Paper Scissors \n")

    playerChoice = int(input(
        "Enter...\n 1 for Rock \n 2 for Paper or \n 3 for Scissor \n\n"))

    if playerChoice not in [1, 2, 3]:
        print("You must enter either 1, 2 or 3 only")
        return rock_paper_scissors()

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

    print("\n Play Again ?")

    while True:
        playAgain = input(" \n Y for yes or \n Q for quit \n\n")
        if playAgain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playAgain.lower() == "y":
        return rock_paper_scissors()
    else:
        print("Thank you for Playing ! ")
        sys.exit("Bye😜")


# View->Appearance->Panel Position->Right
rock_paper_scissors()
