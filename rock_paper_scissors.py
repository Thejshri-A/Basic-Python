import sys
import random
from enum import Enum


def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def rock_paper_scissors():

        nonlocal player_wins
        nonlocal computer_wins
        nonlocal name

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        print("Alright! Let's Play Rock Paper Scissors \n")

        playerChoice = int(input(
            f"Hello {name}! Enter...\n 1 for Rock \n 2 for Paper or \n 3 for Scissor \n\n"))

        if playerChoice not in [1, 2, 3]:
            print(f"{name} You must enter either 1, 2 or 3 only")
            return rock_paper_scissors()

        computerChoice = int(random.choice("123"))

        print("")
        print(f"{name} You chose {str(RPS(playerChoice)).replace('RPS.', '')}.")
        print(
            f"Computer chose {str(RPS(computerChoice)).replace('RPS.', '') }.")
        print("")

        def decide_winner(playerChoice, computerChoice):
            nonlocal player_wins
            nonlocal computer_wins

            if (playerChoice == 1 and computerChoice == 3):
                player_wins += 1
                return f"{name} 🥳🎉🎊🎖 You Win!"
            elif playerChoice == 2 and computerChoice == 1:
                player_wins += 1
                return f"{name} 🥳🎉🎊🎖 You Win!"
            elif playerChoice == 3 and computerChoice == 2:
                player_wins += 1
                return f"{name} 🥳🎉🎊🎖 You Win!"
            elif playerChoice == computerChoice:
                return "😁😉😜😎It's a tie"
            else:
                computer_wins += 1
                return "💻🖥⌨🖱 Computer Wins!"

        game_result = decide_winner(playerChoice, computerChoice)

        print(game_result)

        nonlocal game_count
        game_count += 1
        print(f"Game Count :  {game_count}.")
        print(f"\n {name}'s Wins : {player_wins}.")
        print(f"\n Computer Wins : {computer_wins}.")

        print(f"\n{name}, Play Again ?")

        while True:
            playAgain = input(" \n Y for yes or \n Q for quit \n\n")
            if playAgain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playAgain.lower() == "y":
            return rock_paper_scissors()
        else:
            print(f"Thank you {name}, for Playing ! ")
            sys.exit(f"Bye😜 {name}")
    return rock_paper_scissors


# View->Appearance->Panel Position->Right


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized gaming experience!")

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the player."
    )
    args = parser.parse_args()
    play_rock_paper_scissors = rps(args.name)
    play_rock_paper_scissors()
