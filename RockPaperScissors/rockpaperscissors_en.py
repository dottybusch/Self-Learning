import random

result = ''
gameon = True


while gameon:

    play_again = "x"
    user = "x"

    while user.lower()[:3] not in ["roc", "pap", "sci"]:

        user = input("Pick Rock, Paper, or Scissors! ")

        if user.lower()[:3] not in ["roc", "pap", "sci"]:
            print("Invalid choice!")


    x = random.randint(0,30)

    if x in range(0,10):
        result = "Scissors"
    elif x in range(10,20):
        result = "Rock"
    elif x in range(20,30):
        result = "Paper"

    print(result)
        
    if user.lower()[:3] == result.lower()[:3]:
        print("You tie!")
    elif user.lower()[:3] == 'sci' and result.lower()[:3] == 'pap':
        print("You win!")
    elif user.lower()[:3] == 'sci' and result.lower()[:3] == 'roc':
        print("You lose!")
    elif user.lower()[:3] == 'roc' and result.lower()[:3] == 'pap':
        print("You lose!")
    elif user.lower()[:3] == 'roc' and result.lower()[:3] == 'sci':
        print("You win!")
    elif user.lower()[:3] == 'pap' and result.lower()[:3] == 'sci':
        print("You lose!")
    elif user.lower()[:3] == 'pap' and result.lower()[:3] == 'roc':
        print("You win!")


    while play_again.lower()[0] not in ["y", "n"]:

        play_again = input("\nDo you want to play again? Yes/No ")

        if play_again.lower()[0] not in ["y", "n"]:
            print("Invalid choice!")

        if play_again.lower()[0] == "n":
            gameon = False

