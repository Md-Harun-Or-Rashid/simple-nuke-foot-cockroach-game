import random

ComputerSelection = random.randint(1, 3)
YouWon = 0
PlayingTie = 0
Youlose = 0

while True:
    YourInput = input("Foot, Nuke or Cockroach? (Quit ends): ")
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        ComputerSelection = "Foot"
    if randomNumber == 2:
        ComputerSelection = "Nuke"
    if randomNumber == 3:
        ComputerSelection = "Cockroach"
    if ComputerSelection == YourInput:
        print("You chose:", YourInput)
        print("Computer chose:", ComputerSelection)
        print("It is a tie!")
        PlayingTie += 1
    elif ComputerSelection == "Nuke" and YourInput == "Nuke":
        print("You chose:", YourInput)
        print("Computer chose:", ComputerSelection)
        print("Both LOSE!")
        Youlose += 1
    elif ComputerSelection == "Foot" and YourInput == "Cockroach":
        print("You chose:", YourInput)
        print("Computer chose:", ComputerSelection)
        print("You LOSE!")
        Youlose += 1
    elif ComputerSelection == "Nuke" and YourInput == "Foot":
        print("You chose:", YourInput)
        print("Computer chose:", ComputerSelection)
        print("You LOSE!")
        Youlose += 1
    elif ComputerSelection == "Cockroach" and YourInput == "Nuke":
        print("You chose:", YourInput)
        print("Computer chose:", ComputerSelection)
        print("You LOSE!")
        Youlose += 1
    elif YourInput == "Foot" and ComputerSelection == "Cockroach":
        print("You chose:", YourInput)
        print("Computer chose:", ComputerSelection)
        print("You WIN!")
        YouWon += 1
    elif YourInput == "Nuke" and ComputerSelection == "Foot":
        print("You chose:", YourInput)
        print("Computer chose:", ComputerSelection)
        print("You WIN!")
        YouWon += 1
    elif YourInput == "Cockroach" and ComputerSelection == "Nuke":
        print("You chose:", YourInput)
        print("Computer chose:", ComputerSelection)
        print("You WIN!")
        YouWon += 1
    elif YourInput == "Quit":
        break
    else:
        print("Incorrect selection.")
print("You played", YouWon + Youlose + PlayingTie, "rounds, and won ", YouWon, "rounds, playing tie in ", PlayingTie,
      "rounds.")
