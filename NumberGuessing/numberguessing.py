import random

gameon = True

while gameon:

    x = random.randint(1,100+1)
    user = 0
    trial = 0
    playagain = "x"

    while user != x:
        user = int(input("\nPick a number between 1 and 100! "))
        trial += 1

        if user < x:
            print("Too small. Try again.")
        elif user > x:
            print("Too big. Try again.")

    print("You guessed right!")
    print(f"You needed {trial} tries.")

    while playagain.lower() not in ["y", "n"]:
        playagain = input("\nDo you want to play again? Y/N ")

        if playagain.lower() == "y":
            gameon = True
        elif playagain.lower() == "n":
            gameon = False
