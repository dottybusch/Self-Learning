import random

result = ''
gameon = True

while gameon:

    user = input("Wähle Schere, Stein oder Papier! ")


    x = random.randint(0,30)

    if x in range(0,10):
        result = "Schere"
    elif x in range(10,20):
        result = "Stein"
    elif x in range(20,30):
        result = "Papier"

    print(result)
        
    if user.lower()[:3] == result.lower()[:3]:
        print("Gleichstand!")
    elif user.lower()[:3] == 'sch' and result.lower()[:3] == 'pap':
        print("Du gewinnst!")
    elif user.lower()[:3] == 'sch' and result.lower()[:3] == 'ste':
        print("Du verlierst!")
    elif user.lower()[:3] == 'ste' and result.lower()[:3] == 'pap':
        print("Du verlierst!")
    elif user.lower()[:3] == 'ste' and result.lower()[:3] == 'sch':
        print("Du gewinnst!")
    elif user.lower()[:3] == 'pap' and result.lower()[:3] == 'sch':
        print("Du verlierst!")
    elif user.lower()[:3] == 'pap' and result.lower()[:3] == 'ste':
        print("Du gewinnst!")

    play_again = input("\nMöchtest du noch einmal spielen? Ja/Nein ")

    if play_again.lower()[0] == "n":
        gameon = False
