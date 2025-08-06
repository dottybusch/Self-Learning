import random

result = ''
gameon = True


while gameon:

    play_again = "x"
    user = "x"

    while user.lower()[:3] not in ["sch", "ste", "pap"]:

        user = input("Wähle Schere, Stein oder Papier! ")

        if user.lower()[:3] not in ["sch", "ste", "pap"]:
            print("Ungültige Auswahl!")


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
        

    while play_again.lower()[0] not in ["j", "n"]:

        play_again = input("\nMöchtest du noch einmal spielen? Ja/Nein ")

        if play_again.lower()[0] not in ["j", "n"]:
            print("Ungültige Auswahl!")

        if play_again.lower()[0] == "n":
            gameon = False
