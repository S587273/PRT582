import random

print("Welcome to Rock Paper Scissors. Choose your weapon!")
print("---------------------------------------------------")


# variables
CpuScore = 0
PlayerScore = 0
Draw = 0
PossibleDeals = ["Rock", "Paper", "Scissors"]


def checkForWinner(playerHand, computerHand):
    if (playerHand == "Rock" and computerHand == "Paper"):
        print("YOU LOSE!")
        return "CPU"
    elif (playerHand == "Rock" and computerHand == "Scissors"):
        print("CONGRATS YOU DONT SUCK!")
        return "Player"
    elif (playerHand == "Scissors" and computerHand == "Paper"):
        print("CONGRATS YOU DONT SUCK!")
        return "Player"
    elif (playerHand == "Scissors" and computerHand == "Rock"):
        print("YOU LOSE!")
        return "CPU"
    elif (playerHand == "Paper" and computerHand == "Rock"):
        print("CONGRATS YOU DONT SUCK!")
        return "Player"
    elif (playerHand == "Paper" and computerHand == "Scissors"):
        print("YOU LOSE!")
        return "CPU"
    else:
        print("Its a draw! Play again ?")
        return "Draw"


# game loop
while (PlayerScore != 5 and CpuScore != 5):

    # validate input loop
    while True:
        playerHand = input("\nChoose your weapon.. Rock, Paper or Scissors?: ")
        if (playerHand == "Rock" or playerHand == "Paper" or playerHand ==
                "Scissors"):
            break
        else:
            print("Invalid input. Try again!")

    # computer pick
    computerHand = random.choice(PossibleDeals)

    # results
    print("Your Choice: ", playerHand)
    print("CPU Chose: ", computerHand)
    result = checkForWinner(playerHand, computerHand)
    if (result == "Player"):
        PlayerScore += 1
    elif (result == "CPU"):
        CpuScore += 1
    elif (result == "Draw"):
        Draw += 1
    print("Your Score:", PlayerScore, "CPU:", CpuScore, "Draw:", Draw)

print("Game Over! Thanks for playing")
