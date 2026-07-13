import random

print("===================")
print("Rock Paper Scissors")
print("===================")
print()
print("1) ✊")
print("2) ✋")
print("3) ✌️")

userInput = int(input("Pick a number: "))
computerInput = random.randint(1, 3)

print()

if userInput == 1:
    print("You chose: ✊")
elif userInput == 2:
    print("You chose: ✋")
elif userInput == 3:
    print("You chose: ✌️")

if computerInput == 1:
    print("CPU chose: ✊")
elif computerInput == 2:
    print("CPU chose: ✋")
elif computerInput == 3:
    print("CPU chose: ✌️")

print()

if userInput == computerInput:
    print("It's a tie!")

elif userInput == 1 and computerInput == 3:
    print("The player won!")
elif userInput == 2 and computerInput == 1:
    print("The player won!")
elif userInput == 3 and computerInput == 2:
    print("The player won!")

elif userInput == 1 and computerInput == 2:
    print("Computer won!")
elif userInput == 2 and computerInput == 3:
    print("Computer won!")
elif userInput == 3 and computerInput == 1:
    print("Computer won!")