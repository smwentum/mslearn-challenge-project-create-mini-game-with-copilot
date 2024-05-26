import random

def isValidRockPaperScissors(choice):
    if choice == "rock" or choice == "paper" or choice == "scissors":
        return True
    else:
        return False
    
def getRandomRockPaperScissors():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determineWinner(playerChoice, pcChoice):
    if playerChoice == pcChoice:
        return 0
    elif playerChoice == "rock" and pcChoice == "scissors":
        return 1
    elif playerChoice == "paper" and pcChoice == "rock":
        return 1
    elif playerChoice == "scissors" and pcChoice == "paper":
        return 1
    else:
        return -1

def showStats(playerName, numberOfGames, numberOfWins):
    print("Stats for " + playerName + ":")
    print("Number of games played: " + str(numberOfGames))
    print("Number of wins: " + str(numberOfWins))

print("Welcome to Sai's Rock Paper Scissors Game")

numberOfGames = 0
numberOfWins=0


print("Please enter your name")
playerName = input()



choice = ""

wantToPlay = True
while wantToPlay:
    pcChoice = getRandomRockPaperScissors()
    while(isValidRockPaperScissors(choice) == False):
        print(playerName+", Please enter your choice: rock, paper, or scissors")
        choice = input()


    result = determineWinner(choice, pcChoice)


    if result == 0:
        print("It's a tie!")
    elif result == 1:
        print("You win! "+playerName+" chose "+choice+" and the computer chose "+pcChoice)
        numberOfWins += 1
    else:  
        print("You lose! "+playerName+" chose "+choice+" and the computer chose "+pcChoice)

    numberOfGames += 1
    showStats(playerName, numberOfGames,numberOfWins)
    print("Do you want to play again? (yes or no)")
    playAgain = input()
    if playAgain == "no":
        wantToPlay = False
    else:
        choice = ""
        continue
    
    


